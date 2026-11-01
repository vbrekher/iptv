#!/usr/bin/env python3
"""Filter historical IPTV candidates to streams publicly responsive without credentials.

Only tests HTTP accessibility, NOT copyright/licensing or future uptime.
Must live beside personal_bunny_playlists.py. Python 3.9+, stdlib only.
"""
from __future__ import annotations

import argparse
import csv
import io
import ipaddress
import json
import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse, parse_qsl
from urllib.request import HTTPRedirectHandler, Request, build_opener

import personal_bunny_playlists as builder

BLOCKED_PARAMS = {
    "token", "access_token", "auth", "authorization", "api_key", "apikey",
    "password", "pass", "key", "signature", "sig", "session", "sessionid",
    "expires", "expire", "expiry", "jwt", "hdnea", "hdnts",
}
MAX_MANIFEST_BYTES = 256 * 1024


def public_url(url: str) -> bool:
    """Reject URLs containing credentials, obvious signed tokens, or private hosts."""
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https") or not parsed.hostname:
            return False
        if parsed.username or parsed.password or parsed.fragment:
            return False
        if parsed.port is not None and parsed.port not in (80, 443, 8080, 1935, 8443):
            return False
        if any(k.lower() in BLOCKED_PARAMS for k, _ in parse_qsl(parsed.query, keep_blank_values=True)):
            return False
        host = parsed.hostname
        if host == "localhost" or host.endswith((".local", ".internal", ".localhost")):
            return False
        addresses = socket.getaddrinfo(host, parsed.port or 443, type=socket.SOCK_STREAM)
        if not addresses:
            return False
        return all(ipaddress.ip_address(item[4][0]).is_global for item in addresses)
    except (ValueError, OSError):
        return False


class PublicRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not public_url(newurl):
            raise ValueError("blocked redirect to non-public or credentialed endpoint")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


OPENER = build_opener(PublicRedirects)


def get_data(url: str, timeout: float, max_bytes: int, accept: str, allow_truncated: bool = False) -> tuple[bytes, str, int]:
    if not public_url(url):
        raise ValueError("private, invalid or credentialed URL")
    request = Request(url, headers={"Accept": accept, "User-Agent": "Mozilla/5.0 (IPTV-free-check)"})
    with OPENER.open(request, timeout=timeout) as response:
        body = response.read(max_bytes if allow_truncated else max_bytes + 1)
        effective = response.geturl()
        if not public_url(effective):
            raise ValueError("unsafe final URL")
        if not allow_truncated and len(body) > max_bytes:
            raise ValueError("response exceeds size limit")
        if response.status not in (200, 206):
            raise ValueError("unexpected HTTP status")
        return body, effective, response.status


def first_media_reference(manifest: str) -> str | None:
    lines = [line.strip() for line in manifest.splitlines()]
    for line in lines:
        if line and not line.startswith("#"):
            return line
    return None


def check_stream(url: str, timeout: float) -> tuple[bool, str]:
    """Test unsigned HLS manifest and a small sample of a media segment."""
    try:
        manifest_url = url
        for _ in range(3):
            raw, manifest_url, _ = get_data(
                manifest_url, timeout, MAX_MANIFEST_BYTES,
                "application/vnd.apple.mpegurl, application/x-mpegURL, */*"
            )
            text = raw.decode("utf-8-sig", "replace")
            if not text.lstrip().startswith("#EXTM3U") or "#EXT-X-" not in text:
                return False, "not_hls_manifest"
            if "#EXT-X-KEY:" in text or "#EXT-X-SESSION-KEY:" in text:
                return False, "encrypted_or_key_required"
            child = first_media_reference(text)
            if not child:
                return False, "manifest_has_no_media"
            resolved = urljoin(manifest_url, child)
            if "#EXT-X-STREAM-INF" in text:
                manifest_url = resolved
                continue
            if "#EXTINF" not in text:
                return False, "manifest_has_no_segments"
            # Read only a tiny sample of the first media segment, never copy video.
            segment, _, _ = get_data(resolved, timeout, 1024, "*/*", allow_truncated=True)
            if not segment or segment.lstrip().lower().startswith((b"<!doctype html", b"<html")):
                return False, "segment_not_media"
            return True, "public_hls_manifest_and_segment"
        return False, "too_many_nested_playlists"
    except HTTPError as error:
        return False, f"http_{error.code}"
    except (URLError, TimeoutError, OSError, ValueError, UnicodeError) as error:
        return False, type(error).__name__.lower()


