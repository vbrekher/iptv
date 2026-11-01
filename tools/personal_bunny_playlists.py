#!/usr/bin/env python3
"""Build IPTV M3U playlists for personal hosting on Bunny Storage.

This is a fork-only, opt-in builder. It does NOT republish adult links via GitHub
Pages, modify the upstream safe-for-work generators, bypass authentication, or
invent streams for NSFW catalog entries without a known URL.

Python 3.9+, standard library only.
"""
from __future__ import annotations

import argparse
import csv
import getpass
import io
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen

HISTORIC_REF = "a1f14e961505010b0ef13bcd2a535f658ed51ac1"
HISTORIC_BASE = "https://raw.githubusercontent.com/iptv-org/iptv/" + HISTORIC_REF
OLD_ADULT = HISTORIC_BASE + "/categories/xxx.m3u"
OLD_INDEX = HISTORIC_BASE + "/index.nsfw.m3u"
COMMUNITY_ARCHIVE = "https://raw.githubusercontent.com/hujingguang/ChinaIPTV/557f01be7aa2e04271be26e18b78b695e31c04af/xxx.m3u8"
BLOCKLIST = "https://raw.githubusercontent.com/iptv-org/database/master/data/blocklist.csv"
PUBLIC_INDEX = "https://iptv-org.github.io/iptv/index.m3u"
PUBLIC_COUNTRY = "https://iptv-org.github.io/iptv/countries/{code}.m3u"
REGION_HOSTS = {
    "de": "storage.bunnycdn.com",
    "uk": "uk.storage.bunnycdn.com",
    "ny": "ny.storage.bunnycdn.com",
    "la": "la.storage.bunnycdn.com",
    "sg": "sg.storage.bunnycdn.com",
    "se": "se.storage.bunnycdn.com",
    "br": "br.storage.bunnycdn.com",
    "jh": "jh.storage.bunnycdn.com",
    "syd": "syd.storage.bunnycdn.com",
}
ID_RE = re.compile(r'\btvg-id="([^"]*)"')
GROUP_RE = re.compile(r'\bgroup-title="([^"]*)"')
VALID_COUNTRY = re.compile(r"^[a-z]{2}$")
VALID_ZONE = re.compile(r"^[a-zA-Z0-9_-]{1,80}$")
VALID_HOST = re.compile(r"^[a-z0-9.-]+$")


def fetch_text(url: str, max_bytes: int = 12_000_000) -> str:
    if not url.startswith("https://"):
        raise ValueError("Only HTTPS data sources are accepted")
    req = Request(url, headers={"User-Agent": "vbrekher-iptv-personal-builder/1.0"})
    with urlopen(req, timeout=45) as response:
        raw = response.read(max_bytes + 1)
    if len(raw) > max_bytes:
        raise ValueError("Remote source is unexpectedly large: " + url)
    return raw.decode("utf-8-sig")


def parse_m3u(text: str) -> list[tuple[str, str]]:
    """Return only complete EXTINF + HTTP(S) media URL pairs."""
    result = []
    meta = None
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("#EXTINF:"):
            meta = line
        elif meta is not None and line.startswith(("https://", "http://")):
            url = urlparse(line)
            if url.hostname and not url.username and not url.password:
                result.append((meta, line))
            meta = None
        elif line and not line.startswith("#"):
            meta = None
    return result


def channel_id(meta: str) -> str:
    match = ID_RE.search(meta)
    return match.group(1) if match else ""


def group_names(meta: str) -> list[str]:
    match = GROUP_RE.search(meta)
    return [x.strip() for x in match.group(1).split(";") if x.strip()] if match else ["Undefined"]


def with_group(meta: str, group: str) -> str:
    group = group.replace('"', "").replace("\n", " ").replace("\r", " ")
    if GROUP_RE.search(meta):
        return GROUP_RE.sub(lambda _: 'group-title="' + group + '"', meta, count=1)
    return meta.replace(",", ' group-title="' + group + '",', 1)


def serialize(entries: list[tuple[str, str]]) -> str:
    return "#EXTM3U\n" + "".join(meta + "\n" + url + "\n" for meta, url in entries)


def unique_entries(entries: list[tuple[str, str]]) -> list[tuple[str, str]]:
    seen, out = set(), []
    for meta, url in entries:
        key = (channel_id(meta), url)
        if key not in seen:
            out.append((meta, url))
            seen.add(key)
    return out


def slug(group: str) -> str:
    return re.sub(r"[^a-z0-9-]+", "-", group.lower().replace("_", "-")).strip("-")[:64]


def read_blocklist(text: str) -> dict[str, str]:
    records = {}
    for row in csv.DictReader(io.StringIO(text)):
        if row.get("channel") and row.get("reason"):
            records[row["channel"]] = row["reason"]
    if not records or "nsfw" not in records.values():
        raise ValueError("Unexpected or empty IPTV blocklist")
    return records


