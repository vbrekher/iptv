# Scripts en onderhoudsopdrachten

[English](../scripts.md) · [Nederlands](scripts.md)

De IPTV-org-repository bevat scripts om terugkerend onderhoud te automatiseren. Hiervoor is [Node.js](https://nodejs.org/en) nodig. Deze Node-scripts horen bij het oorspronkelijke IPTV-org-project; voor de aparte Python-tools voor Bunny is **geen Node.js** nodig.

## Overzicht

| Opdracht | Functie |
|---|---|
| act:check | De GitHub-workflow check lokaal uitvoeren |
| act:format | De formatteringsworkflow lokaal uitvoeren |
| act:update | De updateworkflow lokaal uitvoeren |
| act:validate_discussion | Validatie van discussies lokaal simuleren |
| act:validate_issue | Validatie van issues lokaal simuleren |
| act:validate_label | Labelvalidatie lokaal simuleren |
| api:load | Actuele zender- en streamgegevens ophalen |
| discussion:validate | Een discussieverzoek controleren |
| issue:validate | Een issue-aanvraag controleren |
| playlist:format | Interne afspeellijsten formatteren |
| playlist:update | Goedgekeurde wijzigingen verwerken |
| playlist:generate | Openbare M3U-afspeellijsten genereren |
| playlist:validate | ID's en streamlinks controleren |
| playlist:lint | Syntax van interne M3U-bestanden controleren |
| playlist:test | Links in interne afspeellijsten testen |
| playlist:edit | Streams snel toewijzen |
| playlist:export | JSON-export voor de IPTV-org API |
| readme:update | De openbare PLAYLISTS.md-index bijwerken |
| report:create | Rapport van huidige issues maken |
| lint | De onderhoudsscripts op syntax controleren |
| test | Testen van de repository |

## act:check

Voert de [check-workflow](workflows.md#check) lokaal uit met [nektos/gh-act](https://github.com/nektos/gh-act).

~~~bash
npm run act:check
~~~

## act:format

Voert de [format-workflow](workflows.md#format) lokaal uit.

~~~bash
npm run act:format
~~~

## act:update

Voert de [update-workflow](workflows.md#update) lokaal uit.

~~~bash
npm run act:update
~~~

## act:validate_discussion

Simuleert het openen van een GitHub-discussie en controleert de aanvraag. Er is een lokale GitHub-tokenvariabele nodig; plaats nooit echte tokens in gedeelde logs.

~~~bash
npm run act:validate_discussion -- -e .github/mocks/events/discussion_opened.json -s GITHUB_TOKEN=github_pat_***
~~~

## act:validate_issue

Simuleert een nieuw issue.

~~~bash
npm run act:validate_issue -- -e .github/mocks/events/issue_opened.json
~~~

## act:validate_label

Simuleert een goedgekeurd label voor een issue.

~~~bash
npm run act:validate_label -- -e .github/mocks/events/issue_approved.json --actor Bob
~~~

## api:load

Haalt de laatste zender- en streamgegevens op uit [iptv-org/api](https://github.com/iptv-org/api).

~~~bash
npm run api:load
~~~

## discussion:validate

Controleert een discussieverzoek op fouten en schrijft het resultaat naar temp/logs/result.json.

~~~bash
npm run discussion:validate --number=123 --body="### Stream URL..."
~~~

## issue:validate

Controleert een issue-aanvraag en slaat de fouten op in temp/logs/errors.txt.

~~~bash
npm run issue:validate --body="### Stream URL..." --labels="streams:add"
~~~

## playlist:format

Formatteert interne afspeellijsten: URL-normalisatie, duplicaten verwijderen, ongeldige ID's corrigeren of verwijderen en streams sorteren op zendernaam, kwaliteit en label.

~~~bash
# Alle afspeellijsten in streams/ formatteren
npm run playlist:format

# Eén specifiek bestand
npm run playlist:format path/to/playlist.m3u
~~~

## playlist:update

Verwerkt goedgekeurde wijzigingsaanvragen uit GitHub-issues en werkt interne afspeellijsten bij.

~~~bash
npm run playlist:update
~~~

## playlist:generate

Genereert alle openbare afspeellijsten op basis van de database.

~~~bash
npm run playlist:generate
~~~

## playlist:validate

Controleert ID's en URL's in interne afspeellijsten op fouten.

~~~bash
npm run playlist:validate
npm run playlist:validate path/to/playlist.m3u
~~~

## playlist:lint

Controleert interne M3U-bestanden op syntaxfouten.

~~~bash
npm run playlist:lint
npm run playlist:lint path/to/playlist.m3u
~~~

## playlist:test

Test links in interne afspeellijsten en toont per stream het zender-ID, de URL, het label en de status.

~~~bash
npm run playlist:test
npm run playlist:test path/to/playlist.m3u
npm run playlist:test streams/fr.m3u
~~~

Mogelijke statuswaarden zijn bijvoorbeeld OK, LOADING, HTTP_FORBIDDEN, HTTP_NOT_FOUND, HTTP_GATEWAY_TIMEOUT en FFMPEG_STREAMS_NOT_FOUND. Een afspeelbare HTTP-reactie zegt niet automatisch dat het beeld een echte, gratis televisie-uitzending is.

Met de optie --fix verwijdert het script de gevonden defecte streams uit je **lokale kopie** van de afspeellijsten:

~~~bash
npm run playlist:test streams/fr.m3u -- --fix
~~~

Controleer het resultaat voordat je wijzigingen commit; een geoblokkeerde zender is niet per definitie kapot.

## playlist:edit

Hulpprogramma om streams snel aan de juiste kanalen te koppelen.

~~~bash
npm run playlist:edit path/to/playlist.m3u
~~~

## playlist:export

Maakt een JSON-bestand met alle streams voor de [iptv-org/api](https://github.com/iptv-org/api)-repository.

~~~bash
npm run playlist:export
~~~

## readme:update

Werkt de oorspronkelijke PLAYLISTS.md-index met beschikbare afspeellijsten bij.

~~~bash
npm run readme:update
~~~

**Let op:** de eigen drietalige Bunny-catalogus wordt apart bijgehouden en maakt geen onderdeel uit van dit upstream-script.

## report:create

Maakt een rapport over de huidige issues.

~~~bash
npm run report:create
~~~

## lint

Controleert de utilityscripts zelf op syntaxfouten.

~~~bash
npm run lint
~~~

## test

Voert de tests van de bovenstaande scripts uit.

~~~bash
npm test
~~~

## Aanvullende Python-tools van deze fork

Voor Bunny Storage, Pluto TV, landenbestanden en Samsung-Lampa zijn er scripts in [tools/](../../tools). Voorbeelden:

~~~bash
python3 tools/verify_public_hub.py
python3 tools/publish_public_bunny.py --self-test
python3 tools/publish_public_bunny.py --dry-run
~~~

Lees de [Bunny-publicatiehandleiding](PUBLIC_RELEASE.md) voordat je publieke M3U's bijwerkt.
