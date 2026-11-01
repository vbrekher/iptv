#!/usr/bin/env python3
"""One-step provisioning: Bunny Storage + linked Pull Zone + public IPTV playlists.

Requires tools/personal_bunny_playlists.py and tools/free_hls_filter.py locally.
The Bunny Account API Key is read with getpass and never persisted.
Only M3U text/catalog files are uploaded, not video content.
"""
from __future__ import annotations

import argparse
import getpass
import json
import os
import re
import secrets
import shutil
import sys
import tempfile
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import personal_bunny_playlists as catalog
import free_hls_filter as verifier

API = "https://api.bunny.net"
STATE = Path(".bunny-iptv-state.json")
DEST = Path("dist/iptv-published")
READY = Path("dist/iptv-ready")
VALID_NAME = re.compile(r"^[a-z0-9-]{4,60}$")


class SetupError(Exception):
    pass


class BunnyAPI:
    def __init__(self, key):
        if not key.strip():
            raise SetupError("Bunny Account API Key is required")
        self.key = key.strip()

    def call(self, method, path, payload=None):
        body = json.dumps(payload).encode() if payload is not None else None
        req = Request(API + path, data=body, method=method, headers={
            "AccessKey": self.key, "Accept": "application/json",
            "Content-Type": "application/json",
        })
        try:
            with urlopen(req, timeout=35) as response:
                value = response.read(4000000)
                return json.loads(value) if value else {}
        except HTTPError as error:
            raise SetupError("Bunny API " + method + " " + path.split("?")[0] +
                             " HTTP " + str(error.code)) from None
        except (URLError, TimeoutError):
            raise SetupError("Bunny API unavailable; network or account permissions") from None
        except (ValueError, UnicodeDecodeError):
            raise SetupError("Unexpected Bunny API response") from None


def list_zones(api, kind):
    entries = []
    for page in range(1, 21):
        path = "/" + kind + "?" + urlencode({
            "page": page, "perPage": 100, "includeDeleted": "false",
        })
        data = api.call("GET", path)
        if isinstance(data, dict):
            batch = data.get("Items")
            more = data.get("HasMoreItems")
        else:
            batch = data
            more = None
        if not isinstance(batch, list):
            raise SetupError("Invalid Bunny zone listing: " + kind)
        entries.extend(batch)
        if not (bool(more) if more is not None else len(batch) == 100):
            return entries
    raise SetupError("Bunny zone listing too large")


def named(items, name):
    matches = [x for x in items if x.get("Name", "").lower() == name.lower()]
    if len(matches) > 1:
        raise SetupError("Ambiguous existing resource: " + name)
    return matches[0] if matches else None


def load_state(path):
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not VALID_NAME.fullmatch(data.get("name", "")):
            raise SetupError("Invalid local state file; check before retrying")
        return data
    # Save non-secret identity before creating paid resources; reruns reuse them.
    data = {"name": "lampa-iptv-" + secrets.token_hex(4), "region": "DE"}
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    os.chmod(path, 0o600)
    return data


def storage_zone(api, state):
    name = state["name"] + "-storage"
    zone = named(list_zones(api, "storagezone"), name)
    if zone is None:
        print("Creating Storage Zone:", name)
        zone = api.call("POST", "/storagezone", {"Name": name, "Region": "DE"})
    else:
        print("Reusing Storage Zone:", name)
    if not isinstance(zone, dict) or not isinstance(zone.get("Id"), int):
        raise SetupError("Storage Zone ID missing")
    detail = api.call("GET", "/storagezone/" + str(zone["Id"]))
    password = detail.get("Password") or zone.get("Password")
    region = (detail.get("Region") or zone.get("Region") or state.get("region") or "").lower()
    if region not in catalog.REGION_HOSTS:
        raise SetupError(f"Unknown Storage primary region {region!r}; refusing wrong-region upload")
    if not isinstance(password, str) or not password.strip() or set(password) == {"*"}:
        raise SetupError("Storage Zone write password unavailable; Bunny Account key cannot upload files")
    print("Storage primary region:", region, "| upload endpoint:", catalog.REGION_HOSTS[region])
    return {"id": zone["Id"], "name": name, "password": password, "region": region}


def pull_zone(api, state, storage_id):
    name = state["name"] + "-cdn"
    zone = named(list_zones(api, "pullzone"), name)
    if zone is None:
        print("Creating Pull Zone linked to Storage:", name)
        zone = api.call("POST", "/pullzone", {
            "Name": name, "Type": 0, "OriginType": 2,
            "StorageZoneId": storage_id,
        })
    else:
        print("Reusing Pull Zone:", name)
    if not isinstance(zone, dict) or not isinstance(zone.get("Id"), int):
        raise SetupError("Pull Zone ID missing")
    detail = api.call("GET", "/pullzone/" + str(zone["Id"]))
    if detail.get("StorageZoneId") != storage_id or detail.get("OriginType") != 2:
        raise SetupError("Pull Zone is linked to a different origin; refusing upload")
    hosts = detail.get("Hostnames") or zone.get("Hostnames") or []
    hostnames = [
        (item.get("Value") or item.get("Hostname")) if isinstance(item, dict) else item
        for item in hosts
    ]
    host = next((x for x in hostnames if isinstance(x, str) and
                 x.endswith(".b-cdn.net")), name + ".b-cdn.net")
    if not re.fullmatch(r"[a-zA-Z0-9.-]+", host):
        raise SetupError("Unexpected CDN hostname")
    return {"id": zone["Id"], "hostname": host}