def adult_source(entries: list[tuple[str, str]], reasons: dict[str, str]) -> list[tuple[str, str]]:
    """A removed XXX archive plus NSFW-tagged streams in the historical index."""
    return [(meta, url) for meta, url in entries if reasons.get(channel_id(meta)) != "dmca"]


def adult_group(channel: str) -> str:
    if channel.startswith("AdultIPTVnet"):
        return "AdultIPTV"
    if channel.startswith("MyCamTV"):
        return "MyCamTV"
    return "Other Adult"


def prepare(output: Path, include_public: bool, country: str, include_community: bool = False) -> dict:
    print("Reading current blocklist...")
    reasons = read_blocklist(fetch_text(BLOCKLIST))
    nsfw_ids = {key for key, reason in reasons.items() if reason == "nsfw"}

    print("Reading frozen historical XXX list and pre-removal index...")
    category_archive = adult_source(parse_m3u(fetch_text(OLD_ADULT)), reasons)
    historical = [
        item for item in parse_m3u(fetch_text(OLD_INDEX))
        if channel_id(item[0]) in nsfw_ids and reasons.get(channel_id(item[0])) != "dmca"
    ]
    historic_raw = unique_entries(category_archive + historical)
    community = []
    if include_community:
        print("Reading opt-in, unverified community XXX candidate archive...")
        community = [
            item for item in parse_m3u(fetch_text(COMMUNITY_ARCHIVE))
            if channel_id(item[0]) in nsfw_ids and reasons.get(channel_id(item[0])) != "dmca"
        ]
    adult_raw = unique_entries(historic_raw + community)
    if not adult_raw:
        raise RuntimeError("No historic adult URLs found; refusing to generate empty playlist")

    adult = [(with_group(meta, "XXX"), url) for meta, url in adult_raw]
    subgroups = defaultdict(list)
    for meta, url in adult_raw:
        subgroups[adult_group(channel_id(meta))].append((with_group(meta, adult_group(channel_id(meta))), url))

    output.mkdir(parents=True, exist_ok=True)
    (output / "categories").mkdir(exist_ok=True)
    (output / "catalog").mkdir(exist_ok=True)
    (output / "countries").mkdir(exist_ok=True)
    (output / "adult.m3u").write_text(serialize(adult), encoding="utf-8")
    (output / "categories" / "xxx.m3u").write_text(serialize(adult), encoding="utf-8")

    for name, entries in subgroups.items():
        (output / "categories" / (slug(name) + ".m3u")).write_text(
            serialize(entries), encoding="utf-8"
        )

    public = []
    if include_public:
        print("Reading current public index...")
        public = parse_m3u(fetch_text(PUBLIC_INDEX))
        # Keep the original public index entries but exclude explicit DMCA records.
        public = [(m, u) for m, u in public if reasons.get(channel_id(m)) != "dmca"]
        public = unique_entries(public)
        print("Reading current country list: " + country)
        country_playlist = parse_m3u(fetch_text(PUBLIC_COUNTRY.format(code=country)))
        country_playlist = [(m, u) for m, u in country_playlist if reasons.get(channel_id(m)) != "dmca"]
        (output / "countries" / (country + ".m3u")).write_text(
            serialize(unique_entries(country_playlist)), encoding="utf-8"
        )

    combined = unique_entries(public + adult)
    (output / "index.m3u").write_text(serialize(combined), encoding="utf-8")
    (output / "index.category.m3u").write_text(serialize(combined), encoding="utf-8")

    # Generate convenient category URLs for Lampa from actual available streams.
    categories = defaultdict(list)
    for meta, url in public:
        for name in group_names(meta):
            category = slug(name)
            if category and category not in ("xxx", "adultiptv", "mycamtv", "other-adult"):
                categories[category].append((with_group(meta, name), url))
    for name, entries in categories.items():
        (output / "categories" / (name + ".m3u")).write_text(
            serialize(unique_entries(entries)), encoding="utf-8"
        )

    counts = Counter(channel_id(meta) for meta, _ in adult_raw)
    with (output / "catalog" / "nsfw-status.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["channel_id", "status", "historical_urls"])
        for channel in sorted(nsfw_ids):
            writer.writerow([
                channel, "historical_url_unverified" if counts[channel] else "no_known_url",
                counts[channel]
            ])

    result = {
        "nsfw_blocklist_channel_ids": len(nsfw_ids),
        "nsfw_ids_with_historical_url": sum(1 for key in nsfw_ids if counts[key]),
        "nsfw_ids_without_historical_url": sum(1 for key in nsfw_ids if not counts[key]),
        "historical_adult_entries": len(historic_raw),
        "community_archive_enabled": include_community,
        "community_archive_entries": len(community),
        "additional_candidate_entries": len(adult) - len(historic_raw),
        "candidate_adult_entries_total": len(adult),
        "candidate_nsfw_ids_with_urls": len({channel_id(meta) for meta, _ in adult_raw if channel_id(meta) in nsfw_ids}),
        "public_entries": len(public),
        "combined_entries": len(combined),
        "category_playlists": len(categories) + len(subgroups) + 1,
        "country": country if include_public else None,
        "live_streams_tested": 0,
        "source_snapshot": HISTORIC_REF,
        "note": "Historical URL candidates, NOT proof of currently available video."
    }
    (output / "catalog" / "report.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result


def ask(name: str, question: str, secret: bool = False, default: str = "") -> str:
    env = os.environ.get(name)
    if env:
        return env.strip()
    prompt = question + (" [" + default + "]" if default else "") + ": "
    value = getpass.getpass(prompt) if secret else input(prompt)
    return value.strip() or default


def publish(output: Path, prefix: str) -> str:
    zone = ask("BUNNY_STORAGE_ZONE", "Bunny Storage Zone")
    region = ask("BUNNY_STORAGE_REGION", "Primary storage region (de/uk/ny/...)", default="de").lower()
    cdn = ask("BUNNY_CDN_HOST", "Connected Pull Zone hostname (example.b-cdn.net)").lower()
    password = ask("BUNNY_STORAGE_PASSWORD", "Storage Zone password", secret=True)

    if not VALID_ZONE.fullmatch(zone):
        raise ValueError("Invalid Storage Zone name")
    if region not in REGION_HOSTS:
        raise ValueError("Unsupported Bunny primary region: " + region)
    if not VALID_HOST.fullmatch(cdn) or "/" in cdn or "." not in cdn:
        raise ValueError("Enter a hostname only (no https:// or paths)")
    if not password:
        raise ValueError("Storage Zone password is required")

    host = REGION_HOSTS[region]
    files = sorted(path for path in output.rglob("*") if path.is_file())
    print(f"Uploading {len(files)} small playlist/catalog files to {zone}/{prefix}/ ...")
    for path in files:
        rel = path.relative_to(output).as_posix()
        url = "https://" + host + "/" + quote(zone, safe="") + "/" + quote(prefix, safe="/") + "/" + quote(rel, safe="/")
        mime = "application/vnd.apple.mpegurl" if path.suffix == ".m3u" else (
            "text/csv; charset=utf-8" if path.suffix == ".csv" else "application/json"
        )
        request = Request(
            url,
            data=path.read_bytes(),
            method="PUT",
            headers={"AccessKey": password, "Content-Type": mime},
        )
        with urlopen(request, timeout=40) as response:
            if response.status not in (200, 201):
                raise RuntimeError(f"Upload failed for {rel}: HTTP {response.status}")
        print("Uploaded:", rel)
    base = "https://" + cdn + "/" + prefix
    print("\nBunny CDN playlists (after propagation):")
    for name in ("index.m3u", "adult.m3u", "categories/xxx.m3u",
                 "categories/adultiptv.m3u", "categories/mycamtv.m3u",
                 "countries/ua.m3u"):
        if (output / name).exists():
            print(base + "/" + name)
    print("\nBunny caches may require purge or a short TTL after future updates.")
    return base


def self_test() -> None:
    example = ('#EXTM3U\n#EXTINF:-1 tvg-id="AdultIPTVnetOne.us" group-title="XXX",One\n'
               'https://example.org/a.m3u8\n#EXTINF:-1 tvg-id="AdultIPTVnetOne.us",One\n'
               'https://example.org/a.m3u8\n')
    items = parse_m3u(example)
    assert len(items) == 2
    assert len(unique_entries(items)) == 1
    assert channel_id(items[0][0]) == "AdultIPTVnetOne.us"
    assert group_names(with_group(items[1][0], "XXX")) == ["XXX"]
    assert slug("Other Adult") == "other-adult"
    assert len(parse_m3u("#EXTM3U\n#EXTINF:-1,Unknown\n")) == 0
    assert read_blocklist("channel,reason,ref\na.us,nsfw,here\nb.us,dmca,there\n")["b.us"] == "dmca"
    assert not adult_source([(items[0][0], items[0][1])], {"AdultIPTVnetOne.us": "dmca"})
    print("SELF_TEST_PASS")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="dist/iptv", help="Output directory")
    parser.add_argument("--country", default="ua", help="Two-letter country playlist mirror")
    parser.add_argument("--no-public", action="store_true", help="Adult-only index, no public index")
    parser.add_argument("--publish", action="store_true", help="Also upload to connected Bunny Storage")
    parser.add_argument("--include-community", action="store_true", help="Opt in to extra UNVERIFIED community M3U URLs")
    parser.add_argument("--prefix", default="iptv", help="Bunny Storage folder (default: iptv)")
    parser.add_argument("--self-test", action="store_true", help="Run offline parser sanity tests")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if not VALID_COUNTRY.fullmatch(args.country):
        parser.error("--country must be a two-letter lowercase country code")
    if not re.fullmatch(r"[a-z0-9_-]+(?:/[a-z0-9_-]+)*", args.prefix):
        parser.error("--prefix must be a safe folder name, such as iptv")
    try:
        output = Path(args.output)
        prepare(output, not args.no_public, args.country, args.include_community)
        if args.publish:
            publish(output, args.prefix)
    except (HTTPError, URLError, ValueError, RuntimeError, OSError, EOFError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
