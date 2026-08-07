"""Build the SuperClean variant (the "5003" option) with our real content.

Keeps SuperClean's own template, theme, colours, fonts and section styling —
only the content, navigation, service pages and CTAs are ours. All the added
markup uses SuperClean's CSS variables via css/cc.css.

Run:  python build_superclean.py
"""
import io
import json
import os
import re
import shutil
from urllib.parse import quote

from bs4 import BeautifulSoup

from _services import SERVICES, BY_SLUG, related
from _service_pages import PAGES, AREAS_ISB, AREAS_RWP
import finalize as F   # reuse TESTIMONIALS / AREAS so both sites stay in sync

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "superclean-alt")
SRC = os.path.join(ROOT, "site")            # to borrow the service photos

BRAND = "CleanCrew"
SITE_URL = "https://cleancrew-superclean.vercel.app"
PHONE_DISPLAY = "0330 2935777"
PHONE_TEL = "+923302935777"
EMAIL = "mgcleaner364@gmail.com"


def read(p):
    return io.open(p, encoding="utf-8", errors="ignore").read()


def write(p, s):
    io.open(p, "w", encoding="utf-8").write(s)


def wa(msg):
    return "https://wa.me/923302935777?text=" + quote(msg)


WA_GENERAL = wa("Hi %s, I'd like a quote for cleaning in Islamabad / Rawalpindi." % BRAND)

FLOAT = (
    '<div class="cc-float">'
    '<a class="cc-wa" href="%s" target="_blank" rel="noopener" aria-label="WhatsApp us">'
    '<svg viewBox="0 0 24 24"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15s-.77.96-.94 1.16c-.17.2-.35.22-.64.08-.3-.15-1.25-.46-2.38-1.47-.88-.79-1.47-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.6-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.06 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.69.63.71.22 1.36.19 1.87.12.57-.09 1.75-.72 2-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35z"/>'
    '<path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.46 1.32 4.96L2 22l5.25-1.38a9.9 9.9 0 0 0 4.79 1.22h.01c5.46 0 9.91-4.45 9.91-9.91S17.5 2 12.04 2zm0 18.15c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.24 8.25-8.24 2.2 0 4.27.86 5.83 2.42a8.2 8.2 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23z"/></svg></a>'
    '<a class="cc-call" href="tel:%s" aria-label="Call us">'
    '<svg viewBox="0 0 24 24"><path d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg></a>'
    "</div>" % (WA_GENERAL, PHONE_TEL)
)


# ----------------------------------------------------------------- helpers --
def up(depth):
    return "../" * depth


def services_grid(depth=0):
    u = up(depth)
    cards = "".join(
        '<a class="cc-card" href="{u}services/{slug}.html">'
        '<span class="cc-card__media"><img src="{u}images/services/thumb/{thumb}" '
        'alt="{name} in Islamabad and Rawalpindi" width="168" height="168" '
        'loading="lazy" decoding="async"></span>'
        '<span class="cc-card__name">{name}</span>'
        '<span class="cc-card__text">{card}</span>'
        '<span class="cc-card__go" aria-hidden="true">&rsaquo;</span></a>'.format(
            u=u, slug=s["slug"], thumb=os.path.splitext(s["img"])[0] + ".jpg",
            name=s["name"], card=s["card"])
        for s in SERVICES)
    return (
        '<section class="cc-svc" id="services"><div class="container">'
        '<p class="cc-eyebrow">Our services</p>'
        '<h2 class="cc-title">Cleaning services in Islamabad &amp; Rawalpindi</h2>'
        '<p class="cc-lead">Fifteen services covering everything from a single sofa to a '
        'full post-construction handover. Tap any service to see what it includes, what '
        'it does not, and how we price it.</p>'
        '<div class="cc-grid">%s</div></div></section>' % cards)


def areas_strip():
    chips = "".join("<li>%s</li>" % a for a in F.AREAS)
    return (
        '<section class="cc-areas-strip"><div class="container">'
        '<p class="cc-eyebrow">Where we work</p>'
        '<h2 class="cc-title">Serving Islamabad &amp; Rawalpindi</h2>'
        '<p class="cc-lead">We cover both cities in full. These are the areas we are in '
        'most often — if yours is not listed, message us and we will tell you straight '
        'away.</p><ul class="cc-chips">%s</ul></div></section>' % chips)


