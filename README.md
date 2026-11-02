<div align="center">

# 📺 IPTV HUB
### 🌍 Global channels · 📂 Categories · 🪐 Pluto TV · 🔞 Adult · 🐰 Bunny CDN

**Public M3U directory for Samsung Tizen / Lampa, VLC and other IPTV players.**

[![CI](https://github.com/vbrekher/iptv/actions/workflows/personal-bunny-playlists.yml/badge.svg)](https://github.com/vbrekher/iptv/actions/workflows/personal-bunny-playlists.yml) [![License: CC0](https://img.shields.io/badge/License-CC0-5c6bc0.svg)](LICENSE) [![237 M3U](https://img.shields.io/badge/M3U_links-237-2da8a6.svg)](docs/en/BUNNY_PLAYLISTS.md)

**🌐 Language / Taal / Язык:** [English](README.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md)

[📚 All playlists](docs/en/BUNNY_PLAYLISTS.md) · [🚀 Quick start](#quick-start) · [🌍 Countries](#countries) · [📖 Changes](docs/en/FORK_CHANGELOG.md)

</div>

---

> [!IMPORTANT]
> Independent fork of [iptv-org/iptv](https://github.com/iptv-org/iptv), not an official IPTV-org CDN. A published M3U does not guarantee that its source video plays, is HD, is free to watch, or is licensed for redistribution.

## ✨ What makes this fork different

| 🌍 | 📂 | 📺 | 🪐 |
|---|---|---|---|
| 188 countries with flags | 34 themed categories | Lightweight Samsung playlists | Separate Pluto TV and adult category lists |

**237 public M3U links** = 188 countries + 34 categories + 15 featured playlists. This is a directory count, **not** a count of playable TV channels.

### Publication evidence (2 November 2026)

**6 CDN-checked files**, **229 additional Storage-uploaded files**, **2 unconfirmed paths**. The 6 include the previously checked `index.m3u` and 5 files confirmed by the latest terminal `CDN_CHECKS`. These figures reflect specific terminal output, not independent playback testing.

> A note about status: Storage upload = Bunny accepted the M3U file. CDN checked = a terminal GET returned an M3U header. Neither means that the TV channel plays on Samsung.

<a id="quick-start"></a>

## 🚀 Quick start for Samsung / Lampa

Start with a small playlist: very large M3U files have previously made Lampa slow or unresponsive on Samsung Tizen.

| Playlist | Use | Publication | 
|---|---|---|
| **Lampa Clean Lite** | Up to 240 entries, cleaned categories | [lampa-clean-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean-lite.m3u) | ✅ CDN checked in terminal |
| **Pluto TV Lite** | 240 Pluto FAST entries | [plutotv-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u) | ✅ CDN checked in terminal |
| **Russia** | Russian country playlist | [countries/ru.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ru.m3u) | ☑️ Uploaded to Bunny Storage |
| **Ukraine** | Ukrainian country playlist | [countries/ua.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u) | ✅ CDN checked in terminal |
| **Complete IPTV** | Full public IPTV list | [index.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.m3u) | ✅ CDN checked in terminal |
| **Country index** | All countries combined | [index.country.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.country.m3u) | ☑️ Uploaded to Bunny Storage |
| **Adult / XXX** | Previously uploaded original 18+ list | [adult.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/adult.m3u) | ☑️ Uploaded to Bunny Storage |

<details>
<summary><strong>📱 How to open a playlist</strong></summary>

1. In Lampa's IPTV plugin or VLC, choose the option to open a network playlist.
2. Copy the full HTTPS M3U URL, preferably the Lite version on Samsung.
3. Add it as a direct URL; cloud upload to CUB is a separate plugin operation.
4. An accessible M3U is not proof of playable video. Test individual channels and be mindful of regional restrictions.

</details>

<a id="countries"></a>

## 🌍 Countries — Russia first, Ukraine second

All 188 country M3U links are marked as Storage-uploaded in the latest terminal log. Russia and Ukraine are pinned at the top by project preference, followed by the remaining countries.

| Country / Land / Страна | M3U | Status |
|---|---|---|
| 🇷🇺 Russia | [ru.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ru.m3u) | ☑️ Uploaded to Bunny Storage |
| 🇺🇦 Ukraine | [ua.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u) | ✅ CDN checked in terminal |
| 🇩🇪 Germany | [de.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/de.m3u) | ☑️ Uploaded to Bunny Storage |
| 🇳🇱 Netherlands | [nl.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/nl.m3u) | ☑️ Uploaded to Bunny Storage |
| 🇵🇱 Poland | [pl.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/pl.m3u) | ☑️ Uploaded to Bunny Storage |
| 🇺🇰 United Kingdom | [uk.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/uk.m3u) | ☑️ Uploaded to Bunny Storage |
| 🇺🇸 United States | [us.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/us.m3u) | ☑️ Uploaded to Bunny Storage |
| 🇫🇷 France | [fr.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/fr.m3u) | ☑️ Uploaded to Bunny Storage |
| 🇮🇹 Italy | [it.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/it.m3u) | ☑️ Uploaded to Bunny Storage |
| 🇪🇸 Spain | [es.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/es.m3u) | ☑️ Uploaded to Bunny Storage |
| 🇨🇦 Canada | [ca.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ca.m3u) | ☑️ Uploaded to Bunny Storage |
| 🇯🇵 Japan | [jp.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/jp.m3u) | ☑️ Uploaded to Bunny Storage |

**[🗺 Browse all 188 country playlists with flags →](docs/en/BUNNY_PLAYLISTS.md#countries)**

<a id="categories"></a>

## 🎭 Themed playlists

34 category M3Us from the first Bunny upload, including News, Sports, Movies, Science and XXX. Some older lists may contain advertising or stale streams.

| M3U | Status |
|---|---|
| [Новости](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/news.m3u) | ☑️ Uploaded to Bunny Storage |
| [Спорт](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/sports.m3u) | ☑️ Uploaded to Bunny Storage |
| [Фильмы](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/movies.m3u) | ☑️ Uploaded to Bunny Storage |
| [Сериалы](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/series.m3u) | ☑️ Uploaded to Bunny Storage |
| [Музыка](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/music.m3u) | ☑️ Uploaded to Bunny Storage |
| [Детские](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/kids.m3u) | ☑️ Uploaded to Bunny Storage |
| [Образование](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/education.m3u) | ☑️ Uploaded to Bunny Storage |
| [Наука](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/science.m3u) | ☑️ Uploaded to Bunny Storage |
| [Документальные](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/documentary.m3u) | ☑️ Uploaded to Bunny Storage |
| [Путешествия](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/travel.m3u) | ☑️ Uploaded to Bunny Storage |
| [XXX)](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/xxx.m3u) | ☑️ Uploaded to Bunny Storage |

**[📂 Browse all 34 categories →](docs/en/BUNNY_PLAYLISTS.md#categories)**

## 🪐 Pluto TV — independent FAST playlists

Created from a third-party generator; streams use jmp2.uk and may be geoblocked. These are not replacements for paid premium channels.

| M3U | Status |
|---|---|
| [plutotv-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u) | ✅ CDN checked in terminal |
| [plutotv-de.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-de.m3u) | ✅ CDN checked in terminal |
| [plutotv-us.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-us.m3u) | ☑️ Uploaded to Bunny Storage |
| [plutotv-gb.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-gb.m3u) | ☑️ Uploaded to Bunny Storage |
| [plutotv-erotic.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-erotic.m3u) | ✅ CDN checked in terminal |
| [plutotv.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv.m3u) | ☑️ Uploaded to Bunny Storage |

## 🔞 Adult / XXX

18+ lists are separate from general viewing. A technical HLS response does not prove that the channel is really free: paywall screens and promotional cam video have been observed. The retired experimental playlist is not included in this public catalog.

[adult.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/adult.m3u) · [categories/xxx.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/xxx.m3u)

## 🛠 What we changed compared with upstream

Bunny zone provisioning and Storage 401 recovery; country and category exporters; fixed single-category metadata; Lampa Lite files; Pluto FAST playlists; public M3U index with status evidence; machine-readable catalog. Original IPTV-org generators and channel catalog remain credited.

**Documentation:** [Public directory](docs/en/BUNNY_PLAYLISTS.md) · [Publish missing files](docs/en/PUBLIC_RELEASE.md) · [Fork changes](docs/en/FORK_CHANGELOG.md) · [Bunny setup](docs/en/BUNNY_ONE_CLICK.md) · [Pluto and qist research](docs/en/QIST_PLUTOTV.md) · [Personal playlist builder](docs/en/PERSONAL_BUNNY_IPTV.md) · [Machine-readable JSON](catalog/bunny-playlists.json)

---

Based on: [iptv-org/iptv](https://github.com/iptv-org/iptv) · License: [CC0](LICENSE) · [Contributing](CONTRIBUTING.md)

The Bunny CDN hosts M3U metadata, not third-party video. Brands, logos and streams remain subject to their owners' terms.
