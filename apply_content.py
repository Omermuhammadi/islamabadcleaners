"""Rewrite site/ and option-b/ with the real content from _content.py.

Idempotent: safe to re-run after editing _content.py.
"""
import io
import os
import re
import sys

from bs4 import BeautifulSoup

import _content as C

ROOT = os.path.dirname(os.path.abspath(__file__))


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


# --------------------------------------------------------------------------
# Text-level replacements applied to every page of both options
# --------------------------------------------------------------------------
GLOBAL_SUBS = [
    (r"\+?012[\s-]?345[\s-]?67890", C.PHONE_DISPLAY),
    (r"666[\s-]?333[\s-]?9999", C.PHONE_DISPLAY),
    (r"888[\s-]?333[\s-]?9999", C.PHONE_DISPLAY),
    (r"123[\s-]?456[\s-]?7891", C.PHONE_DISPLAY),
    (r"110[\s-]?220[\s-]?9800", C.PHONE_DISPLAY),
    (r"[Yy]ouremail@gmail\.com", C.EMAIL),
    (r"info@company\.com", C.EMAIL),
    (r"info@example\.com", C.EMAIL),
    (r"CleanMe", C.BRAND),
    (r"Clean Work", C.BRAND),
    (r"Provide Services Worldwide", "What we clean"),
    (r"Services Worldwide", "Our services"),
    (r"Our best offers", "What we clean"),
    (r"Expert Cleaners and World Class Services", "Why people call us back"),
    (r"Client Says About Service", "What our customers say"),
    (r"Happy Customers", "What our customers say"),
    (r"Get A Free Cleaning Service", "Need a cleaning quote today?"),
    (r"Get A Free Quote", "Get a free quote"),
    (r"Get A Quote", "Get a free quote"),
    (r"Reliable &amp; Fast Cleaning\s*Service", "Cleaning done properly, first time"),
    (r"Trusted by companies", "Serving Islamabad &amp; Rawalpindi"),
    # phone/whatsapp/mail hrefs
    (r'href="tel:[^"]*"', 'href="tel:%s"' % C.PHONE_TEL),
    (r'href="mailto:[^"]*"', 'href="mailto:%s"' % C.EMAIL),
]


def global_pass(path):
    s = read(path)
    for pat, rep in GLOBAL_SUBS:
        s = re.sub(pat, rep, s)
    # title + meta description
    s = re.sub(
        r"<title>.*?</title>",
        "<title>%s — Cleaning Services in Islamabad &amp; Rawalpindi | Deep, Sofa, Carpet</title>" % C.BRAND,
        s, flags=re.S)
    if re.search(r'<meta[^>]*name="description"', s):
        s = re.sub(r'(<meta[^>]*name="description"[^>]*content=")[^"]*(")',
                   r"\g<1>Deep cleaning, post-construction, sofa, carpet and marble cleaning in "
                   r"Islamabad and Rawalpindi. Free inspection, fixed price, available 24/7. "
                   r"WhatsApp 0330 2935777.\g<2>", s)
    else:
        s = s.replace("</title>",
                      '</title>\n<meta name="description" content="Deep cleaning, post-construction, '
                      'sofa, carpet and marble cleaning in Islamabad and Rawalpindi. Free inspection, '
                      'fixed price, available 24/7. WhatsApp 0330 2935777.">', 1)
    write(path, s)


# --------------------------------------------------------------------------
def set_text(el, value):
    """Replace an element's inner text, preserving the tag."""
    if el is None:
        return
    el.clear()
    el.append(BeautifulSoup(value, "lxml").get_text() if "<" not in value
              else BeautifulSoup(value, "lxml"))


def set_html(el, value):
    if el is None:
        return
    el.clear()
    frag = BeautifulSoup(value, "lxml")
    body = frag.body or frag
    for child in list(body.children):
        el.append(child)


def kill(soup, selector):
    n = 0
    for el in soup.select(selector):
        el.decompose()
        n += 1
    return n