def build_brand(soup, depth):
    """The template logo is a SUPER CLEAN image. Replace it with a wordmark so
    the branding matches the content (the real logo replaces this later)."""
    for a in soup.select("a.navbar-brand"):
        a["href"] = up(depth) + "index.html"
        a.clear()
        a["class"] = a.get("class", []) + ["cc-wordmark"]
        a.append(BRAND)


def fix_a11y(soup):
    """Template gaps: the mobile nav toggle has no accessible name, and
    plugins.js throws because the template's date-picker markup is not on our
    pages."""
    n = 0
    for b in soup.select("button.navbar-toggler"):
        if not b.get("aria-label") and not b.get_text(strip=True):
            b["aria-label"] = "Open navigation menu"
            n += 1
    for b in soup.find_all("button"):
        if b.get("aria-label") or b.get_text(strip=True):
            continue
        b["aria-label"] = "Menu"
        n += 1
    return n


def build_nav(soup, depth):
    build_brand(soup, depth)
    ul = soup.select_one("nav.navbar ul.navbar-nav")
    if ul is None:
        return
    u = up(depth)
    ul.clear()
    for label, href in (("Home", "index.html"), ):
        ul.append(BeautifulSoup(
            '<li class="nav-item"><a class="nav-link" href="%s%s">%s</a></li>'
            % (u, href, label), "lxml").li)
    opts = "".join(
        '<li><a class="dropdown-item" href="%sservices/%s.html">%s</a></li>'
        % (u, s["slug"], s["name"]) for s in SERVICES)
    ul.append(BeautifulSoup(
        '<li class="nav-item dropdown">'
        '<a class="nav-link dropdown-toggle" href="%sservices.html" id="svcDd" '
        'role="button" data-bs-toggle="dropdown" aria-expanded="false">Services</a>'
        '<ul class="dropdown-menu" aria-labelledby="svcDd">'
        '<li><a class="dropdown-item fw-bold" href="%sservices.html">All services</a></li>'
        '<li><hr class="dropdown-divider"></li>%s</ul></li>' % (u, u, opts), "lxml").li)
    for label, href in (("About", "about.html"), ("Contact", "contact.html")):
        ul.append(BeautifulSoup(
            '<li class="nav-item"><a class="nav-link" href="%s%s">%s</a></li>'
            % (u, href, label), "lxml").li)


def build_footer(soup, depth):
    foot = soup.select_one("footer")
    if foot is None:
        return
    u = up(depth)
    col1 = "".join('<li><a href="%sservices/%s.html">%s</a></li>' % (u, s["slug"], s["name"])
                   for s in SERVICES[:8])
    col2 = "".join('<li><a href="%sservices/%s.html">%s</a></li>' % (u, s["slug"], s["name"])
                   for s in SERVICES[8:])
    new = BeautifulSoup(
        '<footer class="bg-dark text-white pt-5">'
        '<div class="container">'
        '<div class="row pb-4">'
        '<div class="col-lg-4 col-12 mb-4">'
        '<p class="h5 text-white">%(b)s</p>'
        '<p class="small" style="color:rgba(255,255,255,.78);max-width:40ch">'
        'Professional cleaning across Islamabad and Rawalpindi — deep cleaning, '
        'post-construction, sofa, carpet, marble and janitorial contracts. Free '
        'inspection, one fixed price, available 24/7.</p>'
        '<ul class="list-unstyled small" style="color:rgba(255,255,255,.85)">'
        '<li class="mb-2"><a class="text-white text-decoration-none" href="tel:%(tel)s">%(ph)s</a></li>'
        '<li class="mb-2"><a class="text-white text-decoration-none" href="%(wa)s">WhatsApp us</a></li>'
        '<li class="mb-2"><a class="text-white text-decoration-none" href="mailto:%(em)s">%(em)s</a></li>'
        '<li class="mb-2">Open 24 hours, 7 days a week</li>'
        '<li>Islamabad &amp; Rawalpindi, Pakistan</li></ul></div>'
        '<div class="col-lg-3 col-md-6 col-12 mb-4"><p class="h6 text-white">Services</p>'
        '<ul class="list-unstyled small cc-flinks">%(c1)s</ul></div>'
        '<div class="col-lg-3 col-md-6 col-12 mb-4"><p class="h6 text-white">More services</p>'
        '<ul class="list-unstyled small cc-flinks">%(c2)s</ul></div>'
        '<div class="col-lg-2 col-md-6 col-12 mb-4"><p class="h6 text-white">Company</p>'
        '<ul class="list-unstyled small cc-flinks">'
        '<li><a href="%(u)sindex.html">Home</a></li>'
        '<li><a href="%(u)sservices.html">All services</a></li>'
        '<li><a href="%(u)sabout.html">About us</a></li>'
        '<li><a href="%(u)scontact.html">Contact</a></li></ul></div>'
        '</div>'
        '<div class="border-top py-3 small" style="border-color:rgba(255,255,255,.15)!important;color:rgba(255,255,255,.7)">'
        '&copy; 2026 %(b)s. Cleaning services in Islamabad &amp; Rawalpindi.</div>'
        '</div></footer>' % {"b": BRAND, "tel": PHONE_TEL, "ph": PHONE_DISPLAY,
                             "em": EMAIL, "wa": WA_GENERAL, "u": u,
                             "c1": col1, "c2": col2}, "lxml").find("footer")
    foot.replace_with(new)


