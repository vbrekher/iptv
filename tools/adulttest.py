#!/usr/bin/env python3
"""Build, test and publish a separate adulttest.m3u on an existing Bunny account.

Python 3.9+, stdlib. Never downloads or stores video files. Does not use
subscription credentials, custom headers, DRM, proxying, or provider tokens.
The legal right to redistribute a stream is NOT established by HTTP 200.
"""
from __future__ import annotations

import argparse
import csv
import getpass
import io
import json
import re
import sys
import tempfile
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlsplit
from urllib.request import Request, urlopen

import auto_bunny_setup as bunny
import free_hls_filter as hls
import personal_bunny_playlists as iptv

# Based on the 16-source November research. Some entries in that research
# referred to a mirror or metadata, not an additional source of streams.
# Inputs are public GitHub texts, not personal subscription playlists.
SOURCES = (
    ("NiceZoneCoder", "NiceZoneCoder/NiceZoneCoder.github.io", "main", "live/m3u/xxx/xxx_4.m3u", "m3u"),
    ("karlovitch", "karlovitch/iptv", "main", "NSFW", "m3u"),
    ("Keglr", "Keglr/IPTV_V6", "main", "Adult.m3u", "m3u"),
    ("SICOPOLY", "SICOPOLY/json2m3u", "main", "tv.json", "json"),
    ("ChinaIPTV", "hujingguang/ChinaIPTV", "main", "xxx.m3u8", "m3u"),
    ("wuvip", "wuvip/tv", "main", "xxx.m3u", "m3u"),
    ("cylim76", "cylim76/install", "main", "iptv/xxx.m3u", "m3u"),
    ("CuanDaily", "CuanDaily/Zabiya-Id", "main", "xxx.m3u", "m3u"),
    ("THEMMMINAT", "THEMMMINAT/xxx-IPTV", "main", "XXX.m3u", "m3u"),
    ("ql-fa NL", "ql-fa/A", "master", "streams/nl.m3u", "m3u"),
    ("IPTV 2024 XXX", "iptv-org/iptv", "a1f14e961505010b0ef13bcd2a535f658ed51ac1", "categories/xxx.m3u", "m3u"),
    ("IPTV 2024 NSFW", "iptv-org/iptv", "a1f14e961505010b0ef13bcd2a535f658ed51ac1", "index.nsfw.m3u", "m3u"),
    ("Pluto TV Germany", "BuddyChewChew/app-m3u-generator", "main", "playlists/plutotv_de.m3u", "m3u"),
    ("Asia 18+ TXT", "lizhaohai369/fork-iptv-m3u8", "main", "18+.txt", "txt"),
    ("hipy Adult", "woshishiq1/hipy-drpy2", "main", "aa999ok/CK/18015/lib/Adult.m3u", "m3u"),
    ("IPTV NSFW blocklist (names only)", "iptv-org/database", "master", "data/blocklist.csv", "metadata"),
)

ADULT_WORDS = re.compile(
    r"(?i)brazzers|penthouse|playboy|hustler|dorcel|redlight|private.?tv|"
    r"vivid|vixen|xxl|erox|eroxxx|exxxotica|dusk|evil angel|reality kings|"
    r"digital playground|digital desire|naughty america|blue hustler|"
    r"extasy|eromania|venus|sexy hot|erotic|beate uhse|hot tv|"
    r"barely legal tv|pornstar|fap tv|french lover|xxx|adult|sex|"
    r"red shoe diaries|gigolos|liebe sünde|heisse|heiße|emmanuelle|"
    r"sanfte berührungen|stimulierende dokus|sinnliche fantasien|"
    r"lust|s66cams|spice|sct|colmax|hotxxl|cineman|blue movie|"
    r"passie|jacquie michel|dancing bear|pink o tv|leotv|babes tv"
)
CAM_WORDS = re.compile(r"(?i)adultiptv|mycamtv|live.?cams|web.?cam|cam4|camsoda|chaturbate|stripchat")
VOD_WORDS = re.compile(r"(?i)\.(?:mp4|mkv|avi|wmv)(?:[?#]|$)|/movie/|/series/|/vod/")
TEEN_WORDS = re.compile(r"(?i)\bteen\b|\bteens\b")
# Plain credentials, embedded tokens and expiration signatures are intentionally
# excluded rather than tested. Token names are only checked, never logged.
BLOCKED_PARAMETERS = hls.BLOCKED_PARAMS | {
    "username", "pwd", "passw", "secret", "user", "client_id",
    "client_secret", "st", "e", "hash", "verify", "play_token"
}
META_RE = re.compile(r'([\w-]+)="([^"]*)"')
MAX_SOURCE_BYTES = 3_000_000
MAX_CANDIDATES = 2500


