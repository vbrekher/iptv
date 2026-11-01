#!/usr/bin/env python3
"""Mirror free Pluto TV channel listings into the EXISTING Bunny Storage Zone.

Pluto streams point to third-party playlist transport (jmp2.uk) and may be
geo-blocked. This is not an official Pluto TV API or a playback guarantee.
Only M3U metadata is hosted on Bunny; no video content is downloaded/proxied.
"""
from __future__ import annotations

import argparse
import getpass
import json
import re
import sys
import tempfile
import time
from collections import defaultdict
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

import auto_bunny_setup as bunny
import personal_bunny_playlists as m3u

UPSTREAM = "https://raw.githubusercontent.com/BuddyChewChew/app-m3u-generator/main/playlists/"
ALL = UPSTREAM + "plutotv_all.m3u"
GERMANY = UPSTREAM + "plutotv_de.m3u"
FILES = ("plutotv.m3u", "plutotv-lite.m3u",
         "plutotv-de.m3u", "plutotv-erotic.m3u")
EXTRAS = ("plutotv-us.m3u", "plutotv-gb.m3u")
COUNTRY_GROUPS = ("United States", "Germany", "United Kingdom", "France",
                  "Spain", "Italy", "Canada", "Brazil", "Argentina", "Mexico",
                  "Chile", "Denmark", "Sweden", "Norway")
# Reject unexpected URL types: never publish subscribed/private/tokenized URLs
# added to a source file at some future date. jmp2.uk is a third-party provider.
JMP = re.compile(r"^https://jmp2\.uk/plu-[0-9a-f]{24}\.m3u8$", re.IGNORECASE)
LOGO = re.compile(r'\btvg-logo="([^"]*)"')
GROUP = re.compile(r'\bgroup-title="([^"]*)"')
TITLE = re.compile(r"^#EXTINF:[^,]*,(.*)$")
URL_TVG = re.compile(r'\burl-tvg="([^"]*)"')


def download(url: str) -> str:
    if url not in (ALL, GERMANY):
        raise ValueError("unrecognized_upstream_playlist")
    req = Request(url, headers={"User-Agent": "Lampa-Bunny-PlutoTV/1.0"})
    with urlopen(req, timeout=45) as resp:
        raw = resp.read(2_000_001)
    if len(raw) > 2_000_000:
        raise ValueError("upstream_m3u_too_large")
    return raw.decode("utf-8-sig")


def extract(text: str, min_count: int, max_count: int) -> tuple[str, list[tuple[str, str]]]:
    lines = text.splitlines()
    if not lines or not lines[0].startswith("#EXTM3U"):
        raise ValueError("missing_m3u_header")
    pending = None
    entries = []
    for line in lines[1:]:
        line = line.strip()
        if line.startswith("#EXTINF:"):
            if pending is not None:
                raise ValueError("missing_stream_url")
            match = TITLE.match(line)
            if not match or not match.group(1).strip():
                raise ValueError("invalid_channel_title")
            groups = GROUP.findall(line)
            if len(groups) != 1 or not groups[0].strip() or ";" in groups[0]:
                raise ValueError("invalid_composite_channel_group")
            logos = LOGO.findall(line)
            if len(logos) > 1 or any(not urlsplit(u).scheme == "https" for u in logos if u):
                raise ValueError("invalid_logo")
            pending = line
        elif pending is not None and line.startswith(("https://", "http://")):
            if not JMP.fullmatch(line):
                raise ValueError("unexpected_stream_url_scheme_or_host")
            entries.append((pending, line))
            pending = None
        elif pending is not None and line and not line.startswith("#"):
            raise ValueError("unexpected_stream_reference")
    if pending is not None:
        raise ValueError("unterminated_channel")
    if not (min_count <= len(entries) <= max_count):
        raise ValueError(f"upstream_count_out_of_bounds_{len(entries)}")
    epg = URL_TVG.search(lines[0])
    epg_url = epg.group(1) if epg else ""
    if epg_url and not epg_url.startswith("https://"):
        raise ValueError("invalid_epg_url")
    return epg_url, entries


def serialize(entries: list[tuple[str, str]], epg: str = "") -> str:
    if not entries:
        raise ValueError("empty_generated_playlist")
    head = "#EXTM3U" + (' url-tvg="' + epg + '"' if epg else "") + "\n"
    return head + "".join(meta + "\n" + url + "\n" for meta, url in entries)


