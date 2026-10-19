import contextlib
import io
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from install import install
from validate import ROOT, package_check


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.target = Path(self.tmp.name) / "installed"

    def quiet_install(self, names, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            install(self.target, names, **kwargs)

    def test_package_works_without_source_repository(self):
        self.quiet_install(["brainkit-story"])
        self.assertEqual([p.name for p in self.target.iterdir()], ["brainkit-story"])
        self.assertEqual(package_check(self.target / "brainkit-story")["name"], "brainkit-story")
        self.assertFalse((self.target / "local").exists())

    def test_refuses_overwrite_and_preserves_user_edits(self):
        self.quiet_install(["brainkit-story"])
        marker = self.target / "brainkit-story" / "my-notes.md"
        marker.write_text("Keep me")
        with self.assertRaises(FileExistsError):
            self.quiet_install(["brainkit-story"])
        self.assertEqual(marker.read_text(), "Keep me")

    def test_preflight_prevents_partial_install(self):
        self.quiet_install(["brainkit-story"])
        with self.assertRaises(FileExistsError):
            self.quiet_install(["brainkit-voice", "brainkit-story"])
        self.assertFalse((self.target / "brainkit-voice").exists())

    def test_rejects_traversal(self):
        with self.assertRaises(ValueError):
            self.quiet_install(["../local"])
        self.assertFalse(self.target.exists())

    def test_dry_run_has_no_filesystem_effect(self):
        self.quiet_install(["brainkit-voice"], dry_run=True)
        self.assertFalse(self.target.exists())

    def test_all_packages_are_independent(self):
        names = [p.name for p in (ROOT / "skills").iterdir() if p.is_dir()]
        self.quiet_install(names)
        for name in names:
            package_check(self.target / name)

    def test_rejects_symlink_in_package(self):
        fixture = Path(self.tmp.name) / "fixture"
        shutil.copytree(ROOT / "skills/brainkit-story", fixture / "skills/brainkit-story")
        shutil.copy2(ROOT / "registry.json", fixture / "registry.json")
        (fixture / "skills/brainkit-story/leak").symlink_to(ROOT / "README.md")
        with self.assertRaises(ValueError):
            self.quiet_install(["brainkit-story"], root=fixture)

    def test_rejects_link_outside_installed_package(self):
        fixture = Path(self.tmp.name) / "fixture"
        shutil.copytree(ROOT / "skills/brainkit-story", fixture / "skills/brainkit-story")
        entry = fixture / "skills/brainkit-story/SKILL.md"
        with entry.open("a") as stream:
            stream.write("\nRead [private](../../local/private.md).\n")
        with self.assertRaises(ValueError):
            package_check(entry.parent)


if __name__ == "__main__":
    unittest.main()
