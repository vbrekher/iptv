# One-command Bunny setup for Lampa IPTV

This opt-in setup is part of the **vbrekher/iptv fork only**. It provisions a
Bunny **Storage Zone + linked Pull Zone** using one **Bunny Account API Key**
prompt, creates M3U playlists from publicly referenced IPTV sources, filters
historical NSFW candidates for anonymous HLS access, and uploads **M3U text
files only**. It does not host video or bypass subscriptions.

## Mac: paste this whole block into Terminal

```bash
mkdir -p "$HOME/iptv-bunny" && cd "$HOME/iptv-bunny"
for file in personal_bunny_playlists.py free_hls_filter.py auto_bunny_setup.py; do
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
2. Downloads the latest public IPTV index, category and Ukraine lists plus
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