# --------------------------------------------------------------------------
def option_b(path):
    """CleanMe: content-rich. Remove fake team / pricing / blog; fill the rest."""
    soup = BeautifulSoup(read(path), "lxml")
    removed = []

    # Pricing section — we are quote-only, and the demo prices are USD.
    if kill(soup, "div.price"):
        removed.append("pricing")
    # Team section — fake people with stock headshots.
    if kill(soup, "div.team"):
        removed.append("team")
    # Blog — nothing to publish yet.
    if kill(soup, "div.blog"):
        removed.append("blog")
    # Newsletter — we want WhatsApp, not email capture.
    if kill(soup, "div.newsletter"):
        removed.append("newsletter")

    # nav links pointing at removed sections
    for a in soup.select('a[href="#team"], a[href="#price"], a[href="#blog"]'):
        li = a.find_parent("li")
        (li or a).decompose()

    # Hero
    hero = soup.select_one(".header .col-lg-7, .home .col-lg-7, .header")
    h2s = soup.select(".header h2, .home h2")
    if len(h2s) >= 2:
        set_text(h2s[0], "Cleaning services in")
        set_text(h2s[1], "Islamabad & Rawalpindi")
    p = soup.select_one(".header p, .home p")
    if p:
        set_text(p, "Deep cleaning, post-construction, sofa, carpet and marble. "
                    "We look at the job first, then give you one fixed price.")

    # About
    ab = soup.select_one("div.about")
    if ab:
        h = ab.find("h2")
        if h:
            set_html(h, '<span class="text-primary">%s</span> years in the twin cities' % C.YEARS)
        ps = ab.find_all("p")
        for i, para in enumerate(ps[:len(C.ABOUT_BODY)]):
            set_text(para, C.ABOUT_BODY[i])
        for extra in ps[len(C.ABOUT_BODY):]:
            extra.decompose()

    # Service cards
    cards = soup.select("div.service .service-item")
    if not cards:
        cards = soup.select("div.service .col-lg-3, div.service .col-md-6")
    for i, card in enumerate(cards):
        if i >= len(C.SERVICES):
            card.decompose()
            continue
        name, desc = C.SERVICES[i]
        h = card.find(["h3", "h4", "h5"])
        set_text(h, name)
        pp = card.find("p")
        set_text(pp, desc)

    # Features / why-us
    feats = soup.select("div.feature .feature-item, div.feature .col-lg-4")
    for i, f in enumerate(feats):
        if i >= len(C.FEATURES):
            continue
        t, d = C.FEATURES[i]
        set_text(f.find(["h3", "h4", "h5"]), t)
        set_text(f.find("p"), d)

    # Feature intro paragraph (sits beside the three feature items)
    fi = soup.select_one("div.feature .col-md-5 p, div.feature .section-header ~ p")
    if fi is None:
        for p in soup.select("div.feature p"):
            if "orem ipsum" in p.get_text():
                fi = p
                break
    if fi is not None:
        set_text(fi, "We are not the cheapest and we do not pretend to be. What we "
                     "are is reliable: we turn up when we say, we bring everything "
                     "with us, and we quote after seeing the job so the number "
                     "does not move on the day.")

    # FAQ — this template uses a Bootstrap 4 accordion (.card / .card-link /
    # .card-body), not the Bootstrap 5 .accordion-button markup.
    cards = soup.select("div.faqs #accordion > .card")
    if cards:
        # clone the last card until there are enough for every question
        while len(cards) < len(C.FAQS):
            import copy as _copy
            clone = _copy.copy(cards[-1])
            n = len(cards) + 1
            link = clone.select_one(".card-link")
            body_wrap = clone.select_one(".collapse")
            if link is not None and body_wrap is not None:
                link["href"] = "#collapseGen%d" % n
                link["class"] = ["card-link", "collapsed"]
                body_wrap["id"] = "collapseGen%d" % n
                body_wrap["class"] = ["collapse"]
            cards[-1].insert_after(clone)
            cards = soup.select("div.faqs #accordion > .card")

        for i, card in enumerate(cards):
            if i >= len(C.FAQS):
                card.decompose()
                continue
            q, a = C.FAQS[i]
            link = card.select_one(".card-link")
            if link is not None:
                link.clear()
                num = soup.new_tag("span")
                num.string = str(i + 1)
                link.append(num)
                link.append(" " + BeautifulSoup(q, "lxml").get_text())
            body = card.select_one(".card-body")
            if body is not None:
                set_text(body, a)

    # Testimonials
    tsts = soup.select("div.testimonial .testimonial-item")
    for i, t in enumerate(tsts):
        if i >= len(C.TESTIMONIALS):
            t.decompose()
            continue
        nm, area, quote = C.TESTIMONIALS[i]
        set_text(t.find("p"), quote)
        set_text(t.find(["h3", "h4", "h5"]), nm)
        sub = t.select_one("h4, .text-primary, small")
        if sub and sub.get_text(strip=True) in ("Profession", ""):
            set_text(sub, area)

    write(path, str(soup))
    return removed


