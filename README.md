<div align="center">

# 📺 IPTV HUB
### Publication evidence (2 November 2026)

**237 / 237 playlist URLs passed the owner's terminal CDN verification** (HTTP 206, `#EXTM3U`; 0 failures). [View all 237 verification results](catalog/cdn-verification-2026-11-02.json). This confirms playlist-file access, **not** video playback or channel availability on Samsung.

> Status `✅ CDN checked in terminal` is based on the recorded CDN GET checks. The third-party streams, their playback and licensing were not tested.

<a id="quick-start"></a>

## 🚀 Quick start for Samsung / Lampa

Start with a small playlist: very large M3U files have previously made Lampa slow or unresponsive on Samsung Tizen.

| Playlist | Use | Publication | 
|---|---|---|
| **Lampa Clean Lite** | Up to 240 entries, cleaned categories | [lampa-clean-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean-lite.m3u) | ✅ CDN checked in terminal |
| **Pluto TV Lite** | 240 Pluto FAST entries | [plutotv-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u) | ✅ CDN checked in terminal |
| **Russia** | Russian country playlist | [countries/ru.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ru.m3u) | ✅ CDN checked in terminal |
| **Ukraine** | Ukrainian country playlist | [countries/ua.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u) | ✅ CDN checked in terminal |
| **Complete IPTV** | Full public IPTV list | [index.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.m3u) | ✅ CDN checked in terminal |
| **Country index** | All countries combined | [index.country.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.country.m3u) | ✅ CDN checked in terminal |
| **Adult / XXX** | Previously uploaded original 18+ list | [adult.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/adult.m3u) | ✅ CDN checked in terminal |

<details>
<summary><strong>📱 How to open a playlist</strong></summary>

1. In Lampa's IPTV plugin or VLC, choose the option to open a network playlist.
2. Copy the full HTTPS M3U URL, preferably the Lite version on Samsung.
3. Add it as a direct URL; cloud upload to CUB is a separate plugin operation.
4. An accessible M3U is not proof of playable video. Test individual channels and be mindful of regional restrictions.

</details>

<a id="countries"></a>

## 🌍 Countries — Russia first, Ukraine second

All 188 country M3U files passed the full 2 November 2026 CDN GET check. Russia and Ukraine remain first by project preference.


| Country / Land / Страна | M3U | Status |
|---|---|---|
| 🇷🇺 Russia | [ru.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ru.m3u) | ✅ CDN checked in terminal |
| 🇺🇦 Ukraine | [ua.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u) | ✅ CDN checked in terminal |
| 🇩🇪 Germany | [de.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/de.m3u) | ✅ CDN checked in terminal |
| 🇳🇱 Netherlands | [nl.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/nl.m3u) | ✅ CDN checked in terminal |
| 🇵🇱 Poland | [pl.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/pl.m3u) | ✅ CDN checked in terminal |
| 🇺🇰 United Kingdom | [uk.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/uk.m3u) | ✅ CDN checked in terminal |
| 🇺🇸 United States | [us.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/us.m3u) | ✅ CDN checked in terminal |
| 🇫🇷 France | [fr.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/fr.m3u) | ✅ CDN checked in terminal |
| 🇮🇹 Italy | [it.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/it.m3u) | ✅ CDN checked in terminal |
| 🇪🇸 Spain | [es.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/es.m3u) | ✅ CDN checked in terminal |
| 🇨🇦 Canada | [ca.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ca.m3u) | ✅ CDN checked in terminal |
| 🇯🇵 Japan | [jp.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/jp.m3u) | ✅ CDN checked in terminal |

