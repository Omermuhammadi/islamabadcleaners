"""IslamabadCleaners site generator.

Reads _site.py (config), _services.py (catalogue), _service_pages.py (+_pages_new.py)
and writes every page in docs/, plus sitemap.xml and robots.txt.

Usage:  python build.py
"""

import json
import os
import urllib.parse

import _site as S
from _services import SERVICES, BY_SLUG, related
from _service_pages import PAGES, AREAS_ISB, AREAS_RWP
import _content as C

try:
    from _pages_new import PAGES as _NEW
    PAGES.update(_NEW)
except ImportError:
    pass
try:
    from _pages_more import PAGES as _MORE
    PAGES.update(_MORE)
except ImportError:
    pass

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")
LASTMOD = "2026-08-07"


def wa_url(text):
    return f"https://wa.me/{S.WHATSAPP}?text={urllib.parse.quote(text)}"


def wa_for(service_name):
    return wa_url(f"Hi IslamabadCleaners, I'd like a quote for {service_name} in Islamabad / Rawalpindi.")


WA_GENERIC_URL = wa_url(S.WA_GENERIC)

# Handcrafted meta descriptions, <=160 chars (the long-form dict metas exceed
# Google's snippet length; these override them for the meta/og tags).
META = {
    "deep-cleaning": "Professional deep cleaning for homes & offices in Islamabad & Rawalpindi. Fixed WhatsApp quote, one price, open 24/7. WhatsApp 0330 2935777.",
    "post-construction-cleaning": "Post-construction cleaning in Islamabad & Rawalpindi — cement dust, paint spots & debris cleared for handover. Fixed WhatsApp quote. 0330 2935777.",
    "post-renovation-cleaning": "Post-renovation cleaning in Islamabad & Rawalpindi — fine dust and residue removed after remodelling. Fixed quote, 24/7. WhatsApp 0330 2935777.",
    "move-in-cleaning": "Move-in cleaning in Islamabad & Rawalpindi — the empty house cleaned properly before you unpack. Fixed price on WhatsApp. 0330 2935777.",
    "move-out-cleaning": "Move-out & end-of-tenancy cleaning in Islamabad & Rawalpindi, done to handover standard. Fixed written quote, 24/7. WhatsApp 0330 2935777.",
    "sofa-cleaning": "Sofa cleaning at home in Islamabad & Rawalpindi — shampoo & hot-water extraction for sofas, armchairs & dining chairs. WhatsApp 0330 2935777.",
    "carpet-cleaning": "Carpet cleaning in Islamabad & Rawalpindi — deep extraction, stain treatment and controlled drying at your home or office. WhatsApp 0330 2935777.",
    "rug-cleaning": "Rug cleaning in Islamabad & Rawalpindi — qaleen, oriental & machine-made rugs washed safely, at home or by pickup. WhatsApp 0330 2935777.",
    "mattress-cleaning": "Mattress cleaning in Islamabad & Rawalpindi — dust, allergens and stains extracted from the layers. Fixed WhatsApp quote, 24/7. 0330 2935777.",
    "office-chair-cleaning": "Office chair cleaning in Islamabad & Rawalpindi — mesh, fabric & leather chairs cleaned in batches, overnight if needed. WhatsApp 0330 2935777.",
    "marble-polishing": "Marble polishing in Islamabad & Rawalpindi — grinding, honing and polishing that restores dull floors and stairs. Fixed quote. WhatsApp 0330 2935777.",
    "tile-cleaning": "Tile & grout cleaning in Islamabad & Rawalpindi — machine cleaning for discoloured tiles mopping can't fix. Fixed WhatsApp quote. 0330 2935777.",
    "floor-care": "Floor care in Islamabad & Rawalpindi — scrubbing, buffing and sealing that keeps hard floors in condition. Fixed quote, 24/7. WhatsApp 0330 2935777.",
    "window-cleaning": "Window cleaning in Islamabad & Rawalpindi — glass, frames, tracks and sills, inside and out, streak-free. Fixed quote, 24/7. WhatsApp 0330 2935777.",
    "glass-cleaning": "Glass cleaning in Islamabad & Rawalpindi — facades, partitions, railings & shower screens, hard-water marks removed. WhatsApp 0330 2935777.",
    "solar-panel-cleaning": "Solar panel cleaning in Islamabad & Rawalpindi — safe removal of the dust layer cutting your output. Fixed WhatsApp quote, 24/7. 0330 2935777.",
    "water-tank-cleaning": "Water tank cleaning in Islamabad & Rawalpindi — overhead & underground tanks emptied, scrubbed and disinfected. Fixed quote. WhatsApp 0330 2935777.",
    "swimming-pool-cleaning": "Swimming pool cleaning in Islamabad & Rawalpindi — green-pool restoration and regular weekly service. Fixed WhatsApp quote. 0330 2935777.",
    "janitorial-services": "Janitorial services in Islamabad & Rawalpindi — trained recurring cleaning staff with supervision for offices & clinics. WhatsApp 0330 2935777.",
}

