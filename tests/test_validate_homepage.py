import importlib.util
import hashlib
import html.parser
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location(
    "validate_site", Path(__file__).resolve().parents[1] / "scripts" / "validate_site.py"
)
assert SPEC is not None and SPEC.loader is not None
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class PageContent(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings = []
        self.images = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag in ("h1", "h2", "h3"):
            self.headings.append(tag)
        if tag == "img":
            self.images.append(dict(attrs))

    def handle_data(self, data):
        self.text.append(data)


class HomepageValidationTests(unittest.TestCase):
    def test_built_landing_page(self):
        root = Path(__file__).resolve().parents[1]
        page = PageContent()
        page.feed((root / "public" / "index.html").read_text(encoding="utf-8"))
        self.assertEqual(page.headings, ["h1", "h2", "h2", "h2"])
        self.assertEqual(len(page.images), 1)
        image = page.images[0]
        self.assertEqual(
            image["src"],
            "/scrumprimer/editorial/vintage_red_stamp_ScrumPrimerCorner.png",
        )
        self.assertTrue(image["alt"])
        self.assertEqual((image["width"], image["height"]), ("960", "768"))
        self.assertEqual(
            hashlib.sha256(
                (root / "public" / "editorial" / "vintage_red_stamp_ScrumPrimerCorner.png").read_bytes()
            ).hexdigest(),
            "a274531e58a9673aea8c939c0e12e8222b8047bc3a24988643a1a6ac11cdd2db",
        )
        rendered = " ".join("".join(page.text).replace("\u2019", "'").split())
        body = (root / "content" / "en" / "_index.md").read_text(encoding="utf-8").split("---", 2)[2]
        for paragraph in body.split("\n\n"):
            expected = paragraph.strip().removeprefix("## ").replace("**", "")
            if expected:
                self.assertIn(" ".join(expected.split()), rendered)
        self.assertIn("Welcome to the Scrum Primer Corner", rendered)
        self.assertIn("not the official Scrum Primer website", rendered)
        self.assertNotIn("awaiting rights review", rendered)

    def test_homepage_documents(self):
        cases = (
            (None, False),
            ("<rss><channel>Feed</channel></rss>", False),
            ("<!doctype html><html><body></body></html>", False),
            ("<!doctype html><h1>One</h1><h1>Two</h1>", False),
            ("<!doctype html><html><body><h1>Welcome</h1></body></html>", True),
        )
        for document, valid in cases:
            with self.subTest(document=document), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                (root / "public").mkdir()
                if document is not None:
                    (root / "public" / "index.html").write_text(document, encoding="utf-8")
                with patch.object(validator, "ROOT", root):
                    if valid:
                        validator.validate_homepage()
                    else:
                        with self.assertRaises(SystemExit):
                            validator.validate_homepage()


if __name__ == "__main__":
    unittest.main()
