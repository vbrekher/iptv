# Onderzoek naar qist-IPTV en de Pluto TV-uploader

[English](../en/QIST_PLUTOTV.md) · [Nederlands](QIST_PLUTOTV.md) · [Русский](../BUNNY_PLAYLISTS.md)

## Onderzochte repositories van qist (1 november 2026)

In de openbare GitHub-zoekresultaten stonden **36 repositories** van qist. De relevante bestanden en beoordelingen:

| Bron | Wat is gevonden | Beoordeling |
|---|---|---|
| [qist/tvbox/list.m3u](https://github.com/qist/tvbox/blob/master/list.m3u) | 824 EXTINF-vermeldingen, CCTV, regionale zenders, Douyu, NewTV | Kandidaten, mogelijk beperkingen per provider of regio |
| [qist/tvbox/tvlive.txt](https://github.com/qist/tvbox/blob/master/tvlive.txt) | circa 1.453 URL's | Vaak Chinese ISP- of IPv6-toegang vereist |
| [qist/tvbox/tvboxtv.txt](https://github.com/qist/tvbox/blob/master/tvboxtv.txt) | circa 1.391 URL's | Veel Chinese providernetwerken en IPv6 |
| [qist/tvbox/ITV.txt](https://github.com/qist/tvbox/blob/master/ITV.txt) | circa 637 URL's | Afspeelbaarheid niet gecontroleerd |
| [qist/tvbox/zb.txt](https://github.com/qist/tvbox/blob/master/zb.txt) | circa 2.908 URL's, alternatieven en RTMP | Eerst normaliseren en testen |
| [qist/tvbox/list.txt](https://github.com/qist/tvbox/blob/master/list.txt) | circa 202 URL's | Kleinere Chinese CCTV-lijst |
| [qist/tvbox/livex.m3u](https://github.com/qist/tvbox/blob/master/livex.m3u) | 14.651 EXTINF-items, opeenvolgende URL's van vod.mycamtv.net | **UITGESLOTEN**: genummerde cam/VOD-bronnen, geen zelfstandige tv-kanalen |
| [qist/tvbox/cat/tjs/18_tv_config.json](https://github.com/qist/tvbox/blob/master/cat/tjs/18_tv_config.json) | Crawlers voor 18+-sites | Geen stabiele lineaire televisie |
| [qist/livetv](https://github.com/qist/livetv) | YouTube Live via een eigen IPTV-runtime | Software, geen kanaallijst |
| [qist/iptv-static-scan](https://github.com/qist/iptv-static-scan) | HTTP/HLS-scanner | Alleen met toestemming voor het doel gebruiken |
| [qist/tvgate](https://github.com/qist/tvgate) | IPTV-gateway/speler | Software, geen bron van gratis kanalen |
| [qist/TVLogo](https://github.com/qist/TVLogo) | Bibliotheek met logo's | Geen videostreams |

Een URL op GitHub bewijst geen juridische toestemming, kwaliteit, beschikbaarheid of geschiktheid voor Samsung in Oekraïne.

## Andere openbare IPTV/FAST-catalogi

- https://github.com/iptv-org/iptv
- https://github.com/BuddyChewChew/app-m3u-generator
- https://github.com/BuddyChewChew/pluto
- https://github.com/matthuisman/i.mjh.nz
- https://github.com/OwnerPlugins/pluto-tv-m3u

## Pluto TV: onafhankelijke M3U-bestanden voor Bunny

De uploader tools/plutotv_bunny.py leest de Pluto TV ALL- en Duitsland-lijsten van [BuddyChewChew/app-m3u-generator](https://github.com/BuddyChewChew/app-m3u-generator). Hij behoudt zendernamen en tvg-logo's en maakt zes bestanden:

| Bestand | Inhoud |
|---|---|
| plutotv.m3u | Alle regio's, ongeveer 3.016 items; te groot voor veel Samsung-plug-ins |
| plutotv-lite.m3u | Maximaal 240 items, verdeeld over landen, zonder zware EPG |
| plutotv-de.m3u | Ongeveer 200 Duitse Pluto-kanalen |
| plutotv-erotic.m3u | Duitse groep Sinnliche Fantasien met circa 8 erotische FAST-kanalen |
| plutotv-us.m3u | Amerikaanse regio |
| plutotv-gb.m3u | Britse regio |

Alle bronnen gebruiken momenteel de externe HLS-dienst **jmp2.uk**, dus dit zijn **geen directe officiële Pluto-stream-URL's**. Regiobeperkingen, onderbrekingen en voorwaarden kunnen gelden. De FAST-lijsten zijn geen equivalent van betaalde Brazzers-, Penthouse-, Hustler- of Dorcel-zenders.

Het programma uploadt alleen deze bestanden onder /iptv/ naar de bestaande Bunny Storage/Pull Zone op basis van .bunny-iptv-state.json. Het maakt geen nieuwe betaalde zones aan en overschrijft adult.m3u of de algemene index niet.

## Eén opdracht voor macOS

Gebruik de oorspronkelijke map $HOME/iptv-bunny:

~~~bash
(
  set -euo pipefail
  cd "$HOME/iptv-bunny"
  for file in personal_bunny_playlists.py free_hls_filter.py     sync_bunny_countries.py build_lampa_lite.py lampa_category_fix.py     auto_bunny_setup.py plutotv_bunny.py
  do
    curl -fsSL --retry 3       "https://raw.githubusercontent.com/vbrekher/iptv/master/tools/$file"       -o "$file"
  done
  python3 plutotv_bunny.py --self-test
  python3 plutotv_bunny.py
)
~~~

De Bunny Account API Key wordt verborgen gevraagd. Deel deze niet. Na publicatie worden PLUTOTV_UPLOAD_COMPLETE en de CDN_CHECK-regels afgedrukt.

~~~text
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv.m3u
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-de.m3u
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-erotic.m3u
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-us.m3u
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-gb.m3u
~~~

Alleen lokaal bouwen: python3 plutotv_bunny.py --dry-run.
Alleen opnieuw uploaden: python3 plutotv_bunny.py --publish-only.

**Status op 2 november 2026:** alle zes Pluto-bestanden zijn naar Bunny Storage geüpload. De CDN-controles voor de Lite-, Duitse en Erotic FAST-bestanden gaven true. Dit betekent niet dat alle videostreams werken.

Bunny host **uitsluitend tekst-M3U's**, geen video. Begin op een Samsung met plutotv-lite.m3u.

[Openbare afspeellijsten](BUNNY_PLAYLISTS.md) · [Publicatiehandleiding](PUBLIC_RELEASE.md)