@dataclass
class Candidate:
    name: str
    url: str
    logo: str = ""
    tvg_id: str = ""
    category: str = "Adult TV"
    sources: set[str] = field(default_factory=set)
    quality_hint: str = "unknown"


def source_url(spec) -> str:
    _, repo, ref, path, _ = spec
    owner, name = repo.split("/")
    return "https://raw.githubusercontent.com/" + owner + "/" + name + "/" + ref + "/" + quote(path, safe="/")


def fetch_text(spec) -> str:
    url = source_url(spec)
    req = Request(url, headers={"User-Agent": "Lampa-adulttest-research/1.0"})
    with urlopen(req, timeout=30) as response:
        data = response.read(MAX_SOURCE_BYTES + 1)
    if len(data) > MAX_SOURCE_BYTES:
        raise ValueError("source_exceeds_size_limit")
    return data.decode("utf-8-sig", errors="replace")


def source_rows(text: str, kind: str) -> list[tuple[str, str, str, str, str]]:
    """Return (title, stream_url, logo, tvg_id, group)."""
    output = []
    if kind == "m3u":
        pending = None
        for raw in text.splitlines():
            line = raw.strip()
            if line.startswith("#EXTINF:"):
                attrs = dict(META_RE.findall(line.split(",", 1)[0]))
                title = line.split(",", 1)[-1].strip()
                pending = (
                    title[:150], "", attrs.get("tvg-logo", ""),
                    attrs.get("tvg-id", ""), attrs.get("group-title", ""),
                )
            elif pending is not None and line.startswith(("https://", "http://")):
                output.append((pending[0], line, pending[2], pending[3], pending[4]))
                pending = None
            elif pending is not None and line and not line.startswith("#"):
                pending = None
    elif kind == "json":
        try:
            doc = json.loads(text)
        except (ValueError, TypeError):
            return []
        def walk(obj, depth=0):
            if depth > 12:
                return
            if isinstance(obj, list):
                for item in obj:
                    walk(item, depth + 1)
            elif isinstance(obj, dict):
                title = obj.get("name") or obj.get("title")
                link = obj.get("url") or obj.get("stream")
                if isinstance(title, str) and isinstance(link, str) and link.startswith(("http://", "https://")):
                    logo = obj.get("logo") or obj.get("image") or ""
                    output.append((title[:150], link, logo if isinstance(logo, str) else "", str(obj.get("id") or ""), ""))
                for child in obj.values():
                    if isinstance(child, (dict, list)):
                        walk(child, depth + 1)
        walk(doc)
    elif kind == "txt":
        for line in text.splitlines():
            if "," not in line or line.startswith(("#", "http")):
                continue
            title, link = line.split(",", 1)
            if link.strip().startswith(("http://", "https://")):
                output.append((title.strip()[:150], link.strip(), "", "", ""))
    return output


def relevant(name: str, tvg_id: str, group: str, source_name: str, nsfw_ids: set[str]) -> bool:
    if source_name == "Pluto TV Germany":
        return "Sinnliche Fantasien" in group
    if source_name in ("IPTV 2024 NSFW", "ql-fa NL", "SICOPOLY"):
        return tvg_id in nsfw_ids or bool(ADULT_WORDS.search(name + " " + group))
    if source_name == "karlovitch":
        # Large file has hundreds of VOD episode/movie titles after its live
        # channel section. Only source-labelled (18+) entries are candidates.
        return "(18+)" in name
    # Remaining inputs are dedicated adult M3U files, but cam names, unsafe
    # URLs and VOD media are still rejected by independent rules.
    return True