def wire_ctas(soup):
    n = 0
    pat = re.compile(r"get a free quote|request a free quote|get started|book now|"
                     r"get a quote|contact us|read more|our services", re.I)
    for a in soup.find_all("a", href=True):
        h = a["href"].strip()
        label = a.get_text(" ", strip=True)
        if h in ("#", "", "javascript:void(0)"):
            if pat.search(label):
                a["href"] = WA_GENERAL
            else:
                a["href"] = "services.html"
            n += 1
        elif os.path.basename(h) in ("blog.html", "blog-single.html",
                                     "service-single.html", "team.html"):
            a["href"] = re.sub(r"[^/]+$", "services.html", h)
            n += 1
        elif os.path.basename(h) == "quote.html":
            # the template's quote page does not exist; WhatsApp is the CTA
            a["href"] = WA_GENERAL
            n += 1
    return n


def head_common(soup, depth, title, desc, path, schema=None):
    u = up(depth)
    head = soup.head
    for t in head.find_all("title"):
        t.decompose()
    for m in head.find_all("meta", attrs={"name": "description"}):
        m.decompose()
    for l in head.find_all("link", rel="canonical"):
        l.decompose()
    tt = soup.new_tag("title"); tt.string = title
    head.append(tt)
    head.append(BeautifulSoup('<meta name="description" content="%s">' % desc, "lxml").meta)
    head.append(BeautifulSoup('<link rel="canonical" href="%s/%s">' % (SITE_URL, path), "lxml").link)
    head.append(BeautifulSoup('<meta name="robots" content="index, follow, max-image-preview:large">', "lxml").meta)
    for l in head.find_all("link", rel=lambda v: v and "icon" in (" ".join(v) if isinstance(v, list) else v)):
        l.decompose()
    head.append(BeautifulSoup('<link rel="icon" href="%sfavicon.ico" sizes="any">' % u, "lxml").link)
    if not head.find("link", href=lambda v: v and "cc.css" in v):
        head.append(BeautifulSoup('<link rel="stylesheet" href="%scss/cc.css">' % u, "lxml").link)
    if schema:
        s = soup.new_tag("script", type="application/ld+json")
        s.string = schema
        head.append(s)


def shell():
    """SuperClean's header/nav/footer/scripts, taken from the built index."""
    soup = BeautifulSoup(read(os.path.join(SITE, "index.html")), "lxml")
    head_links = "\n".join(str(t) for t in soup.head.find_all("link"))
    scripts = "\n".join(str(t) for t in soup.find_all("script", src=True))
    return {
        "links": head_links,
        "header": str(soup.select_one("header") or ""),
        "topbar": str(soup.select_one("nav.header-top") or ""),
        "nav": str(soup.select_one("nav.navbar") or ""),
        "footer": str(soup.select_one("footer") or ""),
        "scripts": scripts,
    }


