#!/usr/bin/env python3
"""Verify the fork's public M3U catalog, status labels and GitHub docs offline."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "catalog/bunny-playlists.json"
DIRECTORY = ROOT / "docs/BUNNY_PLAYLISTS.md"
README = ROOT / "README.md"
ALLOWED = {"user_report_cdn_verified", "user_log_uploaded", "publication_unconfirmed"}


def validate() -> dict:
    catalog = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert catalog["schema_version"] == 1
    expected = {"countries": 188, "categories": 34, "featured": 16, "links": 238}
    assert catalog["totals"] == expected, (catalog["totals"], expected)
    items = catalog["items"]
    assert len(items) == expected["links"]
    assert len({item["id"] for item in items}) == len(items)
    assert len({item["path"] for item in items}) == len(items)
    assert len({item["url"] for item in items}) == len(items)
    assert {x["status"] for x in items} == ALLOWED
    directory = DIRECTORY.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    assert len(readme) >= 5000 and len(directory) >= 25000
    assert "iptv-org/iptv" in readme and "iptv-org/iptv" in directory
    assert "PUBLIC_RELEASE.md" in readme and "FORK_CHANGELOG.md" in readme
    assert "adulttest.m3u" in readme and "plutotv-lite.m3u" in readme
    counts = {"country": 0, "category": 0, "main": 0, "adult": 0, "tizen": 0, "pluto": 0}
    for x in items:
        assert x["group"] in counts, x
        counts[x["group"]] += 1
        url = x["url"]
        parts = urlsplit(url)
        assert parts.scheme == "https"
        assert parts.netloc == "lampa-iptv-875323ab-cdn.b-cdn.net"
        assert parts.path == "/iptv/" + x["path"]
        assert not parts.username and not parts.password and not parts.query and not parts.fragment
        assert re.fullmatch(r"[a-z0-9.-]+(?:/[a-z0-9.-]+)*\.m3u", x["path"]), x["path"]
        assert x["status"] in ALLOWED
        assert url in directory, "Missing direct CDN URL in docs: " + x["path"]
        if x["group"] == "country":
            assert re.fullmatch(r"countries/[a-z]{2}\.m3u", x["path"])
            assert x["flag"] and len(x["flag"]) <= 4
            assert x["country_name"]
        if x["group"] == "category":
            assert x["path"].startswith("categories/")
    assert counts["country"] == expected["countries"], counts
    assert counts["category"] == expected["categories"], counts
    assert sum(counts[k] for k in ("main", "adult", "tizen", "pluto")) == expected["featured"]
    ua = next(x for x in items if x["path"] == "countries/ua.m3u")
    assert ua["status"] == "user_log_uploaded"
    adulttest = next(x for x in items if x["path"] == "adulttest.m3u")
    assert adulttest["status"] == "user_report_cdn_verified"
    for path in ("plutotv-lite.m3u", "plutotv.m3u", "index.country.m3u",
                 "lampa-clean-lite.m3u", "countries/us.m3u"):
        assert next(x for x in items if x["path"] == path)["status"] == "publication_unconfirmed"
    if re.search(r"(?:api[_-]?key|password|secret)\s*[:=]\s*['\"][A-Za-z0-9_-]{16,}", directory, re.I):
        raise AssertionError("Potential credential-like literal in public M3U documentation")
    return {"verified_manifest_items": len(items), "groups": counts}


def main():
    try:
        report = validate()
    except (AssertionError, ValueError, OSError, KeyError) as exc:
        print("PUBLIC_HUB_CATALOG_FAIL", str(exc), file=sys.stderr)
        return 1
    print("PUBLIC_HUB_CATALOG_PASS", json.dumps(report, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
