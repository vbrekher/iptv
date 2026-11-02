# Persoonlijke IPTV-afspeellijsten op Bunny CDN

[English](../en/PERSONAL_BUNNY_IPTV.md) · [Nederlands](PERSONAL_BUNNY_IPTV.md) · [Русский](../BUNNY_PLAYLISTS.md)

De optionele lokale generator hoort bij de fork vbrekher/iptv en staat los van de oorspronkelijke GitHub Pages-publicatie van IPTV-org.

## Wat wel en niet wordt teruggehaald

- De historische NSFW-blokkeerlijst bevatte **368 zender-ID's**. ID's zijn geen videostreams.
- De generator leest de actuele blokkeerlijst en een bevroren momentopname van 29 januari 2024. Daarin waren **65 oude volwassen stream-URL's** te vinden in de XXX-categorie en de index; **61** horen bij momenteel geblokkeerde NSFW-ID's.
- Deze URL's zijn **niet gecontroleerde kandidaten** en kunnen verlopen, betaald of regiogebonden zijn.
- Bronnen met een expliciete DMCA-blokkade worden niet opgenomen.
- Het programma herstelt geen wachtwoorden, persoonlijke abonnements-URL's of betaalde toegangsgegevens en omzeilt geen beperkingen.
- Bunny Storage bevat alleen M3U-tekst; er wordt geen video gedownload, getranscodeerd of geproxyd.
- Controleer vóór openbare publicatie de rechten van de inhoud.

## Uitvoeren op macOS (Python 3.9+)

~~~bash
mkdir -p "$HOME/iptv-bunny"
cd "$HOME/iptv-bunny"
curl -fsSLo personal_bunny_playlists.py   https://raw.githubusercontent.com/vbrekher/iptv/master/tools/personal_bunny_playlists.py
python3 personal_bunny_playlists.py --self-test
python3 personal_bunny_playlists.py --output ./dist/iptv
~~~

Node.js, npm, Tizen SDK en een database zijn niet nodig.

## Gegenereerde bestanden

~~~text
dist/iptv/index.m3u
dist/iptv/index.category.m3u
dist/iptv/adult.m3u
dist/iptv/categories/xxx.m3u
dist/iptv/categories/adultiptv.m3u
dist/iptv/categories/mycamtv.m3u
dist/iptv/categories/other-adult.m3u
dist/iptv/categories/<public-category>.m3u
dist/iptv/countries/ua.m3u
dist/iptv/catalog/nsfw-status.csv
dist/iptv/catalog/report.json
~~~

De algemene index combineert de openbare IPTV-index met historische 18+-kandidaten. De optie --no-public maakt een lijst zonder gewone zenders; --country nl selecteert het openbare landenbestand voor Nederland. Herhaald uitvoeren kan de uitvoermap overschrijven.

Het CSV-bestand nsfw-status.csv vermeldt alle huidige NSFW-identificaties als historical_url_unverified of no_known_url. **Het aantal regels is geen aantal werkende kanalen.**

## Publiceren via Bunny Storage en een gekoppelde Pull Zone

Open het [Bunny-dashboard](https://dash.bunny.net/).

1. Maak een Storage Zone en noteer de naam en primaire regio (bijvoorbeeld de).
2. Maak of koppel een Pull Zone en noteer de hostnaam, bijvoorbeeld my-playlists.b-cdn.net.
3. Zoek het schrijfbare **Storage Zone Password** op onder de toegangsinstellingen; dit is niet de Bunny Account API Key.
4. Controleer het [Acceptable Use Policy](https://bunny.net/acceptable-use/) en de rechten op publicatie.

Voer in de projectmap uit:

~~~bash
python3 personal_bunny_playlists.py --output ./dist/iptv --publish
~~~

De generator vraagt naar de zonenaam, primaire regio, CDN-host en het verborgen wachtwoord en uploadt de kleine M3U-bestanden. Plaats het wachtwoord nooit in een GitHub-bestand, terminalopdracht of openbare log.

Optionele omgevingsvariabelen zijn BUNNY_STORAGE_ZONE, BUNNY_STORAGE_REGION, BUNNY_CDN_HOST en BUNNY_STORAGE_PASSWORD. Vermijd blijvende opslag van het wachtwoord.

Voorbeelden na publicatie:

~~~text
https://my-playlists.b-cdn.net/iptv/index.m3u
https://my-playlists.b-cdn.net/iptv/adult.m3u
https://my-playlists.b-cdn.net/iptv/categories/xxx.m3u
https://my-playlists.b-cdn.net/iptv/categories/adultiptv.m3u
https://my-playlists.b-cdn.net/iptv/categories/mycamtv.m3u
https://my-playlists.b-cdn.net/iptv/categories/other-adult.m3u
https://my-playlists.b-cdn.net/iptv/countries/ua.m3u
~~~

Voeg een URL rechtstreeks aan Lampa toe. Het kenmerk group-title bepaalt de categorie; afzonderlijke categories-bestanden zijn optioneel. Na vervanging kan Bunny een oude versie cachen tot de TTL verloopt of de cache wordt geleegd. Publicatie van de M3U verhuist de video niet naar Bunny en heft geen beperkingen van de aanbieder op.

## GitHub en Bunny gescheiden houden

Het originele IPTV-org-project verwijderde in januari 2024 XXX-verwijzingen na een verzoek van GitHub Trust & Safety. Deze fork zet de officiële GitHub Pages-publicatie van NSFW niet opnieuw aan en commit geen gegenereerde persoonlijke M3U's. De functie is uitsluitend bedoeld voor de fork; voeg deze niet terug in het upstream-project. Publiceer alleen binnen de gebruiksvoorwaarden en rechten van de bronnen.

## Problemen oplossen

- **HTTP 401 bij upload:** controleer het schrijfbare wachtwoord van de Storage Zone en de primaire regio.
- **HTTP 404 vanaf de CDN:** controleer de koppeling met de Pull Zone en de prefix /iptv/.
- **M3U opent, maar geen beeld:** een stream kan verlopen, betaalde toegang vragen, geografisch beperkt of codec-incompatibel zijn. Het gewone openbare kanaalbestand wordt niet altijd live gecontroleerd.
- **Alleen historische volwassen kandidaten:** gebruik --no-public.

[Openbare afspeellijsten](BUNNY_PLAYLISTS.md) · [Publicatiehandleiding](PUBLIC_RELEASE.md)
