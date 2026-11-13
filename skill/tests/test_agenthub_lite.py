"""Local checks: only stdlib, no network or hosted services."""
from pathlib import Path
import importlib.util
import json
import tempfile
import unittest

MODULE_FILE = Path(__file__).resolve().parents[1] / "scripts" / "agenthub_lite.py"
spec = importlib.util.spec_from_file_location("agenthub_lite", MODULE_FILE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class AgentHubLiteTests(unittest.TestCase):
    def test_init_and_build_outputs_agent_friendly_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "my-hub"
            self.assertEqual(mod.cmd_init(root), 0)
            self.assertEqual(mod.cmd_build(root), 0)
            docs = root / "docs"
            for file in ("index.html", "context.md", "context.txt", "llms.txt", ".well-known/agenthub.json", "manifest.json", "changelog.html", "changelog.txt", "projects/first-project.html", "projects/first-project.md", ".nojekyll"):
                self.assertTrue((docs / file).exists(), file)
            manifest = json.loads((docs / "manifest.json").read_text())
            self.assertEqual(manifest["entrypoints"]["agent"], "context.txt")
            self.assertEqual((docs / "context.txt").read_text(), (docs / "context.md").read_text())
            self.assertIn("context.txt", (docs / "llms.txt").read_text())
            self.assertEqual(len(manifest["projects"]), 1)
            self.assertIn("projects/first-project.html", (docs / "index.html").read_text())
            self.assertEqual(mod.cmd_build(root), 0)  # re-build only own generated directory

    def test_rejects_credential_without_printing_or_publishing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "hub"
            mod.cmd_init(root)
            with (root / "context.md").open("a") as file:
                file.write("\npassword: SuperSecretCredential123456\n")
            errors, _ = mod.scan(root)
            self.assertTrue(any("credential assignment" in error for error in errors))
            self.assertEqual(mod.cmd_build(root), 1)
            self.assertFalse((root / "docs").exists())

    def test_escapes_html_and_blocks_javascript_links(self):
        text = "# Demo\n<script>alert(1)</script>\n[bad](javascript:alert(1))\n[safe](https://example.org/)"
        rendered = mod.markdown_to_safe_html(text)
        self.assertNotIn("<script>", rendered)
        self.assertNotIn('href="javascript:', rendered)
        self.assertIn('href="https://example.org/"', rendered)

    def test_rejects_symlinked_source_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "hub"
            mod.cmd_init(root)
            (root / "projects" / "first-project.md").unlink()
            (root / "projects").rmdir()
            (root / "projects").symlink_to(Path(tmp), target_is_directory=True)
            errors, _ = mod.scan(root)
            self.assertTrue(any("不允许符号链接目录" in error for error in errors))

    def test_build_never_overwrites_unowned_docs_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "hub"
            mod.cmd_init(root)
            (root / "docs").mkdir()
            (root / "docs" / "user-file.txt").write_text("do not remove")
            self.assertEqual(mod.cmd_build(root), 1)
            self.assertEqual((root / "docs" / "user-file.txt").read_text(), "do not remove")


if __name__ == "__main__":
    unittest.main()