# ---------------------------------------------------------------- icons ----
def icon(name, size=20):
    paths = {
        "wa": '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.6-6.1c-.3-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1-.2.3-.6.8-.8 1-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.4-3c-.3-.4 0-.5.1-.7l.4-.5c.1-.2.1-.3 0-.5l-.8-1.9c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.5.1-.7.3-.2.3-.9.9-.9 2.2s.9 2.5 1.1 2.7a11 11 0 0 0 4.3 3.8c.6.3 1.1.4 1.4.5.6.2 1.2.2 1.6.1.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2l-.3-.4z"/>',
        "phone": '<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.6.1.3 0 .7-.2 1l-2.3 2.2z"/>',
        "check": '<path d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4L9 16.2z"/>',
        "x": '<path d="M19 6.4 17.6 5 12 10.6 6.4 5 5 6.4 10.6 12 5 17.6 6.4 19 12 13.4 17.6 19 19 17.6 13.4 12 19 6.4z"/>',
        "pin": '<path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5z"/>',
        "clock": '<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 5h-2v6l5.2 3.1 1-1.6-4.2-2.5V7z"/>',
        "mail": '<path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z"/>',
        "shield": '<path d="M12 2 4 5v6c0 5.5 3.4 10.7 8 12 4.6-1.3 8-6.5 8-12V5l-8-3zm-1 14-4-4 1.4-1.4L11 13.2l5.6-5.6L18 9l-7 7z"/>',
        "star": '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1L12 2z"/>',
    }
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="currentColor" '
            f'aria-hidden="true">{paths[name]}</svg>')


# ---------------------------------------------------------------- shell ----
NAV_JS = """<script>
(function () {
  var t = document.querySelector('.nav-toggle'), l = document.querySelector('.nav-links');
  if (!t || !l) return;
  t.addEventListener('click', function () {
    var open = l.classList.toggle('open');
    t.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
})();
</script>"""


def url(path=""):
    """Site-absolute href for a clean path ('' -> '/', 'services' -> '/services')."""
    return f"/{path}" if path else "/"


def canonical_url(path=""):
    """Absolute canonical for a clean path ('' -> BASE_URL + '/')."""
    return f"{S.BASE_URL}/{path}" if path else f"{S.BASE_URL}/"


def out_file(path=""):
    """Where a clean path is written on disk ('services' -> 'services/index.html')."""
    return f"{path}/index.html" if path else "index.html"


def head(title, meta, path, og_image, schema=None):
    """path = clean canonical path, e.g. '' | 'services' | 'services/sofa-cleaning'."""
    canonical = canonical_url(path)
    og_img_url = f"{S.BASE_URL}/{og_image}"
    schema_tag = ""
    if schema:
        schema_tag = ('\n<script type="application/ld+json">'
                      + json.dumps(schema, ensure_ascii=False, separators=(",", ":"))
                      + "</script>")
    return f"""<!DOCTYPE html>
<html lang="en-PK">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{meta}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{S.BRAND}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_img_url}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{meta}">
<meta name="twitter:image" content="{og_img_url}">
<meta name="theme-color" content="#0A2126">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/fonts/fraunces-v38-latin-600.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/figtree-v9-latin-regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/main.css">{schema_tag}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


def nav(current=""):
    def cur(k):
        return ' aria-current="page"' if current == k else ""
    return f"""<header class="site-header">
<div class="wrap nav">
<a class="brand" href="/"><img src="/images/bubbles.png" alt="" width="34" height="34">{S.BRAND}</a>
<button class="nav-toggle" aria-expanded="false" aria-label="Menu">
<svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"/></svg>
</button>
<ul class="nav-links">
<li><a href="/"{cur('home')}>Home</a></li>
<li><a href="/services"{cur('services')}>Services</a></li>
<li><a href="/about"{cur('about')}>About</a></li>
<li><a href="/contact"{cur('contact')}>Contact</a></li>
<li><a class="nav-phone" href="tel:{S.PHONE_TEL}">{S.PHONE_DISPLAY}</a></li>
<li class="nav-cta"><a class="btn btn-wa" href="{WA_GENERIC_URL}" target="_blank" rel="noopener">{icon('wa', 18)} Get a free quote</a></li>
</ul>
</div>
</header>
"""


def footer():
    half = (len(SERVICES) + 1) // 2
    col1 = "\n".join(
        f'<li><a href="/services/{s["slug"]}">{s["name"]}</a></li>' for s in SERVICES[:half])
    col2 = "\n".join(
        f'<li><a href="/services/{s["slug"]}">{s["name"]}</a></li>' for s in SERVICES[half:])
    return f"""<footer class="site-footer">
