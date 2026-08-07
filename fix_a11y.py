"""Accessibility fixes applied to every built page.

Three issues Lighthouse flagged, all in the template's own header/footer chrome:
  1. white text on the light-blue footer = 2.11:1 (fails WCAG AA)
  2. footer titles are <h5> straight after an <h2>, skipping levels
  3. footer social icons are links with no accessible name

Run after build_services.py / build_service_page.py.
"""
import io
import os
import re

from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")

# icon class -> label. The template reuses one class for every social link, so
# we read the <i> inside to work out which network it is.
ICON_LABELS = [
    ("facebook", "Facebook"),
    ("twitter", "Twitter"),
    ("whatsapp", "WhatsApp"),
    ("instagram", "Instagram"),
    ("youtube", "YouTube"),
    ("linkedin", "LinkedIn"),
    ("tiktok", "TikTok"),
]


def html_files(d):
    out = []
    for dp, _dirs, fs in os.walk(d):
        for f in fs:
            if f.endswith(".html"):
                out.append(os.path.join(dp, f))
    return out


def fix(path):
    s = io.open(path, encoding="utf-8", errors="ignore").read()
    soup = BeautifulSoup(s, "lxml")
    changed = 0

    # 1. Footer column titles -> <p>. They are h4/h5/h6 sitting straight after
    # an <h2> in the page body, which skips levels. They are labels, not
    # document structure, so a styled <p> is the correct markup.
    footer = soup.select_one("footer")
    if footer is not None:
        for h in footer.find_all(["h3", "h4", "h5", "h6"]):
            p = soup.new_tag("p")
            p["class"] = h.get("class", []) + ["cc-footer-title"]
            p.string = h.get_text(" ", strip=True)
            h.replace_with(p)
            changed += 1

    # 2. accessible names on the social links
    for a in soup.select("a.social-icon-link"):
        if a.get("aria-label") or a.get_text(strip=True):
            continue
        icon = a.find("i")
        cls = " ".join(icon.get("class", [])) if icon else ""
        label = next((lbl for key, lbl in ICON_LABELS if key in cls), "Social profile")
        a["aria-label"] = "%s (opens in a new tab)" % label
        changed += 1

    # 3. Stray h5/h6 in the page body that skip heading levels. These are
    # labels on call-out boxes ("Need help? Please call us"), not document
    # structure, so a styled <p> is the correct markup.
    body_main = soup.body
    if body_main is not None:
        for h in body_main.find_all(["h5", "h6"]):
            if h.find_parent("footer"):
                continue
            p = soup.new_tag("p")
            p["class"] = h.get("class", []) + ["cc-boxtitle"]
            p.string = h.get_text(" ", strip=True)
            h.replace_with(p)
            changed += 1

    # 4. Every <img> needs an alt attribute. Background/slideshow images are
    # decorative -> empty alt; content images get one derived from the filename.
    for img in soup.find_all("img"):
        if img.has_attr("alt"):
            continue
        src = img.get("src", "") or ""
        name = os.path.basename(src).rsplit(".", 1)[0]
        decorative = ("slideshow" in src or "bubbles" in src
                      or "partners" in src or not name)
        if decorative:
            img["alt"] = ""
        else:
            words = re.sub(r"[-_]+", " ", name).strip()
            words = re.sub(r"\s+", " ", words)
            img["alt"] = (words[:1].upper() + words[1:]) if words else ""
        changed += 1

    if changed:
        io.open(path, "w", encoding="utf-8").write(str(soup))
    return changed


if __name__ == "__main__":
    total = 0
    for f in html_files(SITE):
        n = fix(f)
        total += n
        if n:
            print("  %-46s %d fixes" % (os.path.relpath(f, SITE), n))
    print("total element fixes: %d" % total)
