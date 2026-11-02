# qist IPTV research and Pluto TV Bunny uploader

> **Deployment evidence, 2 November 2026:** the user's Terminal reported successful upload of all six Pluto M3Us. CDN checks passed for `plutotv-lite.m3u`, `plutotv-de.m3u`, and `plutotv-erotic.m3u`. Playback of individual channels is not confirmed.

## qist repositories inspected (2026-11-01)

GitHub public repository search returned 36 qist repositories. Most relevant:

| Source | Evidence | Assessment |
|---|---|---|
| https://github.com/qist/tvbox/blob/master/list.m3u | 824 EXTINF records; CCTV, regional, Douyu, NewTV | IPTV candidate list, operator/region limitations |
| https://github.com/qist/tvbox/blob/master/tvlive.txt | ~1,453 URL occurrences | Chinese ISP/IPv6 access often required |
| https://github.com/qist/tvbox/blob/master/tvboxtv.txt | ~1,391 URL occurrences | Chinese operator streams, many IPv6 |
| https://github.com/qist/tvbox/blob/master/ITV.txt | ~637 URL occurrences | Candidate-only, not playback-verified |
| https://github.com/qist/tvbox/blob/master/zb.txt | ~2,908 URL occurrences, RTMP and alternatives | Requires format normalization |
| https://github.com/qist/tvbox/blob/master/list.txt | ~202 URLs | Smaller Chinese CCTV set |
| https://github.com/qist/tvbox/blob/master/livex.m3u | 14,651 EXTINF; https://vod.mycamtv.net/1.m3u8 up to /14872.m3u8 | EXCLUDE: numbered cam/VOD content, not channels |
| https://github.com/qist/tvbox/blob/master/cat/tjs/18_tv_config.json | 18+ site crawlers | Not stable linear broadcasts |
| https://github.com/qist/livetv | Uses YouTube Live as IPTV; requires runtime | Software, not content list |
| https://github.com/qist/iptv-static-scan | HTTP/HLS scanner | Use only on authorized targets |
| https://github.com/qist/tvgate | IPTV gateway/player | Software, not a channel source |
| https://github.com/qist/TVLogo | Logo library | No live video |

Finding a public source link does not establish licensing, real playback,
video quality or geographic accessibility from a Ukrainian Samsung TV.

## Additional public IPTV/FAST directories

- https://github.com/iptv-org/iptv
- https://github.com/BuddyChewChew/app-m3u-generator
- https://github.com/BuddyChewChew/pluto
- https://github.com/matthuisman/i.mjh.nz
- https://github.com/OwnerPlugins/pluto-tv-m3u

## Pluto TV: isolated M3U publication

The uploader tools/plutotv_bunny.py reads Pluto TV ALL and Germany
M3U playlists from BuddyChewChew/app-m3u-generator. It preserves channel
names and tvg-logo links and emits six separate M3Us:

- plutotv.m3u: all-region, approximately 3016 entries; too big for Samsung.
- plutotv-lite.m3u: at most 240 entries balanced across countries, no huge EPG.
- plutotv-de.m3u: approximately 200 German Pluto channels.
- plutotv-erotic.m3u: German Sinnliche Fantasien category, about 8 channels.
- plutotv-us.m3u: US regional subset.
- plutotv-gb.m3u: UK regional subset.

All sources presently use the third-party jmp2.uk HLS transport, NOT
official Pluto direct URLs. Geo-blocks, interruptions and provider terms
may apply. These playlists are FREE/FAST, not an equivalent to premium
Brazzers, Penthouse, Hustler or Dorcel subscriptions.

The script uploads ONLY these files under /iptv/ to the pre-existing
Bunny Storage + Pull Zone from local .bunny-iptv-state.json; no new
paid resources and no overwrites of adult.m3u or indexes.

### One Terminal command for macOS

Run from the original $HOME/iptv-bunny directory:

    (
      set -euo pipefail
      cd "$HOME/iptv-bunny"
      for file in personal_bunny_playlists.py free_hls_filter.py \
        sync_bunny_countries.py build_lampa_lite.py lampa_category_fix.py \
        auto_bunny_setup.py plutotv_bunny.py
      do
        curl -fsSL --retry 3 \
          "https://raw.githubusercontent.com/vbrekher/iptv/master/tools/$file" \
          -o "$file"
      done
      python3 plutotv_bunny.py --self-test
      python3 plutotv_bunny.py
    )

The script prompts for Bunny Account API Key using hidden input.
Do not share the key. Successful publication prints
PLUTOTV_UPLOAD_COMPLETE plus CDN_CHECK.

Expected CDN paths after successful upload:

    https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv.m3u
    https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u
    https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-de.m3u
    https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-erotic.m3u
    https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-us.m3u
    https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-gb.m3u

Dry-run: python3 plutotv_bunny.py --dry-run
Upload resume: python3 plutotv_bunny.py --publish-only

Only playlist TEXT is hosted on Bunny; video streams remain with their
third-party providers. The stream contents are not individually
playback-verified. Do not import the giant ALL playlist into Lampa/Tizen
unless your IPTV plugin can handle large catalogs.
