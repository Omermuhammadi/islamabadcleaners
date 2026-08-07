"""Generate service detail pages from _service_pages.py.

Reuses the template's own header/nav/footer so the pages are visually identical
to the rest of the site, and injects the SEO body between them.
"""
import io
import json
import os
import re

from bs4 import BeautifulSoup

from _services import BY_SLUG, related
from _service_pages import PAGES, AREAS_ISB, AREAS_RWP

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")
OUT = os.path.join(SITE, "services")

SITE_URL = "https://cleancrew.pk"
PHONE_DISPLAY = "0330 2935777"
PHONE_TEL = "+923302935777"
WA_BASE = "https://wa.me/923302935777?text="


def read(p):
    return io.open(p, encoding="utf-8", errors="ignore").read()


def wa(service_name):
    from urllib.parse import quote
    return WA_BASE + quote(
        "Hi CleanCrew, I'd like a quote for %s in Islamabad / Rawalpindi." % service_name)


def shell():
    """Header + nav + footer lifted from the built home page, path-adjusted."""
    soup = BeautifulSoup(read(os.path.join(SITE, "index.html")), "lxml")
    header = soup.select_one("header.site-header")
    nav = soup.select_one("nav.navbar")
    footer = soup.select_one("footer.site-footer")
    floatbar = soup.select_one(".cc-float")
    head = soup.head

    def fix(el):
        if el is None:
            return ""
        html = str(el)
        # site root is one level up from /services/
        html = re.sub(r'(href|src)="(?!https?:|#|tel:|mailto:|//|\.\./)([^"]+)"',
                      r'\1="../\2"', html)
        return html

    css = "\n".join(
        str(t) for t in head.find_all("link", rel="stylesheet"))
    css = re.sub(r'href="(?!https?:|//)([^"]+)"', r'href="../\1"', css)
    scripts = "\n".join(
        str(t) for t in soup.find_all("script", src=True))
    scripts = re.sub(r'src="(?!https?:|//)([^"]+)"', r'src="../\1"', scripts)

    return {
        "css": css,
        "header": fix(header),
        "nav": fix(nav),
        "footer": fix(footer),
        "float": fix(floatbar),
        "scripts": scripts,
    }


def schema_blocks(slug, page, svc):
    url = "%s/services/%s" % (SITE_URL, slug)
    graph = [
        {
            "@type": "Service",
            "@id": url + "#service",
            "name": re.sub(r"&amp;", "&", page["h1"]),
            "serviceType": svc["name"],
            "url": url,
            "description": page["meta"],
            "provider": {
                "@type": "LocalBusiness",
                "@id": SITE_URL + "/#organization",
                "name": "CleanCrew",
                "telephone": PHONE_TEL,
                "url": SITE_URL,
                "areaServed": [
                    {"@type": "City", "name": "Islamabad"},
                    {"@type": "City", "name": "Rawalpindi"},
                ],
            },
            "areaServed": [
                {"@type": "City", "name": "Islamabad"},
                {"@type": "City", "name": "Rawalpindi"},
            ],
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL},
                {"@type": "ListItem", "position": 2, "name": "Services",
                 "item": SITE_URL + "/services"},
                {"@type": "ListItem", "position": 3, "name": svc["name"], "item": url},
            ],
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in page["faqs"]
            ],
        },
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False)


