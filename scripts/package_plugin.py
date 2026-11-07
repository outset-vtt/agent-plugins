#!/usr/bin/env python3
"""Build deterministic Codex and Claude ZIPs from tracked plugin files.

Run in a Git checkout. New skill files must be staged before packaging.
"""
import hashlib
from pathlib import Path
import subprocess
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1]
plugin = root / "plugins/outset-creator"
destination = root / "dist"
destination.mkdir(exist_ok=True)
tracked = subprocess.check_output(
    ["git", "ls-files", "-z", "--", "plugins/outset-creator", "LICENSE"], cwd=root
).decode().split("\0")
files = sorted(root / name for name in tracked if name)
for path in files:
    if path.is_symlink() or not path.is_file():
        raise SystemExit(f"Expected a regular tracked file: {path.relative_to(root)}")


def write_zip(name, entries):
    path = destination / name
    with ZipFile(path, "w", compression=ZIP_DEFLATED) as archive:
        for source, relative in sorted(entries, key=lambda entry: str(entry[1])):
            info = ZipInfo(str(relative), date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = ZIP_DEFLATED
            archive.writestr(info, source.read_bytes())
    print(path)
    return path


plugin_files = [path for path in files if path.is_relative_to(plugin)]
if plugin / ".codex-plugin/plugin.json" not in plugin_files:
    raise SystemExit("Missing tracked plugin manifest")
skill_roots = sorted({path.parent for path in plugin_files
                      if path.name == "SKILL.md" and path.parent.parent == plugin / "skills"})
if not skill_roots:
    raise SystemExit("No tracked skills found")
archives = [write_zip("outset-creator.zip",
    [(path, path.relative_to(plugin)) for path in plugin_files]
    + [(root / "LICENSE", Path("LICENSE"))])]
for skill in skill_roots:
    archives.append(write_zip(f"{skill.name}.zip",
        [(path, path.relative_to(skill.parent)) for path in plugin_files if path.is_relative_to(skill)]
        + [(root / "LICENSE", Path(skill.name) / "LICENSE")]))
checksums = destination / "SHA256SUMS"
checksums.write_text("".join(
    f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n"
    for path in sorted(archives)))
print(checksums)
