# 📖 Fork change history

[English](../en/FORK_CHANGELOG.md) · [Nederlands](../nl/FORK_CHANGELOG.md) · [Русский](../FORK_CHANGELOG.md)

This independent fork preserves IPTV-org's attribution and adds a Bunny CDN publishing layer, country/category navigation, Lampa-friendly profiles, and Pluto TV M3Us. It does not include or host video files.

## Merged development changes

| Pull request | Changes delivered |
|---|---|
| [#1 — Personal Bunny Playlists](https://github.com/vbrekher/iptv/pull/1) | Initial local Python M3U builder, historical 18+ candidates and Bunny Storage publishing |
| [#2 — Free HLS filter](https://github.com/vbrekher/iptv/pull/2) | Anonymous HLS manifest and small media-segment checks |
| [#3 — Bunny one-click](https://github.com/vbrekher/iptv/pull/3) | Automatic Storage/Pull Zone provisioning with a hidden Account API Key prompt |
| [#4 — 401 recovery](https://github.com/vbrekher/iptv/pull/4) | Correct primary Storage region, writable password, retry/resume |
| [#5 — Country playlists](https://github.com/vbrekher/iptv/pull/5) | Official country M3Us, grouped index and country-only maintenance |
| [#6 — Samsung Tizen Lite](https://github.com/vbrekher/iptv/pull/6) | Small M3U profiles capped at 240 and 600 entries |
| [#7 — Category normalization](https://github.com/vbrekher/iptv/pull/7) | Exactly one category per channel; removed combined labels such as Family;Series |
| [#8 — Retired experimental tester](https://github.com/vbrekher/iptv/pull/8) | Temporary stream-testing utility subsequently removed from the current public release |
| [#9 — Pluto TV and qist](https://github.com/vbrekher/iptv/pull/9) | Pluto all/lite/DE/US/GB/Erotic FAST and qist repository audit |
| [#10 — Public playlist hub](https://github.com/vbrekher/iptv/pull/10) | 237 URLs, 188 flagged countries, 34 categories, release guide and JSON manifest |
| [#11 — Retire public test catalog](https://github.com/vbrekher/iptv/pull/11) | Remove legacy experimental playlist link, generator, test jobs and related guide |

## Current release evidence

On 2 November 2026, the owner supplied a read-only audit of **all 237 publicly listed Bunny CDN M3U URLs**. Every request returned **HTTP 206 and an `#EXTM3U` header: 237 passed, 0 failed**. The machine-readable [verification evidence](../../catalog/cdn-verification-2026-11-02.json) is retained in this repository.

The catalog contains **188 countries, 34 categories and 15 featured playlists**. The earlier deployment run had reported 198 Storage uploads; those upload counts are historical, while the 237/237 result measures public CDN file delivery. **Individual video streams and Samsung playback were not tested.**

## Multilingual landing page

The root GitHub README now includes clearly visible **English, Russian and Dutch** sections, language navigation and direct M3U links. Dedicated localized README files and country/category directories are retained. All 237 reported CDN checks remain available for inspection.

## Quality and access boundaries

- HLS HTTP 200, or a playable video segment, does not prove a real free television channel. Subscription/paywall screens have been observed.
- Pluto uses third-party jmp2.uk transport and may be geographically restricted.
- Very large M3U lists can hang or slow down Lampa on Samsung Tizen.
- The CDN stores text playlists; it never hosts, downloads or decrypts the video.
- The former experimental test generator has been removed from the current public repository. GitHub historical commits remain accessible.

## Current modules

The maintained fork-specific Python modules include personal_bunny_playlists, free_hls_filter, auto_bunny_setup, sync_bunny_countries, build_lampa_lite, lampa_category_fix, plutotv_bunny, publish_public_bunny, check_public_cdn and verify_public_hub.

## Attribution

Original catalog and upstream implementation: [iptv-org/iptv](https://github.com/iptv-org/iptv), distributed under [CC0](../../LICENSE). Broadcaster trademarks, logos and streams may have separate rights. This fork is not an official IPTV-org CDN.

[Public M3U directory](BUNNY_PLAYLISTS.md) · [Publishing guide](PUBLIC_RELEASE.md) · [Homepage](../../README.md)
