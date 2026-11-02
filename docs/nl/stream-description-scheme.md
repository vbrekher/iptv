# Schema voor streambeschrijvingen

Een stream kan alleen worden goedgekeurd als de beschrijving dit formaat heeft:

~~~m3u
#EXTINF:-1 tvg-id="STREAM_ID",STREAM_TITLE (QUALITY) [LABEL]
STREAM_URL
~~~

| Veld | Betekenis | Verplicht | Geldige waarden |
|---|---|---|---|
| STREAM_ID | Unieke stream-ID, bestaande uit zender-ID en eventueel feed-ID. Zie [iptv-org.github.io](https://iptv-org.github.io/). | Nee | channel_id of channel_id@feed_id |
| STREAM_TITLE | Zendernaam en eventueel feednaam. Komma's, '[' en ']' zijn niet toegestaan. | Ja | Tekst |
| QUALITY | Maximale opgegeven streamkwaliteit. | Nee | 2160p, 1080p, 720p, 480p, 360p enz. |
| LABEL | Opmerking over beperkingen in beschikbaarheid. | Nee | Geo-blocked of Not 24/7 |
| STREAM_URL | URL van de stream. | Ja | HTTPS, HTTP, MMS, MMSH, RTSP, RTMP, SRT, RTP, UDP |

Voorbeeld:

~~~m3u
#EXTINF:-1 tvg-id="ExampleTV.us@East",Example TV East (720p) [Geo-blocked]
https://example.com/playlist.m3u8
~~~

Zo nodig kun je een aangepaste [HTTP User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) en [HTTP Referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) opgeven via de richtlijn EXTVLCOPT:

~~~m3u
#EXTINF:-1 tvg-id="ExampleTV.us",Example TV
#EXTVLCOPT:http-referrer=http://example.com/
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)
http://example.com/stream.m3u8
~~~

Bewaar geen persoonlijke cookies, abonnementstokens of wachtwoorden in een openbaar M3U-bestand.

[English](../stream-description-scheme.md) · [Nederlands](stream-description-scheme.md)