<div class="wrap">
<div class="footer-grid">
<div>
<p class="footer-brand"><img src="/images/bubbles.png" alt="" width="30" height="30">{S.BRAND}</p>
<p>Professional cleaning services across Islamabad &amp; Rawalpindi. Fixed written quotes on WhatsApp, available 24/7.</p>
<ul class="footer-contact" style="margin-top:16px">
<li>{icon('phone', 16)}<a href="tel:{S.PHONE_TEL}">{S.PHONE_DISPLAY}</a></li>
<li>{icon('wa', 16)}<a href="{WA_GENERIC_URL}" target="_blank" rel="noopener">WhatsApp us</a></li>
<li>{icon('mail', 16)}<a href="mailto:{S.EMAIL}">{S.EMAIL}</a></li>
<li>{icon('clock', 16)}<span>Open 24 hours, 7 days a week</span></li>
<li>{icon('pin', 16)}<span>Islamabad &amp; Rawalpindi, Pakistan</span></li>
</ul>
</div>
<div><p class="footer-title">Services</p><ul>{col1}</ul></div>
<div><p class="footer-title">More services</p><ul>{col2}</ul></div>
<div><p class="footer-title">Company</p><ul>
<li><a href="/">Home</a></li>
<li><a href="/services">All services</a></li>
<li><a href="/about">About us</a></li>
<li><a href="/contact">Contact</a></li>
</ul></div>
</div>
<div class="footer-bottom">
<p>&copy; {S.BRAND} &mdash; cleaning services in Islamabad &amp; Rawalpindi.</p>
<p><a href="tel:{S.PHONE_TEL}">{S.PHONE_DISPLAY}</a></p>
</div>
</div>
</footer>
"""


def float_ctas(wa_link_url):
    return f"""<a class="float-wa" href="{wa_link_url}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{icon('wa', 28)}</a>
<nav class="mobile-bar" aria-label="Quick contact">
<a class="bar-wa" href="{wa_link_url}" target="_blank" rel="noopener">{icon('wa', 20)} WhatsApp</a>
<a class="bar-call" href="tel:{S.PHONE_TEL}">{icon('phone', 18)} Call now</a>
</nav>
"""


def close(wa_link_url):
    return float_ctas(wa_link_url) + NAV_JS + "\n</body>\n</html>\n"


# ------------------------------------------------------------- schema ------
def org_node():
    return {
        "@type": "LocalBusiness",
        "@id": f"{S.BASE_URL}/#organization",
        "name": S.BRAND,
        "url": f"{S.BASE_URL}/",
        "image": f"{S.BASE_URL}/images/og/default.jpg",
        "logo": f"{S.BASE_URL}/images/bubbles.png",
        "telephone": S.PHONE_TEL,
        "email": S.EMAIL,
        "priceRange": "$$",
        "areaServed": [
            {"@type": "City", "name": "Islamabad"},
            {"@type": "City", "name": "Rawalpindi"},
        ],
        "address": {"@type": "PostalAddress", "addressLocality": "Islamabad",
                    "addressCountry": "PK"},
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                          "Saturday", "Sunday"],
            "opens": "00:00", "closes": "23:59",
        }],
        "sameAs": [f"https://wa.me/{S.WHATSAPP}"],
    }


def faq_nodes(faqs):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }


def crumbs_node(items):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": url}
            for i, (name, url) in enumerate(items)
        ],
    }


# ------------------------------------------------------- page sections -----
def service_card(s):
    return f"""<a class="card" href="/services/{s['slug']}">
<img src="/images/services/{s['slug']}-card.webp" alt="{s['name']} in Islamabad and Rawalpindi" width="480" height="320" loading="lazy" decoding="async">
<div class="card-body">
<h3>{s['name']}</h3>
<p>{s['card']}</p>
<span class="card-more">Details &rarr;</span>
</div>
</a>"""


def areas_section():
    isb = "\n".join(f"<li>{a}</li>" for a in AREAS_ISB)
    rwp = "\n".join(f"<li>{a}</li>" for a in AREAS_RWP)
    return f"""<section class="section section-ink on-ink">
<div class="wrap">
<div class="section-head">
<p class="eyebrow">Where we work</p>
<h2>Covering the twin cities, sector by sector</h2>
<p>If your area isn&rsquo;t listed, message us anyway &mdash; we&rsquo;ll tell you straight away whether we can reach you.</p>
</div>
<div class="areas-cols">
<div><h3>Islamabad</h3><ul class="areas-list">{isb}</ul></div>
<div><h3>Rawalpindi</h3><ul class="areas-list">{rwp}</ul></div>
</div>
</div>
</section>
"""


def cta_band(h2, para, wa_link_url):
    return f"""<section class="section cta-band">
