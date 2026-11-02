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
ALLOWED = {"user_report_cdn_verified", "user_log_uploaded", "publication_unconfirmed", "cdn_check_failed"}


def validate() -> dict:
    catalog = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert catalog["schema_version"] == 1
    expected = {"countries": 188, "categories": 34, "featured": 15, "links": 237}
    assert catalog["totals"] == expected, (catalog["totals"], expected)
    items = catalog["items"]
    assert len(items) == expected["links"]
    assert len({item["id"] for item in items}) == len(items)
    assert len({item["path"] for item in items}) == len(items)
    assert len({item["url"] for item in items}) == len(items)
    assert {x["status"] for x in items} <= ALLOWED
    from collections import Counter
    evidence_counts = Counter(x["status"] for x in items)
    assert sum(evidence_counts.values()) == expected["links"], evidence_counts
    assert evidence_counts["user_report_cdn_verified"] == 237, evidence_counts
    assert catalog["verification"]["evidence_file"] == "catalog/cdn-verification-2026-11-02.json"
    audit = json.loads((ROOT / catalog["verification"]["evidence_file"]).read_text(encoding="utf-8"))
    assert audit["total"] == 237 and audit["passed"] == 237 and audit["failed"] == 0
    assert audit["video_playback_checked"] is False
    checks = {x["path"]: x for x in audit["results"]}
    assert len(checks) == 237
    for item in items:
        check = checks[item["path"]]
        assert check["url"] == item["url"], item["path"]
        assert check["ok"] is True and check["http_status"] in (200, 206)
        assert check["m3u_header"] is True and check["error"] is None

    assert all(x.get("evidence") for x in items if x["status"] == "user_report_cdn_verified")
    countries_ordered = [x["path"] for x in items if x["group"] == "country"]
    assert countries_ordered[:2] == ["countries/ru.m3u", "countries/ua.m3u"]
    assert len(countries_ordered) == 188
    directory = DIRECTORY.read_text(encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    assert len(readme) >= 5000 and len(directory) >= 25000
    assert "adulttest" not in readme.lower() and "adulttest" not in directory.lower()
    assert "iptv-org/iptv" in readme and "iptv-org/iptv" in directory
    assert "PUBLIC_RELEASE.md" in readme and "FORK_CHANGELOG.md" in readme
    assert "plutotv-lite.m3u" in readme
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
    assert all("adulttest" not in x["path"].lower() for x in items)
    # Every M3U URL is documented in all three languages, not just README.
    localized = {
        "en": ROOT / "docs/en/BUNNY_PLAYLISTS.md",
        "nl": ROOT / "docs/nl/BUNNY_PLAYLISTS.md",
        "ru": DIRECTORY,
    }
    for lang, file in localized.items():
        content = file.read_text(encoding="utf-8")
        assert len(content) > 25000, lang
        assert "adulttest.m3u" not in content.lower()
        icons = {"user_report_cdn_verified": "✅ CDN checked in terminal", "user_log_uploaded": "☑️",
                 "publication_unconfirmed": "○", "cdn_check_failed": "⚠️"}
        lines = content.splitlines()
        for x in items:
            assert x["url"] in content, (lang, x["path"])
            matches = [line for line in lines if line.startswith("|")
                       and x["url"] in line]
            assert len(matches) == 1, (lang, x["path"], len(matches))
            assert matches[0].rstrip().endswith("| " + icons[x["status"]] + " |"), (
                lang, x["path"], x["status"])
        assert content.index("/countries/ru.m3u") < content.index("/countries/ua.m3u"), lang
    readmes = {
        "en": README,
        "nl": ROOT / "README.nl.md",
        "ru": ROOT / "README.ru.md",
    }
    for lang, file in readmes.items():
        content = file.read_text(encoding="utf-8")
        assert len(content) >= 6500, lang
        assert "/countries/ru.m3u" in content and "/countries/ua.m3u" in content
        assert content.index("/countries/ru.m3u") < content.index("/countries/ua.m3u"), lang
        assert "README.nl.md" in content and "README.ru.md" in content
        assert "adulttest.m3u" not in content.lower()
    required_docs = (
        "BUNNY_PLAYLISTS.md", "BUNNY_ONE_CLICK.md", "PERSONAL_BUNNY_IPTV.md",
        "PUBLIC_RELEASE.md", "FORK_CHANGELOG.md", "QIST_PLUTOTV.md",
    )
    for lang in ("en", "nl"):
        for name in required_docs:
            path = ROOT / "docs" / lang / name
            assert path.is_file(), str(path)
            assert len(path.read_text(encoding="utf-8")) >= 600, str(path)
    for name in ("FAQ.nl.md", "CONTRIBUTING.nl.md", "PLAYLISTS.nl.md"):
        assert (ROOT / name).is_file(), name
    for name in ("geo-blocking.md", "playlists.md", "scripts.md",
                 "stream-description-scheme.md", "stream-id.md",
                 "stream-testing.md", "tokenized-links.md", "workflows.md",
                 "xtream-codes.md"):
        assert (ROOT / "docs/nl" / name).is_file(), name
    if re.search(r"(?:api[_-]?key|password|secret)\s*[:=]\s*['\"][A-Za-z0-9_-]{16,}", directory, re.I):
        raise AssertionError("Potential credential-like literal in public M3U documentation")
    return {"manifest_items": len(items), "groups": counts, "evidence": dict(evidence_counts), "languages": ["en", "nl", "ru"]}


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
