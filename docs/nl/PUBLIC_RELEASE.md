# 🚀 De volledige IPTV-catalogus publiceren op je bestaande Bunny CDN

[English](../en/PUBLIC_RELEASE.md) · [Nederlands](../nl/PUBLIC_RELEASE.md) · [Русский](../PUBLIC_RELEASE.md)

Deze werkwijze gebruikt je **bestaande** Storage Zone en Pull Zone. Er worden geen nieuwe betaalde zones aangemaakt en `adult.m3u`, oudere categorielijsten en de oorspronkelijke `index.m3u` worden niet overschreven.

- **Storage Zone:** `lampa-iptv-875323ab-storage`
- **Pull Zone:** `lampa-iptv-875323ab-cdn`
- **Base URL:** https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/

### Bevestigde publicatie — 2 november 2026

De eigenaar heeft het script uitgevoerd: **188 landen-M3U's + één landenindex + zes Pluto-M3U's + drie opgeschoonde Samsung-lijsten = 198 geslaagde uploads**. De terminal bevestigde de CDN-controle voor `plutotv-lite.m3u`, `plutotv-de.m3u`, `plutotv-erotic.m3u`, `lampa-clean-lite.m3u` en `countries/ua.m3u` (`true`). Ook de bestaande `index.m3u` was eerder gecontroleerd. Dit is geen test van alle videostreams.

## Eén opdracht voor macOS

1. Haalt de officiële landenlijsten van IPTV-org op. Ontbrekende bestanden worden apart gemeld; een onvolledige spiegel wordt niet als volledig voorgesteld.
2. Maakt zes Pluto TV-M3U's met gegevens van de openbare BuddyChewChew-generator.
3. Maakt drie opgeschoonde M3U's voor Samsung/Lampa als de bestaande lokale `index.m3u` en `adult.m3u` beschikbaar zijn.
4. Vraagt verborgen om de Bunny **Account API Key**, controleert de bestaande Storage/Pull Zone en uploadt uitsluitend de betreffende M3U-bestanden.
5. Controleert enkele openbare CDN-URL's en schrijft het rapport naar `dist/public-hub/publication-report.json` op de Mac.

## Wat de opdracht uitvoert

Gebruik **dezelfde** map `~/iptv-bunny` met `.bunny-iptv-state.json`. Voer de API-sleutel alleen lokaal in; deel hem niet via GitHub of chat.

```bash
(
  set -euo pipefail
  cd "$HOME/iptv-bunny"
  for file in personal_bunny_playlists.py free_hls_filter.py \
    sync_bunny_countries.py build_lampa_lite.py lampa_category_fix.py \
    auto_bunny_setup.py plutotv_bunny.py publish_public_bunny.py
  do
    curl -fsSL --retry 3 \
      "https://raw.githubusercontent.com/vbrekher/iptv/master/tools/$file" -o "$file"
  done
  python3 publish_public_bunny.py --self-test
  python3 publish_public_bunny.py
)
```

## Optionele modi

| Option | Description |
|---|---|
| `--dry-run` | M3U's voorbereiden, geen Bunny API-aanroepen |
| `--only countries` | Alleen landen bijwerken |
| `--only pluto` | Alleen Pluto TV bijwerken |
| `--only clean` | Alleen opgeschoonde Samsung-lijsten |
| `--self-test` | Offline tests zonder sleutel |

## Voorbeelden van openbare afspeellijsten

| M3U | URL |
|---|---|
| 🇷🇺 Rusland | [countries/ru.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ru.m3u) |
| 🇺🇦 Oekraïne | [countries/ua.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u) |
| 🪐 Pluto Lite | [plutotv-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-lite.m3u) |
| 🇩🇪 Pluto Duitsland | [plutotv-de.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-de.m3u) |
| 🔞 Pluto erotische FAST | [plutotv-erotic.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/plutotv-erotic.m3u) |
| 📺 Lampa Clean Lite | [lampa-clean-lite.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean-lite.m3u) |
| 🌍 Alle landen | [index.country.m3u](https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.country.m3u) |

## Problemen oplossen

- **HTTP 401:** voor uploaden is het schrijfbare wachtwoord van de Storage Zone nodig, met de juiste primaire regio; de Account API Key is daarvoor niet geschikt.
- **Pluto speelt niet af:** de video komt via externe `jmp2.uk`-URL's en kan regiobeperkingen hebben. Een geldige M3U garandeert geen videobeeld.
- **Samsung laadt langzaam:** kies `plutotv-lite.m3u` of `lampa-clean-lite.m3u`; de volledige catalogus is groot.
- **Betaalscherm:** dat scherm zit in de externe HLS-stream. Een geslaagde CDN-upload haalt het niet weg.
- **Failed upload to CUB:** een andere cloudfunctie van de Lampa-plug-in; geen Bunny PUT-fout.
- **Latere statusupdates:** de terminal wijzigt GitHub niet automatisch. Werk de catalogus bij op basis van nieuw bewijs; markeer niet-geteste video niet als geverifieerd.

[Catalog](BUNNY_PLAYLISTS.md) · [GitHub](../../README.md)