<div class="wrap">
<h2>{h2}</h2>
<p class="lead">{para}</p>
<div class="cta-row">
<a class="btn btn-wa" href="{wa_link_url}" target="_blank" rel="noopener">{icon('wa')} WhatsApp {S.PHONE_DISPLAY}</a>
<a class="btn btn-ghost" href="tel:{S.PHONE_TEL}">{icon('phone', 18)} Call us</a>
</div>
<p class="cta-trust">{S.CTA_TRUST}</p>
</div>
</section>
"""


def reviews_section():
    stars = "".join(icon("star", 16) for _ in range(5))
    cards = "\n".join(
        f"""<div class="review-card">
<p class="stars" aria-label="5 out of 5 stars">{stars}</p>
<p class="review-text">&ldquo;{text}&rdquo;</p>
<p class="review-who">{name} &middot; {area}</p>
</div>"""
        for name, area, text in C.TESTIMONIALS)
    return f"""<section class="section">
<div class="wrap">
<div class="section-head">
<p class="eyebrow">What customers say</p>
<h2>Word travels fast in the twin cities</h2>
</div>
<div class="review-grid">{cards}</div>
</div>
</section>
"""


def promise_section():
    icons = ["shield", "check", "wa"]
    cards = "\n".join(
        f"""<div class="promise-card">{icon(icons[i], 26)}<h3>{t}</h3><p>{d}</p></div>"""
        for i, (t, d) in enumerate(S.PROMISE))
    return f"""<section class="section section-mist">
<div class="wrap">
<div class="section-head">
<p class="eyebrow">The IslamabadCleaners promise</p>
<h2>No scripts, no surprises</h2>
</div>
<div class="promise-grid">{cards}</div>
</div>
</section>
"""


# ---------------------------------------------------------------- pages ----
def build_home():
    featured = [BY_SLUG[slug] for slug in S.HOME_FEATURED]
    cards = "\n".join(service_card(s) for s in featured)
    steps = "\n".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in S.STEPS)
    faqs_html = "\n".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in C.FAQS)

    schema = {"@context": "https://schema.org", "@graph": [
        org_node(),
        {"@type": "WebSite", "@id": f"{S.BASE_URL}/#website",
         "url": f"{S.BASE_URL}/", "name": S.BRAND,
         "publisher": {"@id": f"{S.BASE_URL}/#organization"}},
        faq_nodes(C.FAQS),
    ]}

    title = "Cleaning Services in Islamabad & Rawalpindi | IslamabadCleaners"
    meta = ("Professional cleaning services in Islamabad & Rawalpindi — deep cleaning, "
            "sofa, carpet, water tank, solar panels & more. Open 24/7. WhatsApp 0330 2935777.")

    html = head(title, meta, "", "images/og/default.jpg", schema)
    html += nav("home")
    html += f"""<main id="main">
<section class="hero on-ink">
<div class="wrap">
<div>
<p class="eyebrow">Islamabad &amp; Rawalpindi &middot; Open 24/7</p>
<h1>Professional cleaning services in Islamabad &amp; Rawalpindi</h1>
<p class="lead">Sofas, carpets, deep cleans, water tanks, solar panels and more &mdash; done properly by an equipped crew, quoted in writing on WhatsApp &mdash; the price we give is the price you pay.</p>
<div class="cta-row">
<a class="btn btn-wa" href="{WA_GENERIC_URL}" target="_blank" rel="noopener">{icon('wa')} WhatsApp {S.PHONE_DISPLAY}</a>
<a class="btn btn-ghost" href="tel:{S.PHONE_TEL}">{icon('phone', 18)} Call us</a>
</div>
<p class="cta-trust">{S.CTA_TRUST}</p>
<ul class="trust-row">
<li>{icon('check', 18)} 10+ years in the twin cities</li>
<li>{icon('check', 18)} Available 24/7</li>
<li>{icon('check', 18)} We bring all equipment</li>
</ul>
</div>
<figure class="arch">
<img src="/images/hero-crew.webp" alt="IslamabadCleaners cleaners vacuuming and mopping a living room in Islamabad" width="900" height="1125" fetchpriority="high" decoding="async">
</figure>
</div>
</section>

<section class="section section-mist" id="services">
<div class="wrap">
<div class="section-head">
<p class="eyebrow">What we clean</p>
<h2>One crew for every cleaning job in the twin cities</h2>
<p>From a single sofa to a full post-construction handover &mdash; each service has its own machines, method and page.</p>
</div>
<div class="card-grid">{cards}</div>
<p class="grid-foot"><a class="btn btn-ink" href="/services">See all {len(SERVICES)} services</a></p>
</div>
</section>

