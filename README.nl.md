<div align="center">

# 📺 IPTV HUB
### 🌍 Global channels · 📂 Categories · 🪐 Pluto TV · 🔞 Adult · 🐰 Bunny CDN

**Openbare M3U-catalogus voor Samsung Tizen / Lampa, VLC en andere IPTV-spelers.**

[![CI](https://github.com/vbrekher/iptv/actions/workflows/personal-bunny-playlists.yml/badge.svg)](https://github.com/vbrekher/iptv/actions/workflows/personal-bunny-playlists.yml) [![License: CC0](https://img.shields.io/badge/License-CC0-5c6bc0.svg)](LICENSE) [![237 M3U](https://img.shields.io/badge/M3U_links-237-2da8a6.svg)](docs/nl/BUNNY_PLAYLISTS.md)

**🌐 Language / Taal / Язык:** [English](README.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md)

[📚 Alle afspeellijsten](docs/nl/BUNNY_PLAYLISTS.md) · [🚀 Snel starten](#quick-start) · [🌍 Landen](#countries) · [📖 Wijzigingen](docs/nl/FORK_CHANGELOG.md)

</div>

---

> [!IMPORTANT]
> Onafhankelijke fork van [iptv-org/iptv](https://github.com/iptv-org/iptv); geen officiële CDN van IPTV-org. Een gepubliceerde M3U garandeert niet dat een videostream werkt, HD is, gratis kan worden bekeken of legaal opnieuw mag worden verspreid.

## ✨ Wat deze fork toevoegt

| 🌍 | 📂 | 📺 | 🪐 |
|---|---|---|---|
| 188 landen met vlaggen | 34 thematische categorieën | Lichte Samsung-afspeellijsten | Aparte Pluto TV- en 18+-lijsten |

**237 openbare M3U-links** = 188 landen + 34 categorieën + 15 speciale afspeellijsten. Dit zijn adressen, **geen 237 bewezen werkende zenders**.

### Publicatiestatus (2 november 2026)

**237/237 openbare M3U-bestanden zijn in de terminal via de CDN gecontroleerd** (HTTP 206 en `#EXTM3U`; 0 fouten). [Volledig controlerapport](catalog/cdn-verification-2026-11-02.json). Dit bevestigt de bereikbaarheid van de bestanden, **niet** of elke zender op Samsung afspeelt.

> **✅ CDN checked in terminal** betekent dat de afspeellijst bereikbaar was. Videoweergave en distributierechten zijn niet gecontroleerd.

<a id="quick-start"></a>

## 🚀 Snel starten met Samsung / Lampa

Begin met een kleine lijst: grote M3U-bestanden hebben Lampa op Samsung Tizen eerder traag gemaakt.

| Afspeellijst | Inhoud | Publicatie | 
|---|---|---|
| **Lampa Clean Lite** | Maximaal 240 items, opgeschoonde categorieën | [lampa-clean-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean-lite.m3u) | ✅ CDN checked in terminal |
| **Pluto TV Lite** | 240 Pluto FAST-zenders | [plutotv-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u) | ✅ CDN checked in terminal |
| **Rusland** | Russische landenlijst | [countries/ru.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ru.m3u) | ✅ CDN checked in terminal |
| **Oekraïne** | Oekraïense landenlijst | [countries/ua.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u) | ✅ CDN checked in terminal |
| **Volledige IPTV** | Volledige openbare IPTV-index | [index.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.m3u) | ✅ CDN checked in terminal |
| **Landenindex** | Alle landen samen | [index.country.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.country.m3u) | ✅ CDN checked in terminal |
| **Adult / XXX** | Oorspronkelijke 18+-lijst | [adult.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/adult.m3u) | ✅ CDN checked in terminal |

<details>
<summary><strong>📱 Een afspeellijst openen</strong></summary>

1. Open in de IPTV-plug-in van Lampa of in VLC een netwerkafspeellijst.
2. Kopieer de volledige HTTPS-M3U-link. Kies op Samsung bij voorkeur de Lite-versie.
3. Voeg de lijst rechtstreeks via de URL toe. Uploaden naar CUB is een andere plug-infunctie.
4. Een leesbare M3U zegt niets over de afspeelbaarheid van iedere zender; regionale beperkingen zijn mogelijk.

</details>

<a id="countries"></a>

## 🌍 Landen — eerst Rusland, dan Oekraïne

Alle 188 landenlijsten zijn op 2 november 2026 via de CDN gecontroleerd. Rusland staat eerst, gevolgd door Oekraïne.

| Country / Land / Страна | M3U | Status |
|---|---|---|
| 🇷🇺 Rusland | [ru.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ru.m3u) | ✅ CDN checked in terminal |
| 🇺🇦 Oekraïne | [ua.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u) | ✅ CDN checked in terminal |
| 🇩🇪 Duitsland | [de.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/de.m3u) | ✅ CDN checked in terminal |
| 🇳🇱 Nederland | [nl.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/nl.m3u) | ✅ CDN checked in terminal |
| 🇵🇱 Polen | [pl.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/pl.m3u) | ✅ CDN checked in terminal |
| 🇺🇰 Verenigd Koninkrijk | [uk.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/uk.m3u) | ✅ CDN checked in terminal |
| 🇺🇸 Verenigde Staten | [us.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/us.m3u) | ✅ CDN checked in terminal |
| 🇫🇷 Frankrijk | [fr.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/fr.m3u) | ✅ CDN checked in terminal |
| 🇮🇹 Italië | [it.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/it.m3u) | ✅ CDN checked in terminal |
| 🇪🇸 Spanje | [es.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/es.m3u) | ✅ CDN checked in terminal |
| 🇨🇦 Canada | [ca.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ca.m3u) | ✅ CDN checked in terminal |
| 🇯🇵 Japan | [jp.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/jp.m3u) | ✅ CDN checked in terminal |

**[🗺 Bekijk alle 188 landen met vlaggen →](docs/nl/BUNNY_PLAYLISTS.md#countries)**

<a id="categories"></a>

## 🎭 Thematische afspeellijsten

34 categorie-M3U's uit de eerste Bunny-upload, waaronder Nieuws, Sport, Films, Wetenschap en XXX. Oudere lijsten kunnen reclame of verouderde streams bevatten.

| M3U | Status |
|---|---|
| [Nieuws](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/news.m3u) | ✅ CDN checked in terminal |
| [Sport](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/sports.m3u) | ✅ CDN checked in terminal |
| [Films](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/movies.m3u) | ✅ CDN checked in terminal |
| [Series](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/series.m3u) | ✅ CDN checked in terminal |
| [Muziek](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/music.m3u) | ✅ CDN checked in terminal |
| [Kinderen](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/kids.m3u) | ✅ CDN checked in terminal |
| [Onderwijs](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/education.m3u) | ✅ CDN checked in terminal |
| [Wetenschap](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/science.m3u) | ✅ CDN checked in terminal |
| [Documentaires](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/documentary.m3u) | ✅ CDN checked in terminal |
| [Reizen](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/travel.m3u) | ✅ CDN checked in terminal |
| [XXX](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/xxx.m3u) | ✅ CDN checked in terminal |

**[📂 Bekijk alle 34 categorieën →](docs/nl/BUNNY_PLAYLISTS.md#categories)**

## 🪐 Pluto TV — aparte FAST-afspeellijsten

Gebouwd met gegevens van een externe generator; de streams gebruiken jmp2.uk en kunnen regiobeperkingen hebben. Dit zijn geen vervangers van betaalde premiumzenders.

| M3U | Status |
|---|---|
| [plutotv-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u) | ✅ CDN checked in terminal |
| [plutotv-de.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-de.m3u) | ✅ CDN checked in terminal |
| [plutotv-us.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-us.m3u) | ✅ CDN checked in terminal |
| [plutotv-gb.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-gb.m3u) | ✅ CDN checked in terminal |
| [plutotv-erotic.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-erotic.m3u) | ✅ CDN checked in terminal |
| [plutotv.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv.m3u) | ✅ CDN checked in terminal |

## 🔞 Adult / XXX

18+-lijsten staan los van de gewone catalogus. Een geslaagde HLS-controle bewijst niet dat de stream echt gratis is: er zijn betaalschermen en camreclames waargenomen. De oude testlijst is niet opgenomen.

[adult.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/adult.m3u) · [categories/xxx.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/xxx.m3u)

## ✅ Alle 237 Bunny-CDN-links controleren

Deze alleen-lezen controle test iedere URL op HTTP 200/206 en de echte `#EXTM3U`-header. Er is geen Bunny API-sleutel nodig; video wordt niet afgespeeld. Voer dit uit op je Mac:

```bash
mkdir -p "$HOME/iptv-bunny"
cd "$HOME/iptv-bunny"
curl -fsSL --retry 3 https://raw.githubusercontent.com/vbrekher/iptv/master/tools/check_public_cdn.py -o check_public_cdn.py
curl -fsSL --retry 3 https://raw.githubusercontent.com/vbrekher/iptv/master/catalog/bunny-playlists.json -o bunny-playlists.json
python3 check_public_cdn.py --self-test
python3 check_public_cdn.py --catalog bunny-playlists.json --output public-cdn-report.json
```

De opdracht toont `CDN_CHECKED`, `CDN_FAILED` en alle mislukte paden. Met het **lokale JSON-rapport** kunnen de statussen in de drie talen en in de catalogus worden bijgewerkt. Een geslaagde Storage-upload krijgt niet automatisch ✅; afspeelbaarheid van videostreams is niet getest.

## 🛠 Wat we hebben aangepast ten opzichte van het origineel

Automatisch instellen van Bunny-zones en herstel van Storage 401; M3U-bestanden per land en categorie; één duidelijke categorie per zender; lichte Lampa-lijsten; Pluto FAST; een openbare directory met publicatiestatus en een machineleesbare catalogus. Het oorspronkelijke IPTV-org-project blijft vermeld.

**Documentatie:** [Openbare catalogus](docs/nl/BUNNY_PLAYLISTS.md) · [Ontbrekende bestanden publiceren](docs/nl/PUBLIC_RELEASE.md) · [Wijzigingen aan de fork](docs/nl/FORK_CHANGELOG.md) · [Bunny instellen](docs/nl/BUNNY_ONE_CLICK.md) · [Pluto en qist-onderzoek](docs/nl/QIST_PLUTOTV.md) · [Persoonlijke afspeellijsten](docs/nl/PERSONAL_BUNNY_IPTV.md) · [JSON-catalogus](catalog/bunny-playlists.json)

---

Gebaseerd op: [iptv-org/iptv](https://github.com/iptv-org/iptv) · Licentie: [CC0](LICENSE) · [Contributing](CONTRIBUTING.md)

Bunny CDN host M3U-metagegevens, niet de videobeelden van derden. Merken, logo's en streams vallen onder de voorwaarden van hun eigenaren.