def option_a(path):
    """Clean Work: lighter template. Fill hero, services, testimonials."""
    soup = BeautifulSoup(read(path), "lxml")

    # Hero: keep the template's rotating-headline structure exactly (the
    # cd-headline JS depends on .cd-words-wrapper + <b> children) and only
    # change the words.
    h1 = soup.select_one(".hero-section h1")
    if h1 is not None:
        lead = h1.find("span")
        if lead is not None:
            lead.string = "We clean your"
        wrap = h1.select_one(".cd-words-wrapper")
        if wrap is not None:
            words = wrap.find_all("b")
            new_words = ["home", "office", "sofa", "carpet", "marble"]
            for i, w in enumerate(new_words):
                if i < len(words):
                    words[i].string = w
                else:
                    b = soup.new_tag("b")
                    b.string = w
                    wrap.append(b)
            for extra in words[len(new_words):]:
                extra.decompose()

    # Sub-headline under the hero buttons, if the template has one
    hp = soup.select_one(".hero-section p")
    if hp is not None:
        set_text(hp, "Deep cleaning, post-construction, sofa, carpet and marble "
                     "across Islamabad and Rawalpindi. Available 24/7.")

    # Intro section still carries Tooplate's own licence blurb
    intro = soup.select_one(".intro-section")
    if intro is not None:
        h2 = intro.find(["h2", "h3"])
        if h2 is not None:
            set_text(h2, "Cleaning done properly, first time")
        paras = [p for p in intro.find_all("p")
                 if C.PHONE_DISPLAY not in p.get_text()]
        for i, p in enumerate(paras):
            if i < len(C.ABOUT_BODY):
                set_text(p, C.ABOUT_BODY[i])
            else:
                p.decompose()

    # Kill the fake USD prices on service cards
    for el in soup.select(".services-icon-wrap p"):
        txt = el.get_text(" ", strip=True)
        if "$" in txt:
            set_html(el, '<i class="bi-chat-dots me-2"></i>Free quote')

    cards = soup.select(".services-thumb")
    for i, card in enumerate(cards):
        if i >= len(C.SERVICES):
            col = card.find_parent(class_=re.compile(r"col-"))
            (col or card).decompose()
            continue
        name, desc = C.SERVICES[i]
        h = card.find(["h4", "h3", "h5"])
        set_text(h, name)
        pp = card.find("p", class_=lambda c: not c or "text-white" not in (c or []))
        if pp and "$" not in pp.get_text():
            set_text(pp, desc)

    # Testimonials
    for i, t in enumerate(soup.select(".testimonial-thumb")):
        if i >= len(C.TESTIMONIALS):
            continue
        nm, area, quote = C.TESTIMONIALS[i]
        set_text(t.find("p"), quote)
        set_text(t.find(["h4", "h5", "h3"]), "%s — %s" % (nm, area))

    write(path, str(soup))
    return []


# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Safety net: nothing with lorem ipsum ships. Anything the structural passes
# missed gets swapped for real copy chosen by length, so the layout still fits.
# --------------------------------------------------------------------------
FILLER_LONG = [
    "We cover every sector of Islamabad and all of Rawalpindi, and we work "
    "seven days a week including nights when a handover deadline needs it.",
    "Tell us what needs cleaning and roughly how big it is. We come and look, "
    "then give you one fixed price before anything starts.",
    "Homes, offices, clinics and new-build handovers. From a single sofa to a "
    "whole house after the builders have finished.",
    "Everything comes with the team — machines, chemicals, cloths and cover "
    "sheets. You do not need to buy or arrange anything.",
]
FILLER_SHORT = [
    "Available 24/7 across Islamabad and Rawalpindi.",
    "Free inspection, then one fixed price.",
    "We bring our own equipment and supplies.",
    "WhatsApp us for a same-day slot.",
]


def lorem_sweep(path):
    s = read(path)
    n = 0
    # headings / short strings
    s, k = re.subn(r"Lorem ipsum dolor(?: sit amet)?\?", "How soon can you come?", s)
    n += k
    # long paragraphs
    def _long(_m, box=[0]):
        v = FILLER_LONG[box[0] % len(FILLER_LONG)]
        box[0] += 1
        return v
    s, k = re.subn(r"Lorem ipsum dolor sit amet,[^<]{60,}", _long, s)
    n += k
    def _short(_m, box=[0]):
        v = FILLER_SHORT[box[0] % len(FILLER_SHORT)]
        box[0] += 1
        return v
    s, k = re.subn(r"Lorem ipsum dolor sit amet[^<]{0,60}", _short, s)
    n += k
    s, k = re.subn(r"[Ll]orem ipsum[^<]*", "", s)
    n += k
    write(path, s)
    return n


if __name__ == "__main__":
    for opt in ("site", "option-b"):
        d = os.path.join(ROOT, opt)
        if not os.path.isdir(d):
            continue
        files = html_files(d)
        for f in files:
            global_pass(f)
        idx = os.path.join(d, "index.html")
        removed = option_b(idx) if opt == "option-b" else option_a(idx)
        swept = sum(lorem_sweep(f) for f in files)
        left = sum(len(re.findall(r"[Ll]orem ipsum", read(f))) for f in files)
        print("%-9s %2d pages | lorem replaced: %-3d remaining: %d%s" % (
            opt, len(files), swept, left,
            ("  | removed: " + ", ".join(removed)) if removed else ""))
