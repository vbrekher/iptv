# One-command Bunny setup for Lampa IPTV

This opt-in setup is part of the **vbrekher/iptv fork only**. It provisions a
Bunny **Storage Zone + linked Pull Zone** using one **Bunny Account API Key**
prompt, creates M3U playlists from publicly referenced IPTV sources, filters
historical NSFW candidates for anonymous HLS access, and uploads **M3U text
files only**. It does not host video or bypass subscriptions.

## Mac: paste this whole block into Terminal

```bash
mkdir -p "$HOME/iptv-bunny" && cd "$HOME/iptv-bunny"
for file in personal_bunny_playlists.py free_hls_filter.py auto_bunny_setup.py sync_bunny_countries.py build_lampa_lite.py lampa_category_fix.py; do
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

## Correct Lampa categories (composite group-title defect)

**Why Lampa showed hundreds of one-channel categories:** The original source M3U
sometimes uses `group-title="Documentary;Education;Outdoor;Relax"` or
`group-title="Family;Series"`. Some Lampa plugins treat each entire string
as a distinct category instead of splitting it, multiplying category names.
Our earlier full `index.category.m3u` was merely a copy of the raw index,
so these composite group strings were incorrectly passed through.

The fixed generator uses a fixed IPTV category vocabulary and assigns exactly
**one canonical group** to each channel: e.g. Documentary and Series.
Rare groups are folded into General. XXX stays in its own group.
No URLs or channels are removed from the full catalog.

On an already installed Bunny, run exactly this (same Mac directory and zones):

```bash
(
  set -e
  cd "$HOME/iptv-bunny"
  for file in auto_bunny_setup.py lampa_category_fix.py; do
    curl -fsSL --retry 3 \
      "https://raw.githubusercontent.com/vbrekher/iptv/master/tools/$file" \
      -o "$file"
  done
  python3 auto_bunny_setup.py --fix-categories-only
)
```

This reuses the **same Storage Zone and Pull Zone**, takes only the locally saved
`dist/iptv-ready/index.m3u` and `adult.m3u`, and uploads just the repaired
full indexes and 240/600-item variants. It never rechecks 72 streams,
does not download countries again, and does not rewrite `adult.m3u` or
`countries/*.m3u`. The terminal prompts once for Bunny Account API Key.

After upload, **delete the old playlist entry in Lampa** and add the new,
cache-safe URL:

```text
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean-lite.m3u
```

If your television handles that, try:

```text
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-clean.m3u
```

All categories in one full file:

```text
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/index.clean.m3u
```

**CUB warning:** `[M3U Function (Failed upload to CUB)]` refers to a CUB
cloud upload attempt by a Lampa plugin, not a Bunny Storage API PUT. This
script fixes M3U structure, not the user's CUB login, cloud permissions,
plugin, or CUB server availability. For isolation, try adding the new small
M3U as a direct URL in the IPTV player without choosing any CUB upload/sync
action. If upload-to-CUB remains mandatory in the installed plugin, diagnose
that specific plugin separately; category repair alone cannot guarantee it.

## Lampa on Samsung Tizen: fast, category-balanced playlists

The full `index.m3u` and `index.category.m3u` contain many thousands of
entries. On Samsung's Tizen browser runtime the IPTV plugin may hang while
processing these large M3U files. The one-click installer can now upload two
additional small playlists without changing your full catalog:

- `/iptv/lampa-lite.m3u` — **up to 240 entries**, including the previously
  tested adult streams plus a balanced sample from every available public
  category. **Try this first** on Samsung.
- `/iptv/lampa.m3u` — **up to 600 entries**, same group names, more choices.

Both use `group-title` tags, including `XXX`. They are static M3U files,
not proxies or locally hosted video; the public part is **not live-tested**.
The original `index.m3u`, `index.category.m3u`, `adult.m3u`, country and
category playlists remain untouched.

### Publish only the lightweight files to your already-provisioned Bunny

```bash
(
  set -e
  cd "$HOME/iptv-bunny"
  for file in auto_bunny_setup.py build_lampa_lite.py; do
    curl -fsSL --retry 3 \
      "https://raw.githubusercontent.com/vbrekher/iptv/master/tools/$file" \
      -o "$file"
  done
  python3 auto_bunny_setup.py --lite-only
)
```

Enter the **Bunny Account API Key** only when prompted (hidden input).
This mode reuses existing resources and local M3U files; it does **not**
create zones, re-scan the 72 adult candidates, re-download 188 country files,
or re-upload the 11,420-channel index.

After successful upload:

```text
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa-lite.m3u
https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/lampa.m3u
```

If the 240-entry playlist also hangs, test `/iptv/adult.m3u` (about 46
entries). If even the small file fails, investigate TV connectivity, CDN
response, CORS and IPTV plugin errors rather than assuming size is the only
cause. Loading an M3U successfully does not mean individual streams will
play on Samsung. No need to reinstall Lampa or wipe settings as a first step.

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