def repath(html, depth):
    if depth == 0:
        return html
    return re.sub(r'(href|src)="(?!https?:|#|tel:|mailto:|//|\.\./|data:)([^"]+)"',
                  r'\1="%s\2"' % up(depth), html)


# ------------------------------------------------------------------ index --
def build_index():
    p = os.path.join(SITE, "index.html")
    soup = BeautifulSoup(read(p), "lxml")

    secs = [s for s in soup.body.find_all("section", recursive=True)
            if not s.find_parent("section")]

    # drop pricing + blog (quote-only pricing; no blog content yet)
    for s in secs:
        txt = s.get_text(" ", strip=True)[:60].lower()
        if "our subscription" in txt or "news & articles" in txt or "news &amp; articles" in txt:
            s.decompose()

    # services carousel -> our oval grid
    for s in soup.body.find_all("section"):
        if s.select_one(".services-swiper, .service"):
            s.replace_with(BeautifulSoup(services_grid(0), "lxml").find("section"))
            break

    # testimonials
    for s in soup.body.find_all("section"):
        sw = s.select_one(".testimonial-swiper")
        if not sw:
            continue
        cards = "".join(
            '<div class="col-lg-3 col-md-6 mb-4"><div class="p-4 bg-white h-100" '
            'style="border:1px solid var(--cc-line);border-radius:12px">'
            '<div class="d-flex align-items-center mb-3">'
            '<img src="images/avatar/%s" alt="%s, %s" width="56" height="56" '
            'style="width:56px;height:56px;border-radius:50%%;object-fit:cover" loading="lazy">'
            '<div class="ms-3"><p class="mb-0 fw-bold">%s</p>'
            '<p class="mb-0 small text-muted">%s</p></div></div>'
            '<p class="mb-0" style="font-size:15px;line-height:1.65">%s</p>'
            "</div></div>" % (img.split("/")[-1], name, area, name, area, quote_)
            for name, area, img, quote_ in F.TESTIMONIALS)
        s.replace_with(BeautifulSoup(
            '<section class="padding-medium bg-gray"><div class="container">'
            '<p class="cc-eyebrow">Reviews</p>'
            '<h2 class="cc-title">What our customers say</h2>'
            '<p class="cc-lead">Real jobs across Islamabad and Rawalpindi.</p>'
            '<div class="row">%s</div></div></section>' % cards, "lxml").find("section"))
        break

    # about/intro section still carries the template's generic filler copy
    for sec in soup.body.find_all("section"):
        hd = sec.find(["h2", "h3"])
        if hd and "welcome to" in hd.get_text(" ", strip=True).lower():
            hd.string = "Eight years cleaning the twin cities"
            eb = sec.find("p")
            paras = [p for p in sec.find_all("p") if p is not eb]
            body = [
                "We are a cleaning company based in Islamabad, working across both "
                "Islamabad and Rawalpindi. We handle one-off jobs like deep cleans, "
                "sofas, carpets and marble, the deadline work that comes with moving "
                "or building, and regular janitorial contracts for offices and clinics.",
                "We bring our own equipment and materials to every job, and we quote "
                "after seeing the property rather than guessing over the phone — so "
                "the price we give you is the price you pay.",
            ]
            for i, para in enumerate(paras):
                if i < len(body):
                    para.string = body[i]
                else:
                    para.decompose()
            break

    # features section: use our three real reasons
    for sec in soup.body.find_all("section"):
        hd = sec.find(["h2", "h3"])
        if hd and "some of our features" in hd.get_text(" ", strip=True).lower():
            hd.string = "Why people call us back"
            feats = sec.select(".feature")
            reasons = [
                ("Available 24/7", "Call or WhatsApp at any hour. We usually reply "
                 "within minutes and can often be there the same day."),
                ("We bring everything", "Our own machines, chemicals and supplies come "
                 "with the team. You do not have to arrange or buy anything."),
                ("The right size crew", "We scale the team to the job — one cleaner "
                 "for a sofa, a full crew for a post-construction handover."),
            ]
            for i, fe in enumerate(feats):
                if i >= len(reasons):
                    continue
                t, d = reasons[i]
                h = fe.find(["h3", "h4", "h5"])
                if h: h.string = t
                pp = fe.find("p")
                if pp: pp.string = d
            break

    # areas strip appended before the footer
    foot = soup.select_one("footer")
    if foot:
        foot.insert_before(BeautifulSoup(areas_strip(), "lxml").find("section"))

    build_nav(soup, 0)
    build_footer(soup, 0)
    fix_a11y(soup)
    wire_ctas(soup)
    head_common(soup, 0,
                "%s — Cleaning Services in Islamabad & Rawalpindi" % BRAND,
                "Deep cleaning, post-construction, sofa, carpet and marble cleaning in "
                "Islamabad and Rawalpindi. Free inspection, fixed price, available 24/7. "
                "WhatsApp 0330 2935777.", "")
    if not soup.select_one(".cc-float"):
        soup.body.append(BeautifulSoup(FLOAT, "lxml").find("div"))
    write(p, str(soup))
    print("  index.html rebuilt")


