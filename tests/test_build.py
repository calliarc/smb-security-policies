"""Tests for scripts/build.py. Run with: python3 -m unittest discover -s tests"""

import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import build  # noqa: E402

EXAMPLE_CONFIG = REPO_ROOT / "company.example.yml"
POLICIES = REPO_ROOT / "policies"


class FillTests(unittest.TestCase):
    def test_fill_replaces_known_and_reports_unknown(self):
        text = "Hello {{COMPANY_NAME}}, owner {{ POLICY_OWNER }}, {{MISSING}}."
        out, unresolved = build.fill(text, {"COMPANY_NAME": "Acme", "POLICY_OWNER": "COO"})
        self.assertEqual(out, "Hello Acme, owner COO, {{MISSING}}.")
        self.assertEqual(unresolved, {"MISSING"})

    def test_empty_value_counts_as_unresolved(self):
        _, unresolved = build.fill("{{A}}", {"A": ""})
        self.assertEqual(unresolved, {"A"})

    def test_template_notes_are_stripped(self):
        text = "# T\n\n<!-- TEMPLATE NOTE: replace {{PLACEHOLDER}}\nmore -->\n\nBody"
        self.assertEqual(build.strip_template_notes(text), "# T\n\nBody")

    def test_simple_yaml_fallback(self):
        data = build._parse_simple_yaml(
            '# comment\nA: "x: y"\nB: plain # trailing\nC: \'q\'\nD: "say \\"hi\\""\n')
        self.assertEqual(data, {"A": "x: y", "B": "plain", "C": "q", "D": 'say "hi"'})


class ExampleConfigTests(unittest.TestCase):
    def test_example_config_covers_every_placeholder(self):
        config = build.load_config(EXAMPLE_CONFIG)
        missing = build.list_placeholders(POLICIES) - set(config)
        self.assertFalse(missing, f"company.example.yml is missing: {sorted(missing)}")

    def test_strict_markdown_build_leaves_no_placeholders(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "dist"
            written = build.build(EXAMPLE_CONFIG, POLICIES, out, ["md"],
                                  strict=True, combined=True)
            self.assertEqual(len(written["md"]), len(list(POLICIES.glob("*.md"))) + 1)
            for path in written["md"]:
                text = path.read_text(encoding="utf-8")
                self.assertNotIn("{{", text, path.name)
                self.assertNotIn("TEMPLATE NOTE", text, path.name)
                self.assertIn("Example Co Ltd", text, path.name)

    def test_without_pandoc_falls_back_to_markdown(self):
        with tempfile.TemporaryDirectory() as tmp, \
                mock.patch.object(build.shutil, "which", return_value=None), \
                mock.patch("sys.stderr"):
            written = build.build(EXAMPLE_CONFIG, POLICIES, Path(tmp) / "dist", ["md", "docx", "pdf"])
            self.assertTrue(written["md"])
            self.assertEqual(written["docx"], [])
            self.assertEqual(written["pdf"], [])

    def test_refuses_to_overwrite_sources(self):
        with self.assertRaises(build.BuildError):
            build.build(EXAMPLE_CONFIG, POLICIES, REPO_ROOT, ["md"])

    def test_strict_build_fails_on_missing_values(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = Path(tmp) / "company.yml"
            cfg.write_text('COMPANY_NAME: "Acme"\n', encoding="utf-8")
            with self.assertRaises(build.BuildError):
                build.build(cfg, POLICIES, Path(tmp) / "dist", ["md"], strict=True)
            self.assertFalse((Path(tmp) / "dist").exists())


if __name__ == "__main__":
    unittest.main()
