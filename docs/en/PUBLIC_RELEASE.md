# 🚀 Publish the complete IPTV directory to your existing Bunny CDN

[English](../en/PUBLIC_RELEASE.md) · [Nederlands](../nl/PUBLIC_RELEASE.md) · [Русский](../PUBLIC_RELEASE.md)

This procedure is for an **existing** Storage Zone and Pull Zone. It does not create billable resources or overwrite the old `adult.m3u`, category files, or original `index.m3u`.

- **Storage Zone:** `lampa-iptv-875323ab-storage`
- **Pull Zone:** `lampa-iptv-875323ab-cdn`
- **Base URL:** https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/

### Current deployment evidence — 2 November 2026

The owner already ran this script successfully: **188 country M3Us + one country index + six Pluto M3Us + three clean Samsung files = 198 successful uploads**. The command returned CDN checks for `plutotv-lite.m3u`, `plutotv-de.m3u`, `plutotv-erotic.m3u`, `lampa-clean-lite.m3u`, and `countries/ua.m3u`, all `true`. The existing `index.m3u` was also checked in an earlier run. This is not a full playback test.

## One command for macOS

1. Fetches official IPTV-org country lists. A missing or broken country file is reported individually, without falsely claiming a complete mirror.
2. Builds six Pluto TV M3Us from the BuddyChewChew public playlist generator.
3. Builds three cleaned Samsung/Lampa M3Us when local `index.m3u` and `adult.m3u` are present.
4. Prompts for the Bunny **Account API Key** with hidden input, verifies the already existing Storage/Pull Zone, and uploads only selected M3U files.
5. Checks a few public CDN URLs and writes `dist/public-hub/publication-report.json` on the owner's Mac.

## What the command does

Use the **same** `~/iptv-bunny` directory that contains `.bunny-iptv-state.json`. The API key is entered locally and must not be sent to GitHub or chat.

```bash
(
  set -euo pipefail
  cd "$HOME/iptv-bunny"
  for file in personal_bunny_playlists.py free_hls_filter.py \
    sync_bunny_countries.py build_lampa_lite.py lampa_category_fix.py \
    auto_bunny_setup.py plutotv_bunny.py publish_public_bunny.py
  do
    curl -fsSL --retry 3 \
      "https://raw.githubusercontent.com/vbrekher/iptv/master/tools/$file" -o "$file"
  done
  python3 publish_public_bunny.py --self-test
  python3 publish_public_bunny.py
)
```

## Optional modes

| Option | Description |
|---|---|
| `--dry-run` | Prepare M3Us, never call the Bunny API |
| `--only countries` | Refresh country playlists only |
| `--only pluto` | Refresh Pluto TV only |
| `--only clean` | Refresh only cleaned Samsung playlists |
| `--self-test` | Offline local tests, no credentials |

## Public playlist examples

| M3U | URL |
|---|---|
| 🇷🇺 Russia | [countries/ru.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ru.m3u) |
| 🇺🇦 Ukraine | [countries/ua.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u) |
| 🪐 Pluto Lite | [plutotv-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u) |
| 🇩🇪 Pluto Germany | [plutotv-de.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-de.m3u) |
| 🔞 Pluto Erotic FAST | [plutotv-erotic.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-erotic.m3u) |
| 📺 Lampa Clean Lite | [lampa-clean-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean-lite.m3u) |
| 🌍 All countries | [index.country.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.country.m3u) |

## Troubleshooting

- **HTTP 401:** Bunny Storage needs the writable Storage Zone password and the correct primary region; do not upload with the Account API Key directly.
- **Pluto video fails:** the video is served by third-party `jmp2.uk` URLs and may be geographically restricted. A valid M3U does not guarantee playback.
- **Samsung takes too long:** prefer `plutotv-lite.m3u` or `lampa-clean-lite.m3u`; the all-region catalog is large.
- **Subscription payment screen:** the external HLS stream contains the paywall screen; CDN upload success does not remove it.
- **Failed upload to CUB:** a separate Lampa plugin cloud feature; not a Bunny Storage PUT error.
- **Future status updates:** terminal reports do not automatically edit GitHub. Update the machine-readable catalog with the new evidence; never mark untested video as verified.

[Catalog](BUNNY_PLAYLISTS.md) · [GitHub](../../README.md)