def run(args) -> int:
    source = Path(args.input)
    destination = Path(args.output)
    if source.resolve() == destination.resolve():
        raise ValueError("Use distinct input and output directories")
    original = source / "adult.m3u"
    if not original.is_file():
        raise ValueError(f"Missing generated adult playlist: {original}")
    entries = builder.unique_entries(builder.parse_m3u(original.read_text(encoding="utf-8-sig")))
    print(f"Checking {len(entries)} historical candidate URLs (without login or passwords)...")
    results = [None] * len(entries)

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(check_stream, url, args.timeout): index
            for index, (_, url) in enumerate(entries)
        }
        for future in as_completed(futures):
            index = futures[future]
            results[index] = future.result()
            meta, _ = entries[index]
            print(f"[{index + 1}/{len(entries)}] {builder.channel_id(meta) or 'unknown'}: "
                  + ("OPEN" if results[index][0] else results[index][1]))

    verified = [item for item, result in zip(entries, results) if result[0]]
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "categories").mkdir(exist_ok=True)
    (destination / "catalog").mkdir(exist_ok=True)
    playlist = builder.serialize(verified)
    for name in ("adult.m3u", "index.m3u", "index.category.m3u"):
        (destination / name).write_text(playlist, encoding="utf-8")
    (destination / "categories" / "xxx.m3u").write_text(playlist, encoding="utf-8")

    groups = {}
    for meta, url in verified:
        title = builder.adult_group(builder.channel_id(meta))
        groups.setdefault(title, []).append((builder.with_group(meta, title), url))
    for group, items in groups.items():
        (destination / "categories" / (builder.slug(group) + ".m3u")).write_text(
            builder.serialize(items), encoding="utf-8"
        )

    with (destination / "catalog" / "probe-results.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["channel_id", "status", "reason", "url"])
        for (meta, url), result in zip(entries, results):
            writer.writerow([builder.channel_id(meta), "open" if result[0] else "rejected", result[1], url])

    report = {
        "total_historical_candidates": len(entries),
        "open_hls_candidates": len(verified),
        "rejected_candidates": len(entries) - len(verified),
        "unique_open_channel_ids": len({builder.channel_id(meta) for meta, _ in verified}),
        "content_rights_verified": False,
        "samsung_playback_verified": False,
        "method": "anonymous HTTP GET of manifest and a small media segment",
        "note": "Anonymous accessibility does not prove content is licensed or will remain free.",
    }
    (destination / "catalog" / "free-check-report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if not verified:
        print("No accessible candidate streams; refusing to upload an empty playlist.", file=sys.stderr)
        return 2
    if args.publish:
        builder.publish(destination, args.prefix)
    return 0


def self_test() -> None:
    assert not public_url("http://127.0.0.1/file.m3u8")
    assert not public_url("https://localhost/file.m3u8")
    assert not public_url("https://example.com/file.m3u8?token=secret")
    assert not public_url("https://user:pass@example.com/live.m3u8")
    assert first_media_reference("#EXTM3U\n#EXT-X-VERSION:3\n#EXTINF:4,\nseg.ts\n") == "seg.ts"
    assert first_media_reference("#EXTM3U\n#EXT-X-VERSION:3\n") is None
    print("FREE_HLS_SELF_TEST_PASS")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="dist/iptv", help="Directory created by the builder")
    parser.add_argument("--output", default="dist/iptv-free", help="Directory for tested playlists")
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--timeout", type=float, default=7.0)
    parser.add_argument("--publish", action="store_true", help="Upload only tested playlists to Bunny")
    parser.add_argument("--prefix", default="iptv", help="Bunny Storage prefix")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if not 1 <= args.workers <= 16 or not 1 <= args.timeout <= 30:
        parser.error("--workers must be 1..16 and --timeout must be 1..30")
    if not builder.re.fullmatch(r"[a-z0-9_-]+(?:/[a-z0-9_-]+)*", args.prefix):
        parser.error("Invalid --prefix")
    try:
        return run(args)
    except (ValueError, OSError, HTTPError, URLError) as err:
        print("ERROR:", err, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
