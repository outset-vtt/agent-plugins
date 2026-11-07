# Release Outset Creator

Requires Python 3 and Git. From a checkout, update `.codex-plugin/plugin.json` under `plugins/outset-creator/`, the documented release links and release notes together. Keep credentials and private data out of tracked plugin files.

```sh
python3 scripts/validate.py
python3 scripts/test_packaging.py
python3 scripts/package_plugin.py
```

The packager replaces the generated `dist/` directory only after a successful build, removing obsolete artifacts. A failed build preserves the previous output. Do not store hand-authored files in `dist/`.

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

Commit to `main`, then dispatch **Publish verified release**. The workflow checks out the dispatch SHA, reruns validation and packaging tests, checks the matching guide release is published, and creates a draft with these exact six assets. It downloads and compares every asset and checksum before publishing. Publish the matching guide release first using its workflow. Both workflows refuse an existing version tag; investigate an interrupted draft before retrying rather than overwriting it.

The release version comes from the plugin manifest; release notes come from `RELEASE_NOTES.md`. Skill links must target the matching guide tag, enforced by `validate.py`. Do not replace an existing tag or silently replace its assets. Download the published files and compare their checksums with the local build before announcing the release. Keep generated `dist/` files out of commits.

Archive checks establish packaging correctness, not an authenticated Claude or Codex installation. Document any host smoke tests separately. Skills still require the separately authorized [Outset MCP connection](connect-outset.md) for live operations.
