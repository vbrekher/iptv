# Veelgestelde vragen (FAQ)

[English](FAQ.md) · [Nederlands](FAQ.nl.md) · [Русский](README.ru.md)

### Mijn favoriete zender ontbreekt in de afspeellijst.

Vraag hulp in de [discussies van de IPTV-org-community](https://github.com/orgs/iptv-org/discussions). Misschien heeft iemand al een werkende link die nog niet in een afspeellijst is toegevoegd.

Niet alle tv-zenders zijn online beschikbaar. Als er geen legitieme, bereikbare stream bestaat, kunnen wij die niet zelf maken.

### Komt er ook Video On Demand (VOD) in de afspeellijsten?

**Nee.** De catalogus is gericht op live televisie en niet op losse films of series op aanvraag.

### Waarom staat een zender wel op iptv-org.github.io maar niet in de playlist?

[iptv-org.github.io](https://iptv-org.github.io) is een uitgebreide database met tv-zenders, niet een lijst van streams die de beheerders daadwerkelijk bezitten of kunnen afspelen. Alleen zenders met bekende werkende streamlinks verschijnen in de openbare afspeellijsten.

Gebruik de zoekfilter 'streams:>0' op de website om te zien voor welke zenders streams bekend zijn.

### Kan ik een radiostation toevoegen?

**Ja**, als het [visuele radio](https://en.wikipedia.org/wiki/Visual_radio) is, waarbij audio en video tegelijk worden uitgezonden.

### Waarom worden Xtream Codes-serverlinks niet geaccepteerd?

Dit type IPTV-link is vaak instabiel, verloopt snel en kan persoonlijke toegangsgegevens bevatten. Het is praktischer deze links niet in de openbare upstream-catalogus op te nemen dan dagelijks verdwenen adressen te vervangen. Lees ook [Xtream Codes](docs/nl/xtream-codes.md).

### Zijn Bunny-CDN-links in deze fork allemaal afspeelbaar?

**Nee.** We onderscheiden de succesvolle upload van een M3U-bestand naar Storage, een afzonderlijke CDN-controle en de daadwerkelijke weergave van een stream. De inhoud van externe streams kan een betaalscherm of reclame bevatten.

Bekijk de [openbare catalogus](docs/nl/BUNNY_PLAYLISTS.md) voor de status per bestand.
