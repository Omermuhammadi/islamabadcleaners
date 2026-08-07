"""Convert raw-images/*.jpg into optimized site images.

Outputs per service slug:
  docs/images/services/{slug}-card.webp   640x427  (3:2)
  docs/images/services/{slug}-hero.webp   720x720  (1:1)
  docs/images/og/{slug}.jpg               1200x630 JPEG (social previews)
Plus:
  docs/images/hero-home.webp              900x1125 (4:5 arch)
  docs/images/about-team.webp             720x720
  docs/images/og/default.jpg              1200x630 from hero-home
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


def main():
    os.makedirs(OUT_SVC, exist_ok=True)
    os.makedirs(OUT_OG, exist_ok=True)

    missing = []
    for s in SERVICES:
        slug = s["slug"]
        src = os.path.join(RAW, f"{slug}.jpg")
        if not os.path.exists(src):
            missing.append(slug)
            continue
        im = load(src)
        save_capped(cover(im, 640, 427), os.path.join(OUT_SVC, f"{slug}-card.webp"), "WEBP", QUALITY_WEBP)
        save_capped(cover(im, 720, 720), os.path.join(OUT_SVC, f"{slug}-hero.webp"), "WEBP", QUALITY_WEBP)
        save_capped(cover(im, 1200, 630), os.path.join(OUT_OG, f"{slug}.jpg"), "JPEG", QUALITY_JPG, OG_MAX_KB)
        print(f"ok  {slug}")

    hero = os.path.join(RAW, "hero-home.jpg")
    if os.path.exists(hero):
        im = load(hero)
        save_capped(cover(im, 900, 1125, fx=0.74), os.path.join(OUT_IMG, "hero-home.webp"), "WEBP", QUALITY_WEBP)
    else:
        missing.append("hero-home")

    team = os.path.join(RAW, "about-team.jpg")
    if os.path.exists(team):
        im = load(team)
        save_capped(cover(im, 720, 720), os.path.join(OUT_IMG, "about-team.webp"), "WEBP", QUALITY_WEBP)
        # homepage hero: 4:5 crop centred on the crew
        save_capped(cover(im, 900, 1125, fx=0.42), os.path.join(OUT_IMG, "hero-crew.webp"), "WEBP", QUALITY_WEBP)
        save_capped(cover(im, 1200, 630, fx=0.42), os.path.join(OUT_OG, "default.jpg"), "JPEG", QUALITY_JPG, OG_MAX_KB)
    else:
        missing.append("about-team")

    credits = os.path.join(RAW, "credits.txt")
    if os.path.exists(credits):
        shutil.copyfile(credits, os.path.join(OUT_IMG, "CREDITS.txt"))

    if missing:
        print("MISSING:", ", ".join(missing))
        raise SystemExit(1)
    print("All images generated.")


if __name__ == "__main__":
    main()
