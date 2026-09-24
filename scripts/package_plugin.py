#!/usr/bin/env python3
"""Build an importable skills-only plugin archive without local files."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root = Path(__file__).resolve().parents[1]
plugin = root / "plugins/outset-creator"
destination = root / "dist/outset-creator.zip"
destination.parent.mkdir(exist_ok=True)
with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
    for directory in (plugin / ".codex-plugin", plugin / "skills"):
        for path in sorted(directory.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(plugin))
    archive.write(root / "LICENSE", "LICENSE")
print(destination)
