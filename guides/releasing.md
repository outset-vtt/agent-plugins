# Release Outset Creator

Requires Python 3 and Git. From a checkout, update `.codex-plugin/plugin.json` under `plugins/outset-creator/`, the documented release links and release notes together. Keep credentials and private data out of tracked plugin files.

```sh
python3 scripts/validate.py
python3 scripts/test_packaging.py
python3 scripts/package_plugin.py
```

Stage newly added skill files before packaging. The packager includes tracked plugin files and the repository license; it excludes untracked local files. It normalizes ZIP timestamps and permissions so repeated builds in the same environment produce identical bytes. The tests inspect actual archives, including scene references and checksum contents. CI runs these commands and uploads their outputs.

## Release assets

| File | Consumer |
| --- | --- |
| `outset-creator.zip` | Codex plugin-capable host; manifest and skills at archive root |
| `author-outset-compendium.zip` | Claude custom skill upload |
| `build-outset-scenes.zip` | Claude custom skill upload, including supporting references |
| `generate-outset-assets.zip` | Claude custom skill upload |
| `manage-outset-monsters.zip` | Claude custom skill upload |
| `SHA256SUMS` | SHA-256 checksums for the five archives |

Publish a new tag against the exact checked commit after CI passes. Attach these six files from that commit's build to its GitHub release. Do not replace an existing tag or silently replace its assets. Download the published files and compare their checksums with the local build before announcing the release. Keep generated `dist/` files out of commits.

Archive checks establish packaging correctness, not an authenticated Claude or Codex installation. Document any host smoke tests separately. Skills still require the separately authorized [Outset MCP connection](connect-outset.md) for live operations.