def safe_stream_url(url: str) -> tuple[bool, str]:
    try:
        part = urlsplit(url)
        if part.scheme not in ("http", "https") or not part.hostname:
            return False, "invalid_url"
        if part.username or part.password:
            return False, "embedded_credentials"
        if part.fragment:
            return False, "fragment"
        if part.hostname in ("localhost", "0.0.0.0"):
            return False, "private_url"
        if part.hostname.endswith((".local", ".internal", ".localhost")):
            return False, "private_url"
        for key, value in __import__("urllib.parse", fromlist=["parse_qsl"]).parse_qsl(part.query, keep_blank_values=True):
            if key.lower() in BLOCKED_PARAMETERS:
                return False, "signed_or_subscription_query"
        if re.search(r"/(?:live|iptv|get)\b/[^/?]{5,}/[^/?]{5,}/", part.path, re.IGNORECASE):
            return False, "subscription_path"
        if re.search(r"(?i)/(?:playlist|player)_api\.php|/get\.php|/xmltv\.php", part.path):
            return False, "subscription_api"
        if VOD_WORDS.search(url):
            return False, "vod_not_linear_tv"
        return True, "candidate"
    except ValueError:
        return False, "malformed_url"


def choose_category(source: str, name: str) -> str:
    if source == "Pluto TV Germany":
        return "Erotic FAST"
    return "Adult TV"


def safe_logo(url: str) -> str:
    try:
        part = urlsplit(url)
        if part.scheme != "https" or not part.hostname or part.username or part.password:
            return ""
        if any(k.lower() in BLOCKED_PARAMETERS for k, _ in
               __import__("urllib.parse", fromlist=["parse_qsl"]).parse_qsl(part.query)):
            return ""
        return url[:800]
    except (ValueError, TypeError):
        return ""


def hint(name: str) -> str:
    m = re.search(r"(?i)\b(?:2160|1080|720|576|480)p\b|\b(?:4K|UHD|FHD|HD)\b", name)
    return m.group(0) if m else "unknown"


def sanitize(text: str, limit: int = 140) -> str:
    return text.replace('"', "'").replace("\r", " ").replace("\n", " ").replace("\\", "").strip()[:limit]


def collect() -> tuple[list[Candidate], dict, list[dict]]:
    nsfw_ids: set[str] = set()
    results: list[dict] = []
    seen: dict[str, Candidate] = {}
    skipped = Counter()
    block = SOURCES[-1]
    try:
        text = fetch_text(block)
        nsfw_ids = {row["channel"] for row in csv.DictReader(io.StringIO(text))
                    if row.get("reason") == "nsfw" and row.get("channel")}
        results.append({"source": block[0], "kind": "metadata", "ids": len(nsfw_ids), "status": "ok"})
    except Exception as exc:
        results.append({"source": block[0], "kind": "metadata", "status": "error_" + type(exc).__name__})
    if not nsfw_ids:
        raise RuntimeError("NSFW blocklist unavailable; refusing poorly classified mixed sources")
    for spec in SOURCES[:-1]:
        label, _, _, _, kind = spec
        try:
            raw = fetch_text(spec)
            rows = source_rows(raw, kind)
            before = len(seen)
            for name, url, logo, tvg_id, group in rows:
                name = sanitize(name)
                if not relevant(name, tvg_id, group, label, nsfw_ids):
                    skipped["not_adult"] += 1
                    continue
                if CAM_WORDS.search(name + " " + group):
                    skipped["cam_source"] += 1
                    continue
                if TEEN_WORDS.search(name):
                    skipped["teen_label_excluded"] += 1
                    continue
                valid, reason = safe_stream_url(url)
                if not valid:
                    skipped[reason] += 1
                    continue
                if not name:
                    skipped["missing_title"] += 1
                    continue
                if url in seen:
                    seen[url].sources.add(label)
                    if not seen[url].logo:
                        seen[url].logo = safe_logo(logo)
                    continue
                if len(seen) >= MAX_CANDIDATES:
                    raise ValueError("candidate_limit_exceeded")
                seen[url] = Candidate(
                    name=name, url=url, logo=safe_logo(logo),
                    tvg_id=sanitize(tvg_id, 90),
                    category=choose_category(label, name),
                    sources={label}, quality_hint=hint(name)
                )
            results.append({"source": label, "kind": kind, "rows": len(rows),
                            "new_unique_candidates": len(seen) - before, "status": "ok"})
            print(f"Source {label}: {len(rows)} entries, +{len(seen)-before} unique candidates")
        except (HTTPError, URLError, OSError, UnicodeError, ValueError) as exc:
            results.append({"source": label, "kind": kind, "status": "error_" + type(exc).__name__})
            print(f"Source {label}: {type(exc).__name__} (skipped)")
    return list(seen.values()), dict(skipped), results