def prepare_public_candidates(generated, checked, published):
    """Never publish unverified adult entries, failed probes, or private diagnostics."""
    published.mkdir(parents=True, exist_ok=True)
    for dirname in ("countries", "categories"):
        if (generated / dirname).is_dir():
            shutil.copytree(generated / dirname, published / dirname, dirs_exist_ok=True)
    (published / "catalog").mkdir(exist_ok=True)
    verified = catalog.parse_m3u((checked / "adult.m3u").read_text(encoding="utf-8"))
    all_source = catalog.parse_m3u((generated / "index.m3u").read_text(encoding="utf-8"))
    adult_source = catalog.parse_m3u((generated / "adult.m3u").read_text(encoding="utf-8"))
    unverified_pairs = {(catalog.channel_id(m), u) for m, u in adult_source}
    public = [(m, u) for m, u in all_source
              if (catalog.channel_id(m), u) not in unverified_pairs]
    merged = catalog.unique_entries(public + verified)
    for name, items in (("adult.m3u", verified), ("index.m3u", merged),
                        ("index.category.m3u", merged)):
        (published / name).write_text(catalog.serialize(items), encoding="utf-8")
    categories = published / "categories"
    categories.mkdir(exist_ok=True)
    for key in ("xxx", "adultiptv", "mycamtv", "other-adult"):
        (categories / (key + ".m3u")).unlink(missing_ok=True)
    if (checked / "categories").exists():
        for path in (checked / "categories").glob("*.m3u"):
            shutil.copyfile(path, categories / path.name)
    (categories / "xxx.m3u").write_text(catalog.serialize(verified), encoding="utf-8")
    report = json.loads((checked / "catalog/free-check-report.json").read_text())
    report["public_index_entries_not_individually_tested"] = len(public)
    report["combined_entries"] = len(merged)
    report["video_files_hosted"] = False
    report["distribution_rights_verified"] = False
    (published / "catalog/report.json").write_text(json.dumps(report, indent=2) + "\n")
    return len(verified), len(merged)


def publish(api, state, storage, pull, published):
    """Retry 401 on freshly created Storage Zones; refresh credentials each retry.

    No credentials are written to files. Account API key is never used on
    the Storage API, only the Storage Zone's writable Password.
    """
    for attempt in range(1, 7):
        variables = {
            "BUNNY_STORAGE_ZONE": storage["name"],
            "BUNNY_STORAGE_REGION": storage["region"],
            "BUNNY_CDN_HOST": pull["hostname"],
            "BUNNY_STORAGE_PASSWORD": storage["password"],
        }
        previous = {k: os.environ.get(k) for k in variables}
        try:
            os.environ.update(variables)
            catalog.publish(published, "iptv")
            return
        except HTTPError as error:
            if error.code not in (401, 403):
                raise SetupError(f"Bunny Storage upload HTTP {error.code}; no resources were recreated") from None
            if attempt == 6:
                raise SetupError(
                    f"Bunny Storage still returns HTTP {error.code} after 6 attempts. "
                    f"Zone: {storage['name']}, primary region: {storage['region']}, "
                    f"endpoint: {catalog.REGION_HOSTS[storage['region']]}. "
                    "Bunny requires the WRITE Storage Zone Password (not the Account API Key "
                    "or ReadOnlyPassword). Check Bunny Storage > FTP & API Access and the "
                    "primary storage region. Re-run with --upload-only; resources will be reused."
                ) from None
            wait = min(2 ** attempt, 16)
            print(
                f"Storage API HTTP {error.code} (attempt {attempt}/6). "
                f"Refreshing zone credentials and retrying in {wait}s; no new resources..."
            )
        finally:
            for key, value in previous.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value
        time.sleep(wait)
        storage = storage_zone(api, state)


def verify_public_cdn(hostname):
    for attempt in range(4):
        try:
            req = Request("https://" + hostname + "/iptv/index.m3u")
            with urlopen(req, timeout=12) as response:
                if response.status == 200 and response.read(80).startswith(b"#EXTM3U"):
                    return True
        except (OSError, HTTPError, URLError, TimeoutError):
            pass
        if attempt < 3:
            time.sleep(2)
    return False


