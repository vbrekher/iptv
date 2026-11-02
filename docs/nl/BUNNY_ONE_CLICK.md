# Bunny in één opdracht instellen voor Lampa IPTV

[English](../en/BUNNY_ONE_CLICK.md) · [Nederlands](BUNNY_ONE_CLICK.md) · [Русский](../BUNNY_PLAYLISTS.md)

Deze optionele installatie hoort uitsluitend bij de onafhankelijke fork **vbrekher/iptv**. Het programma maakt een Bunny **Storage Zone** en een gekoppelde **Pull Zone** aan met één verborgen invoer van de **Bunny Account API Key**. Het bouwt M3U-bestanden met openbaar vermelde IPTV-bronnen, controleert historische 18+-kandidaten op anonieme HLS-toegang en uploadt **alleen tekstbestanden**, nooit videobestanden. Het omzeilt geen abonnementen.

## macOS: plak de volledige opdracht in Terminal

\`\`\`bash
mkdir -p "$HOME/iptv-bunny" && cd "$HOME/iptv-bunny"
for file in personal_bunny_playlists.py free_hls_filter.py auto_bunny_setup.py sync_bunny_countries.py build_lampa_lite.py lampa_category_fix.py; do
  curl -fsSL --retry 3 \
    "https://raw.githubusercontent.com/vbrekher/iptv/master/tools/$file" \
    -o "$file" || exit 1
done
python3 auto_bunny_setup.py
\`\`\`

Terminal vraagt verborgen om **Bunny Account API Key**. Gebruik de Account API Key, niet het wachtwoord van de Storage Zone. Het programma haalt het schrijfwachtwoord automatisch op via de beheers-API van Bunny. Sleutels worden niet in bronbestanden of GitHub-commits opgeslagen. Deel sleutels nooit via chat. Benodigd: Python 3.9 of nieuwer, zonder npm.

## Wat doet het installatieprogramma?

1. Controleert de rechten van de Bunny Account API Key.
2. Haalt de openbare IPTV-index, categorieën, landbestanden en historische 18+-kandidaten op. De aanvullende community-kandidaten staan standaard aan; schakel ze uit met \`--without-community\`.
3. Vraagt anoniem de HLS-manifesten en een klein deel van een mediasegment op. Ongeldige of niet-reagerende kandidaten worden weggelaten; logins, DRM-omzeiling en getekende abonnementstokens worden niet gebruikt.
4. Maakt een Storage Zone aan in regio **DE** en koppelt de Pull Zone via \`StorageZoneId\` en \`OriginType=2\`. **Dit zijn betaalde Bunny-resources.**
5. Uploadt uitsluitend M3U-tekst en kleine catalogusbestanden, geen video.
6. Toont de publieke CDN-adressen en controleert een M3U-antwoord.
7. Bewaart alleen niet-gevoelige resourcenamen in \`.bunny-iptv-state.json\`. Vanuit dezelfde map hergebruikt de volgende uitvoering de zones.

De meeste gewone IPTV-kanalen worden **niet individueel live getest**. De historische 18+-kandidaten krijgen wel een beperkte technische HLS-controle. HTTP-toegang bewijst nooit of een stream echt gratis, van goede kwaliteit of juridisch verspreidbaar is.

Na publicatie verschijnen onder meer deze URL's:

\`\`\`text
https://<your-pull-zone>.b-cdn.net/iptv/index.m3u
https://<your-pull-zone>.b-cdn.net/iptv/adult.m3u
https://<your-pull-zone>.b-cdn.net/iptv/categories/xxx.m3u
https://<your-pull-zone>.b-cdn.net/iptv/countries/ru.m3u
https://<your-pull-zone>.b-cdn.net/iptv/countries/ua.m3u
\`\`\`

Voeg de gewenste M3U-URL rechtstreeks toe aan Lampa. Als geen enkele 18+-kandidaat door de controle komt, bevat \`adult.m3u\` geen zenders. De algemene index kan dan nog steeds worden gepubliceerd.

## Fout in de Lampa-categorieën verhelpen

In oudere M3U's stonden samengestelde waarden zoals \`group-title="Documentary;Education;Outdoor;Relax"\` en \`group-title="Family;Series"\`. Sommige Lampa-plug-ins lezen zo'n hele waarde als **één aparte categorie**, waardoor honderden categorieën met slechts één zender verschenen.

De gerepareerde generator kiest voor iedere zender **precies één standaardcategorie** (bijvoorbeeld Documentary of Series). Zeer kleine groepen worden onder General geplaatst; XXX blijft apart. Het volledige bestand behoudt dezelfde zender-URL's.

Werk de al aanwezige installatie bij vanuit dezelfde map:

\`\`\`bash
(
  set -e
  cd "$HOME/iptv-bunny"
  for file in auto_bunny_setup.py lampa_category_fix.py; do
    curl -fsSL --retry 3 \
      "https://raw.githubusercontent.com/vbrekher/iptv/master/tools/$file" -o "$file"
  done
  python3 auto_bunny_setup.py --fix-categories-only
)
\`\`\`

Dit hergebruikt de bestaande zones en lokale \`index.m3u\` en \`adult.m3u\`. De 72 historische kandidaten worden niet opnieuw gescand, landenbestanden worden niet opnieuw opgehaald en het oorspronkelijke \`adult.m3u\` wordt niet overschreven.

Gebruik vervolgens een **nieuw playlist-item** in Lampa met één van deze adressen:

\`\`\`text
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean-lite.m3u
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean.m3u
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.clean.m3u
\`\`\`

**CUB-fout:** \`[M3U Function (Failed upload to CUB)]\` verwijst naar een cloudactie van een Lampa-plug-in, niet naar het uploaden naar Bunny Storage. Deze normalisatie herstelt geen CUB-account, cloudrechten of externe CUB-server. Probeer de nieuwe M3U daarom bij voorkeur rechtstreeks via de IPTV-URL.

## Snelle afspeellijsten voor Samsung Tizen

Een M3U met duizenden items kan de IPTV-plug-in van een Samsung-tv vertragen of laten vastlopen. Daarom maakt de fork kleine, per categorie verdeelde lijsten:

- \`/iptv/lampa-lite.m3u\` — maximaal **240 items**, inclusief eerder geteste 18+-verwijzingen; probeer deze eerst.
- \`/iptv/lampa.m3u\` — maximaal **600 items**, dezelfde categorieën met meer keuze.

Deze lijsten bevatten \`group-title\`, maar hosten geen eigen video. De gewone openbare bronnen zijn niet individueel getest.

Alleen deze kleine bestanden uploaden:

\`\`\`bash
(
  set -e
  cd "$HOME/iptv-bunny"
  for file in auto_bunny_setup.py build_lampa_lite.py; do
    curl -fsSL --retry 3 \
      "https://raw.githubusercontent.com/vbrekher/iptv/master/tools/$file" -o "$file"
  done
  python3 auto_bunny_setup.py --lite-only
)
\`\`\`

Deze onderhoudsmodus maakt geen nieuwe zones, scant geen historische videolinks en uploadt de grote index niet. Als ook de 240-itemversie blijft hangen, controleer dan de netwerkverbinding van de tv, het CDN-antwoord, CORS en de betreffende IPTV-plug-in. Het is niet nodig om meteen heel Lampa opnieuw te installeren.

## Alle landen op een bestaande Bunny-zone

De eerste installer uploadde alleen \`countries/ua.m3u\`. Dat was een beperking van de oorspronkelijke fork-code, niet van Bunny of IPTV-org. De huidige landenmodule leest de officiële landenindex van IPTV-org.

\`\`\`bash
cd "$HOME/iptv-bunny"
for file in auto_bunny_setup.py sync_bunny_countries.py; do
  curl -fsSL --retry 3 \
    "https://raw.githubusercontent.com/vbrekher/iptv/master/tools/$file" -o "$file"
done
python3 auto_bunny_setup.py --countries-only
\`\`\`

\`--countries-only\` hergebruikt de bestaande Storage/Pull Zone en maakt **geen nieuwe betaalde zones**. Deze oudere importeur stopt als een bronbestand ontbreekt. De nieuwere centrale publicatietool \`publish_public_bunny.py\` meldt fouten per land en kan de overige beschikbare landen toch uploaden.

**Status op 2 november 2026:** volgens de terminaluitvoer zijn **188 landbestanden plus \`index.country.m3u\` naar Bunny Storage geüpload**. De CDN-controle voor \`countries/ua.m3u\` gaf \`true\`. De overige individuele videostreams zijn niet geverifieerd. In onze documentatie staat 🇷🇺 Rusland eerst, 🇺🇦 Oekraïne tweede.

\`\`\`text
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ru.m3u
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.country.m3u
\`\`\`

## Herstel van Bunny Storage HTTP 401

Een \`401 Unauthorized\` tijdens **Uploading ...** betekent dat de Storage API het schrijfwachtwoord of de primaire regio van de zone niet accepteerde. Het is niet per se een fout van de Account API Key of de IPTV-kanaalcontrole.

De installer haalt de **werkelijke primaire regio** op, ververst de toegang tot de Storage Zone en herhaalt een HTTP 401/403-upload met beperkte wachttijden. Voor het uploaden worden de gegenereerde bestanden lokaal opgeslagen, zodat herhaald scannen niet nodig is.

Als een upload uitvalt:

\`\`\`bash
cd "$HOME/iptv-bunny"
python3 auto_bunny_setup.py --upload-only
\`\`\`

Laat \`.bunny-iptv-state.json\` staan. Controleer bij herhaalde fouten in het Bunny-dashboard onder **Storage → FTP & API Access** het schrijfbare Storage Zone Password en de primaire regio. De algemene Account API Key en ReadOnlyPassword zijn **geen geldige schrijfsleutels voor de Storage API**. Verwijder niet zomaar werkende zones.

## Beveiliging en beperkingen

- De Bunny Account API Key en het schrijfwachtwoord worden niet als plaintext opgeslagen in het project.
- Er is geen Bunny Stream, Magic Containers of Database nodig.
- Alleen anonieme technische HLS-toegang wordt gecontroleerd; licenties, betalingsstatus en Tizen-codecs niet.
- De CDN kan oudere versies cachen; gebruik zo nodig een korte TTL of verwijder de betreffende cache.
- Nieuwe video wordt nooit door Bunny opgeslagen, gedecodeerd, omgeleid of gedownload.
- Echte livechecks vereisen de account van de eigenaar, diens netwerk en Samsung-tv. Broncode-tests mogen dit niet als bewezen eind-tot-eindwerking presenteren.

Lokale test zonder Bunny-resourcewijzigingen:

\`\`\`bash
python3 auto_bunny_setup.py --self-test
\`\`\`

[Volledige M3U-catalogus](BUNNY_PLAYLISTS.md) · [Publicatiehandleiding](PUBLIC_RELEASE.md)
