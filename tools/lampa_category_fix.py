#!/usr/bin/env python3
"""Repair Lampa M3U category metadata. One canonical category per channel.

This module never discovers streams or claims their availability. It only
rewrites group-title and emits small M3U variants from existing local files.
"""
from __future__ import annotations

import json
import tempfile
from collections import Counter
from pathlib import Path

import build_lampa_lite as lite
import personal_bunny_playlists as m3u

# Actual IPTV-org categories, intentionally bounded and not generated from
# arbitrary semicolon-delimited metadata or a new category per combination.
CATEGORIES = (
    "Animation", "Auto", "Business", "Classic", "Comedy", "Cooking", "Culture",
    "Documentary", "Education", "Entertainment", "Family", "General",
    "Interactive", "Kids", "Legislative", "Lifestyle", "Movies", "Music",
    "News", "Outdoor", "Public", "Relax", "Religious", "Science", "Series",
    "Shop", "Sports", "Travel", "Weather", "XXX",
)
CANON = {x.lower(): x for x in CATEGORIES}
# Semantic specificity wins when a channel belongs to several categories.
PRIORITY = (
    "XXX", "Series", "Movies", "Documentary", "Sports", "News", "Music",
    "Kids", "Animation", "Science", "Education", "Cooking", "Comedy",
    "Business", "Auto", "Travel", "Outdoor", "Classic", "Culture",
    "Legislative", "Religious", "Family", "Entertainment", "Lifestyle",
    "Public", "Weather", "Relax", "Shop", "Interactive", "General",
)
RANK = {name: i for i, name in enumerate(PRIORITY)}


def pick_group(meta: str, adult: bool = False) -> str:
    if adult:
        return "XXX"
    options = {CANON[g.lower().strip()] for g in m3u.group_names(meta)
               if g.lower().strip() in CANON and CANON[g.lower().strip()] != "XXX"}
    return min(options, key=lambda g: RANK.get(g, 999)) if options else "General"


def normalize(entries: list[tuple[str, str]], adult_entries: list[tuple[str, str]],
              minimum: int) -> tuple[list[tuple[str, str]], dict[str, int]]:
    """Group exactly once, preserve order/count/URLs and all non-group metadata."""
    adult_keys = {(m3u.channel_id(m), u) for m, u in adult_entries}
    adult_ids = {m3u.channel_id(m) for m, _ in adult_entries if m3u.channel_id(m)}
    choices = [
        pick_group(meta, adult=(m3u.channel_id(meta), url) in adult_keys or
                   (m3u.channel_id(meta) in adult_ids and bool(m3u.channel_id(meta))))
        for meta, url in entries
    ]
    totals = Counter(choices)
    # Prevent dozens of tiny categories, but never suppress XXX.
    choices = [group if group == "XXX" or totals[group] >= minimum else "General"
               for group in choices]
    result = [
        (m3u.with_group(meta, group), url)
        for (meta, url), group in zip(entries, choices)
    ]
    assert len(result) == len(entries)
    assert [url for _, url in result] == [url for _, url in entries]
    assert all(m3u.group_names(meta) == [group] and ";" not in group
               for (meta, _), group in zip(result, choices))
    return result, dict(sorted(Counter(choices).items()))


