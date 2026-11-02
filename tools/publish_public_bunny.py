#!/usr/bin/env python3
"""Publish missing country/Pluto/clean-Lampa M3Us to an EXISTING Bunny zone.

One hidden Bunny Account API Key prompt, one existing resource identity.
No new zones, stream probing, credential persistence, media proxy or DRM work.
"""
from __future__ import annotations

import argparse
import getpass
import json
import shutil
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import auto_bunny_setup as bunny
import lampa_category_fix as cleaner
import plutotv_bunny as pluto
import sync_bunny_countries as countries

OUTPUT = Path("dist/public-hub")


def existing_api():
    if not bunny.STATE.is_file():
        raise RuntimeError("Missing original .bunny-iptv-state.json: cd ~/iptv-bunny first")
    state = bunny.load_state(bunny.STATE)
    key = getpass.getpass("Bunny Account API Key (hidden): ")
    if not key:
        raise RuntimeError("Bunny Account API Key is empty")
    api = bunny.BunnyAPI(key)
    del key
    # Absolutely forbid new paid resource creation.
    zone_name, pull_name = state["name"] + "-storage", state["name"] + "-cdn"
    if bunny.named(bunny.list_zones(api, "storagezone"), zone_name) is None:
        raise RuntimeError("Existing Storage Zone not found; refusing zone creation")
    if bunny.named(bunny.list_zones(api, "pullzone"), pull_name) is None:
        raise RuntimeError("Existing Pull Zone not found; refusing zone creation")
    return api, state, bunny.storage_zone(api, state)


def get_existing_pull(api, state, storage):
    return bunny.pull_zone(api, state, storage["id"])


def collect_countries(target: Path, workers: int = 8, read_index=None, fetch=None):
    """Mirror healthy country sources, record unavailable entries explicitly.

    Unlike the old all-or-nothing importer, one historical 404 does not
    prevent publishing the other 187 country playlists. It never claims a
    partial mirror is complete and never invents a missing M3U.
    """
    read_index = read_index or countries.fetch_index_markdown
    fetch = fetch or countries.fetch_m3u
    codes = countries.extract_country_codes(read_index())
    target.mkdir(parents=True, exist_ok=True)
    folder = target / "countries"
    folder.mkdir(exist_ok=True)
    available: dict[str, bytes] = {}
    missing: dict[str, str] = {}

    def load_one(code):
        # Bounded attempts for CDN/transient failures, no fabricated content.
        for attempt in range(3):
            try:
                return fetch(countries.COUNTRY_BASE + code + ".m3u")
            except (HTTPError, URLError, TimeoutError, OSError) as exc:
                reason = type(exc).__name__
                if attempt >= 2 or (isinstance(exc, HTTPError) and exc.code == 404):
                    raise RuntimeError(reason) from None
                time.sleep(1 + attempt)
        raise RuntimeError("UnknownError")

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(load_one, code): code for code in codes}
        for future in as_completed(futures):
            code = futures[future]
            try:
                data = future.result()
                if not data.startswith(b"#EXTM3U"):
                    raise ValueError("not_m3u")
                available[code] = data
            except Exception as exc:
                missing[code] = type(exc).__name__ if type(exc).__name__ != "RuntimeError" else str(exc)
    if len(available) < 100 or "ua" not in available:
        raise RuntimeError("Insufficient countries downloaded; aborting country upload safely")
    for code, blob in sorted(available.items()):
        (folder / (code + ".m3u")).write_bytes(blob)
    # Grouped playlist is only a bonus; no fake success when missing.
    try:
        grouped = fetch(countries.GROUPED_URL)
        if grouped.startswith(b"#EXTM3U"):
            (target / "index.country.m3u").write_bytes(grouped)
        else:
            missing["index.country"] = "not_m3u"
    except (HTTPError, URLError, TimeoutError, OSError, ValueError) as exc:
        missing["index.country"] = type(exc).__name__
    report = {
        "expected": len(codes), "published_ready": len(available),
        "missing": dict(sorted(missing.items())),
        "complete": len(available) == len(codes) and "index.country" not in missing,
        "codes": sorted(available),
        "note": "HTTP HLS playback for country TV channels not tested"
    }
    print("COUNTRIES_PREPARED", len(available), "/", len(codes))
    if missing:
        print("COUNTRIES_MISSING", json.dumps(report["missing"], ensure_ascii=False))
    return report


def prepare_clean(target: Path):
    local = bunny.READY if (bunny.READY / "index.m3u").is_file() else bunny.DEST
    if not (local / "index.m3u").is_file() or not (local / "adult.m3u").is_file():
        print("CLEAN_SKIPPED: local index.m3u/adult.m3u absent")
        return None
    stage = target / "clean"
    cleaner.build(local, stage)
    # We intentionally don't reupload a huge legacy combined catalog
    # unless the user requested it. New clean links are the upgrade.
    publish = target / "clean-upload"
    publish.mkdir(exist_ok=True)
    for name in ("index.clean.m3u", "lampa-clean-lite.m3u", "lampa-clean.m3u"):
        shutil.copy2(stage / name, publish / name)
    return publish


def prepare_pluto(target: Path):
    stage = target / "pluto"
    report = pluto.create(pluto.download(pluto.ALL), pluto.download(pluto.GERMANY), stage)
    return stage, report


