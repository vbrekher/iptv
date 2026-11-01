# One-command Bunny setup for Lampa IPTV

This opt-in setup is part of the **vbrekher/iptv fork only**. It provisions a
Bunny **Storage Zone + linked Pull Zone** using one **Bunny Account API Key**
prompt, creates M3U playlists from publicly referenced IPTV sources, filters
historical NSFW candidates for anonymous HLS access, and uploads **M3U text
files only**. It does not host video or bypass subscriptions.

## Mac: paste this whole block into Terminal

```bash
mkdir -p "$HOME/iptv-bunny" && cd "$HOME/iptv-bunny"
for file in personal_bunny_playlists.py free_hls_filter.py auto_bunny_setup.py sync_bunny_countries.py; do
  curl -fsSL --retry 3 \
    "https://raw.githubusercontent.com/vbrekher/iptv/master/tools/$file" \
    -o "$file" || exit 1
done
python3 auto_bunny_setup.py
```

The script asks only:

```text
Bunny Account API Key (hidden):
```

Enter your **Account API Key**, not your Storage Zone password. The installer
retrieves the storage credentials through Bunny's management API. The key is
not stored in files, commands, logs or committed to GitHub. Do not send it in
chat. Requires Python 3.9+, no npm dependencies.

## What the installer does

1. Validates Bunny Account API permissions.
2. Downloads the latest public IPTV index, categories, and all listed country playlists plus
   frozen historical adult candidate links. Opt-in community candidate inputs
   are enabled by default, with `--without-community` to omit them.
3. Checks historical adult HLS manifest and a short sample of a segment without
   login, signed tokens or decryption. Invalid/unresponsive links are omitted.
4. Creates a uniquely named Storage Zone in **DE** and a Pull Zone linked via
   `StorageZoneId`, `OriginType=2`. This creates **billable Bunny resources**.
5. Uploads only curated M3U text/metadata, **not video files or rejected URLs**.
6. Reports the M3U URLs and verifies the public Pull Zone response.
7. Stores local non-secret resource names in `.bunny-iptv-state.json`. Re-running
   from the same directory reuses the same zones, without duplicate creation.

The current IPTV-org public index is **not individually live-tested**. Only
the adult candidates go through the separate anonymous HLS probe.

After a successful upload, the script prints URLs like:

```text
https://<your-pull-zone>.b-cdn.net/iptv/index.m3u
https://<your-pull-zone>.b-cdn.net/iptv/adult.m3u
https://<your-pull-zone>.b-cdn.net/iptv/categories/xxx.m3u
https://<your-pull-zone>.b-cdn.net/iptv/countries/ua.m3u
```

Copy any M3U URL into Lampa's playlist importer. If no adult candidate passes,
`adult.m3u` contains no channel entries and the public index is still published
without the unverified adult streams.

## Country playlists: all countries on your existing Bunny

The first installer version published only `countries/ua.m3u`. This was an
implementation omission, not a restriction of Bunny or IPTV-org.

**Update only the installer and country mirror module**, while staying in the
same directory so the existing `.bunny-iptv-state.json` is reused:

```bash
cd "$HOME/iptv-bunny"
for file in auto_bunny_setup.py sync_bunny_countries.py; do
  curl -fsSL --retry 3 \
    "https://raw.githubusercontent.com/vbrekher/iptv/master/tools/$file" -o "$file"
done
python3 auto_bunny_setup.py --countries-only
```

Enter only the Bunny **Account API Key**, hidden by the terminal.
`--countries-only` will **never create new Storage/Pull Zones**. It uses
the zones from the existing local state and downloads every country listed in
IPTV-org's official `PLAYLISTS.md` index, plus the official grouped country
playlist. All listed files are checked for the M3U header before uploading.
If any listed country download fails, the upload does not start.

After success, examples:

```text
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.country.m3u
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/ua.m3u
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/us.m3u
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/de.m3u
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/nl.m3u
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/pl.m3u
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/countries/uk.m3u
```

These are *expected paths after the upload succeeds*, not a guarantee they
already exist. The command prints the exact count from the official
country-list index, a local report at
`dist/iptv-published/catalog/country-sync-report.json`, and the CDN URLs.
The public country playlists are mirrors of IPTV-org, not personally verified
for playback; existing separately tested adult M3Us remain untouched.

The full `python3 auto_bunny_setup.py` command also populates all country
files on future runs. Use `--countries-only` now to **skip** rescanning adult
candidate streams, reuploading 39 files, and reprovisioning anything.

## Recover from Bunny Storage 401 without creating duplicate zones

A `401 Unauthorized` at **Uploading ...** means the Bunny Storage API did not
accept the Storage Zone write password or primary-region endpoint. It does not
mean the account key is invalid, nor that the IPTV probe failed.

The installer now reads the primary region from Bunny's management API, refreshes
the Storage Zone write password, and retries HTTP 401/403 with bounded delays.
It stores generated M3U text locally **before** uploading so subsequent attempts
do not require another live stream scan.

Run from the **same** `$HOME/iptv-bunny` directory (keep
`.bunny-iptv-state.json`):

```bash
cd "$HOME/iptv-bunny"
curl -fsSL --retry 3 -o auto_bunny_setup.py \
  https://raw.githubusercontent.com/vbrekher/iptv/master/tools/auto_bunny_setup.py
python3 auto_bunny_setup.py
```

On any **future** upload failure, the freshly generated files remain in
`dist/iptv-ready/`. You may resume the upload without rescanning:

```bash
python3 auto_bunny_setup.py --upload-only
```

**Important:** The older installer discarded generated files in a temporary
directory after failure, so the first upgraded run must recheck the 72 stream
candidates once. The existing Storage Zone and Pull Zone will be reused using
the saved resource-group name.

If the upload still fails after six attempts, the error gives the exact Storage
Zone name, primary region and endpoint, without printing any secret. Confirm
the **writable** Storage Zone password in Bunny > Storage > FTP & API Access;
do not use the account key or ReadOnlyPassword as the Storage API access key.
Do **not** delete the zones, recreate resources or rotate credentials as a
first troubleshooting step.

## Security and limitations

- Only **anonymous technical accessibility** is checked, not redistribution
  rights, payment status, or Samsung codec compatibility. Do not assume any
  of the historical entries work today.
- No Bunny Stream, Magic Containers or Database is required.
- The Account API Key remains in memory only during the process.
- The Storage Zone password is retrieved programmatically and is only
  temporarily used for uploads; it is not saved.
- Existing user zones are never changed or deleted. If the Pull Zone origin
  does not match the expected Storage Zone, the installer stops.
- CDN may cache old files. Configure TTL/purge separately if you refresh.
- On failed provisioning, rerun from the **same directory** to reuse the
  resource names; do not delete the local state file.
- End-to-end real Bunny creation, network-stream checks and Samsung playback
  require the owner's credentials/device and are not claimed by source tests.

Offline self-test without Bunny changes:

```bash
python3 auto_bunny_setup.py --self-test
```
