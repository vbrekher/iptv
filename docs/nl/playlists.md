# Afspeellijsten

De repository gebruikt twee typen M3U-afspeellijsten: **intern** en **openbaar**.

## Interne afspeellijsten

Deze staan in de map [streams/](../../streams) en bevatten de links die op dit moment in de repository beschikbaar zijn. De links zijn per land en per uitzenddienst gerangschikt, vooral om het beheer makkelijker te maken.

Een minimale interne afspeellijst:

~~~m3u
#EXTM3U
#EXTINF:-1 tvg-id="ExampleTV.us@SD",Example TV (720p)
https://example.com/playlist.m3u8
~~~

Als voor een zender een gids beschikbaar is in de [EPG-repository](https://github.com/iptv-org/epg/blob/master/GUIDES.md), kan de header hiernaar verwijzen:

~~~m3u
#EXTM3U x-tvg-url="https://example.com/guide.xml"
~~~

Omdat scripts deze bestanden verwerken, gelden de volgende regels:

- De bestandsuitgang is '.m3u'.
- Het bestand begint met '#EXTM3U'.
- Elke link volgt het [schema voor streambeschrijvingen](stream-description-scheme.md).
- Regeleinden zijn [CRLF](https://developer.mozilla.org/en-US/docs/Glossary/CRLF).
- De tekencodering is UTF-8 zonder BOM.

## Openbare afspeellijsten

Openbare afspeellijsten zijn bedoeld voor kijkers. Het upstream-project genereert ze iedere dag om **00:00 UTC** met het script 'playlist:generate' en publiceert ze in de [gh-pages-branch](https://github.com/iptv-org/iptv/tree/gh-pages).

Zenders worden ingedeeld op basis van de beschrijving in de [iptv-org-database](https://github.com/iptv-org/database). Een zender met uitzendgebied 'c/IT' komt bijvoorbeeld in 'countries/it.m3u' terecht.

Normaal wordt per zender alleen de beste beschikbare stream opgenomen, rekening houdend met kwaliteit en labels. De uitzondering is de map 'raw/'.

Bij een geldige [stream-ID](stream-id.md) worden logo, categorie, land en taal aan de beschrijving toegevoegd:

~~~m3u
#EXTM3U x-tvg-url="https://example.com/guide.xml"
#EXTINF:-1 tvg-id="ExampleTV.us@SD" tvg-logo="https://example.com/logo.png" group-title="Movies",Example TV (720p)
https://example.com/playlist.m3u8
~~~

De volledige oorspronkelijke lijst staat in [PLAYLISTS.md](../../PLAYLISTS.md). De onafhankelijke Bunny-catalogus van onze fork staat in [BUNNY_PLAYLISTS.md](BUNNY_PLAYLISTS.md).

[English](../playlists.md) · [Nederlands](playlists.md)
