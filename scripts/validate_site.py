#!/usr/bin/env python3
"""Validate content front matter and generated project-site URLs."""

from __future__ import annotations

import html.parser
import re
import sys
import tomllib
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin, urlsplit


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FIELDS = ("title", "page_id", "lang", "origin", "rights_status")
PAGE_ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
URL_ATTRIBUTES = {"href", "src", "action", "poster"}


class URLCollector(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.urls: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name in URL_ATTRIBUTES and value:
                self.urls.append(value)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)


def fail(message: str) -> None:
    raise SystemExit(f"Validation error: {message}")


def load_config() -> tuple[str, str]:
    config = tomllib.loads((ROOT / "hugo.toml").read_text(encoding="utf-8"))
    base_url = config.get("baseURL")
    content_dir = config.get("languages", {}).get("en", {}).get("contentDir")
    if not isinstance(base_url, str) or not base_url.endswith("/scrumprimer/"):
        fail("hugo.toml baseURL must end with /scrumprimer/")
    if not isinstance(content_dir, str) or content_dir != "content/en":
        fail("English contentDir must be content/en")
    return base_url, content_dir


def parse_front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        fail(f"{path.relative_to(ROOT)}: YAML front matter must start with ---")

    try:
        end = next(index for index in range(1, len(lines)) if lines[index].strip() == "---")
    except StopIteration:
        fail(f"{path.relative_to(ROOT)}: YAML front matter has no closing ---")

    fields: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:end], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[:1].isspace() or line.lstrip().startswith("- "):
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", line)
        if not match:
            fail(f"{path.relative_to(ROOT)}:{line_number}: expected a YAML front matter field")
        key, value = match.groups()
        if key in fields:
            fail(f"{path.relative_to(ROOT)}:{line_number}: duplicate front matter field {key!r}")
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        fields[key] = value

    for field in REQUIRED_FIELDS:
        if not fields.get(field, "").strip():
            fail(f"{path.relative_to(ROOT)}: missing required front matter field {field!r}")
    if fields["lang"] != "en":
        fail(f"{path.relative_to(ROOT)}: Phase 1 content must use lang: en")
    if not PAGE_ID_PATTERN.fullmatch(fields["page_id"]):
        fail(f"{path.relative_to(ROOT)}: page_id must be a lowercase slug")
    return fields


def validate_front_matter(content_dir: str) -> None:
    pages = sorted((ROOT / content_dir).rglob("*.md"))
    if not pages:
        fail(f"no Markdown content found in {content_dir}")
    seen_page_ids: set[str] = set()
    for path in pages:
        fields = parse_front_matter(path)
        page_id = fields["page_id"]
        if page_id in seen_page_ids:
            fail(f"duplicate page_id {page_id!r}")
        seen_page_ids.add(page_id)
    print(f"Validated required front matter in {len(pages)} Markdown page(s).")


def expected_routes() -> list[str]:
    routes = []
    for line in (ROOT / "tests" / "expected-pages.txt").read_text(encoding="utf-8").splitlines():
        route = line.strip()
        if not route or route.startswith("#"):
            continue
        if not route.startswith("/") or route.startswith("//") or ".." in route.split("/"):
            fail(f"invalid expected site-relative route {route!r}")
        routes.append(route)
    if not routes:
        fail("tests/expected-pages.txt does not declare any expected routes")
    return routes


def validate_sitemap(base_url: str, routes: list[str]) -> None:
    sitemap_path = ROOT / "public" / "sitemap.xml"
    if not sitemap_path.is_file():
        fail("Hugo did not generate public/sitemap.xml")
    root = ET.parse(sitemap_path).getroot()
    sitemap_urls = {
        element.text
        for element in root.iter()
        if element.tag.endswith("loc") and element.text
    }

    base = urlsplit(base_url)
    prefix = base.path
    for url in sitemap_urls:
        parsed = urlsplit(url)
        if parsed.scheme != base.scheme or parsed.netloc != base.netloc:
            fail(f"sitemap URL is outside the configured site origin: {url}")
        if not parsed.path.startswith(prefix):
            fail(f"sitemap URL is missing the /scrumprimer/ project prefix: {url}")

    for route in routes:
        expected = urljoin(base_url, route.lstrip("/"))
        if expected not in sitemap_urls:
            fail(f"expected route is missing from sitemap: {expected}")
    print(f"Validated {len(sitemap_urls)} sitemap URL(s) and {len(routes)} expected route(s).")


def validate_html_urls(base_url: str) -> None:
    base = urlsplit(base_url)
    html_files = sorted((ROOT / "public").rglob("*.html"))
    checked = 0
    for path in html_files:
        parser = URLCollector()
        parser.feed(path.read_text(encoding="utf-8"))
        for url in parser.urls:
            if url.startswith(("#", "data:", "mailto:", "tel:", "javascript:")):
                continue
            resolved = urlsplit(urljoin(base_url, url))
            if resolved.scheme in {"http", "https"} and resolved.netloc == base.netloc:
                if not resolved.path.startswith(base.path):
                    fail(f"{path.relative_to(ROOT / 'public')}: local URL lacks /scrumprimer/ prefix: {url}")
            checked += 1
    print(f"Validated project-path handling for {checked} URL reference(s) in {len(html_files)} HTML file(s).")


def validate_homepage() -> None:
    path = ROOT / "public" / "index.html"
    if not path.is_file():
        fail("Hugo did not generate public/index.html; an RSS feed is not a homepage")
    text = path.read_text(encoding="utf-8")
    if not re.search(r"<!doctype\s+html\s*>", text, re.IGNORECASE):
        fail("public/index.html must be an HTML document, not a feed")
    if len(re.findall(r"<h1(?:\s[^>]*)?>", text, re.IGNORECASE)) != 1:
        fail("public/index.html must contain exactly one main heading")
    print("Validated an HTML homepage with exactly one main heading.")


def main() -> None:
    base_url, content_dir = load_config()
    validate_front_matter(content_dir)
    routes = expected_routes()
    validate_sitemap(base_url, routes)
    validate_homepage()
    validate_html_urls(base_url)


if __name__ == "__main__":
    main()
