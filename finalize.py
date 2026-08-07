"""Final pass over option-a: nav, footer, testimonials, areas strip, CTAs.

Idempotent — safe to re-run. Run order:
    apply_content.py -> build_services.py -> build_service_page.py
    -> finalize.py -> fix_a11y.py
"""
import io
import os
import re
from urllib.parse import quote

from bs4 import BeautifulSoup

from _services import SERVICES

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")

BRAND = "CleanCrew"
PHONE_DISPLAY = "0330 2935777"
PHONE_TEL = "+923302935777"
EMAIL = "mgcleaner364@gmail.com"

# Pages the template shipped that we do not want in the live site.
DROP_PAGES = ["coming-soon.html", "services-detail.html"]

AREAS = [
    "DHA Islamabad", "Bahria Town", "Bahria Enclave", "F-6 / F-7 / F-8",
    "F-10 / F-11", "G-9 / G-10 / G-11", "E-11", "Blue Area",
    "Gulberg Greens", "PWD &amp; Media Town", "Saddar &amp; Cantt",
    "Chaklala Scheme III", "Askari", "Adiala Road",
]

# NOTE: avatar files 01, 02 and 05 are women; 03, 04 and 06 are men. Keep the
# pairing consistent with the names — a mismatched photo is the first thing that
# makes a review section look fabricated.
TESTIMONIALS = [
    ("Ali R.", "Bahria Town", "images/avatar/happy-customer-04.jpg",
     "Builders left our new house full of cement dust. They cleared all of it in a "
     "day and the price was exactly what they quoted after the visit."),
    ("Ayesha K.", "F-11, Islamabad", "images/avatar/happy-customer-05.jpg",
     "Booked a deep clean before Eid. The team came on time, brought everything with "
     "them, and the kitchen looked better than when we moved in."),
    ("Hassan M.", "DHA Phase 2", "images/avatar/happy-customer-06.jpg",
     "Two sofas and a carpet. The smell is completely gone and the colour came back. "
     "They replied on WhatsApp within a few minutes of my message."),
    ("Omer S.", "Chaklala, Rawalpindi", "images/avatar/happy-customer-03.jpg",
     "We use them for our office now. Same staff every time and the supervisor "
     "actually checks the work, which is more than the last company did."),
]


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


def wa(msg):
    return "https://wa.me/923302935777?text=" + quote(msg)


WA_GENERAL = wa("Hi %s, I'd like a quote for cleaning in Islamabad / Rawalpindi." % BRAND)


def up(depth):
    return "../" * depth


# ---------------------------------------------------------------- navigation
def build_nav(soup, depth):
    """Replace the template's Pages dropdown with a real services menu."""
    ul = soup.select_one("nav.navbar ul.navbar-nav")
    if ul is None:
        return
    u = up(depth)
    ul.clear()

    def item(label, href, extra=""):
        li = BeautifulSoup(
            '<li class="nav-item"><a class="nav-link %s" href="%s">%s</a></li>'
            % (extra, href, label), "lxml").li
        ul.append(li)

    item("Home", u + "index.html")

    # Services dropdown, built from the single source of truth
    opts = "".join(
        '<li><a class="dropdown-item" href="%sservices/%s.html">%s</a></li>'
        % (u, s["slug"], s["name"]) for s in SERVICES)
    dd = BeautifulSoup(
        '<li class="nav-item dropdown">'
        '<a class="nav-link dropdown-toggle" href="%sservices.html" '
        'id="servicesDropdown" role="button" data-bs-toggle="dropdown" '
        'aria-expanded="false">Services</a>'
        '<ul class="dropdown-menu" aria-labelledby="servicesDropdown">'
        '<li><a class="dropdown-item fw-bold" href="%sservices.html">All services</a></li>'
        '<li><hr class="dropdown-divider"></li>'
        '%s</ul></li>' % (u, u, opts), "lxml").li
    ul.append(dd)

    item("About", u + "about.html")
    item("Contact", u + "contact.html")

    # Header CTA. It lived inside this <ul> in the template, so it has to be
    # re-added after the clear() above rather than patched in place.
    cta = BeautifulSoup(
        '<li class="nav-item ms-lg-3">'
        '<a class="nav-link custom-btn custom-border-btn btn cc-nav-cta" href="%s">'
        '<i class="bi-whatsapp me-2"></i>Get a free quote</a></li>' % WA_GENERAL,
        "lxml").li
    ul.append(cta)


