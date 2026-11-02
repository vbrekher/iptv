# GitHub Actions-workflows

Om de [scripts](scripts.md) automatisch uit te voeren, gebruikt het oorspronkelijke IPTV-org-project [GitHub Actions](https://docs.github.com/en/actions/using-workflows). Elke workflow bevat een vaste set scripts en kan handmatig of als reactie op een GitHub-gebeurtenis worden gestart.

## check

Wordt uitgevoerd bij nieuwe pull requests. Voert achtereenvolgens 'api:load', 'playlist:lint' en 'playlist:validate' uit. Fouten blokkeren de samenvoeging.

## format

Voert achtereenvolgens 'api:load', 'playlist:format', 'playlist:lint' en 'playlist:validate' uit.

## update

De geplande upstream-taak wordt dagelijks om **00:00 UTC** uitgevoerd. Hij draait 'api:load', 'playlist:update', 'playlist:lint', 'playlist:validate', 'playlist:generate', 'playlist:export' en 'readme:update'. Bij succes worden de nieuwe bestanden automatisch uitgerold.

## validate_discussion

Wordt gestart bij het aanmaken of bewerken van een discussie. Het script 'discussion:validate' controleert de aanvraag; gevonden fouten worden door de bot als commentaar gemeld.

## validate_issue

Wordt gestart bij het aanmaken of bewerken van een issue. 'issue:validate' controleert de aanvraag; fouten worden in het issue gemeld.

## validate_label

Wordt gestart wanneer een issue een nieuw label krijgt. Een onjuist label kan door de bot worden verwijderd, met een uitleg in een commentaar.

## Extra controles in deze fork

De onafhankelijke Bunny-fork bevat ook een workflow voor de M3U-generator, de openbare catalogus, Pluto TV en offline veiligheidstests. De melding dat een GitHub-test is geslaagd betekent **niet** dat alle CDN-bestanden op een privéaccount zijn gepubliceerd of dat een stream op Samsung afspeelt.

[English](../workflows.md) · [Nederlands](workflows.md)
