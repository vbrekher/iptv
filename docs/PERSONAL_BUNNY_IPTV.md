# Personal IPTV playlists on Bunny CDN

This **opt-in local builder** is intended for the `vbrekher/iptv` fork.
It is deliberately separate from the upstream GitHub Pages publishing workflow.

## What is (and is not) restored

- The upstream NSFW blocklist contains **368 channel identifiers** (at the time this feature was prepared). Identifiers are **not video streams**.
- The builder reads the latest upstream blocklist and a frozen pre-removal (2024-01-29) snapshot.
- In the inspected snapshot, **65 historical adult stream URLs** could be recovered across the old XXX category and old full index, of which **61 refer to currently NSFW-blocklisted identifiers**. These are **unverified candidate URLs**; they may be dead, paywalled, or restricted.
- Channels with an explicit `dmca` blocklist reason are **never included** in the restored adult playlist.
- No passwords, private playlist tokens, or paid provider credentials are recovered or bypassed.
- Nothing in this feature hosts, downloads, transcodes, or proxies the live video. Bunny Storage holds **M3U text files only**.
- Do not assume the historic URLs are still available or that redistribution is permitted. Verify rights for any publicly published playlist.

## Run on macOS (Python 3.9+)

```sh
gh repo clone vbrekher/iptv
cd iptv
git switch feat/personal-adult-playlists-bunny

python3 tools/personal_bunny_playlists.py --self-test
python3 tools/personal_bunny_playlists.py --output ./dist/iptv
```

No npm, Node.js, Tizen SDK or database is needed.

Output files:

```text
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
```

`index.m3u` combines the current public upstream IPTV index with the historical adult candidates. `--no-public` produces an adult-only index. `--country nl` changes the optional public country mirror. The output directory can be overwritten by a later run.

The `nsfw-status.csv` file lists **all current NSFW identifiers**, each marked `historical_url_unverified` or `no_known_url`. **Do not mistake its number of rows for playable channels.**

## Publish with Bunny Storage and a connected Pull Zone

In [bunny.net dashboard](https://dash.bunny.net/):

1. Create a **Storage Zone**, and note its name and **primary region** (e.g. `de`).
2. In the Storage Zone, create/connect a **Pull Zone** and note its hostname, e.g. `my-playlists.b-cdn.net`.
3. Find the **Storage Zone password** on the Storage Zone access/settings screen. This is **not** your global Bunny account API key.
4. Confirm the [Bunny Acceptable Use Policy](https://bunny.net/acceptable-use/), content rights, and whether the intended publication is permitted.

From the project directory:

```sh
python3 tools/personal_bunny_playlists.py --output ./dist/iptv --publish
```

The script prompts for the Storage Zone name, region, Pull Zone hostname and password (hidden input). It then uploads each small playlist/catalog file using the Bunny Storage API. **Never paste your Storage password into GitHub files, terminal commands, or public logs.**

For subsequent scripted runs, optional environment variables are `BUNNY_STORAGE_ZONE`, `BUNNY_STORAGE_REGION`, `BUNNY_CDN_HOST`, and `BUNNY_STORAGE_PASSWORD`. Avoid persisting a password in shell history.

Example URLs after a successful upload (replace `my-playlists` with your actual Pull Zone hostname):

```text
https://my-playlists.b-cdn.net/iptv/index.m3u
https://my-playlists.b-cdn.net/iptv/adult.m3u
https://my-playlists.b-cdn.net/iptv/categories/xxx.m3u
https://my-playlists.b-cdn.net/iptv/categories/adultiptv.m3u
https://my-playlists.b-cdn.net/iptv/categories/mycamtv.m3u
https://my-playlists.b-cdn.net/iptv/categories/other-adult.m3u
https://my-playlists.b-cdn.net/iptv/countries/ua.m3u
```

Paste one URL into the M3U playlist importer in Lampa. The `group-title` fields provide in-app categories; separate `categories/*.m3u` files are optional focused playlists.

After updates, Bunny CDN may serve a cached older M3U until cache expiry. Set a short cache TTL for M3U files or purge the corresponding URLs in the Bunny dashboard. **Publishing the M3U does not move the video streams to Bunny or remove any provider-side restriction.**

## Keep GitHub and Bunny separate

The upstream `iptv-org/iptv` project removed XXX links following a GitHub Trust & Safety request in January 2024. This branch **does not commit generated adult M3Us or enable NSFW output in the public GitHub Pages workflow**. Do not turn the upstream deploy workflow back on for these playlists; use Bunny for the independently generated files, subject to its terms and the rights to redistribute any included links.

Do not merge any NSFW restoration into the upstream repo. The feature is strictly fork-specific.

## Troubleshooting

- `HTTP 401` on upload: verify the **Storage Zone password** and primary region, not the CDN hostname.
- `HTTP 404` from the CDN: verify the Pull Zone is connected to the correct Storage Zone and the `/iptv/` prefix is correct.
- Playlist opens, but a channel does not play: the stream URL may have expired, require authentication, be geo-restricted, or use an unsupported codec. Check the `catalog/report.json`; live validation is explicitly **not performed**.
- For a stand-alone playlist without public IPTV channels, pass `--no-public`.