def write_m3u(items: list[Candidate], target: Path):
    lines = ["#EXTM3U"]
    for item in items:
        logo = ' tvg-logo="' + sanitize(item.logo, 800) + '"' if item.logo else ""
        tvg_id = ' tvg-id="' + sanitize(item.tvg_id, 90) + '"' if item.tvg_id else ""
        lines.append('#EXTINF:-1' + tvg_id + logo +
                     ' group-title="' + item.category + '",' + sanitize(item.name))
        lines.append(item.url)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")


def probe(item: Candidate, timeout: float) -> tuple[bool, str, str]:
    # Limit checks to unauthenticated HLS with readable non-DRM media segments.
    # Stream quality and copyright are *not* established by an HTTP response.
    if not hls.public_url(item.url):
        return False, "unsafe_or_nonpublic_host", ""
    ok, reason = hls.check_stream(item.url, timeout)
    resolution = "unverified"
    if ok:
        try:
            body, _, _ = hls.get_data(item.url, timeout, 128_000,
                                     "application/vnd.apple.mpegurl, */*")
            match = re.search(rb"\bRESOLUTION=(\d{3,4})x(\d{3,4})\b", body)
            if match:
                resolution = match.group(1).decode() + "x" + match.group(2).decode()
        except (ValueError, HTTPError, URLError, OSError):
            pass
    return ok, reason, resolution


