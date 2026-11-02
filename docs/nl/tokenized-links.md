# Links met tijdelijke tokens

Een getokeniseerde URL bevat een unieke, door de server gegenereerde tekenreeks waarmee een specifieke gebruiker of sessie toegang krijgt tot een IPTV-stream.

Voorbeelden:

~~~text
https://example.com/index.m3u8?token=9f192891-eca5-2435-b9cb-147f376cdc1e
https://example.com/index.m3u8?s=aWE0maGFzaF92YWx1
https://example.com/index.m3u8?wmsAuthSign=c2bWU9Ni8yMC8yMDIVydmVyX3Rp2IDc6MDk6MjAgUmFsaWRtaWE0maGFzaF92YWx1ZTE5SkNSQkhqUG5JZVRRPT0md51dGVzPTMwJmlkPTZhMzZlNT1lRzlsZG4rOXYwZTIzNDk
~~~

Aanbieders vernieuwen tokens regelmatig; daarom kunnen zulke links na korte tijd stoppen met werken.

Soms staat er ook een vervaltijd in het [UNIX-tijdstempelformaat](https://en.wikipedia.org/wiki/Unix_time). Voorbeeld:

~~~text
https://example.com/index.m3u8?token=2IDc6MDk6MjAgUmF&e=1813661332
~~~

In dit voorbeeld correspondeert 1813661332 met 2027-06-22T10:48:52.000Z. Na die tijd kan de stream weigeren.

Publiceer geen gepersonaliseerde URLs met tokens uit je eigen abonnement in een openbare GitHub-repository.

[English](../tokenized-links.md) · [Nederlands](tokenized-links.md)