**[🗺 Browse all 188 country playlists with flags →](docs/en/BUNNY_PLAYLISTS.md#countries)**

<a id="categories"></a>

## 🎭 Themed playlists

34 category M3Us from the first Bunny upload, including News, Sports, Movies, Science and XXX. Some older lists may contain advertising or stale streams.

| M3U | Status |
|---|---|
| [News](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/news.m3u) | ✅ CDN checked in terminal |
| [Sports](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/sports.m3u) | ✅ CDN checked in terminal |
| [Movies](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/movies.m3u) | ✅ CDN checked in terminal |
| [Series](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/series.m3u) | ✅ CDN checked in terminal |
| [Music](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/music.m3u) | ✅ CDN checked in terminal |
| [Kids](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/kids.m3u) | ✅ CDN checked in terminal |
| [Education](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/education.m3u) | ✅ CDN checked in terminal |
| [Science](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/science.m3u) | ✅ CDN checked in terminal |
| [Documentaries](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/documentary.m3u) | ✅ CDN checked in terminal |
| [Travel](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/travel.m3u) | ✅ CDN checked in terminal |
| [XXX](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/xxx.m3u) | ✅ CDN checked in terminal |

**[📂 Browse all 34 categories →](docs/en/BUNNY_PLAYLISTS.md#categories)**

## 🪐 Pluto TV — independent FAST playlists

Created from a third-party generator; streams use jmp2.uk and may be geoblocked. These are not replacements for paid premium channels.

| M3U | Status |
|---|---|
| [plutotv-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u) | ✅ CDN checked in terminal |
| [plutotv-de.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-de.m3u) | ✅ CDN checked in terminal |
| [plutotv-us.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-us.m3u) | ✅ CDN checked in terminal |
| [plutotv-gb.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-gb.m3u) | ✅ CDN checked in terminal |
| [plutotv-erotic.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-erotic.m3u) | ✅ CDN checked in terminal |
| [plutotv.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv.m3u) | ✅ CDN checked in terminal |

## 🔞 Adult / XXX

18+ lists are separate from general viewing. A technical HLS response does not prove that the channel is really free: paywall screens and promotional cam video have been observed. The retired experimental playlist is not included in this public catalog.

[adult.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/adult.m3u) · [categories/xxx.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/xxx.m3u)

## ✅ Verify all 237 Bunny CDN URLs

The read-only checker tests every published URL with an HTTP GET (200/206) and a real `#EXTM3U` header. No Bunny API key or channel-stream playback is involved. Run on your Mac:

```bash
mkdir -p "$HOME/iptv-bunny"
cd "$HOME/iptv-bunny"
curl -fsSL --retry 3 https://raw.githubusercontent.com/vbrekher/iptv/master/tools/check_public_cdn.py -o check_public_cdn.py
curl -fsSL --retry 3 https://raw.githubusercontent.com/vbrekher/iptv/master/catalog/bunny-playlists.json -o bunny-playlists.json
python3 check_public_cdn.py --self-test
python3 check_public_cdn.py --catalog bunny-playlists.json --output public-cdn-report.json
```

The command prints `CDN_CHECKED`, `CDN_FAILED`, and an individual list of failed paths. Share the **local JSON report** to synchronize this README, all three localized directories and the catalog with verified statuses. Do not mark a URL ✅ merely because its Storage upload succeeded. A passing CDN result does not verify the underlying TV stream.

## 🛠 What we changed compared with upstream

Bunny zone provisioning and Storage 401 recovery; country and category exporters; fixed single-category metadata; Lampa Lite files; Pluto FAST playlists; public M3U index with status evidence; machine-readable catalog. Original IPTV-org generators and channel catalog remain credited.

**Documentation:** [Public directory](docs/en/BUNNY_PLAYLISTS.md) · [Publish missing files](docs/en/PUBLIC_RELEASE.md) · [Fork changes](docs/en/FORK_CHANGELOG.md) · [Bunny setup](docs/en/BUNNY_ONE_CLICK.md) · [Pluto and qist research](docs/en/QIST_PLUTOTV.md) · [Personal playlist builder](docs/en/PERSONAL_BUNNY_IPTV.md) · [Machine-readable JSON](catalog/bunny-playlists.json)

---

Based on: [iptv-org/iptv](https://github.com/iptv-org/iptv) · License: [CC0](LICENSE) · [Contributing](CONTRIBUTING.md)

The Bunny CDN hosts M3U metadata, not third-party video. Brands, logos and streams remain subject to their owners' terms.