def run(args) -> int:
    # The cached local state prevents accidental creation of new Bunny zones.
    if not bunny.STATE.is_file():
        raise RuntimeError("Existing .bunny-iptv-state.json required: cd $HOME/iptv-bunny")
    root = Path(args.output)
    root.mkdir(parents=True, exist_ok=True)
    if args.publish_only:
        return publish_saved(root)
    candidates, rejected, sources = collect()
    if not candidates:
        raise RuntimeError("No safe stream candidates found; no upload")
    candidates.sort(key=lambda c: (c.category, c.name.lower(), c.url))
    write_m3u(candidates, root / "adulttest-candidates.m3u")
    print(f"UNTESTED CANDIDATES: {len(candidates)}; saved locally (not uploaded)")
    good: list[Candidate] = []
    result_rows = []
    tally = Counter()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        future_map = {pool.submit(probe, c, args.timeout): c for c in candidates}
        for i, future in enumerate(as_completed(future_map), 1):
            c = future_map[future]
            try:
                success, reason, resolution = future.result()
            except Exception as exc:
                success, reason, resolution = False, "probe_" + type(exc).__name__, ""
            tally[reason] += 1
            if success:
                good.append(c)
            result_rows.append({
                "name": c.name, "category": c.category, "logo": c.logo,
                "url": c.url, "sources": "|".join(sorted(c.sources)),
                "status": "open_hls" if success else "rejected",
                "reason": reason, "resolution": resolution,
                "advertised_quality": c.quality_hint,
            })
            print(f"[{i}/{len(candidates)}] {'OPEN' if success else 'FAIL'} "
                  f"{sanitize(c.name, 72)} ({reason}, {resolution})")
    good.sort(key=lambda c: (c.category, c.name.lower(), c.url))
    write_m3u(good, root / "adulttest.m3u")
    result_rows.sort(key=lambda r: (r["status"], r["name"].lower(), r["url"]))
    with (root / "adulttest-results.csv").open("w", newline="", encoding="utf-8") as fh:
        columns = ("name", "category", "logo", "url", "sources", "status", "reason",
                   "resolution", "advertised_quality")
        writer = csv.DictWriter(fh, fieldnames=columns)
        writer.writeheader()
        writer.writerows(result_rows)
    report = {
        "source_count_research": len(SOURCES),
        "sources": sources,
        "candidate_urls_deduplicated": len(candidates),
        "open_anonymous_hls": len(good),
        "rejected": len(candidates)-len(good),
        "excluded_before_probe": rejected,
        "reasons": dict(tally),
        "adulttest_uploaded": False,
        "rights_verified": False,
        "hd_quality_verified": False,
        "samsung_playback_verified": False,
        "notes": [
            "Only HLS playlists with a readable small media sample pass.",
            "A candidate filename containing HD/4K does not prove actual resolution.",
            "Anonymous accessibility does not prove broadcasting rights.",
            "Excludes apparent subscription credentials, cam-source playlists, VOD and teen-labelled names.",
            "Private source audit and rejected URLs stay on this Mac; never upload them to Bunny.",
        ]
    }
    (root / "adulttest-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    if not good:
        print("No anonymous HLS candidates passed. No Bunny upload performed.")
        return 2
    if args.dry_run:
        print("DRY RUN: no Bunny upload. Local:", root.resolve())
        return 0

    return publish_saved(root)


def publish_saved(root: Path) -> int:
    """Resume a completed successful probe without repeating source scans."""
    playlist = root / "adulttest.m3u"
    report_file = root / "adulttest-report.json"
    if not playlist.is_file() or not report_file.is_file():
        raise RuntimeError("Missing completed local Adulttest files. Run the normal test first.")
    report = json.loads(report_file.read_text(encoding="utf-8"))
    if report.get("open_anonymous_hls", 0) <= 0:
        raise RuntimeError("No previously tested accessible streams; refusing to publish an empty M3U")
    local_data = playlist.read_bytes()
    if not local_data.startswith(b"#EXTM3U") or len(iptv.parse_m3u(local_data.decode("utf-8-sig"))) != report["open_anonymous_hls"]:
        raise RuntimeError("Local Adulttest playlist does not match validated report; rerun probe")
    if not bunny.STATE.is_file():
        raise RuntimeError("Missing existing .bunny-iptv-state.json; do not recreate Bunny zones")
    state = bunny.load_state(bunny.STATE)
    key = getpass.getpass("Bunny Account API Key (hidden): ")
    api = bunny.BunnyAPI(key)
    key = ""
    stor_name = state["name"] + "-storage"
    pull_name = state["name"] + "-cdn"
    if not bunny.named(bunny.list_zones(api, "storagezone"), stor_name):
        raise RuntimeError("Existing Bunny Storage Zone not found; refusing to create new resources")
    if not bunny.named(bunny.list_zones(api, "pullzone"), pull_name):
        raise RuntimeError("Existing Bunny Pull Zone not found; refusing to create new resources")
    storage = bunny.storage_zone(api, state)
    pull = bunny.pull_zone(api, state, storage["id"])
    with tempfile.TemporaryDirectory(prefix="lampa-adulttest-upload-") as temp:
        upload = Path(temp)
        (upload / "adulttest.m3u").write_bytes(local_data)
        # The only public Bunny object modified is /iptv/adulttest.m3u.
        bunny.publish(api, state, storage, pull, upload)
    report["adulttest_uploaded"] = True
    report["cdn_url"] = "https://" + pull["hostname"] + "/iptv/adulttest.m3u"
    # A reachable CDN is different from a successful Storage PUT.
    report["cdn_verified"] = False
    try:
        request = Request(report["cdn_url"] + "?v=" + str(__import__("time").time_ns()),
                          headers={"User-Agent": "Lampa-adulttest-check/1.0"})
        with urlopen(request, timeout=15) as response:
            report["cdn_verified"] = (response.status == 200 and response.read(7) == b"#EXTM3U")
    except (HTTPError, URLError, OSError, TimeoutError):
        pass
    report_file.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("\nADULTTEST_UPLOAD_COMPLETE:", report["cdn_url"])
    print("CDN_CHECK:", "VERIFIED" if report["cdn_verified"] else "NOT_VERIFIED (check propagation)")
    print("OPEN:", report["open_anonymous_hls"], "/", report["candidate_urls_deduplicated"])
    print("LOCAL REPORT:", report_file.resolve())
    return 0


def self_test():
    m3u = ('#EXTM3U\n'
           '#EXTINF:-1 tvg-id="Channel.us" tvg-logo="https://images.example/logo.png" '
           'group-title="XXX",Brazzers TV HD\nhttps://example.com/live.m3u8\n'
           '#EXTINF:-1 group-title="XXX",MyCamTV Anal\nhttps://example.com/cam.m3u8\n')
    rows = source_rows(m3u, "m3u")
    assert len(rows) == 2 and rows[0][2] == "https://images.example/logo.png"
    assert CAM_WORDS.search(rows[1][0])
    assert relevant("Brazzers TV", "Channel.us", "XXX", "NiceZoneCoder", {"Channel.us"})
    assert not relevant("News", "News.us", "News", "ql-fa NL", set())
    assert not relevant("TeleMadrid", "", "", "SICOPOLY", set())
    assert relevant("Dorcel", "", "", "SICOPOLY", set())
    assert not relevant("M. Dorcel - Episode 1", "", "", "karlovitch", set())
    assert relevant("Dorcel TV FHD (18+) NL", "", "", "karlovitch", set())
    assert relevant("Pluto TV Emmanuelle Filme", "", "Sinnliche Fantasien", "Pluto TV Germany", set())
    assert safe_stream_url("https://example.org/live.m3u8")[0]
    assert not safe_stream_url("https://example.org/live?token=secret")[0]
    assert not safe_stream_url("https://user:secret@example.org/live.m3u8")[0]
    assert not safe_stream_url("http://example.org/live/user1234/pass1234/1.m3u8")[0]
    assert not safe_stream_url("https://example.org/movie/32.mp4")[0]
    example = Candidate(name="Brazzers TV HD", url="https://example.org/live.m3u8",
                        logo="https://example.org/logo.png", category="Adult TV")
    with tempfile.TemporaryDirectory() as temp:
        out = Path(temp) / "adulttest.m3u"
        write_m3u([example], out)
        assert 'group-title="Adult TV"' in out.read_text()
        assert 'tvg-logo="https://example.org/logo.png"' in out.read_text()
        assert len(iptv.parse_m3u(out.read_text())) == 1
    assert len(SOURCES) == 16
    print("ADULTTEST_OFFLINE_SELF_TEST_PASS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="dist/adulttest")
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--timeout", type=float, default=7)
    parser.add_argument("--dry-run", action="store_true", help="Test all streams but do not upload to Bunny")
    parser.add_argument("--publish-only", action="store_true", help="Upload previous verified local M3U without repeating probes")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.dry_run and args.publish_only:
        parser.error("--dry-run and --publish-only cannot be combined")
    if not (1 <= args.workers <= 12 and 1 <= args.timeout <= 25):
        parser.error("workers must be 1..12 and timeout 1..25 seconds")
    try:
        return run(args)
    except (ValueError, RuntimeError, OSError, HTTPError, URLError) as exc:
        print("ERROR:", str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