def unique(items: list[tuple[str, str]]) -> list[tuple[str, str]]:
    result = []
    seen = set()
    for meta, url in items:
        # Region-specific copies of the same channel can exist; dedupe only exact
        # metadata+URL combinations so the original all-region catalog is retained.
        key = (meta, url)
        if key not in seen:
            seen.add(key)
            result.append((meta, url))
    return result


def round_robin(entries: list[tuple[str, str]], limit: int = 240
                ) -> list[tuple[str, str]]:
    groups: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for item in entries:
        groups[GROUP.search(item[0]).group(1)].append(item)
    order = sorted(groups)
    selected, channels = [], set()
    index = 0
    while len(selected) < limit:
        progressed = False
        for country in order:
            if index >= len(groups[country]):
                continue
            meta, url = groups[country][index]
            # Pluto's 24-hex channel ID in the stream path
            cid = url.split("/plu-", 1)[-1].split(".", 1)[0]
            if cid in channels:
                continue
            selected.append((meta, url))
            channels.add(cid)
            progressed = True
            if len(selected) >= limit:
                break
        if not progressed and all(index >= len(groups[c]) - 1 for c in order):
            break
        index += 1
    return selected


def create(source_all: str, source_de: str, output: Path) -> dict:
    all_epg, all_entries = extract(source_all, 500, 6000)
    de_epg, de_entries = extract(source_de, 100, 400)
    all_entries = unique(all_entries)
    de_entries = unique(de_entries)
    fast = [row for row in de_entries
            if "Sinnliche Fantasien" in GROUP.search(row[0]).group(1)]
    if not (1 <= len(fast) <= 30):
        raise ValueError("German erotic FAST category changed or missing; refusing incomplete output")
    lite = round_robin(all_entries, limit=240)
    if len(lite) < 100:
        raise ValueError("lightweight profile unexpectedly small")
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "plutotv.m3u": serialize(all_entries, all_epg),
        "plutotv-lite.m3u": serialize(lite),  # No huge EPG requested by Tizen.
        "plutotv-de.m3u": serialize(de_entries, de_epg),
        "plutotv-erotic.m3u": serialize(fast, de_epg),
    }
    # Intentional aliases from official "all" metadata, avoid fetching more
    # hosts and keep bounded count for Samsung.
    for suffix, group in (("us", "United States"), ("gb", "United Kingdom")):
        regional = [x for x in all_entries if GROUP.search(x[0]).group(1) == group]
        if regional:
            paths[f"plutotv-{suffix}.m3u"] = serialize(regional, all_epg)
    for name, text in paths.items():
        (output / name).write_text(text, encoding="utf-8")
    report = {
        "upstream": "BuddyChewChew/app-m3u-generator",
        "upstream_all_entries": len(all_entries),
        "upstream_germany_entries": len(de_entries),
        "erotic_fast_channels_germany": len(fast),
        "files": {name: {
            "entries": len(m3u.parse_m3u(text)),
            "bytes": len(text.encode("utf-8"))
        } for name, text in paths.items()},
        "all_country_groups": sorted({GROUP.search(x[0]).group(1) for x in all_entries}),
        "direct_stream_host": "jmp2.uk (third-party, not official pluto.tv)",
        "streams_playback_tested": False,
        "geo_restrictions_removed": False,
        "rights_to_rebroadcast_video_verified": False,
        "adult_hardcore_claimed": False,
        "note": "Only playlist metadata is uploaded; no video is hosted on Bunny."
    }
    return report


def ensure_existing_bunny():
    if not bunny.STATE.is_file():
        raise RuntimeError("Missing .bunny-iptv-state.json. Run inside the EXISTING ~/iptv-bunny directory")
    state = bunny.load_state(bunny.STATE)
    print("Existing resource group:", state["name"])
    key = getpass.getpass("Bunny Account API Key (hidden): ")
    if not key:
        raise ValueError("Missing Bunny Account API Key")
    api = bunny.BunnyAPI(key)
    key = ""
    if not bunny.named(bunny.list_zones(api, "storagezone"), state["name"] + "-storage"):
        raise RuntimeError("Storage Zone missing; refusing to create a new paid resource")
    if not bunny.named(bunny.list_zones(api, "pullzone"), state["name"] + "-cdn"):
        raise RuntimeError("Pull Zone missing; refusing to create a new paid resource")
    storage = bunny.storage_zone(api, state)
    pull = bunny.pull_zone(api, state, storage["id"])
    return api, state, storage, pull


