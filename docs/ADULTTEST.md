# Adulttest — isolated adult IPTV audit and Bunny M3U publication

Separate pipeline. Never overwrites the existing adult playlist, categories, country playlists or combined index. Publishes only /iptv/adulttest.m3u.

## One-paste command for existing Mac and Bunny zones

Run inside the existing $HOME/iptv-bunny directory so the local nonsecret state identifies the right Storage/Pull zones.

    (
      set -euo pipefail
      cd "$HOME/iptv-bunny"
      for file in \
        personal_bunny_playlists.py \
        free_hls_filter.py \
        sync_bunny_countries.py \
        build_lampa_lite.py \
        lampa_category_fix.py \
        auto_bunny_setup.py \
        adulttest.py
      do
        curl -fsSL --retry 3 \
          "https://raw.githubusercontent.com/vbrekher/iptv/master/tools/$file" \
          -o "$file"
      done
      python3 adulttest.py --self-test
      python3 adulttest.py
    )

If uploading to Bunny fails after the tests succeeded, **do not rescan**
all sources and channels. Resume the saved local playlist with:

    cd "$HOME/iptv-bunny"
    python3 adulttest.py --publish-only

This mode verifies the local M3U entry count against the saved report,
reuses existing Storage/Pull zones, and only retries the upload.

For local test only, replace the last line with:

    python3 adulttest.py --dry-run

The code inventories the 16 research source identities (15 public files plus
one IPTV NSFW blocklist). Some are exact mirrors or archives; 16 does not mean
16 unique sources of current working video.

## What it produces

- dist/adulttest/adulttest-candidates.m3u: all unique safe URL candidates, LOCAL ONLY.
- dist/adulttest/adulttest-results.csv: every probe result, source(s), advertised
  quality and HLS master resolution when available, LOCAL ONLY.
- dist/adulttest/adulttest-report.json: counts and rejection reasons, LOCAL ONLY.
- dist/adulttest/adulttest.m3u: only successful anonymous HLS candidate links,
  the one file uploaded to /iptv/adulttest.m3u.

The playlist includes a human-readable name, source-provided tvg-logo
or an official IPTV-org logos.json match for a known tvg-id (never invented),
tvg-id where provided and a SINGLE group-title, either Adult TV or Erotic FAST. Broken, private, obvious subscription-token, cam
advertising, embedded user/password, teen-labelled and VOD-only candidates
are excluded. No paid-service bypass, DRM circumvention, custom stream
headers, or reverse proxy is provided.

Every accepted URL must return an anonymous HLS manifest and a tiny sample
of a media segment. HTTP status by itself does not establish quality,
rights or Tizen compatibility. Labels HD/FHD/4K in source titles
are NOT proof of resolution, and even an actual HLS master resolution
does not show whether on-screen webcam advertising is present.

Only after the tests, when one or more streams passed, the CLI prompts
for Bunny Account API Key with hidden input. It retrieves the Storage Zone
write password from the Bunny management API and reuses existing zones,
never creates new billable zones, and uploads ONLY adulttest.m3u.

After successful publication the expected endpoint is:

    https://lampa-iptv-875323ab-cdn.b-cdn.net/iptv/adulttest.m3u

Remove any previous Adulttest entry from Lampa and reimport the URL through
the direct IPTV importer, not via a CUB cloud upload feature.

### Limitations

- Anonymous HTTP readability does not prove content is licensed or legally
  redistributable. Verify provenance/permission before public promotion.
- No account key is saved; original candidate and rejected URL lists stay
  on the Mac. Do not upload these diagnostics to GitHub.
- Original user-provided personal IPTV provider credentials are not copied
  into this script or published.
- Some of the 16 lists may be inaccessible and many URLs may be stale.
- The last step is not yet executed in the user's Bunny account; the owner
  performs it from Terminal. GitHub CI only covers offline source checks.
