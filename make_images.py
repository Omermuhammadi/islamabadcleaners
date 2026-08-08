"""Convert source images into optimized site images.

Outputs per service slug:
  docs/images/services/{slug}-card.webp   640x427  (3:2)
  docs/images/services/{slug}-hero.webp   720x720  (1:1)
  docs/images/og/{slug}.jpg               1200x630 JPEG (social previews)
Plus the four page heroes (AI-generated brand set, all sources 4:5):
  docs/images/hero-crew.webp              900x1125  homepage   <- "landing page hero new.png"
  docs/images/about-team.webp             900x1125  about      <- "about page new.png"
  docs/images/services-page.webp          900x1125  services   <- "service page new.png"
  docs/images/hero-home.webp              900x1125  contact    <- "contact page new.png"
  docs/images/og/default.jpg              1200x630  from the homepage hero
  docs/images/CREDITS.txt                 copied from raw-images/credits.txt

Usage: python make_images.py
"""

import os
import shutil
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "raw-images")
OUT_SVC = os.path.join(ROOT, "docs", "images", "services")
OUT_OG = os.path.join(ROOT, "docs", "images", "og")
OUT_IMG = os.path.join(ROOT, "docs", "images")

from _services import SERVICES  # noqa: E402

QUALITY_WEBP = 74
QUALITY_JPG = 78
MAX_KB = 145
OG_MAX_KB = 95  # social previews don't need more

MANUAL_SOURCES = {
    "deep-cleaning": "deep cl.jpg",
    "carpet-cleaning": "carpet-cle.jpg",
    "house-cleaning": "HOUSE CL.jpg",
    "office-chair-cleaning": "chair cl.jpg",
    "dining-chair-cleaning": "dinning chairs clea.jpg",
    "janitorial-services": "janitorial services cl.jpg",
    "mattress-cleaning": "mattress cl.jpg",
    "rug-cleaning": "rug-cle.jpg",
    "swimming-pool-cleaning": "swimming-pool-cle.jpg",
    "tile-cleaning": "tiles-cle.jpg",
    "water-tank-cleaning": "water tank cl.jpg",
}


def first_existing(*paths):
    for path in paths:
        if path and os.path.isfile(path):
            return path
    return None


def save_capped(im, path, fmt, quality, max_kb=MAX_KB):
    """Save, stepping quality down until the file is under max_kb."""
    q = quality
    while True:
        if fmt == "WEBP":
            im.save(path, "WEBP", quality=q)
        else:
            im.save(path, "JPEG", quality=q, optimize=True, progressive=True)
        if os.path.getsize(path) / 1024 <= max_kb or q <= 40:
            break
        q -= 8


def cover(im, w, h, fx=0.5, fy=0.5):
    """Crop to w:h around focal point (fx, fy in 0..1) then resize to (w, h)."""
    src_w, src_h = im.size
    target = w / h
    src = src_w / src_h
    if src > target:
        new_w = int(src_h * target)
        x = min(max(int(src_w * fx - new_w / 2), 0), src_w - new_w)
        box = (x, 0, x + new_w, src_h)
    else:
        new_h = int(src_w / target)
        y = min(max(int(src_h * fy - new_h / 2), 0), src_h - new_h)
        box = (0, y, src_w, y + new_h)
    return im.crop(box).resize((w, h), Image.LANCZOS)


def load(path):
    im = Image.open(path)
    im.load()
    if im.mode != "RGB":
        im = im.convert("RGB")
    return im


def erase_screen_button(im):
    """Paint out the garbled AI-generated button on the contact source's
    phone screen (coords fixed to the 1856x2304 "contact page new.png").
    The screen around it is uniform white, so a flat fill sampled from the
    screen is invisible."""
    if im.size != (1856, 2304):
        return
    px = im.load()
    # sample clean screen white just below the button
    box = im.crop((580, 1088, 620, 1100))
    n = (box.width * box.height)
    fill = tuple(sum(ch) // n for ch in zip(*list(box.getdata())))
    for y in range(1041, 1084):
        for x in range(543, 666):
            px[x, y] = fill


def main():
    os.makedirs(OUT_SVC, exist_ok=True)
    os.makedirs(OUT_OG, exist_ok=True)

    for s in SERVICES:
        slug = s["slug"]
        src = first_existing(
            os.path.join(ROOT, MANUAL_SOURCES.get(slug, "")),
            os.path.join(ROOT, f"{slug}.jpg"),
            os.path.join(ROOT, f"{slug}.png"),
            os.path.join(RAW, f"{slug}.jpg"),
        )
        if not src:
            continue
        im = load(src)
        save_capped(cover(im, 480, 320), os.path.join(OUT_SVC, f"{slug}-card.webp"), "WEBP", QUALITY_WEBP, 25)
        save_capped(cover(im, 720, 720), os.path.join(OUT_SVC, f"{slug}-hero.webp"), "WEBP", QUALITY_WEBP, 90)
        save_capped(cover(im, 1200, 630), os.path.join(OUT_OG, f"{slug}.jpg"), "JPEG", QUALITY_JPG, 80)
        print(f"ok  {slug}")

    landing = first_existing(
        os.path.join(ROOT, "landing page hero new.png"),
        os.path.join(RAW, "landing page hero new.png"),
    )
    if landing:
        im = load(landing)
        save_capped(cover(im, 900, 1125), os.path.join(OUT_IMG, "hero-crew.webp"), "WEBP", QUALITY_WEBP)
        # social preview: crop the wide band around the crew's faces
        save_capped(cover(im, 1200, 630, fy=0.35), os.path.join(OUT_OG, "default.jpg"), "JPEG", QUALITY_JPG, OG_MAX_KB)

    team = first_existing(
        os.path.join(ROOT, "about page new.png"),
        os.path.join(RAW, "about page new.png"),
    )
    if team:
        im = load(team)
        save_capped(cover(im, 900, 1125), os.path.join(OUT_IMG, "about-team.webp"), "WEBP", QUALITY_WEBP)

    svc_page = first_existing(
        os.path.join(ROOT, "service page new.png"),
        os.path.join(RAW, "service page new.png"),
    )
    if svc_page:
        im = load(svc_page)
        save_capped(cover(im, 900, 1125), os.path.join(OUT_IMG, "services-page.webp"), "WEBP", QUALITY_WEBP)

    contact = first_existing(
        os.path.join(ROOT, "contact page new.png"),
        os.path.join(RAW, "contact page new.png"),
    )
    if contact:
        im = load(contact)
        erase_screen_button(im)
        save_capped(cover(im, 900, 1125), os.path.join(OUT_IMG, "hero-home.webp"), "WEBP", QUALITY_WEBP)

    credits = os.path.join(RAW, "credits.txt")
    if os.path.exists(credits):
        shutil.copyfile(credits, os.path.join(OUT_IMG, "CREDITS.txt"))

    print("Image generation complete.")


if __name__ == "__main__":
    main()