<section class="section">
<div class="wrap">
<div class="section-head">
<p class="eyebrow">How it works</p>
<h2>From message to spotless in three steps</h2>
</div>
<ol class="steps">{steps}</ol>
</div>
</section>

{promise_section()}

{reviews_section()}

<section class="section section-mist">
<div class="wrap">
<div class="section-head">
<p class="eyebrow">Common questions</p>
<h2>Before you message us</h2>
</div>
<div class="faq">{faqs_html}</div>
</div>
</section>

{areas_section()}

{cta_band("Get your free quote today",
          "Tell us the job on WhatsApp — we usually reply within minutes, any hour of the day.",
          WA_GENERIC_URL)}
</main>
"""
    html += footer() + close(WA_GENERIC_URL)
    write(out_file(""), html)


def build_services_index():
    cards = "\n".join(service_card(s) for s in SERVICES)
    schema = {"@context": "https://schema.org", "@graph": [
        org_node(),
        crumbs_node([("Home", canonical_url()),
                     ("Services", canonical_url("services"))]),
    ]}
    title = "All Cleaning Services in Islamabad & Rawalpindi | IslamabadCleaners"
    meta = (f"All {len(SERVICES)} IslamabadCleaners services across Islamabad & Rawalpindi — from "
            "sofa and carpet to water tanks and solar panels. WhatsApp 0330 2935777.")
    html = head(title, meta, "services", "images/og/default.jpg", schema)
    html += nav("services")
    html += f"""<main id="main">
<section class="page-hero on-ink">
<div class="wrap">
<div>
<ol class="crumbs"><li><a href="/">Home</a></li><li aria-current="page">Services</li></ol>
<h1>Every cleaning service we offer</h1>
<p class="lead">{len(SERVICES)} services, one standard: a fixed written quote on WhatsApp, one price, and a walkthrough before we leave.</p>
<div class="cta-row">
<a class="btn btn-wa" href="{WA_GENERIC_URL}" target="_blank" rel="noopener">{icon('wa')} Get a free quote</a>
</div>
<p class="cta-trust">{S.CTA_TRUST}</p>
</div>
<figure class="arch">
<img src="/images/about-team.webp" alt="IslamabadCleaners professional cleaning team at work" width="720" height="720" loading="lazy" decoding="async">
</figure>
</div>
</section>
<section class="section">
<div class="wrap">
<div class="section-head">
<p class="eyebrow">The full list</p>
<h2>Pick the job &mdash; each page explains it honestly</h2>
</div>
<div class="card-grid">{cards}</div>
</div>
</section>
{areas_section()}
{cta_band("Not sure which service you need?",
          "Describe the problem on WhatsApp and we'll tell you exactly what it needs — honestly.",
          WA_GENERIC_URL)}
</main>
"""
    html += footer() + close(WA_GENERIC_URL)
    write(out_file("services"), html)


def build_service_page(slug):
    s = BY_SLUG[slug]
    d = dict(PAGES[slug])
    d["meta"] = META.get(slug, d["meta"])
    wa_link_url = wa_for(s["name"])
    path = f"services/{slug}"
    canonical = canonical_url(path)

    intro = "\n".join(f"<p>{para}</p>" for para in d["intro"])
    included = "\n".join(f"<li>{icon('check', 18)}<span>{i}</span></li>" for i in d["included"])
    excluded = "\n".join(f"<li>{icon('x', 18)}<span>{i}</span></li>" for i in d["excluded"])
    process = "\n".join(f"<li><div><h3>{t}</h3><p>{x}</p></div></li>" for t, x in d["process"])
    factors = "\n".join(f"<li><h3>{t}</h3><p>{x}</p></li>" for t, x in d["price_factors"])
    faqs_html = "\n".join(f"<details><summary>{q}</summary><p>{a}</p></details>"
                          for q, a in d["faqs"])
    areas = "\n".join(f"<li>{a}</li>" for a in AREAS_ISB + AREAS_RWP)
    closing = "\n".join(f"<p>{para}</p>" for para in d["closing"])
    rel_cards = "\n".join(service_card(r) for r in related(slug))

    schema = {"@context": "https://schema.org", "@graph": [
        org_node(),
        {"@type": "Service", "@id": f"{canonical}#service",
         "name": s["name"], "serviceType": s["name"],
         "description": d["meta"], "url": canonical,
         "provider": {"@id": f"{S.BASE_URL}/#organization"},
         "areaServed": [{"@type": "City", "name": "Islamabad"},
                        {"@type": "City", "name": "Rawalpindi"}]},
        crumbs_node([("Home", canonical_url()),
                     ("Services", canonical_url("services")),
                     (s["name"], canonical)]),
        faq_nodes(d["faqs"]),
    ]}

    title = f"{s['name']} in Islamabad & Rawalpindi | IslamabadCleaners"
    html = head(title, d["meta"], path, f"images/og/{slug}.jpg", schema)
    html += nav("services")
    html += f"""<main id="main">
