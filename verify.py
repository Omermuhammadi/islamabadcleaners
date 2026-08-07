"""Bulletproof gate for the built site in docs/.

Checks every page: internal links resolve (case-exact), head/meta/schema
correctness, HTML structure, banned strings, weights, sitemap parity.
Exits non-zero on any failure.

Usage: python verify.py
"""

import json
import os
import re
import sys
import urllib.parse
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")

import _site as S  # noqa: E402

ERRORS = []
WARNINGS = []

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

BANNED = ["cleancrew.pk", "tooplate", "bootstrap", "freepik", "jquery",
          "Ayesha K.", "Bilal R.", "Hina M.", "Usman T.", "backstretch"]


def err(page, msg):
    ERRORS.append(f"{page}: {msg}")


class Audit(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.h1 = 0
        self.headings = []
        self.links = []
        self.imgs = []
        self.canonical = None
        self.title = None
        self.metas = {}
        self.jsonld = []
        self._in_title = False
        self._in_script_ld = False
        self._buf = ""
        self.misnest = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
            self._buf = ""
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in_script_ld = True
            self._buf = ""
        if tag == "h1":
            self.h1 += 1
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.headings.append(int(tag[1]))
        if tag == "a" and a.get("href"):
            self.links.append(a)
        if tag == "img":
            self.imgs.append(a)
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        if tag == "meta":
            if a.get("name"):
                self.metas[a["name"]] = a.get("content", "")
            if a.get("property"):
                self.metas[a["property"]] = a.get("content", "")
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
            self.title = self._buf.strip()
        if tag == "script" and self._in_script_ld:
            self._in_script_ld = False
            self.jsonld.append(self._buf)
        if tag in VOID:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        else:
            if tag in self.stack:
                while self.stack and self.stack[-1] != tag:
                    self.misnest.append(self.stack.pop())
                if self.stack:
                    self.stack.pop()
            else:
                self.misnest.append(f"/{tag}")

    def handle_data(self, data):
        if self._in_title or self._in_script_ld:
            self._buf += data


def exact_exists(path):
    """Case-sensitive existence check on Windows."""
    if not os.path.exists(path):
        return False
    d, name = os.path.split(path)
    try:
        return name in os.listdir(d)
    except OSError:
        return False


def check_page(rel):
    page = rel.replace("\\", "/")
    full = os.path.join(DOCS, rel)
    with open(full, encoding="utf-8") as f:
        html = f.read()

    low = html.lower()
    for b in BANNED:
        if b.lower() in low:
            err(page, f"banned string present: {b!r}")

    p = Audit()
    p.feed(html)

    is_404 = page == "404.html"

    if p.h1 != 1:
        err(page, f"expected exactly one <h1>, found {p.h1}")
    if p.misnest:
        err(page, f"misnested/unmatched tags: {p.misnest[:5]}")
    if p.stack and p.stack != []:
        err(page, f"unclosed tags at EOF: {p.stack[:5]}")

    # heading order never skips down levels
    prev = 0
    for h in p.headings:
        if prev and h > prev + 1:
            err(page, f"heading level jump h{prev} -> h{h}")
        prev = h

    if not p.title:
        err(page, "missing <title>")
    elif len(p.title) > 70:
        WARNINGS.append(f"{page}: title {len(p.title)} chars: {p.title!r}")
    desc = p.metas.get("description", "")
    if not desc:
        err(page, "missing meta description")
    elif len(desc) > 165:
        WARNINGS.append(f"{page}: meta description {len(desc)} chars")

    expected_canonical = f"{S.BASE_URL}/" if page == "index.html" else f"{S.BASE_URL}/{page}"
    if not is_404 and p.canonical != expected_canonical:
        err(page, f"canonical {p.canonical!r} != {expected_canonical!r}")

    for k in ("og:title", "og:description", "og:url", "og:image",
              "twitter:card", "twitter:image"):
        if not p.metas.get(k):
            err(page, f"missing {k}")
    ogi = p.metas.get("og:image", "")
    if ogi and not ogi.startswith("https://"):
        err(page, f"og:image not absolute: {ogi}")

    if is_404:
        if "noindex" not in p.metas.get("robots", ""):
            err(page, "404 must be noindex")
    else:
        if "index, follow" not in p.metas.get("robots", ""):
            err(page, "missing robots index,follow")
        if not p.jsonld:
            err(page, "missing JSON-LD")

    for block in p.jsonld:
        try:
            data = json.loads(block)
        except json.JSONDecodeError as e:
            err(page, f"JSON-LD does not parse: {e}")
            continue
        graph = data.get("@graph", [data])
        types = [n.get("@type") for n in graph]
        if not is_404 and "LocalBusiness" not in types:
            err(page, "JSON-LD missing LocalBusiness node")

    base_dir = os.path.dirname(full)
    for a in p.links:
        href = a["href"]
        if href.startswith(("http://", "https://")):
            if "wa.me" in href:
                if f"wa.me/{S.WHATSAPP}" not in href:
                    err(page, f"wa.me link wrong number: {href}")
                q = urllib.parse.urlparse(href).query
                text = urllib.parse.parse_qs(q).get("text", [""])[0]
                if not text:
                    err(page, f"wa.me link missing text param: {href}")
            if a.get("target") == "_blank" and "noopener" not in a.get("rel", ""):
                err(page, f"target=_blank without noopener: {href}")
            continue
        if href.startswith(("mailto:", "tel:", "#")):
            continue
        target = href.split("#")[0]
        if not target:
            continue
        resolved = os.path.normpath(os.path.join(base_dir, target))
        if not exact_exists(resolved):
            err(page, f"broken link: {href}")

    for img in p.imgs:
        src = img.get("src", "")
        if "alt" not in img:
            err(page, f"img missing alt: {src}")
        if not img.get("width") or not img.get("height"):
            err(page, f"img missing width/height: {src}")
        if src and not src.startswith("http"):
            resolved = os.path.normpath(os.path.join(base_dir, src))
            if not exact_exists(resolved):
                err(page, f"broken img src: {src}")


def check_sitemap(pages):
    sm = os.path.join(DOCS, "sitemap.xml")
    with open(sm, encoding="utf-8") as f:
        xml = f.read()
    locs = re.findall(r"<loc>(.*?)</loc>", xml)
    disk = set()
    for rel in pages:
        page = rel.replace("\\", "/")
        if page == "404.html":
            continue
        disk.add(f"{S.BASE_URL}/" if page == "index.html" else f"{S.BASE_URL}/{page}")
    smset = set(locs)
    for missing in disk - smset:
        err("sitemap.xml", f"page on disk not in sitemap: {missing}")
    for ghost in smset - disk:
        err("sitemap.xml", f"sitemap URL has no file: {ghost}")

    with open(os.path.join(DOCS, "robots.txt"), encoding="utf-8") as f:
        robots = f.read()
    if f"{S.BASE_URL}/sitemap.xml" not in robots:
        err("robots.txt", "does not point at the live sitemap URL")


def check_weights(pages):
    for dirpath, _, files in os.walk(os.path.join(DOCS, "images")):
        for f in files:
            fp = os.path.join(dirpath, f)
            kb = os.path.getsize(fp) / 1024
            if kb > 150:
                err("weights", f"image over 150 KB: {f} ({kb:.0f} KB)")
    css = os.path.getsize(os.path.join(DOCS, "css", "main.css")) / 1024
    if css > 30:
        err("weights", f"main.css over 30 KB ({css:.0f} KB)")
    total = 0
    for dirpath, _, files in os.walk(DOCS):
        for f in files:
            total += os.path.getsize(os.path.join(dirpath, f))
    if total / 1024 / 1024 > 3.5:
        err("weights", f"docs/ total {total/1024/1024:.2f} MB > 3.5 MB")

    # services.html page weight: html + css + fonts + its images
    svc = os.path.join(DOCS, "services.html")
    with open(svc, encoding="utf-8") as f:
        html = f.read()
    weight = os.path.getsize(svc) + os.path.getsize(os.path.join(DOCS, "css", "main.css"))
    for m in re.findall(r'src="([^"]+)"', html):
        fp = os.path.normpath(os.path.join(DOCS, m))
        if os.path.exists(fp):
            weight += os.path.getsize(fp)
    for f in os.listdir(os.path.join(DOCS, "fonts")):
        weight += os.path.getsize(os.path.join(DOCS, "fonts", f))
    if weight / 1024 > 600:
        err("weights", f"services.html page weight {weight/1024:.0f} KB > 600 KB")


def main():
    pages = []
    for dirpath, _, files in os.walk(DOCS):
        for f in files:
            if f.endswith(".html"):
                pages.append(os.path.relpath(os.path.join(dirpath, f), DOCS))
    print(f"Auditing {len(pages)} pages...")

    titles, descs = {}, {}
    for rel in sorted(pages):
        check_page(rel)
        with open(os.path.join(DOCS, rel), encoding="utf-8") as f:
            html = f.read()
        t = re.search(r"<title>(.*?)</title>", html, re.S)
        d = re.search(r'name="description" content="(.*?)"', html)
        if t:
            titles.setdefault(t.group(1), []).append(rel)
        if d:
            descs.setdefault(d.group(1), []).append(rel)
    for t, ps in titles.items():
        if len(ps) > 1:
            err("dupes", f"duplicate title on {ps}: {t!r}")
    for d, ps in descs.items():
        if len(ps) > 1:
            err("dupes", f"duplicate description on {ps}")

    check_sitemap(pages)
    check_weights(pages)

    for w in WARNINGS:
        print(f"  WARN  {w}")
    if ERRORS:
        print(f"\n{len(ERRORS)} ERRORS:")
        for e in ERRORS:
            print(f"  FAIL  {e}")
        sys.exit(1)
    print(f"ALL CHECKS PASSED ({len(pages)} pages, {len(WARNINGS)} warnings)")


if __name__ == "__main__":
    main()
