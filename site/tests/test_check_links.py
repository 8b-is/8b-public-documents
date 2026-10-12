"""Exercise the production checker against disposable static builds."""
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

CHECKER = Path(__file__).resolve().parents[1] / "scripts" / "check-links.py"


class CheckLinksTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "scripts").mkdir()
        self.dist = self.root / "dist"
        self.dist.mkdir()
        shutil.copyfile(CHECKER, self.root / "scripts/check-links.py")
        (self.root / "outside.html").write_text("outside deployment")

    def check(self, link, base="", succeeds=False):
        (self.dist / "index.html").write_text(f'<a href="{link}">test</a>')
        result = subprocess.run(
            [sys.executable, str(self.root / "scripts/check-links.py")],
            env={**os.environ, "SITE_BASE": base}, capture_output=True,
            text=True, timeout=5,
        )
        self.assertEqual(result.returncode == 0, succeeds, result.stderr)
        if not succeeds:
            self.assertIn(link, result.stderr)

    def test_relative_escape(self):
        self.check("../outside.html")

    def test_encoded_escape(self):
        self.check("%2e%2e/outside.html")

    def test_base_path_escape(self):
        self.check("/library/../outside.html", base="/library")

    def test_file_symlink_escape(self):
        (self.dist / "linked.html").symlink_to(self.root / "outside.html")
        self.check("linked.html")

    def test_directory_index_symlink_escape(self):
        (self.dist / "guide").mkdir()
        (self.dist / "guide/index.html").symlink_to(self.root / "outside.html")
        self.check("guide/")

    def test_valid_internal_and_project_base(self):
        (self.dist / "guide").mkdir()
        (self.dist / "guide/index.html").write_text("guide")
        for link, base in [("guide/", ""), ("guide/../index.html", ""),
                           ("/library/guide/", "/library"),
                           ("/guide/", ""), ("#section", ""),
                           ("https://example.com/", "")]:
            with self.subTest(link=link):
                self.check(link, base, succeeds=True)


if __name__ == "__main__":
    unittest.main()