<section class="page-hero on-ink">
<div class="wrap">
<div>
<ol class="crumbs">
<li><a href="/">Home</a></li>
<li><a href="/services">Services</a></li>
<li aria-current="page">{s['name']}</li>
</ol>
<h1>{d['h1']}</h1>
<p class="lead">{d['hero_p']}</p>
<div class="cta-row">
<a class="btn btn-wa" href="{wa_link_url}" target="_blank" rel="noopener">{icon('wa')} WhatsApp {S.PHONE_DISPLAY}</a>
<a class="btn btn-ghost" href="tel:{S.PHONE_TEL}">{icon('phone', 18)} Call us</a>
</div>
<p class="cta-trust">{S.CTA_TRUST}</p>
</div>
<figure class="arch">
<img src="/images/services/{slug}-hero.webp" alt="{s['name']} in Islamabad and Rawalpindi" width="720" height="720" fetchpriority="high" decoding="async">
</figure>
</div>
</section>

<div class="wrap article-layout">
<article class="article">
<h2>{d['h2_intro']}</h2>
{intro}
<h2>{d['h2_included']}</h2>
<p>{d['included_intro']}</p>
<ul class="checklist">{included}</ul>
<div class="article-cta">
<p>Want this done at your place? Send us the details on WhatsApp &mdash; fixed quote in minutes.</p>
<a class="btn btn-wa" href="{wa_link_url}" target="_blank" rel="noopener">{icon('wa')} Get a free quote</a>
</div>
<h2>What this service does not include</h2>
<ul class="exclist">{excluded}</ul>
<h2>How it works</h2>
<ol class="process">{process}</ol>
<h2>What affects the price</h2>
<ul class="factors">{factors}</ul>
<h2>Frequently asked questions</h2>
<div class="faq">{faqs_html}</div>
<h2>Areas we cover</h2>
<p>{d['areas_intro']}</p>
<ul class="areas-inline">{areas}</ul>
<h2>{d['closing_h2']}</h2>
{closing}
<div class="cta-row" style="margin-top:24px">
<a class="btn btn-wa" href="{wa_link_url}" target="_blank" rel="noopener">{icon('wa')} WhatsApp {S.PHONE_DISPLAY}</a>
<a class="btn btn-ghost" href="tel:{S.PHONE_TEL}">{icon('phone', 18)} Call us</a>
</div>
<p class="cta-trust">{S.CTA_TRUST}</p>
</article>
<aside>
<div class="aside-box on-ink">
<h2>Get a fixed quote</h2>
<p>Send your area, the size of the job and a photo or two &mdash; you get one fixed price in writing.</p>
<a class="btn btn-wa" href="{wa_link_url}" target="_blank" rel="noopener">{icon('wa')} WhatsApp us</a>
<a class="btn btn-ghost" href="tel:{S.PHONE_TEL}">{icon('phone', 18)} Call now</a>
<a class="aside-phone" href="tel:{S.PHONE_TEL}">{S.PHONE_DISPLAY}</a>
<p class="cta-trust">{S.CTA_TRUST}</p>
</div>
</aside>
</div>

<section class="related">
<div class="wrap">
<div class="section-head">
<p class="eyebrow">Related services</p>
<h2>You might also need</h2>
</div>
<div class="card-grid">{rel_cards}</div>
</div>
</section>
</main>
"""
    html += footer() + close(wa_link_url)
    write(out_file(path), html)


def build_about():
    body = "\n".join(f"<p>{para}</p>" for para in C.ABOUT_BODY)
    features = "\n".join(
        f"""<div class="promise-card">{icon('check', 26)}<h3>{t}</h3><p>{d}</p></div>"""
        for t, d in C.FEATURES)
    schema = {"@context": "https://schema.org", "@graph": [
        org_node(),
        crumbs_node([("Home", canonical_url()),
                     ("About", canonical_url("about"))]),
    ]}
    title = "About IslamabadCleaners | Cleaning Company in Islamabad & Rawalpindi"
    meta = ("IslamabadCleaners is a cleaning company serving Islamabad & Rawalpindi 24/7 — own "
            "equipment, fixed written quotes on WhatsApp. 0330 2935777.")
    html = head(title, meta, "about", "images/og/default.jpg", schema)
    html += nav("about")
    html += f"""<main id="main">