# ------------------------------------------------------------- inner pages --
def page(depth, title, desc, path, h1, lead, body, img, schema=None):
    sh = shell()
    u = up(depth)
    doc = BeautifulSoup(
        "<!DOCTYPE html><html lang='en-PK'><head><meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width, initial-scale=1'>"
        + repath(sh["links"], depth) + "</head><body>"
        + repath(sh["header"], depth)   # already contains both navs
        + '<section class="cc-hero" style="background-image:url(\'%simages/services/%s\')">'
          '<div class="container">%s<h1>%s</h1><p>%s</p>'
          '<a class="cc-btn cc-btn--wa" href="%s">Get a free quote on WhatsApp</a>'
          '<a class="cc-btn cc-btn--ghost" href="tel:%s">%s</a>'
          '</div></section>' % (u, img, "", h1, lead, WA_GENERAL, PHONE_TEL, PHONE_DISPLAY)
        + body
        # the template's plugins.js initialises a date picker and throws
        # "Does div#select-date exist?" on pages that have no booking form
        + '<div id="select-date" hidden aria-hidden="true"></div>'
        + repath(sh["footer"], depth) + FLOAT + repath(sh["scripts"], depth)
        + "</body></html>", "lxml")
    build_nav(doc, depth)
    fix_a11y(doc)
    wire_ctas(doc)
    head_common(doc, depth, title, desc, path, schema)
    return str(doc)


def service_schema(slug, pg, svc):
    url = "%s/services/%s" % (SITE_URL, slug)
    return json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "Service", "@id": url + "#service",
         "name": re.sub("&amp;", "&", pg["h1"]), "serviceType": svc["name"],
         "url": url, "description": pg["meta"],
         "provider": {"@type": "LocalBusiness", "@id": SITE_URL + "/#organization",
                      "name": BRAND, "telephone": PHONE_TEL, "url": SITE_URL},
         "areaServed": [{"@type": "City", "name": "Islamabad"},
                        {"@type": "City", "name": "Rawalpindi"}]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL},
            {"@type": "ListItem", "position": 2, "name": "Services", "item": SITE_URL + "/services"},
            {"@type": "ListItem", "position": 3, "name": svc["name"], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pg["faqs"]]},
    ]}, ensure_ascii=False)


