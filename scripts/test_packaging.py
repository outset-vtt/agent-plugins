"""Exercise the shipped archive interfaces, including clean and repeated builds."""
import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {"author-outset-compendium", "build-outset-scenes",
          "generate-outset-assets", "manage-outset-monsters"}


class PackagingTest(unittest.TestCase):
    def test_downloads_preserve_skills_and_references_without_local_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            shutil.copytree(ROOT / "plugins", root / "plugins")
            shutil.copytree(ROOT / "scripts", root / "scripts")
            shutil.copy(ROOT / "LICENSE", root / "LICENSE")
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            subprocess.run(["git", "add", "plugins", "LICENSE"], cwd=root, check=True)
            plugin = root / "plugins/outset-creator"
            (plugin / "skills/build-outset-scenes/private-notes.md").write_text("Do not ship")
            (plugin / ".codex-plugin/.env").write_text("Do not ship")
            command = [sys.executable, "scripts/package_plugin.py"]
            subprocess.run(command, cwd=root, check=True, capture_output=True)
            dist = root / "dist"
            expected = {"outset-creator.zip", "SHA256SUMS"} | {f"{skill}.zip" for skill in SKILLS}
            self.assertEqual({path.name for path in dist.iterdir()}, expected)
            with ZipFile(dist / "outset-creator.zip") as bundle:
                self.assertIn(".codex-plugin/plugin.json", bundle.namelist())
                for name in bundle.namelist():
                    self.assertNotIn("private-notes", name)
                    self.assertNotIn(".env", name)
                for skill in SKILLS:
                    with ZipFile(dist / f"{skill}.zip") as archive:
                        names = set(archive.namelist())
                        self.assertIn(f"{skill}/SKILL.md", names)
                        self.assertIn(f"{skill}/LICENSE", names)
                        self.assertTrue(all(name.startswith(f"{skill}/") for name in names))
                        source_files = {path.relative_to(plugin / "skills").as_posix()
                            for path in (plugin / "skills" / skill).rglob("*")
                            if path.is_file() and path.name != "private-notes.md"}
                        self.assertEqual(names, source_files | {f"{skill}/LICENSE"})
                        for name in source_files:
                            self.assertEqual(archive.read(name), bundle.read(f"skills/{name}"))
                        self.assertEqual(archive.read(f"{skill}/LICENSE"), (root / "LICENSE").read_bytes())
            for line in (dist / "SHA256SUMS").read_text().splitlines():
                digest, filename = line.split("  ")
                self.assertEqual(digest, hashlib.sha256((dist / filename).read_bytes()).hexdigest())
            first_build = {path.name: path.read_bytes() for path in dist.iterdir()}
            (dist / "retired-skill.zip").write_bytes(b"obsolete release artifact")
            (dist / "old-notes.txt").write_text("obsolete output")
            subprocess.run(command, cwd=root, check=True, capture_output=True)
            self.assertEqual(first_build, {path.name: path.read_bytes() for path in dist.iterdir()})
            # A source read failure must not discard the last successful build.
            (plugin / "skills/build-outset-scenes/SKILL.md").unlink()
            failed = subprocess.run(command, cwd=root, capture_output=True)
            self.assertNotEqual(failed.returncode, 0)
            self.assertEqual(first_build, {path.name: path.read_bytes() for path in dist.iterdir()})


if __name__ == "__main__":
    unittest.main()