<section class="page-hero on-ink">
<div class="wrap">
<div>
<ol class="crumbs"><li><a href="/">Home</a></li><li aria-current="page">About</li></ol>
<h1>A cleaning company that quotes honestly and shows up</h1>
<p class="lead">Based in Islamabad, working across both twin cities &mdash; one-off deep cleans, furniture and floors, and regular contracts for offices and clinics.</p>
<div class="cta-row">
<a class="btn btn-wa" href="{WA_GENERIC_URL}" target="_blank" rel="noopener">{icon('wa')} WhatsApp {S.PHONE_DISPLAY}</a>
</div>
<p class="cta-trust">{S.CTA_TRUST}</p>
</div>
<figure class="arch">
<img src="/images/about-team.webp" alt="IslamabadCleaners cleaning team with professional equipment" width="720" height="720" fetchpriority="high" decoding="async">
</figure>
</div>
</section>
<div class="wrap article-layout">
<article class="article">
<h2>Who we are</h2>
{body}
<h2>How we work</h2>
<p>Every job &mdash; from one office chair to a full post-construction handover &mdash; runs the same way: you message us, you send photos, you get one fixed price in writing on WhatsApp, the crew arrives with everything it needs, and you walk through the finished work with the supervisor before we leave.</p>
<h2>What we will tell you honestly</h2>
<p>If a stain will not come out fully, we say so before we start. If a job does not need the expensive service, we tell you the cheaper one is enough. And if something is outside what we do &mdash; plumbing, pest control, repairs &mdash; we say that too, instead of doing it badly.</p>
</article>
<aside>
<div class="aside-box on-ink">
<h2>Talk to us</h2>
<p>Fastest on WhatsApp &mdash; we reply within minutes, day or night.</p>
<a class="btn btn-wa" href="{WA_GENERIC_URL}" target="_blank" rel="noopener">{icon('wa')} WhatsApp us</a>
<a class="btn btn-ghost" href="tel:{S.PHONE_TEL}">{icon('phone', 18)} Call now</a>
<a class="aside-phone" href="tel:{S.PHONE_TEL}">{S.PHONE_DISPLAY}</a>
<p class="cta-trust">{S.CTA_TRUST}</p>
</div>
</aside>
</div>
<section class="section section-mist">
<div class="wrap">
<div class="section-head">
<p class="eyebrow">Why people call us back</p>
<h2>Three things we never skip</h2>
</div>
<div class="promise-grid">{features}</div>
</div>
</section>
{areas_section()}
{cta_band("Ready when you are", "Message us the job — we'll take it from there.", WA_GENERIC_URL)}
</main>
"""
    html += footer() + close(WA_GENERIC_URL)
    write(out_file("about"), html)


def build_contact():
    faqs = C.FAQS[:5]
    faqs_html = "\n".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    schema = {"@context": "https://schema.org", "@graph": [
        org_node(),
        crumbs_node([("Home", canonical_url()),
                     ("Contact", canonical_url("contact"))]),
        faq_nodes(faqs),
    ]}
    title = "Contact IslamabadCleaners | WhatsApp 0330 2935777 | Islamabad & Rawalpindi"
    meta = ("Contact IslamabadCleaners for cleaning in Islamabad and Rawalpindi. WhatsApp or "
            "call 0330 2935777 — replies in minutes, fixed quotes on WhatsApp, open 24/7.")
    html = head(title, meta, "contact", "images/og/default.jpg", schema)
    html += nav("contact")
    html += f"""<main id="main">
<section class="page-hero on-ink">
<div class="wrap">
<div>
<ol class="crumbs"><li><a href="/">Home</a></li><li aria-current="page">Contact</li></ol>
<h1>Message us &mdash; we reply in minutes</h1>
<p class="lead">WhatsApp is fastest. Tell us the service you need, your area, and roughly how big the job is. We are open 24 hours, every day.</p>
<div class="cta-row">
<a class="btn btn-wa" href="{WA_GENERIC_URL}" target="_blank" rel="noopener">{icon('wa')} WhatsApp {S.PHONE_DISPLAY}</a>
<a class="btn btn-ghost" href="tel:{S.PHONE_TEL}">{icon('phone', 18)} Call {S.PHONE_DISPLAY}</a>
</div>
<p class="cta-trust">{S.CTA_TRUST}</p>
</div>
<figure class="arch">
<img src="/images/hero-home.webp" alt="IslamabadCleaners technician cleaning a sofa" width="900" height="1125" fetchpriority="high" decoding="async">
</figure>
</div>
</section>
<div class="wrap article-layout">
<article class="article">
<h2>What to tell us when you message</h2>
<p>Three things get you an accurate answer fastest:</p>
<ul class="checklist">
<li>{icon('check', 18)}<span><strong>The service</strong> &mdash; e.g. sofa cleaning, deep clean, water tank, solar panels</span></li>
<li>{icon('check', 18)}<span><strong>Your area</strong> &mdash; sector or society, so we can slot you into a route</span></li>
<li>{icon('check', 18)}<span><strong>The size</strong> &mdash; marla/kanal for property jobs, or a count for items like sofas and chairs. Photos help.</span></li>
</ul>
<h2>Commercial and contract enquiries</h2>
<p>For offices, clinics, restaurants and housing societies we handle recurring janitorial contracts as well as one-off jobs. Message us with the site address and what you need covered, and we will arrange a visit and a written monthly quote.</p>
<h2>Common questions</h2>
<div class="faq">{faqs_html}</div>
</article>
<aside>
<div class="aside-box on-ink">
<h2>Contact details</h2>
<p>Phone &amp; WhatsApp, any hour:</p>
<a class="btn btn-wa" href="{WA_GENERIC_URL}" target="_blank" rel="noopener">{icon('wa')} WhatsApp us</a>
<a class="btn btn-ghost" href="tel:{S.PHONE_TEL}">{icon('phone', 18)} Call now</a>
<a class="aside-phone" href="tel:{S.PHONE_TEL}">{S.PHONE_DISPLAY}</a>
<p class="cta-trust">Email: <a href="mailto:{S.EMAIL}" style="color:#fff">{S.EMAIL}</a></p>
</div>
</aside>
</div>
{areas_section()}
</main>
"""
    html += footer() + close(WA_GENERIC_URL)
    write(out_file("contact"), html)


def build_404():
    title = "Page not found | IslamabadCleaners"
    meta = "That page does not exist. Browse IslamabadCleaners' cleaning services for Islamabad and Rawalpindi."
    html = head(title, meta, "404", "images/og/default.jpg")
    # 404s must not be indexed
    html = html.replace('content="index, follow, max-image-preview:large"',
                        'content="noindex, follow"')
    html += nav()
    html += f"""<main id="main">