def build_service_pages():
    out = os.path.join(SITE, "services")
    os.makedirs(out, exist_ok=True)
    for slug, pg in PAGES.items():
        svc = BY_SLUG[slug]
        walink = wa("Hi %s, I'd like a quote for %s in Islamabad / Rawalpindi."
                    % (BRAND, svc["name"]))
        body = (
            '<section class="cc-body"><div class="container"><div class="row">'
            '<div class="col-lg-8 col-12">'
            '<nav class="cc-crumbs mb-3"><a href="../index.html">Home</a> &rsaquo; '
            '<a href="../services.html">Services</a> &rsaquo; <span>%s</span></nav>'
            '<h2>%s</h2>%s'
            '<h2>%s</h2><p>%s</p><ul>%s</ul>'
            '<div class="cc-panel"><h3>What is not included as standard</h3>'
            '<p>These are separate jobs with their own equipment and pricing. We can add '
            'any of them to your booking — just ask when you get your quote.</p>'
            '<ul class="cc-cross">%s</ul></div>'
            '<h2>How the job works, step by step</h2>%s'
            '<h2>What determines the price</h2>'
            '<p>We do not publish a fixed price list, because the same service can cost '
            'very differently from one property to the next. Here is exactly what a quote '
            'is based on, so there are no surprises on the day.</p>%s'
            '<h2>Areas we cover in Islamabad and Rawalpindi</h2><p>%s</p>'
            '<h3>Islamabad</h3><ul class="cc-chips">%s</ul>'
            '<h3>Rawalpindi</h3><ul class="cc-chips">%s</ul>'
            '<h2>Frequently asked questions</h2><div class="cc-faq">%s</div>'
            '<h2>%s</h2>%s'
            '<p><a class="cc-btn cc-btn--wa" href="%s">Message us on WhatsApp</a></p>'
            '</div>'
            '<div class="col-lg-4 col-12"><aside class="cc-aside">'
            '<h3>Free inspection, fixed price</h3>'
            '<p>Tell us the area and the size of the property. We will come and look at it '
            'free of charge, then give you one price that does not move.</p>'
            '<a class="cc-btn cc-btn--wa" href="%s">WhatsApp us</a>'
            '<a class="cc-btn cc-btn--ghost" href="tel:%s" style="color:#fff">%s</a>'
            '<div class="cc-fact"><span>&#9679;</span><span>Open 24 hours, 7 days a week</span></div>'
            '<div class="cc-fact"><span>&#9679;</span><span>All machines and materials included</span></div>'
            '<div class="cc-fact"><span>&#9679;</span><span>Covering all of Islamabad and Rawalpindi</span></div>'
            '</aside></div></div></div></section>'
            '<section class="cc-related"><div class="container">'
            '<p class="cc-eyebrow">More services</p>'
            '<h2 class="cc-title" style="margin-bottom:30px">You might also need</h2>'
            '<div class="cc-related-grid">%s</div></div></section>'
            % (svc["name"],
               pg.get("h2_intro", "What this service involves"),
               "".join("<p>%s</p>" % x for x in pg["intro"]),
               pg.get("h2_included", "What is included"),
               pg.get("included_intro", "Everything below is standard."),
               "".join("<li>%s</li>" % x for x in pg["included"]),
               "".join("<li>%s</li>" % x for x in pg["excluded"]),
               "".join("<h3>%d. %s</h3><p>%s</p>" % (i + 1, t, b)
                       for i, (t, b) in enumerate(pg["process"])),
               "".join("<h3>%s</h3><p>%s</p>" % (t, b) for t, b in pg["price_factors"]),
               pg["areas_intro"],
               "".join("<li>%s</li>" % a for a in AREAS_ISB),
               "".join("<li>%s</li>" % a for a in AREAS_RWP),
               "".join('<details%s><summary>%s</summary><div class="cc-faq__a">%s</div></details>'
                       % (" open" if i == 0 else "", q, a)
                       for i, (q, a) in enumerate(pg["faqs"])),
               pg["closing_h2"], "".join("<p>%s</p>" % x for x in pg["closing"]),
               walink, walink, PHONE_TEL, PHONE_DISPLAY,
               "".join('<a class="cc-related-card" href="%s.html"><strong>%s</strong>'
                       '<span>%s</span></a>' % (r["slug"], r["name"], r["card"])
                       for r in related(slug, 4))))
        html = page(1, pg["title"], pg["meta"], "services/" + slug,
                    pg["h1"], pg["hero_p"], body, svc["img"],
                    service_schema(slug, pg, svc))
        write(os.path.join(out, slug + ".html"), html)
    print("  %d service pages built" % len(PAGES))


