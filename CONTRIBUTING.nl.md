# Bijdragen aan het project

[English](CONTRIBUTING.md) · [Nederlands](CONTRIBUTING.nl.md) · [Русский](README.ru.md)

## Inleiding

**IPTV-org** is niet alleen een verzameling links. Dankzij jarenlang onderhoud bestaat er een kennisbank voor [zenders](https://github.com/iptv-org/database), [streams](https://github.com/iptv-org/iptv) en [elektronische programmagidsen](https://github.com/iptv-org/epg). Om deze gegevens te beheren, gelden strikte regels voor structuur, naamgeving en moderatie.

Deze fork heeft daarnaast eigen Bunny- en Lampa-tools. Bijdragen aan die code horen thuis in [vbrekher/iptv](https://github.com/vbrekher/iptv), terwijl updates aan de oorspronkelijke zenderdatabase volgens de upstream-regels worden ingediend.

## Hoe kan ik bijdragen?

### Een nieuwe streamlink toevoegen

Er zijn twee mogelijkheden:

1. Stuur een aanvraag via het [formulier voor een stream](https://github.com/iptv-org/iptv/issues/new?assignees=&labels=streams:add&projects=&template=1_streams_add.yml&title=Add%3A+). Na goedkeuring wordt de link bij een volgende update toegevoegd.
2. Voeg een link zelf toe in een [pull request](https://github.com/iptv-org/iptv/pulls). Zie [Afspeellijsten](docs/nl/playlists.md).

Controleer vooraf het volgende:

- Gebruik een geldige [stream-ID](docs/nl/stream-id.md).
- De zender staat niet op de [blokkeerlijst](https://iptv-org.github.io/).
- De URL staat nog niet in de repository; controleer dit met [GitHub Code Search](https://github.com/search?q=repo%3Aiptv-org%2Fiptv+http%3A%2F%2Fexample.com&type=code).
- De stream werkt stabiel. Volg de handleiding [Streams testen](docs/nl/stream-testing.md).
- Controleer of de stream [geografisch is geblokkeerd](docs/nl/geo-blocking.md); vermeld dit indien van toepassing.
- Vermijd [Xtream Codes](docs/nl/xtream-codes.md) en [tijdelijke tokenlinks](docs/nl/tokenized-links.md).
- De URL verwijst zo rechtstreeks mogelijk naar de uitzending, zonder onnodige omleidingen.

Als een stream slechts in bepaalde landen werkt of regelmatig onderbroken wordt, vermeld dit duidelijk in je aanvraag.

**Belangrijk:** een aanvraag zonder geldige stream-ID of werkende URL wordt direct gesloten.

### De beschrijving van een stream corrigeren

De meeste metadata (zendernaam, feednaam, categorie, taal, uitzendgebied en logo) worden met de stream-ID uit de [database](https://github.com/iptv-org/database) gehaald. Er zijn daarom twee gebruikelijke oorzaken van fouten:

- **Verkeerde stream-ID:** wijzig de ID via het [streambewerkingformulier](https://github.com/iptv-org/iptv/issues/new?assignees=&labels=streams%3Aedit&projects=&template=2_streams_edit.yml&title=Edit%3A+). De lijst met beschikbare zenders en ID's staat op [iptv-org.github.io](https://iptv-org.github.io/).
- **Onjuiste databasegegevens:** controleer de invoer en volg de [bijdrage-instructies voor de database](https://github.com/iptv-org/database/blob/master/CONTRIBUTING.md#how-to-edit-a-database-entry).

Na goedkeuring wordt de beschrijving automatisch in de verschillende publicaties bijgewerkt.

### Een defecte stream melden

Gebruik het [formulier voor defecte streams](https://github.com/iptv-org/iptv/issues/new?assignees=&labels=streams:remove&projects=&template=3_streams_report.yml&title=Broken%3A+). Zodra een werkende vervanger beschikbaar is, kan deze worden toegevoegd; anders kan de defecte link worden verwijderd.

Controleer vooraf of de URL nog in de repository staat en of de fout niet alleen door een [regioblokkade](docs/nl/geo-blocking.md) wordt veroorzaakt. Zie [Streams testen](docs/nl/stream-testing.md).

**Belangrijk:** een issue zonder geldige stream-URL wordt gesloten.

### Mijn zender uit de lijst laten verwijderen

De eigenaar van een zender of een officiële vertegenwoordiger kan het [verwijderingsformulier](https://github.com/iptv-org/iptv/issues/new?assignees=&labels=removal+request&projects=&template=6_copyright-claim.yml&title=Remove%3A+) invullen. Dergelijke verzoeken worden doorgaans binnen één werkdag beoordeeld. Na goedkeuring wordt de link verwijderd en de zender aan de [blokkeerlijst](https://github.com/iptv-org/database/blob/master/data/blocklist.csv) toegevoegd om herpublicatie te voorkomen.

Verzoeken van niet-bevoegde derden worden gesloten.

## Structuur van de repository

- **.github/** — discussiesjablonen, issuesjablonen, [GitHub Actions-workflows](docs/nl/workflows.md) en gedragscode.
- **.readme/** — afbeelding en sjabloon voor de oorspronkelijke afspeellijsten.
- **scripts/** — interne Node.js-onderhoudsscripts; [documentatie](docs/nl/scripts.md).
- **streams/** — oorspronkelijke interne afspeellijsten; [uitleg](docs/nl/playlists.md).
- **tests/** — tests voor de broncode.
- **CONTRIBUTING.md** — originele Engelstalige bijdrage-instructies.
- **PLAYLISTS.md** — door upstream gegenereerde afspeellijstindex.
- **README.md** — Engelstalige hoofdpagina van de fork.
- **tools/** — aanvullende Python-scripts voor Bunny, Pluto en Lampa.
- **catalog/** — machineleesbare catalogus met publicatiestatus.
- **docs/en/** en **docs/nl/** — gebruikersdocumentatie in het Engels en Nederlands.

Respecteer de originele auteurs van IPTV-org. Deel nooit privéabonnementen, wachtwoorden of persoonlijke IPTV-sleutels in een pull request.