def verify_cdn(host: str, filename: str):
    base = f"https://{host}/iptv/{filename}"
    req = Request(base + "?catalog_check=" + str(time.time_ns()),
                  headers={"User-Agent": "IPTV-Bunny-Public-Hub/1.0"})
    try:
        with urlopen(req, timeout=18) as response:
            return response.status == 200 and response.read(8).startswith(b"#EXTM3U")
    except (HTTPError, URLError, TimeoutError, OSError):
        return False


def self_test():
    import tempfile
    codes = ["ua", "us"] + [
        chr(97 + n // 26) + chr(97 + n % 26) for n in range(130)
    ]
    md = " ".join(countries.COUNTRY_BASE + c + ".m3u" for c in codes)
    def mock_fetch(url):
        if url.endswith("/mr.m3u"):
            raise HTTPError(url, 404, "Not found", None, None)
        return b"#EXTM3U\n#EXTINF:-1,Example\nhttps://example.com/live.m3u8\n"
    with tempfile.TemporaryDirectory() as tmp:
        staged = Path(tmp) / "countries-upload"
        r = collect_countries(staged, read_index=lambda: md, fetch=mock_fetch)
        assert r["complete"] and r["expected"] == len(r["codes"])
        assert (staged / "countries/ua.m3u").exists()
        assert (staged / "index.country.m3u").exists()
        # One missing country should not suppress hundreds of healthy files.
        md += " " + countries.COUNTRY_BASE + "mr.m3u"
        r = collect_countries(staged, read_index=lambda: md, fetch=mock_fetch)
        assert not r["complete"] and r["missing"]["mr"] == "HTTPError"
        assert r["published_ready"] >= 100
    print("PUBLIC_HUB_OFFLINE_TEST_PASS")


def run(args):
    if args.self_test:
        self_test()
        return 0
    jobs = [x for x in ("countries", "pluto", "clean") if not args.only or x in args.only]
    if not jobs:
        raise RuntimeError("No jobs selected")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="iptv-public-hub-") as temp:
        stages = {}
        status = {}
        location = Path(temp)
        # Source data prepared first. A failure in one optional package does
        # not erase existing sources or block the other packages.
        for job in jobs:
            try:
                if job == "countries":
                    stage = location / "countries-upload"
                    status["countries"] = collect_countries(stage)
                    stages["countries"] = stage
                elif job == "pluto":
                    stage, report = prepare_pluto(location)
                    stages["pluto"] = stage
                    status["pluto"] = report
                elif job == "clean":
                    stage = prepare_clean(location)
                    if stage is not None:
                        stages["clean"] = stage
                        status["clean"] = {"files": 3}
                    else:
                        status["clean"] = {"skipped": "local_index_missing"}
            except Exception as exc:
                status[job] = {"failed": type(exc).__name__, "detail": str(exc)[:200]}
                print("PREPARE_FAILED", job, type(exc).__name__, str(exc)[:200])
        if not stages:
            raise RuntimeError("No package prepared; nothing to publish")
        if args.dry_run:
            print("DRY_RUN: no Bunny API call, no upload.")
            print(json.dumps(status, ensure_ascii=False, indent=2))
            return 0
        api, state, storage = existing_api()
        pull = get_existing_pull(api, state, storage)
        base = "https://" + pull["hostname"] + "/iptv/"
        published_files = []
        for name, stage in stages.items():
            print("PUBLISHING", name, "to EXISTING Bunny zone")
            try:
                # Use existing Storage Zone write password and bounded retries.
                bunny.publish(api, state, storage, pull, stage)
                paths = [p.relative_to(stage).as_posix() for p in stage.rglob("*") if p.is_file()]
                published_files.extend(paths)
                status[name]["uploaded"] = len(paths)
            except Exception as exc:
                status[name]["upload_failed"] = type(exc).__name__
                print("UPLOAD_FAILED", name, type(exc).__name__, str(exc)[:200])
        report = {"playlist_base": base,
                  "published": sorted(set(published_files)),
                  "results": status,
                  "cdn_checks": {
                      p: verify_cdn(pull["hostname"], p)
                      for p in ("plutotv-lite.m3u", "plutotv-de.m3u",
                                "plutotv-erotic.m3u", "lampa-clean-lite.m3u",
                                "countries/ua.m3u")
                      if p in published_files
                  },
                  "checked_at_unix": int(time.time()),
                  "video_playback_checked": False}
        OUTPUT.joinpath("publication-report.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        print("\nPUBLIC_HUB_UPLOAD_SUMMARY")
        print("Files published:", len(set(published_files)))
        for p in sorted(set(published_files)):
            if p.startswith(("plutotv", "lampa-clean", "index.clean")) or p in ("countries/ua.m3u", "countries/us.m3u", "index.country.m3u"):
                print(base + p)
        print("CDN_CHECKS:", json.dumps(report["cdn_checks"]))
        print("LOCAL_REPORT:", OUTPUT / "publication-report.json")
        if any(v.get("upload_failed") or v.get("failed") for v in status.values()):
            return 2
        return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Prepare M3U locally; never connect to Bunny")
    parser.add_argument("--only", choices=("countries", "pluto", "clean"), nargs="+", help="Publish selected packages")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        return run(args)
    except (RuntimeError, ValueError, HTTPError, URLError, OSError, EOFError) as exc:
        print("ERROR:", type(exc).__name__, str(exc)[:400], file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