<div class="wrap page-404">
<p class="display">404</p>
<h1>That page has been cleaned away</h1>
<p>The link is broken or the page has moved. Everything we offer is one click away.</p>
<div class="cta-row" style="justify-content:center">
<a class="btn btn-ink" href="/">Go to homepage</a>
<a class="btn btn-wa" href="{WA_GENERIC_URL}" target="_blank" rel="noopener">{icon('wa')} WhatsApp us</a>
</div>
</div>
</main>
"""
    html += footer() + close(WA_GENERIC_URL)
    # 404.html stays a real file at the root — the host serves it for any miss.
    write("404.html", html)


# ------------------------------------------------------------- routing -----
def clean_paths():
    """Every indexable page, as a clean path ('' = homepage)."""
    return ["", "services", "about", "contact"] + [f"services/{s['slug']}" for s in SERVICES]


def build_vercel_json():
    """Redirect every legacy .html URL to its clean equivalent (permanent, 308).

    Written to both the repo root and docs/ so it applies whether the Vercel
    project's root directory is the repo or the docs/ output folder.
    """
    config = {
        "cleanUrls": True,
        "trailingSlash": False,
        "redirects": [
            {"source": f"/{path}.html", "destination": url(path), "permanent": True}
            for path in clean_paths() if path
        ] + [{"source": "/index.html", "destination": "/", "permanent": True}],
    }
    body = json.dumps(config, indent=2) + "\n"
    for target in (os.path.join(ROOT, "vercel.json"), os.path.join(DOCS, "vercel.json")):
        with open(target, "w", encoding="utf-8", newline="\n") as f:
            f.write(body)


# ---------------------------------------------------- sitemap & robots -----
def build_sitemap():
    urls = "\n".join(
        f"<url><loc>{canonical_url(p)}</loc><lastmod>{LASTMOD}</lastmod></url>"
        for p in clean_paths())
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{urls}\n</urlset>\n")
    with open(os.path.join(DOCS, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    with open(os.path.join(DOCS, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {S.BASE_URL}/sitemap.xml\n")


WRITTEN = set()


def write(rel, html):
    path = os.path.join(DOCS, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    WRITTEN.add(os.path.normpath(path))


def prune():
    """Delete .html files left over from a previous layout, and empty dirs."""
    for dirpath, _, files in os.walk(DOCS):
        for f in files:
            if not f.endswith(".html"):
                continue
            full = os.path.normpath(os.path.join(dirpath, f))
            if full not in WRITTEN:
                os.remove(full)
                print(f"  pruned stale page: {os.path.relpath(full, DOCS)}")
    for dirpath, dirnames, files in os.walk(DOCS, topdown=False):
        if dirpath != DOCS and not dirnames and not files:
            os.rmdir(dirpath)


def main():
    build_home()
    build_services_index()
    for s in SERVICES:
        if s["slug"] not in PAGES:
            raise SystemExit(f"ERROR: no page content for {s['slug']}")
        build_service_page(s["slug"])
    build_about()
    build_contact()
    build_404()
    prune()
    build_sitemap()
    build_vercel_json()
    print(f"Built {4 + len(SERVICES) + 1} pages + sitemap + robots + vercel.json into docs/")


if __name__ == "__main__":
    main()