# ---------------------------------------------------------------- areas strip
def build_areas(soup, depth):
    sec = soup.select_one(".partners-section")
    if sec is None:
        return
    chips = "".join('<li>%s</li>' % a for a in AREAS)
    new = BeautifulSoup(
        '<section class="cc-areas-strip">'
        '<div class="container">'
        '<p class="svc__eyebrow">Where we work</p>'
        '<h2 class="svc__title">Serving Islamabad &amp; Rawalpindi</h2>'
        '<p class="svc__lead">We cover both cities in full. These are the areas we are in '
        'most often — if yours is not listed, message us and we will tell you straight away.</p>'
        '<ul class="cc-areas cc-areas--center">%s</ul>'
        '</div></section>' % chips, "lxml").find("section")
    sec.replace_with(new)


# ---------------------------------------------------------------- testimonials
def build_testimonials(soup, depth):
    sec = soup.select_one(".testimonial-section")
    if sec is None:
        return
    u = up(depth)
    cards = []
    for name, area, img, quote_text in TESTIMONIALS:
        cards.append(
            '<div class="col-lg-3 col-md-6 col-12 mb-4 mb-lg-0">'
            '<div class="featured-block h-100">'
            '<div class="d-flex align-items-center mb-3">'
            '<img class="avatar-image img-fluid" src="%s%s" alt="%s, %s" '
            'width="60" height="60" loading="lazy">'
            '<div class="ms-3">'
            '<p class="cc-tst-name mb-0">%s</p>'
            '<div class="reviews-icons mb-1" role="img" aria-label="5 out of 5 stars">'
            '<i class="bi-star-fill"></i><i class="bi-star-fill"></i>'
            '<i class="bi-star-fill"></i><i class="bi-star-fill"></i>'
            '<i class="bi-star-fill"></i></div>'
            '<p class="cc-tst-area mb-0">%s</p>'
            '</div></div>'
            '<p class="mb-0">%s</p>'
            '</div></div>' % (u, img, name, area, name, area, quote_text))

    new = BeautifulSoup(
        '<section class="testimonial-section section-padding section-bg">'
        '<div class="section-overlay"></div>'
        '<div class="container">'
        '<div class="row">'
        '<div class="col-lg-12 col-12 text-center mb-5">'
        '<h2 class="text-white mb-2">What our customers say</h2>'
        '<p class="text-white-50 mb-0">Real jobs across Islamabad and Rawalpindi.</p>'
        '</div>%s</div></div></section>' % "".join(cards), "lxml").find("section")
    sec.replace_with(new)