def build(source: Path, output: Path) -> dict:
    """Generate only replacement full indexes + lite M3Us; never modify source."""
    raw_index = source / "index.m3u"
    raw_adult = source / "adult.m3u"
    if not raw_index.is_file() or not raw_adult.is_file():
        raise ValueError("Existing index.m3u and adult.m3u are required")
    entries = m3u.parse_m3u(raw_index.read_text(encoding="utf-8-sig"))
    adult = m3u.parse_m3u(raw_adult.read_text(encoding="utf-8-sig"))
    if len(entries) < 50:
        raise ValueError("Source index unexpectedly small")
    # Keep any duplicate stream variants present in the source, in original order.
    repaired, groups = normalize(entries, adult, minimum=10)
    output.mkdir(parents=True, exist_ok=True)
    (output / "catalog").mkdir(exist_ok=True)
    serialized = m3u.serialize(repaired)
    for name in ("index.m3u", "index.category.m3u"):
        (output / name).write_text(serialized, encoding="utf-8")

    with tempfile.TemporaryDirectory(prefix="lampa-normalization-") as tmp:
        work = Path(tmp)
        (work / "index.m3u").write_text(serialized, encoding="utf-8")
        (work / "adult.m3u").write_bytes(raw_adult.read_bytes())
        lite_report = lite.build(work, output)
        for name, _ in lite.PROFILES:
            small = m3u.parse_m3u((output / name).read_text(encoding="utf-8"))
            normalized, by_group = normalize(small, adult, minimum=3)
            (output / name).write_text(m3u.serialize(normalized), encoding="utf-8")
            lite_report["playlists"][name]["categories"] = sorted(by_group)
            lite_report["playlists"][name]["per_category"] = by_group
            lite_report["playlists"][name]["bytes"] = (output / name).stat().st_size
            assert all(v >= 3 or k == "XXX" for k, v in by_group.items())
    report = {
        "source_entries": len(entries),
        "repaired_entries": len(repaired),
        "source_urls_preserved": True,
        "single_group_per_entry": True,
        "group_counts": groups,
        "lite": lite_report["playlists"],
        "stream_health_retested": False,
        "bunny_video_hosted": False,
    }
    (output / "catalog/category-repair-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return report


def test() -> None:
    import tempfile
    a = ('#EXTINF:-1 tvg-id="a.us" group-title="Documentary;Education;Outdoor;Relax",A',
         "https://example.org/a.m3u8")
    b = ('#EXTINF:-1 tvg-id="b.us" group-title="Family;Series",B',
         "https://example.org/b.m3u8")
    c = ('#EXTINF:-1 tvg-id="c.us" group-title="OneOffCategory",C',
         "https://example.org/c.m3u8")
    assert pick_group(a[0]) == "Documentary"
    assert pick_group(b[0]) == "Series"
    assert pick_group(c[0]) == "General"
    adult = ('#EXTINF:-1 tvg-id="x.us" group-title="XXX",X',
             "https://example.org/x.m3u8")
    xs = [a] * 20 + [b] * 20 + [c] + [adult]
    transformed, groups = normalize(xs, [adult], minimum=10)
    assert groups == {"Documentary": 20, "General": 1, "Series": 20, "XXX": 1}
    assert transformed[0][0].count('group-title="') == 1
    assert all(";" not in m3u.group_names(meta)[0] for meta, _ in transformed)
    with tempfile.TemporaryDirectory() as root:
        original, out = Path(root) / "old", Path(root) / "new"
        original.mkdir()
        sample = [a, b, c, adult]
        for i in range(900):
            group = ["News", "Music", "Sports", "Movies", "Documentary", "Education",
                     "Kids", "Science", "Travel", "Comedy", "Business", "General"][i % 12]
            sample.append((
                f'#EXTINF:-1 tvg-id="{i}.us" group-title="{group};General",Station {i}',
                f'https://example.org/tv/{i}.m3u8'
            ))
        (original / "index.m3u").write_text(m3u.serialize(sample))
        (original / "adult.m3u").write_text(m3u.serialize([adult]))
        before = (original / "index.m3u").read_bytes()
        report = build(original, out)
        assert before == (original / "index.m3u").read_bytes()
        assert report["source_entries"] == len(sample)
        assert report["source_urls_preserved"]
        for name in ("index.m3u", "index.category.m3u", "lampa-lite.m3u", "lampa.m3u"):
            data = m3u.parse_m3u((out / name).read_text())
            groups = Counter(m3u.group_names(meta)[0] for meta, _ in data)
            assert groups and all(v >= 3 or k == "XXX" for k, v in groups.items())
            assert all(len(m3u.group_names(meta)) == 1 for meta, _ in data)
        assert [u for _, u in m3u.parse_m3u((out / "index.m3u").read_text())] == [u for _, u in sample]
    print("LAMPA_CATEGORY_REPAIR_TEST_PASS")


if __name__ == "__main__":
    test()