def build(slug):
    svc = BY_SLUG[slug]
    page = PAGES[slug]
    sh = shell()
    walink = wa(svc["name"])

    incl = "".join("<li>%s</li>" % x for x in page["included"])
    excl = "".join("<li>%s</li>" % x for x in page["excluded"])
    steps = "".join(
        "<h3>%d. %s</h3><p>%s</p>" % (i + 1, t, b)
        for i, (t, b) in enumerate(page["process"]))
    factors = "".join(
        "<h3>%s</h3><p>%s</p>" % (t, b) for t, b in page["price_factors"])
    faqs = "".join(
        '<details%s><summary>%s</summary><div class="cc-faq__a">%s</div></details>'
        % (" open" if i == 0 else "", q, a)
        for i, (q, a) in enumerate(page["faqs"]))
    isb = "".join("<li>%s</li>" % a for a in AREAS_ISB)
    rwp = "".join("<li>%s</li>" % a for a in AREAS_RWP)
    intro = "".join("<p>%s</p>" % p for p in page["intro"])
    closing = "".join("<p>%s</p>" % p for p in page["closing"])
    rel = "".join(
        '<a class="cc-related-card" href="%s.html"><strong>%s</strong><span>%s</span></a>'
        % (r["slug"], r["name"], r["card"]) for r in related(slug, 4))

    return f"""<!DOCTYPE html>
<html lang="en-PK">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page["title"]}</title>
<meta name="description" content="{page["meta"]}">
<link rel="canonical" href="{SITE_URL}/services/{slug}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:title" content="{page["title"]}">
<meta property="og:description" content="{page["meta"]}">
<meta property="og:url" content="{SITE_URL}/services/{slug}">
{sh["css"]}
<script type="application/ld+json">{schema_blocks(slug, page, svc)}</script>
</head>
<body>
{sh["header"]}
{sh["nav"]}

<section class="svcpage-hero" style="background-image:url('../images/services/{svc["img"]}')">
  <div class="container">
    <nav class="svcpage-crumbs" aria-label="Breadcrumb">
      <a href="../index.html">Home</a> &rsaquo; <a href="../services.html">Services</a>
      &rsaquo; <span>{svc["name"]}</span>
    </nav>
    <h1>{page["h1"]}</h1>
    <p>{page["hero_p"]}</p>
    <a class="cc-btn cc-btn--wa" href="{walink}">
      <i class="bi-whatsapp"></i> Get a free quote on WhatsApp
    </a>
    <a class="cc-btn cc-btn--ghost" href="tel:{PHONE_TEL}">
      <i class="bi-telephone-fill"></i> {PHONE_DISPLAY}
    </a>
  </div>
</section>

<section class="svcbody">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-12">

        <h2>{page.get("h2_intro", "What this service involves")}</h2>
        {intro}

        <h2>{page.get("h2_included", "What is included")}</h2>
        <p>{page.get("included_intro", "Every job we quote covers the following as standard. If something you need is not on this list, tell us before we quote and we will price it in.")}</p>
        <ul>{incl}</ul>

        <div class="cc-panel">
          <h3>What is not included as standard</h3>
          <p>These are separate jobs with their own equipment and pricing. We can add
          any of them to your booking — just ask when you get your quote.</p>
          <ul class="cc-cross">{excl}</ul>
        </div>

        <h2>How the job works, step by step</h2>
        {steps}

        <h2>What determines the price</h2>
        <p>We do not publish a fixed price list, because the same service can cost very
        differently from one property to the next. Here is exactly what a deep cleaning
        quote is based on, so there are no surprises on the day.</p>
        {factors}

        <h2>Areas we cover in Islamabad and Rawalpindi</h2>
        <p>{page["areas_intro"]}</p>
        <h3>Islamabad</h3>
        <ul class="cc-areas">{isb}</ul>
        <h3>Rawalpindi</h3>
        <ul class="cc-areas">{rwp}</ul>

        <h2>Frequently asked questions</h2>
        <div class="cc-faq">{faqs}</div>

        <h2>{page["closing_h2"]}</h2>
        {closing}
        <p>
          <a class="cc-btn cc-btn--wa" href="{walink}" style="color:#10233a">
            <i class="bi-whatsapp"></i> Message us on WhatsApp
          </a>
        </p>

      </div>

      <div class="col-lg-4 col-12">
        <aside class="cc-aside">
          <h3>Free inspection, fixed price</h3>
          <p>Tell us the area and the size of the property. We will come and look at it
          free of charge, then give you one price that does not move.</p>
          <a class="cc-btn cc-btn--wa" href="{walink}">
            <i class="bi-whatsapp"></i> WhatsApp us
          </a>
          <a class="cc-btn cc-btn--ghost" href="tel:{PHONE_TEL}">
            <i class="bi-telephone-fill"></i> {PHONE_DISPLAY}
          </a>
          <div class="cc-aside-fact"><i class="bi-clock-fill"></i>
            <span>Open 24 hours, 7 days a week. Same-day slots often available.</span></div>
          <div class="cc-aside-fact"><i class="bi-tools"></i>
            <span>We bring all machines, chemicals and materials.</span></div>
          <div class="cc-aside-fact"><i class="bi-geo-alt-fill"></i>
            <span>Covering all of Islamabad and Rawalpindi.</span></div>
        </aside>
      </div>
    </div>
  </div>
</section>

<section class="cc-related">
  <div class="container">
    <p class="svc__eyebrow">More services</p>
    <h2 class="svc__title" style="margin-bottom:34px">You might also need</h2>
    <div class="cc-related-grid">{rel}</div>
  </div>
</section>

{sh["footer"]}
{sh["float"]}
{sh["scripts"]}
</body>
</html>
"""


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for slug in PAGES:
        html = build(slug)
        p = os.path.join(OUT, slug + ".html")
        io.open(p, "w", encoding="utf-8").write(html)
        words = len(re.sub(r"<[^>]+>", " ", html).split())
        print("built services/%s.html  (~%d words of copy)" % (slug, words))