# ---------------------------------------------------------------- footer
def build_footer(soup, depth):
    foot = soup.select_one("footer.site-footer")
    if foot is None:
        return
    u = up(depth)
    year = 2026

    svc_links = "".join(
        '<li><a href="%sservices/%s.html">%s</a></li>' % (u, s["slug"], s["name"])
        for s in SERVICES[:8])
    svc_links2 = "".join(
        '<li><a href="%sservices/%s.html">%s</a></li>' % (u, s["slug"], s["name"])
        for s in SERVICES[8:])

    new = BeautifulSoup(
        '<footer class="site-footer">'
        '<div class="container">'
        '<div class="row">'

        # brand + contact
        '<div class="col-lg-4 col-12 mb-4">'
        '<p class="cc-footer-title">%(brand)s</p>'
        '<p class="cc-foot-text">Professional cleaning across Islamabad and Rawalpindi — '
        'deep cleaning, post-construction, sofa, carpet, marble and janitorial contracts. '
        'Free inspection, one fixed price, available 24/7.</p>'
        '<ul class="cc-foot-contact">'
        '<li><i class="bi-telephone-fill"></i> <a href="tel:%(tel)s">%(phone)s</a></li>'
        '<li><i class="bi-whatsapp"></i> <a href="%(wa)s">WhatsApp us</a></li>'
        '<li><i class="bi-envelope-fill"></i> <a href="mailto:%(email)s">%(email)s</a></li>'
        '<li><i class="bi-clock-fill"></i> Open 24 hours, 7 days a week</li>'
        '<li><i class="bi-geo-alt-fill"></i> Islamabad &amp; Rawalpindi, Pakistan</li>'
        '</ul>'
        '</div>'

        # services col 1
        '<div class="col-lg-3 col-md-6 col-12 mb-4">'
        '<p class="cc-footer-title">Services</p>'
        '<ul class="cc-foot-links">%(svc1)s</ul>'
        '</div>'

        # services col 2
        '<div class="col-lg-3 col-md-6 col-12 mb-4">'
        '<p class="cc-footer-title">More services</p>'
        '<ul class="cc-foot-links">%(svc2)s</ul>'
        '</div>'

        # company
        '<div class="col-lg-2 col-md-6 col-12 mb-4">'
        '<p class="cc-footer-title">Company</p>'
        '<ul class="cc-foot-links">'
        '<li><a href="%(u)sindex.html">Home</a></li>'
        '<li><a href="%(u)sservices.html">All services</a></li>'
        '<li><a href="%(u)sabout.html">About us</a></li>'
        '<li><a href="%(u)scontact.html">Contact</a></li>'
        '</ul>'
        '</div>'

        '</div>'

        '<div class="site-footer-bottom row align-items-center">'
        '<div class="col-lg-8 col-12">'
        '<p class="mb-0">&copy; %(year)d %(brand)s. Cleaning services in Islamabad '
        '&amp; Rawalpindi.</p>'
        '</div>'
        '<div class="col-lg-4 col-12 text-lg-end">'
        '<p class="mb-0"><a href="tel:%(tel)s">%(phone)s</a></p>'
        '</div>'
        '</div>'

        '</div></footer>' % {
            "brand": BRAND, "tel": PHONE_TEL, "phone": PHONE_DISPLAY,
            "email": EMAIL, "wa": WA_GENERAL, "u": u, "year": year,
            "svc1": svc_links, "svc2": svc_links2,
        }, "lxml").find("footer")
    foot.replace_with(new)


# ---------------------------------------------------------------- CTAs
GENERIC_CTA_TEXT = re.compile(
    r"get started|get a quote|get a free quote|book now|explore now|contact us now|"
    r"request a quote|make an appointment|book a call",
    re.I)


def fix_ctas(soup):
    """Any dead '#' CTA becomes a working WhatsApp link."""
    n = 0
    for a in soup.find_all("a"):
        href = (a.get("href") or "").strip()
        label = a.get_text(" ", strip=True)
        if href in ("#", "", "javascript:void(0)") and GENERIC_CTA_TEXT.search(label):
            a["href"] = WA_GENERAL
            n += 1
    # anything still pointing at the dropped pages
    for a in soup.find_all("a", href=True):
        for dead in DROP_PAGES:
            if a["href"].endswith(dead):
                a["href"] = "services.html" if "services" in dead else "index.html"
                n += 1
    return n


# The backstretch jQuery plugin injects the hero background as a real <img>
# at runtime with no alt attribute, so it cannot be fixed in the source HTML.
# The image is purely decorative, so an empty alt is the correct value.
A11Y_SCRIPT = """<script>
(function () {
  function fixBackstretch() {
    document.querySelectorAll('.backstretch img:not([alt])')
      .forEach(function (i) { i.setAttribute('alt', ''); });
  }
  document.addEventListener('DOMContentLoaded', fixBackstretch);
  window.addEventListener('load', fixBackstretch);
  if (window.MutationObserver) {
    new MutationObserver(fixBackstretch)
      .observe(document.documentElement, { childList: true, subtree: true });
  }
})();
</script>"""


def add_icons(soup, depth):
    """Favicon + touch icon. Without these the browser requests /favicon.ico
    and logs a 404 in the console on every page."""
    head = soup.head
    if head is None:
        return
    u = up(depth)
    for link in head.find_all("link", rel=lambda v: v and "icon" in " ".join(
            v if isinstance(v, list) else [v])):
        link.decompose()
    head.append(BeautifulSoup(
        '<link rel="icon" href="%sfavicon.ico" sizes="any">' % u, "lxml").link)
    head.append(BeautifulSoup(
        '<link rel="apple-touch-icon" href="%sapple-touch-icon.png">' % u, "lxml").link)