def build_simple_pages():
    # services index
    body = ('<section class="cc-body pb-0"><div class="container"></div></section>'
            + services_grid(0) + areas_strip())
    write(os.path.join(SITE, "services.html"),
          page(0, "All Cleaning Services in Islamabad & Rawalpindi | " + BRAND,
               "All 15 cleaning services we provide in Islamabad and Rawalpindi — deep "
               "cleaning, post-construction, sofa, carpet, marble, tile, window, solar "
               "panel and janitorial. Free inspection and fixed price.",
               "services", "Our cleaning services",
               "Fifteen services across Islamabad and Rawalpindi. Free inspection, one "
               "fixed price, available 24/7.", body, "deep-cleaning.jpg"))

    # about + contact reuse the copy already written for the main site
    import build_pages as BP
    for name, title, desc, h1, lead, bodysrc in (
        ("about", "About %s | Cleaning Company in Islamabad & Rawalpindi" % BRAND,
         "About CleanCrew — a cleaning company working across Islamabad and Rawalpindi "
         "for eight years. Our own staff, our own equipment, free inspection and one "
         "fixed price. Open 24/7.",
         "About " + BRAND,
         "Eight years cleaning homes, offices and new builds across Islamabad and "
         "Rawalpindi.", BP.ABOUT_BODY),
        ("contact", "Contact %s | Cleaning Services Islamabad & Rawalpindi" % BRAND,
         "Contact CleanCrew for cleaning in Islamabad and Rawalpindi. WhatsApp or call "
         "0330 2935777, open 24 hours a day. Free inspection and a fixed price.",
         "Contact us",
         "WhatsApp or call 0330 2935777 — any hour, any day.", BP.CONTACT_BODY),
    ):
        b = (bodysrc.replace("svcbody", "cc-body").replace("cc-aside-fact", "cc-fact")
             .replace("cc-panel", "cc-panel"))
        write(os.path.join(SITE, name + ".html"),
              page(0, title, desc, name, h1, lead, b, "deep-cleaning.jpg"))
    print("  services.html, about.html, contact.html built")


def copy_assets():
    src_img = os.path.join(SRC, "images", "services")
    dst_img = os.path.join(SITE, "images", "services")
    os.makedirs(os.path.join(dst_img, "thumb"), exist_ok=True)
    n = 0
    for f in os.listdir(src_img):
        if f.lower().endswith((".jpg", ".jpeg", ".png")):
            shutil.copy2(os.path.join(src_img, f), os.path.join(dst_img, f)); n += 1
    for f in os.listdir(os.path.join(src_img, "thumb")):
        shutil.copy2(os.path.join(src_img, "thumb", f),
                     os.path.join(dst_img, "thumb", f)); n += 1
    dst_av = os.path.join(SITE, "images", "avatar")
    os.makedirs(dst_av, exist_ok=True)
    for f in os.listdir(os.path.join(SRC, "images", "avatar")):
        shutil.copy2(os.path.join(SRC, "images", "avatar", f), os.path.join(dst_av, f)); n += 1
    for f in ("favicon.ico", "apple-touch-icon.png"):
        p = os.path.join(SRC, f)
        if os.path.exists(p):
            shutil.copy2(p, os.path.join(SITE, f))
    print("  %d image assets copied" % n)


def build_meta_files():
    write(os.path.join(SITE, "robots.txt"),
          "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE_URL)
    import datetime
    today = datetime.date.today().isoformat()
    urls = [("/", 1.0), ("/services", .9), ("/about", .6), ("/contact", .7)]
    urls += [("/services/" + s["slug"], .8) for s in SERVICES]
    x = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    x += ['  <url><loc>%s%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>'
          % (SITE_URL, u, today, p) for u, p in urls]
    x.append("</urlset>")
    write(os.path.join(SITE, "sitemap.xml"), "\n".join(x) + "\n")
    write(os.path.join(SITE, "vercel.json"), json.dumps({
        "$schema": "https://openapi.vercel.sh/vercel.json",
        "cleanUrls": True, "trailingSlash": False,
        "headers": [
            {"source": "/(.*)", "headers": [
                {"key": "X-Content-Type-Options", "value": "nosniff"},
                {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"}]},
            {"source": "/(.*)\\.(jpg|jpeg|png|webp|svg|ico|woff2?)", "headers": [
                {"key": "Cache-Control", "value": "public, max-age=86400, must-revalidate"}]},
        ]}, indent=2) + "\n")
    print("  robots.txt, sitemap.xml, vercel.json written")


if __name__ == "__main__":
    copy_assets()
    build_index()
    build_service_pages()
    build_simple_pages()
    build_meta_files()
    print("SuperClean variant built.")
