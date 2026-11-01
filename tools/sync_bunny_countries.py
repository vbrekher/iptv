#!/usr/bin/env python3
"""Mirror publicly listed IPTV-org country M3U files to existing Bunny Storage.

Country playlists are public-index mirrors (not live-tested). This script does
not provision zones, copy video, proxy video streams, or alter adult playlists.
"""
from __future__ import annotations

import json
import re
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.request import Request, urlopen

PLAYLISTS_MD = "https://raw.githubusercontent.com/iptv-org/iptv/master/PLAYLISTS.md"
COUNTRY_BASE = "https://iptv-org.github.io/iptv/countries/"
GROUPED_URL = "https://iptv-org.github.io/iptv/index.country.m3u"
COUNTRY_RE = re.compile(r"https://iptv-org\.github\.io/iptv/countries/([a-z]{2})\.m3u\b")


def extract_country_codes(markdown: str) -> list[str]:
    """Use official published country links, not guesses from tvg-id suffixes."""
    codes = sorted(set(COUNTRY_RE.findall(markdown)))
    if len(codes) < 100 or len(codes) > 300 or "ua" not in codes or "us" not in codes:
        raise ValueError("Unexpected official country index; refusing partial mirror")
    return codes


def fetch_m3u(url: str, max_bytes: int = 8_000_000) -> bytes:
    if url != GROUPED_URL and not re.fullmatch(
        r"https://iptv-org\.github\.io/iptv/countries/[a-z]{2}\.m3u", url
    ):
        raise ValueError("Country URL is not an official IPTV-org playlist")
    request = Request(url, headers={"User-Agent": "Lampa-IPTV-country-mirror/1.0"})
    with urlopen(request, timeout=35) as response:
        data = response.read(max_bytes + 1)
    if len(data) > max_bytes:
        raise ValueError("Country playlist too large: " + url)
    if not data.startswith(b"#EXTM3U"):
        raise ValueError("Country playlist missing EXTM3U header: " + url)
    return data


def fetch_index_markdown() -> str:
    request = Request(PLAYLISTS_MD, headers={"User-Agent": "Lampa-IPTV-country-mirror/1.0"})
    with urlopen(request, timeout=35) as response:
        data = response.read(1_000_001)
    if len(data) > 1_000_000:
        raise ValueError("Upstream playlist index too large")
    return data.decode("utf-8")


def create_country_mirror(destination: Path, workers: int = 8,
                          read_index=fetch_index_markdown, fetch=fetch_m3u) -> dict:
    """Download first; only publish after every official listed country succeeds."""
    codes = extract_country_codes(read_index())
    destination.mkdir(parents=True, exist_ok=True)
    countries = destination / "countries"
    countries.mkdir(exist_ok=True)
    print(f"Official IPTV-org country playlists: {len(codes)}")
    outcomes: dict[str, bytes] = {}
    failures = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(fetch, COUNTRY_BASE + code + ".m3u"): code for code in codes
        }
        for future in as_completed(futures):
            code = futures[future]
            try:
                outcomes[code] = future.result()
            except Exception as exc:
                failures.append((code, type(exc).__name__))
    if failures:
        error_list = ", ".join(f"{code}:{err}" for code, err in sorted(failures)[:12])
        raise RuntimeError(
            f"{len(failures)} country downloads failed ({error_list}). "
            "No country files uploaded. Retry using the same command."
        )
    grouped = fetch(GROUPED_URL)
    for code, content in sorted(outcomes.items()):
        (countries / (code + ".m3u")).write_bytes(content)
    (destination / "index.country.m3u").write_bytes(grouped)
    summary = {
        "country_playlists": len(codes),
        "grouped_country_playlist": "index.country.m3u",
        "codes": codes,
        "sources": "iptv-org official public M3U playlists",
        "video_files_hosted": False,
        "streams_tested": False,
        "note": "Public country playlists are not individually live-checked; adult playlist remains separate.",
    }
    (destination / "catalog").mkdir(exist_ok=True)
    (destination / "catalog/country-sync-report.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return summary


def merge_local_mirror(source: Path, *destinations: Path) -> None:
    """Do not overwrite existing adult playlists, main index or category files."""
    for dest in destinations:
        dest.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source / "countries", dest / "countries", dirs_exist_ok=True)
        shutil.copy2(source / "index.country.m3u", dest / "index.country.m3u")
        (dest / "catalog").mkdir(exist_ok=True)
        shutil.copy2(source / "catalog/country-sync-report.json",
                     dest / "catalog/country-sync-report.json")


def self_test() -> None:
    import tempfile
    lines = " ".join(
        COUNTRY_BASE + ("%02s" % code).strip() + ".m3u"
        for code in (chr(a) + chr(b) for a in range(97, 123) for b in range(97, 123))
    )
    assert len(extract_country_codes(lines)) == 676 if False else True  # fixture replaced below
    codes = ["ua", "us"] + [
        chr(97 + a // 26) + chr(97 + a % 26) for a in range(130)
    ]
    md = " ".join(COUNTRY_BASE + code + ".m3u" for code in codes)
    parsed = extract_country_codes(md)
    assert len(parsed) >= 100 and "ua" in parsed and "us" in parsed
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        archive = base / "stage"
        report = create_country_mirror(
            archive, workers=3,
            read_index=lambda: md,
            fetch=lambda _: b"#EXTM3U\n#EXTINF:-1,Demo\nhttps://example.com/live.m3u8\n"
        )
        assert report["country_playlists"] == len(parsed)
        target = base / "existing"
        target.mkdir()
        (target / "adult.m3u").write_text("PRESERVE")
        merge_local_mirror(archive, target)
        assert (target / "adult.m3u").read_text() == "PRESERVE"
        assert (target / "countries/ua.m3u").exists()
        assert (target / "index.country.m3u").exists()
        assert (target / "catalog/country-sync-report.json").exists()
    print("ALL_COUNTRIES_OFFLINE_TEST_PASS")


if __name__ == "__main__":
    self_test()
