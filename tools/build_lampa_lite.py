#!/usr/bin/env python3
"""Create small, category-balanced M3U playlists for low-memory Samsung Tizen Lampa.

Reads the existing locally saved index.m3u and adult.m3u. No stream URLs
are probed, fetched, decrypted or proxied. It never alters the full catalog.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Iterable

import personal_bunny_playlists as m3u

PROFILES = (("lampa-lite.m3u", 240), ("lampa.m3u", 600))
EXCLUDED = {"xxx", "adultiptv", "mycamtv", "other adult"}


def key(meta: str, url: str) -> tuple[str, str]:
    return (m3u.channel_id(meta), url)


def balanced_selection(public: list[tuple[str, str]], capacity: int
                       ) -> tuple[list[tuple[str, str]], dict[str, int]]:
    groups: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for meta, url in public:
        for group in m3u.group_names(meta):
            group = group.strip() or "Undefined"
            if group.lower() in EXCLUDED:
                continue
            groups[group].append((m3u.with_group(meta, group), url))
    # Sort only within each group: favor non-geo-blocked and 24/7 candidates,
    # then higher-quality variants. This is NOT a live stream test.
    def rank(item: tuple[str, str]):
        meta, url = item
        blocked = int("Geo-blocked" in meta)
        parttime = int("Not 24/7" in meta)
        m = m3u.re.search(r"\((\d+)[pi]\)", meta)
        height = int(m.group(1)) if m else 0
        return (blocked, parttime, -height, 0 if url.startswith("https://") else 1,
                m3u.channel_id(meta), url)
    for group in groups:
        groups[group].sort(key=rank)
    order = sorted(groups, key=lambda g: (g.lower() == "undefined", g.lower()))
    selected: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    counts: dict[str, int] = defaultdict(int)
    indexes = {group: 0 for group in order}
    while len(selected) < capacity:
        advanced = False
        for group in order:
            candidates = groups[group]
            while indexes[group] < len(candidates):
                candidate = candidates[indexes[group]]
                indexes[group] += 1
                identifier = key(*candidate)
                if identifier in seen:
                    continue
                seen.add(identifier)
                selected.append(candidate)
                counts[group] += 1
                advanced = True
                break
            if len(selected) >= capacity:
                break
        if not advanced:
            break
    return selected, dict(sorted(counts.items()))


def build(input_dir: Path, output_dir: Path) -> dict:
    index_file = input_dir / "index.m3u"
    adult_file = input_dir / "adult.m3u"
    if not index_file.is_file() or not adult_file.is_file():
        raise ValueError("Expected locally saved index.m3u and adult.m3u under " + str(input_dir))

    index = m3u.unique_entries(m3u.parse_m3u(index_file.read_text(encoding="utf-8-sig")))
    adult = m3u.unique_entries(m3u.parse_m3u(adult_file.read_text(encoding="utf-8-sig")))
    adult_keys = {key(meta, url) for meta, url in adult}
    adult_ids = {m3u.channel_id(meta) for meta, _ in adult if m3u.channel_id(meta)}
    public = [(meta, url) for meta, url in index
              if key(meta, url) not in adult_keys and m3u.channel_id(meta) not in adult_ids
              and "XXX" not in m3u.group_names(meta)]

    if len(public) < 50:
        raise ValueError("Public source index unexpectedly small; refusing publication")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "catalog").mkdir(exist_ok=True)
    report = {
        "full_index_entries_unchanged": len(index),
        "adult_entries_from_prior_check": len(adult),
        "adult_retested": False,
        "playlists": {},
        "note": "The public index entries are not individually live-verified; only adult.m3u is drawn from the previously verified local list.",
    }
    for filename, maximum in PROFILES:
        if len(adult) > maximum:
            raise ValueError("Adult list exceeds profile capacity")
        selection, by_category = balanced_selection(public, maximum - len(adult))
        output = selection + [
            (m3u.with_group(meta, "XXX"), url) for meta, url in adult
        ]
        text = m3u.serialize(output)
        (output_dir / filename).write_text(text, encoding="utf-8")
        if len(output) > maximum or not text.startswith("#EXTM3U\n"):
            raise AssertionError("Invalid lightweight playlist")
        report["playlists"][filename] = {
            "entries": len(output),
            "adult_entries": len(adult),
            "public_entries": len(selection),
            "categories": sorted(list(by_category) + (["XXX"] if adult else [])),
            "per_category": dict(by_category, **({"XXX": len(adult)} if adult else {})),
            "bytes": len(text.encode("utf-8")),
        }
    (output_dir / "catalog/lampa-lite-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return report


def self_test() -> None:
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        source = base / "existing"
        out = base / "lite"
        source.mkdir()
        adult = [
            ('#EXTINF:-1 tvg-id="Adult.us" group-title="XXX",Adult', "https://example.net/adult.m3u8")
        ]
        public = []
        for group in ["News", "Music", "Sports", "Movies", "Kids", "Science", "Education"]:
            for i in range(100):
                public.append((
                    f'#EXTINF:-1 tvg-id="{group}{i}.us" group-title="{group}",{group} {i}',
                    f'https://example.net/{group}/{i}.m3u8'
                ))
        (source / "index.m3u").write_text(m3u.serialize(public + adult))
        (source / "adult.m3u").write_text(m3u.serialize(adult))
        initial = (source / "index.m3u").read_bytes()
        report = build(source, out)
        assert (source / "index.m3u").read_bytes() == initial
        for name, maximum in PROFILES:
            items = m3u.parse_m3u((out / name).read_text())
            assert len(items) == maximum
            assert len({key(*item) for item in items}) == len(items)
            assert sum("XXX" in m3u.group_names(meta) for meta, _ in items) == 1
            assert all(any(group in m3u.group_names(meta) for meta, _ in items)
                       for group in ["News", "Music", "Sports", "Movies", "Kids", "Science", "Education"])
            assert report["playlists"][name]["entries"] == maximum
    print("LAMPA_LITE_OFFLINE_TEST_PASS")


if __name__ == "__main__":
    self_test()
