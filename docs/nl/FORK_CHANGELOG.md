# 📖 Wijzigingen in deze fork

[English](../en/FORK_CHANGELOG.md) · [Nederlands](../nl/FORK_CHANGELOG.md) · [Русский](../FORK_CHANGELOG.md)

Deze onafhankelijke fork vermeldt de oorspronkelijke makers van IPTV-org en voegt publicatie via Bunny CDN, landen en categorieën, Lampa-vriendelijke afspeellijsten en Pluto TV toe. De fork host geen videobestanden.

## Samengevoegde ontwikkelfasen

| Pull request | Toegevoegde functies |
|---|---|
| [#1 — Personal Bunny Playlists](https://github.com/vbrekher/iptv/pull/1) | Lokale Python-generator voor M3U, historische 18+-kandidaten en publicatie op Bunny Storage |
| [#2 — Free HLS filter](https://github.com/vbrekher/iptv/pull/2) | Anonieme controle van HLS-manifest en een klein videosegment |
| [#3 — Bunny one-click](https://github.com/vbrekher/iptv/pull/3) | Automatische aanleg van Storage/Pull Zone met verborgen invoer van de Account API Key |
| [#4 — 401 recovery](https://github.com/vbrekher/iptv/pull/4) | Juiste primaire opslagregio, schrijfwachtwoord, opnieuw proberen en hervatten |
| [#5 — Country playlists](https://github.com/vbrekher/iptv/pull/5) | Officiële landen-M3U's, gezamenlijke index en onderhoud per land |
| [#6 — Samsung Tizen Lite](https://github.com/vbrekher/iptv/pull/6) | Kleine M3U-profielen van maximaal 240 en 600 items |
| [#7 — Category normalization](https://github.com/vbrekher/iptv/pull/7) | Precies één categorie per zender; geen samengestelde labels zoals Family;Series |
| [#8 — Retired experimental tester](https://github.com/vbrekher/iptv/pull/8) | Tijdelijke testfunctie voor streams, later uit de huidige openbare versie verwijderd |
| [#9 — Pluto TV and qist](https://github.com/vbrekher/iptv/pull/9) | Pluto volledig/lite/DE/US/GB/Erotic FAST en onderzoek naar qist-repositories |
| [#10 — Public playlist hub](https://github.com/vbrekher/iptv/pull/10) | 237 URL's, 188 landen met vlag, 34 categorieën, publicatiehandleiding en JSON-manifest |
| [#11 — Retire public test catalog](https://github.com/vbrekher/iptv/pull/11) | Verwijderde experimentele playlist, generator, CI-tests en bijbehorende handleiding |

## Bevestigde publicatiestatus

Op 2 november 2026 heeft de eigenaar **alle 237 openbare M3U-URL's** via Bunny CDN gecontroleerd. Elke aanvraag gaf **HTTP 206 en een `#EXTM3U`-header: 237 geslaagd, 0 mislukt**. Het volledige [controlerapport](../../catalog/cdn-verification-2026-11-02.json) is bewaard.

De directory bevat **188 landen, 34 categorieën en 15 speciale afspeellijsten**. De eerdere 198 Storage-uploads zijn historische publicatiegegevens; de nieuwe controle betreft alle 237 publieke CDN-bestanden. **Afspelen van individuele videostreams en op Samsung is niet getest.**

## Meertalige hoofdpagina

De GitHub-hoofdpagina toont nu **Engels, Russisch en Nederlands** met duidelijke navigatie en directe M3U-links. De aparte vertaalde README-bestanden en volledige catalogi blijven beschikbaar.

## Grenzen aan kwaliteit en toegang

- Een HLS HTTP 200 of een afspeelbaar videosegment bewijst niet dat een zender echt gratis is; er zijn betaalmeldingen gezien.
- Pluto gebruikt de externe dienst jmp2.uk en kan regiobeperkingen hebben.
- Zeer grote M3U-bestanden kunnen Lampa op Samsung Tizen traag maken of laten vastlopen.
- De CDN bewaart alleen afspeellijsten in tekstvorm; video wordt niet gehost, gedownload of ontsleuteld.
- De vroegere experimentele testgenerator is verwijderd uit de huidige openbare code. De historische GitHub-commits blijven bestaan.

## Huidige modules

De fork beheert onder andere personal_bunny_playlists, free_hls_filter, auto_bunny_setup, sync_bunny_countries, build_lampa_lite, lampa_category_fix, plutotv_bunny, publish_public_bunny, check_public_cdn en verify_public_hub.

## Herkomst en auteursrecht

Oorspronkelijke catalogus en basis: [iptv-org/iptv](https://github.com/iptv-org/iptv), onder [CC0](../../LICENSE). Merken, logo's en streams kunnen afzonderlijke rechten hebben. Deze fork is geen officiële CDN van IPTV-org.

[Public M3U directory](BUNNY_PLAYLISTS.md) · [Publishing guide](PUBLIC_RELEASE.md) · [Homepage](../../README.md)
