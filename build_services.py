"""Build the oval services section into site/index.html and wire custom.css.

Run after apply_content.py.
"""
import io
import os
import re

from bs4 import BeautifulSoup

from _services import SERVICES

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")

WA = ("https://wa.me/923302935777?text="
      "Hi%20CleanCrew%2C%20I%27d%20like%20a%20quote%20for%20cleaning.")


def read(p):
    return io.open(p, encoding="utf-8", errors="ignore").read()


def write(p, s):
    io.open(p, "w", encoding="utf-8").write(s)


def html_files(d):
    out = []
    for dp, _dirs, fs in os.walk(d):
        for f in fs:
            if f.endswith(".html"):
                out.append(os.path.join(dp, f))
    return out


def link_custom_css(path):
    """Add custom.css after the template stylesheet, with the right depth."""
    s = read(path)
    rel = os.path.relpath(os.path.join(SITE, "css", "custom.css"),
                          os.path.dirname(path)).replace("\\", "/")
    tag = '<link href="%s" rel="stylesheet">' % rel
    if 'custom.css' in s:
        s = re.sub(r'<link[^>]*custom\.css[^>]*>', tag, s)
    else:
        m = re.search(r'(<link[^>]*tooplate-clean-work\.css[^>]*>)', s)
        if m:
            s = s.replace(m.group(1), m.group(1) + "\n" + tag, 1)
        else:
            s = s.replace("</head>", tag + "\n</head>", 1)
    write(path, s)


def services_section(depth=0):
    """depth 0 = site root, 1 = /services/*.html"""
    up = "../" * depth
    cards = []
    for sv in SERVICES:
        cards.append(
            '<a class="svc-card" href="{up}services/{slug}.html">'
            '<span class="svc-card__media">'
            # 400px square thumbnail, not the 1200px hero original — the card
            # renders it at 172px (see optimize_images.py)
            '<img src="{up}images/services/thumb/{thumb}" '
            'alt="{name} in Islamabad and Rawalpindi" '
            'width="172" height="172" loading="lazy" decoding="async">'
            "</span>"
            '<span class="svc-card__name">{name}</span>'
            '<span class="svc-card__text">{card}</span>'
            '<span class="svc-card__go" aria-hidden="true">'
            '<i class="bi-chevron-right"></i></span>'
            "</a>".format(up=up, slug=sv["slug"],
                          thumb=os.path.splitext(sv["img"])[0] + ".jpg",
                          name=sv["name"], card=sv["card"])
        )

    return (
        '<section class="svc" id="services-section">'
        '<div class="container">'
        '<p class="svc__eyebrow">Our services</p>'
        '<h2 class="svc__title">Cleaning services in Islamabad &amp; Rawalpindi</h2>'
        '<p class="svc__lead">Fifteen services covering everything from a single sofa to a '
        'full post-construction handover. Tap any service to see exactly what it includes, '
        'what it does not, and how we price it.</p>'
        '<div class="svc__grid">' + "".join(cards) + "</div>"
        "</div></section>"
    )


def main():
    for f in html_files(SITE):
        link_custom_css(f)

    idx = os.path.join(SITE, "index.html")
    soup = BeautifulSoup(read(idx), "lxml")

    old = soup.select_one(".services-section") or soup.select_one("section.svc")
    if old is None:
        print("!! services section not found")
        return
    new = BeautifulSoup(services_section(0), "lxml")
    old.replace_with(new.find("section"))

    # nav: point "Services" at the new section / services index
    for a in soup.select('a[href*="services"]'):
        if a.get_text(strip=True).lower() in ("services", "our services"):
            a["href"] = "services.html"

    write(idx, str(soup))
    print("index.html services section rebuilt: %d cards" % len(SERVICES))

    # --- services.html: replace the two old listing sections with one grid ---
    lp = os.path.join(SITE, "services.html")
    if os.path.exists(lp):
        ls = BeautifulSoup(read(lp), "lxml")
        old_secs = ls.select("section.services-section")
        if old_secs:
            grid = BeautifulSoup(services_section(0), "lxml").find("section")
            old_secs[0].replace_with(grid)
            for extra in old_secs[1:]:
                extra.decompose()
        # page title/meta for the listing page
        if ls.title:
            ls.title.string = ("All Cleaning Services in Islamabad & Rawalpindi | CleanCrew")
        desc = ls.find("meta", attrs={"name": "description"})
        if desc:
            desc["content"] = (
                "All 15 cleaning services we provide in Islamabad and Rawalpindi — deep "
                "cleaning, post-construction, sofa, carpet, marble, tile, window, solar "
                "panel and janitorial. Free inspection and fixed price.")
        # banner heading
        b = ls.select_one(".banner-section h1, .banner-section h2")
        if b is not None:
            b.string = "Our cleaning services in Islamabad & Rawalpindi"
        write(lp, str(ls))
        print("services.html rebuilt with the same grid")

    print("custom.css linked in %d pages" % len(html_files(SITE)))


if __name__ == "__main__":
    main()
