# Beschikbare IPTV-afspeellijsten

[English — volledige oorspronkelijke lijst](PLAYLISTS.md) · [Nederlands](PLAYLISTS.nl.md) · [Русский — Bunny-catalogus](docs/BUNNY_PLAYLISTS.md)

Dit is de Nederlandstalige toegang tot de afspeellijsten van de onafhankelijke fork **vbrekher/iptv**. De oorspronkelijke [PLAYLISTS.md](PLAYLISTS.md) wordt automatisch door IPTV-org opgebouwd en bevat de volledige tabel met bronlanden, categorieën en M3U-adressen. Kanaalnamen, codes, bestandspaden en M3U-URL's blijven daar in hun oorspronkelijke vorm, omdat zij identifiers en geen te vertalen gebruikersinterface zijn.

## De Bunny-catalogus van deze fork

De [Nederlandstalige openbare catalogus](docs/nl/BUNNY_PLAYLISTS.md) bevat **237 directe M3U-links**, verdeeld in:

- **188 landen** met vlaggen, met 🇷🇺 Rusland eerst en 🇺🇦 Oekraïne tweede.
- **34 categorieën**, zoals Nieuws, Sport, Films, Documentaires en Muziek.
- **15 speciale afspeellijsten**, waaronder Samsung Clean Lite, Pluto TV en de aparte 18+-categorie.

Voor een Samsung-tv is [Lampa Clean Lite](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean-lite.m3u) vaak handiger dan een grote catalogus.

## Publicatiestatus

Volgens de terminaluitvoer van de eigenaar op **2 november 2026** zijn 198 M3U-bestanden succesvol naar Bunny Storage geüpload: 188 landbestanden, de landenindex, zes Pluto TV-lijsten en drie opgeschoonde Samsung-lijsten. Vijf bestanden uit die run zijn tevens via CDN gecontroleerd. Het hoofdbestand index.m3u was al eerder gecontroleerd.

In totaal zijn in de huidige catalogus **6 CDN-controles**, **229 overige bevestigde Storage-uploads** en **2 niet-bevestigde adressen** geregistreerd. **Dit zijn geen afspeeltests van de afzonderlijke zenders.**

## Directe M3U-adressen

| Afspeellijst | URL |
|---|---|
| 🇷🇺 Rusland | [countries/ru.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ru.m3u) |
| 🇺🇦 Oekraïne | [countries/ua.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u) |
| 🌍 Alle landen | [index.country.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.country.m3u) |
| 📺 Samsung Clean Lite | [lampa-clean-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean-lite.m3u) |
| 🪐 Pluto TV Lite | [plutotv-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u) |
| 📰 Nieuws | [categories/news.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/news.m3u) |
| ⚽ Sport | [categories/sports.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/categories/sports.m3u) |

Bekijk **[alle 237 links en de status per bestand](docs/nl/BUNNY_PLAYLISTS.md)**. De complete upstream-dataset staat in [PLAYLISTS.md](PLAYLISTS.md).

## Belangrijk

Een M3U-bestand kan bestaan en via Bunny worden geleverd terwijl de videostream wegens een betaalmuur, regioblokkade, reclame of ongeschikte codec niet werkt. Bunny host alleen afspeellijsten, geen video.

[Homepage in het Nederlands](README.nl.md) · [Publicatiehandleiding](docs/nl/PUBLIC_RELEASE.md) · [Bijdragen](CONTRIBUTING.nl.md)