def selfhost_fonts(soup, depth):
    """Replace the Google Fonts <link> with the self-hosted stylesheet.

    Measured on the live deployment: the fonts.googleapis.com request was
    1014ms of render-blocking time for a 1KB file, because it needs a fresh
    DNS lookup and TLS handshake to a third-party origin before the page can
    paint. Serving the same faces from our own origin removes that entirely.
    """
    u = up(depth)
    head = soup.head
    if head is None:
        return
    for link in list(head.find_all("link", href=True)):
        h = link["href"]
        if "fonts.googleapis.com" in h or "fonts.gstatic.com" in h:
            link.decompose()
    # drop the now-pointless preconnects too
    for link in list(head.find_all("link", rel=True)):
        rels = link.get("rel")
        rels = " ".join(rels) if isinstance(rels, list) else (rels or "")
        if "preconnect" in rels and "fonts.g" in (link.get("href") or ""):
            link.decompose()
    if not head.find("link", href=lambda v: v and "poppins.css" in v):
        # must come before the template CSS so it can be overridden
        tag = BeautifulSoup(
            '<link href="%scss/poppins.css" rel="stylesheet">' % u, "lxml").link
        first = head.find("link", rel="stylesheet")
        if first:
            first.insert_before(tag)
        else:
            head.append(tag)


def preload_hero(soup, path):
    """The hero background is injected by the backstretch jQuery plugin, so the
    browser cannot discover it until jQuery has parsed and run — measured at
    ~2.7s of pure load delay on the live deployment, and it is the LCP element.
    Preloading it lets the download start with the HTML.

    Only index.html uses .hero-section; the other pages use .banner-section or
    .svcpage-hero, which are CSS backgrounds already discoverable."""
    if os.path.basename(path) != "index.html" or soup.select_one(".hero-section") is None:
        return
    head = soup.head
    if head is None or soup.find("link", rel="preload", attrs={"as": "image"}):
        return
    head.append(BeautifulSoup(
        '<link rel="preload" as="image" fetchpriority="high" '
        'href="images/slideshow/afro-woman-cleaning-window-with-rag-home.jpg">',
        "lxml").link)


def inject_a11y_script(soup):
    if soup.find("script", string=re.compile("fixBackstretch")):
        return 0
    body = soup.body
    if body is None:
        return 0
    body.append(BeautifulSoup(A11Y_SCRIPT, "lxml").find("script"))
    return 1


def fix_404(soup):
    """The 404 page inherited the home page's title/description. Give it its
    own, and keep it out of the index."""
    if soup.title:
        soup.title.string = "Page not found | %s" % BRAND
    desc = soup.find("meta", attrs={"name": "description"})
    if desc:
        desc["content"] = ("That page does not exist. Browse our cleaning services in "
                           "Islamabad and Rawalpindi, or message us on WhatsApp.")
    if not soup.find("meta", attrs={"name": "robots"}):
        head = soup.head
        if head is not None:
            head.append(BeautifulSoup(
                '<meta name="robots" content="noindex, follow">', "lxml").meta)
    # canonical pointing at the home page would be wrong here
    for c in soup.find_all("link", rel="canonical"):
        c.decompose()


def main():
    # drop the template-only pages
    for p in DROP_PAGES:
        fp = os.path.join(SITE, p)
        if os.path.exists(fp):
            os.remove(fp)
            print("removed %s" % p)

    for path in html_files(SITE):
        depth = 1 if os.path.dirname(path) != SITE else 0
        soup = BeautifulSoup(read(path), "lxml")

        build_nav(soup, depth)
        build_footer(soup, depth)
        add_icons(soup, depth)
        # The stock partner-logo strip appears on several template pages, not
        # just the home page — replace it wherever it occurs.
        build_areas(soup, depth)
        if os.path.basename(path) == "index.html" and depth == 0:
            build_testimonials(soup, depth)
        ctas = fix_ctas(soup)
        inject_a11y_script(soup)
        preload_hero(soup, path)
        selfhost_fonts(soup, depth)
        if os.path.basename(path) == "page-404.html":
            fix_404(soup)

        write(path, str(soup))
        print("  %-40s nav+footer rebuilt, %d CTAs wired" %
              (os.path.relpath(path, SITE), ctas))


if __name__ == "__main__":
    main()
