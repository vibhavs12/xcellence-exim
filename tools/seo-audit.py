#!/usr/bin/env python3
"""Lightweight SEO checks for the generated static site."""

from html.parser import HTMLParser
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
ROUTES = {
    "index.html": "",
    "about.html": "about-us/",
    "rice.html": "rice/",
    "coffee.html": "tea-coffee/",
    "spices.html": "spices/",
    "sugar.html": "sugar-icumsa-45/",
    "export-process.html": "export-process/",
    "certificates.html": "certificates/",
    "contact.html": "contact-us/",
    "privacy.html": "privacy/",
}


def output_path(source):
    route = ROUTES[source]
    return Path("index.html" if not route else route + "index.html")


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._in_title = False
        self.h1_count = 0
        self.description = ""
        self.canonical = ""
        self.robots = ""
        self.links = []
        self.ids = set()
        self.images_without_alt = 0
        self.json_ld = []
        self.organization_schema = None
        self._in_json_ld = False
        self._json_parts = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "meta":
            if values.get("name") == "description":
                self.description = values.get("content", "")
            if values.get("name") == "robots":
                self.robots = values.get("content", "")
        elif tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href", "")
        elif tag == "a" and values.get("href"):
            self.links.append(values["href"])
        elif tag == "img" and "alt" not in values:
            self.images_without_alt += 1
        elif tag == "script" and values.get("type") == "application/ld+json":
            self._in_json_ld = True
            self._json_parts = []
        if values.get("id"):
            self.ids.add(values["id"])

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_json_ld:
            raw = "".join(self._json_parts).strip()
            self.json_ld.append(raw)
            try:
                schema = json.loads(raw)
            except json.JSONDecodeError:
                schema = None
            if isinstance(schema, dict) and schema.get("@type") == "Organization":
                self.organization_schema = schema
            self._in_json_ld = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_json_ld:
            self._json_parts.append(data)


def parse_page(path):
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def main():
    errors = []
    parsed = {name: parse_page(ROOT / output_path(name)) for name in ROUTES}
    titles = {}
    descriptions = {}

    for name, page in parsed.items():
        title = page.title.strip()
        description = page.description.strip()
        if not 30 <= len(title) <= 75:
            errors.append(f"{name}: title length is {len(title)} (expected 30–75)")
        if not 110 <= len(description) <= 180:
            errors.append(f"{name}: description length is {len(description)} (expected 110–180)")
        if title in titles:
            errors.append(f"{name}: duplicate title also used by {titles[title]}")
        if description in descriptions:
            errors.append(f"{name}: duplicate description also used by {descriptions[description]}")
        titles[title] = name
        descriptions[description] = name
        if page.h1_count != 1:
            errors.append(f"{name}: expected one h1, found {page.h1_count}")
        if not page.canonical.startswith("https://xcellenceexim.com/"):
            errors.append(f"{name}: invalid canonical {page.canonical!r}")
        if "index" not in page.robots or "follow" not in page.robots:
            errors.append(f"{name}: page is not index, follow")
        if page.images_without_alt:
            errors.append(f"{name}: {page.images_without_alt} image(s) missing alt")
        for raw in page.json_ld:
            try:
                json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"{name}: invalid JSON-LD: {exc}")
        organization = page.organization_schema
        if organization is None:
            errors.append(f"{name}: missing Organization JSON-LD")
        else:
            if organization.get("name") != "Xcellence Exim":
                errors.append(f"{name}: Organization name must be Xcellence Exim")
            if organization.get("url") != "https://xcellenceexim.com/":
                errors.append(f"{name}: Organization URL must be the production home page")
            if "Indian agricultural merchant exporter" not in organization.get("description", ""):
                errors.append(f"{name}: Organization description must identify an Indian agricultural merchant exporter")
            address = organization.get("address", {})
            for field, expected in {
                "@type": "PostalAddress",
                "addressLocality": "Kota",
                "addressRegion": "Rajasthan",
                "addressCountry": "IN",
            }.items():
                if address.get(field) != expected:
                    errors.append(f"{name}: Organization address {field} must be {expected}")
            contact = organization.get("contactPoint", {})
            if contact.get("@type") != "ContactPoint" or contact.get("contactType") != "export sales":
                errors.append(f"{name}: Organization contact point must be export sales")
            if "https://www.linkedin.com/company/xcellence-exim/" not in organization.get("sameAs", []):
                errors.append(f"{name}: Organization sameAs must include the Xcellence Exim LinkedIn profile")

    route_sources = {route: source for source, route in ROUTES.items()}
    for name, page in parsed.items():
        for href in page.links:
            parts = urlsplit(href)
            if parts.scheme or parts.netloc or href.startswith(("#", "mailto:", "tel:")):
                continue
            route = parts.path
            if route in ("", "./"):
                target_name = "index.html"
            else:
                target_name = route_sources.get(route)
            if target_name is None:
                errors.append(f"{name}: broken internal link {href}")
                continue
            if parts.fragment and parts.fragment not in parsed[target_name].ids:
                errors.append(f"{name}: missing fragment target {href}")

    try:
        tree = ET.parse(ROOT / "sitemap.xml")
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locations = tree.findall(".//sm:loc", ns)
        if len(locations) != len(ROUTES):
            errors.append(f"sitemap.xml: expected {len(ROUTES)} URLs, found {len(locations)}")
        expected = {"https://xcellenceexim.com/" + route for route in ROUTES.values()}
        actual = {node.text for node in locations}
        if actual != expected:
            errors.append("sitemap.xml: canonical clean URL set does not match generated pages")
    except ET.ParseError as exc:
        errors.append(f"sitemap.xml: invalid XML: {exc}")

    redirect_lines = (ROOT / "_redirects").read_text(encoding="utf-8").splitlines()
    nested_contact_redirect = next(
        (line.split() for line in redirect_lines
         if line.strip() and not line.lstrip().startswith("#")
         and line.split()[0] == "/sugar-icumsa-45/contact-us/"),
        None,
    )
    if nested_contact_redirect is None or nested_contact_redirect[1:] != ["/contact-us/", "301"]:
        errors.append("_redirects: malformed nested contact route must permanently redirect to /contact-us/")

    if errors:
        print("SEO audit failed:")
        for error in errors:
            print(" -", error)
        return 1

    for source, route in ROUTES.items():
        if source == "index.html":
            continue
        redirect = parse_page(ROOT / source)
        if "noindex" not in redirect.robots:
            errors.append(f"{source}: redirect fallback must be noindex")
        expected_canonical = "https://xcellenceexim.com/" + route
        if redirect.canonical != expected_canonical:
            errors.append(f"{source}: redirect canonical should be {expected_canonical}")

    if errors:
        print("SEO audit failed:")
        for error in errors:
            print(" -", error)
        return 1

    print(f"SEO audit passed for {len(ROUTES)} indexable clean-URL pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
