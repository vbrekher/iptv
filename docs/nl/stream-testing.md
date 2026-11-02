# IPTV-streams testen

Controleer een stream door deze stappen te volgen:

1. Open de link in een speler met ondersteuning voor [HLS](https://en.wikipedia.org/wiki/HTTP_Live_Streaming) of [DASH](https://en.wikipedia.org/wiki/Dynamic_Adaptive_Streaming_over_HTTP), bijvoorbeeld [VLC](https://www.videolan.org/vlc/index.html).
2. Kijk **minimaal één minuut**. Het afspelen moet stabiel zijn; sommige teststreams stoppen al na 15 tot 30 seconden.
3. Start de stream opnieuw. Controleer of het niet slechts een korte herhalende videolus is en of de link beschikbaar blijft.

Als de stream niet afspeelt, raadpleeg dan de foutlog van de speler. In VLC is dit **Tools → Messages**.

Als de stream wel in de browser maar niet in VLC werkt, kan het zijn dat de server bepaalde [User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent)- of [Referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer)-headers verwacht.

Open de webpagina, druk op **F12**, bekijk **Network** en filter op 'm3u' of 'mpd'. Open vervolgens **Headers** om te zien welke verzoekheaders worden verzonden.

Een M3U-bestand met de vereiste opties kan er als volgt uitzien:

~~~m3u
#EXTM3U
#EXTINF:-1,Example TV
#EXTVLCOPT:http-referrer=https://example.com
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)
https://example.com/playlist.m3u8
~~~

Sla het bestand op met de extensie '.m3u' en open het in de speler. Dit kan compatibiliteitsproblemen oplossen, maar omzeilt geen geldig abonnement of licentiebeperkingen. Zet geen privéheaders in openbare bestanden.

Gebruik voor streams die al in de repository staan het script [playlist:test](scripts.md#playlisttest).

**Let op:** ook een technisch werkende HLS-stream kan uitsluitend een reclamebeeld of een betaalmelding laten zien. Controleer daarom het daadwerkelijke videobeeld.

[English](../stream-testing.md) · [Nederlands](stream-testing.md)