def self_test():
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        s1 = load_state(folder / "state.json")
        assert load_state(folder / "state.json") == s1
        assert "api" not in (folder / "state.json").read_text().lower()
        original = folder / "source"
        checked = folder / "checked"
        out = folder / "out"
        for p in (original / "categories", original / "countries",
                  checked / "categories", checked / "catalog"):
            p.mkdir(parents=True)
        media = '#EXTINF:-1 tvg-id="Adult.us" group-title="XXX",Adult\nhttps://example.com/a.m3u8\n'
        news = '#EXTINF:-1 tvg-id="News.us" group-title="News",News\nhttps://example.com/n.m3u8\n'
        (original / "index.m3u").write_text("#EXTM3U\n" + news + media)
        (original / "adult.m3u").write_text("#EXTM3U\n" + media)
        (checked / "adult.m3u").write_text("#EXTM3U\n")
        (checked / "catalog/free-check-report.json").write_text("{}")
        count, total = prepare_public_candidates(original, checked, out)
        assert (count, total) == (0, 1)
        assert "Adult.us" not in (out / "index.m3u").read_text()
        assert (out / "categories/xxx.m3u").read_text() == "#EXTM3U\n"
    class FakeAPI:
        def __init__(self):
            self.storage = []
            self.pull = []
            self.created = 0
        def call(self, method, path, payload=None):
            if path.startswith("/storagezone?"):
                return {"Items": self.storage, "HasMoreItems": False}
            if path.startswith("/pullzone?"):
                return {"Items": self.pull, "HasMoreItems": False}
            if method == "POST" and path == "/storagezone":
                self.created += 1
                zone = {"Name": payload["Name"], "Id": 10, "Password": "fake"}
                self.storage.append(zone)
                return zone
            if method == "GET" and path == "/storagezone/10":
                return self.storage[0]
            if method == "POST" and path == "/pullzone":
                self.created += 1
                zone = {"Name": payload["Name"], "Id": 20,
                        "StorageZoneId": 10, "OriginType": 2}
                self.pull.append(zone)
                return zone
            if method == "GET" and path == "/pullzone/20":
                return self.pull[0]
            raise AssertionError(path)
    fake = FakeAPI()
    state = {"name": "lampa-iptv-test"}
    z = storage_zone(fake, state)
    p = pull_zone(fake, state, z["id"])
    storage_zone(fake, state)
    pull_zone(fake, state, z["id"])
    assert fake.created == 2 and p["hostname"].endswith(".b-cdn.net")
    print("ONE_CLICK_BUNNY_SELF_TEST_PASS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--without-community", action="store_true")
    parser.add_argument("--upload-only", action="store_true", help="Resume upload from dist/iptv-ready; no stream probing")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    print("Lampa IPTV Bunny setup — only M3U files; Bunny resources incur charges.")
    api_key = getpass.getpass("Bunny Account API Key (hidden): ")
    api = BunnyAPI(api_key)
    api_key = ""
    list_zones(api, "storagezone")  # validate account access before creating
    state = load_state(STATE)
    print("Using resource group:", state["name"])
    if args.upload_only:
        if not (READY / "index.m3u").is_file() or not (READY / "adult.m3u").is_file():
            raise SetupError("No saved dist/iptv-ready playlist: first run without --upload-only")
        print("Resuming saved playlists without rechecking streams:", READY)
    else:
        with tempfile.TemporaryDirectory(prefix="lampa-iptv-") as folder:
            root = Path(folder)
            candidates = root / "candidates"
            checked = root / "checked"
            out = root / "public"
            catalog.prepare(candidates, True, "ua", not args.without_community)
            outcome = verifier.run(argparse.Namespace(
                input=str(candidates), output=str(checked), workers=6, timeout=7.,
                publish=False, prefix="iptv",
            ))
            if outcome not in (0, 2):
                raise SetupError("Stream verification failed")
            adult_count, combined_count = prepare_public_candidates(candidates, checked, out)
            print("Adult candidates responding anonymously:", adult_count)
            print("Public catalog + verified adult candidates:", combined_count)
            if READY.exists():
                shutil.rmtree(READY)
            READY.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(out, READY)
            print("Saved playlists locally for safe retry:", READY)
    storage = storage_zone(api, state)
    pull = pull_zone(api, state, storage["id"])
    publish(api, state, storage, pull, READY)
    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(READY, DEST)
    base = "https://" + pull["hostname"] + "/iptv/"
    print("\\nLampa M3U addresses:")
    for path in ("index.m3u", "adult.m3u", "categories/xxx.m3u",
                 "countries/ua.m3u"):
        print(base + path)
    print("Public CDN index:", "VERIFIED" if verify_public_cdn(pull["hostname"])
          else "NOT VERIFIED (check Pull Zone origin and cache)")
    print("Report:", DEST / "catalog/report.json")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (SetupError, ValueError, OSError, json.JSONDecodeError) as exc:
        print("ERROR:", exc, file=sys.stderr)
        sys.exit(1)
