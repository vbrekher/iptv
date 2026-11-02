#!/usr/bin/env python3
"""Read-only verification of every public IPTV HUB playlist on Bunny CDN.

Verifies CDN HTTP response and #EXTM3U header, NOT channel playback.
No Bunny API key, no writes to Storage, no stream playback.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

EXPECTED_HOST = "lampa-iptv-875323ab-cdn.b-cdn.net"
EXPECTED_PREFIX = "/iptv/"
USER_AGENT = "IPTV-HUB-CDN-Audit/1.0"
MAX_HEAD_BYTES = 2048


class NoRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def m3u_header(data: bytes) -> bool:
    return data.removeprefix(b"\xef\xbb\xbf").lstrip(b" \t\r\n").startswith(b"#EXTM3U")


def validate_manifest(catalog: dict) -> list[dict]:
    items = catalog.get("items")
    if not isinstance(items, list) or len(items) != 237:
        raise ValueError("Expected exactly 237 manifest items; refusing incomplete audit")
    if catalog.get("totals", {}).get("links") != len(items):
        raise ValueError("Catalog total does not match manifest")
    paths = set()
    for item in items:
        path = item.get("path")
        url = item.get("url")
        if not isinstance(path, str) or not isinstance(url, str):
            raise ValueError("Missing path or URL")
        parsed = urlsplit(url)
        if (parsed.scheme != "https" or parsed.netloc != EXPECTED_HOST
                or parsed.path != EXPECTED_PREFIX + path
                or parsed.query or parsed.fragment or ".." in path
                or path in paths or not path.endswith(".m3u")):
            raise ValueError("Unexpected CDN URL or duplicate path: " + path)
        paths.add(path)
    if [x["path"] for x in items if x.get("group") == "country"][:2] != [
            "countries/ru.m3u", "countries/ua.m3u"]:
        raise ValueError("Country order changed")
    if any("adulttest" in item["path"].lower() for item in items):
        raise ValueError("Retired playlist unexpectedly present")
    return items


def verify_one(item: dict, timeout: float, retries: int, opener=None) -> dict:
    opener = opener or build_opener(NoRedirects())
    result = {"path": item["path"], "url": item["url"], "ok": False,
              "http_status": None, "m3u_header": False, "error": None}
    for attempt in range(retries + 1):
        request = Request(item["url"], headers={
            "User-Agent": USER_AGENT,
            "Accept": "audio/x-mpegurl, application/vnd.apple.mpegurl, */*",
            "Accept-Encoding": "identity",
            "Range": "bytes=0-2047",
            "Cache-Control": "no-cache",
        })
        try:
            with opener.open(request, timeout=timeout) as response:
                status = response.getcode()
                result["http_status"] = status
                if response.geturl() != item["url"]:
                    result["error"] = "unexpected_redirect"
                elif status not in (200, 206):
                    result["error"] = "http_" + str(status)
                else:
                    result["m3u_header"] = m3u_header(response.read(MAX_HEAD_BYTES))
                    result["ok"] = result["m3u_header"]
                    result["error"] = None if result["ok"] else "invalid_m3u_header"
                    if result["ok"]:
                        return result
                    # An HTML error page with status 200 should not be retried.
                    return result
        except HTTPError as exc:
            result["http_status"] = exc.code
            result["error"] = "http_" + str(exc.code)
            if exc.code in (401, 403, 404, 410):
                return result
        except (URLError, TimeoutError, ConnectionError, OSError) as exc:
            result["error"] = type(exc).__name__
        if attempt < retries:
            time.sleep(min(0.5 * (attempt + 1), 2.0))
    return result


def self_test():
    assert m3u_header(b"#EXTM3U\n#EXTINF:-1,Channel\nhttps://example.org/live.m3u8\n")
    assert m3u_header(b"\xef\xbb\xbf#EXTM3U\r\n")
    assert not m3u_header(b"<html>Access denied</html>")
    assert not m3u_header(b"")
    assert not m3u_header(b"#EXTINF:-1,Missing header")
    print("IPTV_CDN_AUDIT_SELF_TEST_PASS")


def run(args) -> int:
    raw = Path(args.catalog).read_bytes()
    items = validate_manifest(json.loads(raw.decode("utf-8-sig")))
    output = Path(args.output).expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc).isoformat(timespec="seconds")
    results = [None] * len(items)
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        work = {
            pool.submit(verify_one, item, args.timeout, args.retries): i
            for i, item in enumerate(items)
        }
        for future in as_completed(work):
            i = work[future]
            try:
                results[i] = future.result()
            except Exception as exc:
                results[i] = {
                    "path": items[i]["path"], "url": items[i]["url"],
                    "ok": False, "http_status": None,
                    "m3u_header": False, "error": type(exc).__name__,
                }
    passed = sum(bool(r["ok"]) for r in results)
    failed = len(results) - passed
    report = {
        "schema_version": 1,
        "catalog_sha256": hashlib.sha256(raw).hexdigest(),
        "checked_at_utc": started,
        "completed_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "method": "GET Range bytes=0-2047; HTTP 200/206 and #EXTM3U",
        "cdn_host": EXPECTED_HOST,
        "total": len(results),
        "passed": passed,
        "failed": failed,
        "video_playback_checked": False,
        "results": results,
    }
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8")
    print(f"CDN_CHECKED {passed} / {len(results)}")
    print(f"CDN_FAILED {failed}")
    for r in results:
        if not r["ok"]:
            print("FAILED", r["path"], r["http_status"], r["error"])
    print("REPORT_FILE", output.resolve())
    print("VIDEO_PLAYBACK_CHECKED false")
    if not failed:
        print("ALL_237_CDN_M3U_CHECKS_PASS")
    return 0 if not failed else 2


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", default="bunny-playlists.json",
                        help="Downloaded catalog/bunny-playlists.json")
    parser.add_argument("--output", default="public-cdn-report.json",
                        help="Local JSON report; contains no credentials")
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if not (1 <= args.workers <= 24 and 1 <= args.timeout <= 60
            and 0 <= args.retries <= 5):
        parser.error("workers 1-24; timeout 1-60; retries 0-5")
    try:
        return run(args)
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        print("CDN_AUDIT_ERROR", str(exc)[:300], file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