def verify_cdn(hostname: str, filename: str) -> bool:
    for attempt in range(3):
        try:
            req = Request("https://" + hostname + "/iptv/" + filename + "?v=" +
                          str(int(time.time())), headers={"User-Agent": "Lampa-PlutoTV-Verify/1.0"})
            with urlopen(req, timeout=12) as response:
                if response.status == 200 and response.read(8).startswith(b"#EXTM3U"):
                    return True
        except (HTTPError, URLError, TimeoutError, OSError):
            pass
        if attempt < 2:
            time.sleep(2)
    return False


def publish(local: Path) -> int:
    needed = ["plutotv.m3u", "plutotv-lite.m3u",
              "plutotv-de.m3u", "plutotv-erotic.m3u"]
    if any(not (local / p).is_file() for p in needed):
        raise RuntimeError("Local PlutoTV playlist build missing; run normally first")
    api, state, storage, pull = ensure_existing_bunny()
    with tempfile.TemporaryDirectory(prefix="lampa-pluto-upload-") as temp:
        staged = Path(temp)
        for path in sorted(local.glob("plutotv*.m3u")):
            staged.joinpath(path.name).write_bytes(path.read_bytes())
        # Only staged Pluto M3U files are uploaded to the iptv/ prefix.
        bunny.publish(api, state, storage, pull, staged)
    base = "https://" + pull["hostname"] + "/iptv/"
    print("\nPLUTOTV_UPLOAD_COMPLETE")
    for name in sorted(x.name for x in local.glob("plutotv*.m3u")):
        print(base + name)
    for name in ("plutotv-lite.m3u", "plutotv-de.m3u", "plutotv-erotic.m3u"):
        print("CDN_CHECK", name, "VERIFIED" if verify_cdn(pull["hostname"], name) else "NOT_VERIFIED")
    return 0


def test():
    def row(i, group="United States"):
        cid = f"{i:024x}"
        return (f'#EXTINF:-1 tvg-id="{cid}" tvg-logo="https://images.pluto.tv/logo.png" '
                f'group-title="{group}",Example {i}\nhttps://jmp2.uk/plu-{cid}.m3u8')
    all_src = "#EXTM3U\n" + "\n".join(row(i, ["Germany", "United States", "United Kingdom"][i % 3]) for i in range(600))
    de_src = "#EXTM3U\n" + "\n".join(row(1000 + i, "Sinnliche Fantasien" if i < 8 else "News") for i in range(150))
    with tempfile.TemporaryDirectory() as temp:
        path = Path(temp)
        report = create(all_src, de_src, path)
        assert report["upstream_all_entries"] == 600
        assert report["erotic_fast_channels_germany"] == 8
        assert report["files"]["plutotv-lite.m3u"]["entries"] == 240
        assert report["files"]["plutotv-erotic.m3u"]["entries"] == 8
        for f in path.glob("*.m3u"):
            text = f.read_text()
            assert text.startswith("#EXTM3U")
            assert all(";" not in GROUP.search(meta).group(1) for meta, _ in m3u.parse_m3u(text))
        # Rejection must fail closed.
        for edited in (
            all_src.replace("https://jmp2.uk/", "https://example.com/", 1),
            all_src.replace("https://jmp2.uk/", "http://jmp2.uk/", 1),
            all_src.replace('group-title="Germany"', 'group-title="Germany;Other"', 1)
        ):
            try:
                create(edited, de_src, path)
                raise AssertionError("Unsafe/incorrect source entry accepted")
            except ValueError:
                pass
    print("PLUTOTV_OFFLINE_TEST_PASS")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="dist/plutotv")
    parser.add_argument("--dry-run", action="store_true", help="Prepare local files only")
    parser.add_argument("--publish-only", action="store_true", help="Reuse saved Pluto M3Us and publish")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        test()
        return 0
    if args.dry_run and args.publish_only:
        parser.error("Do not combine --dry-run and --publish-only")
    local = Path(args.output)
    try:
        if not args.publish_only:
            print("Fetching Pluto TV all regions and Germany...")
            report = create(download(ALL), download(GERMANY), local)
            (local / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
            print("Generated:", json.dumps(report["files"], indent=2))
            print("Report:", local / "report.json")
        if args.dry_run:
            print("DRY RUN: nothing uploaded to Bunny")
            return 0
        return publish(local)
    except (RuntimeError, ValueError, HTTPError, URLError, OSError, EOFError) as e:
        print("ERROR:", type(e).__name__, str(e), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
