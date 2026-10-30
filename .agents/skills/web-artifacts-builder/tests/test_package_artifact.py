"""Local utility tests, not task examples or exam scenarios."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "package-artifact.py"
spec = importlib.util.spec_from_file_location("package_artifact", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.body = self.root / "body.html"
        self.body.write_text('<main><button id="b">실행</button></main>', encoding="utf-8")
        self.css = self.root / "style.css"
        self.css.write_text("main {max-width: 60rem;}", encoding="utf-8")
        self.js = self.root / "app.js"
        self.js.write_text("document.querySelector('#b').onclick = () => {};", encoding="utf-8")
        self.out = self.root / "output" / "artifact.html"

    def run_package(self, **kwargs):
        return module.package(self.body, [self.css], [self.js], self.out, **kwargs)

    def test_packages_utf8_and_escapes_title(self):
        self.run_package(title='도구 <test> & "demo"')
        text = self.out.read_text(encoding="utf-8")
        self.assertIn("도구 &lt;test&gt; &amp; &quot;demo&quot;", text)
        self.assertIn('lang="ko"', text)
        self.assertIn("실행", text)
        self.assertIn("<style>\nmain", text)
        self.assertIn("<script>\ndocument", text)

    def test_no_overwrite(self):
        self.run_package()
        before = self.out.read_bytes()
        with self.assertRaises(FileExistsError):
            self.run_package()
        self.assertEqual(before, self.out.read_bytes())

    def test_missing_input_creates_no_output(self):
        self.js.unlink()
        with self.assertRaises(FileNotFoundError):
            self.run_package()
        self.assertFalse(self.out.exists())

    def test_full_document_rejected(self):
        self.body.write_text("<!DOCTYPE html><html></html>", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.run_package()

    def test_empty_body_rejected(self):
        self.body.write_text("  \n", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.run_package()

    def test_script_delimiter_rejected(self):
        self.js.write_text('const x = "</SCRIPT>";', encoding="utf-8")
        with self.assertRaises(ValueError):
            self.run_package()

    def test_style_delimiter_rejected(self):
        self.css.write_text("/* </style> */", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.run_package()

    def test_invalid_language_rejected(self):
        with self.assertRaises(ValueError):
            self.run_package(lang='ko" onclick="x')

    def test_optional_css_and_js(self):
        module.package(self.body, [], [], self.out)
        self.assertNotIn("<script>", self.out.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
