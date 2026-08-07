"""Resize and recompress the site's images.

The template shipped 1500px-wide photos that the service cards display at
172px, which is ~950 KiB of wasted transfer on the home page alone.

Two things happen here:
  1. Every image is capped at a sensible max width and recompressed.
  2. Service photos additionally get a small thumbnail in images/services/thumb/
     for the card grid, since the full-size file is still needed for the
     service-page hero backgrounds.

Safe to re-run: already-optimised files are skipped via a marker file.
"""
import io
import json
import os

from PIL import Image

SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
IMAGES = os.path.join(SITE, "images")
MARKER = os.path.join(IMAGES, ".optimized.json")

# max width by directory role
CAPS = {
    "slideshow": 1600,   # full-bleed hero backgrounds
    "services": 1200,    # service page hero backgrounds
    "teams": 600,
    "avatar": 200,
    "partners": 400,
    None: 1200,          # everything else
}
THUMB_WIDTH = 400        # service card grid (displayed at 172px, 2x for retina)
QUALITY = 78


def role(path):
    parts = os.path.normpath(path).split(os.sep)
    for r in CAPS:
        if r and r in parts:
            return r
    return None


def optimise(path, max_w, quality=QUALITY):
    before = os.path.getsize(path)
    with Image.open(path) as im:
        fmt = im.format
        w, h = im.size
        if w > max_w:
            im = im.resize((max_w, round(h * max_w / w)), Image.LANCZOS)
        if fmt == "PNG":
            # These are photographs saved as PNG — huge for no benefit.
            # Keep the extension (markup references it) but store JPEG-quality
            # data by flattening and re-encoding as an optimised PNG.
            im = im.convert("RGB")
            im.save(path, "PNG", optimize=True)
        else:
            im = im.convert("RGB")
            im.save(path, "JPEG", quality=quality, optimize=True, progressive=True)
    return before, os.path.getsize(path)


def main():
    done = {}
    if os.path.exists(MARKER):
        done = json.load(io.open(MARKER, encoding="utf-8"))

    total_before = total_after = 0
    changed = 0

    for dp, _dirs, files in os.walk(IMAGES):
        if "thumb" in dp:
            continue
        for f in files:
            if not f.lower().endswith((".jpg", ".jpeg", ".png")):
                continue
            p = os.path.join(dp, f)
            key = os.path.relpath(p, IMAGES).replace("\\", "/")
            sig = "%d" % os.path.getsize(p)
            if done.get(key) == sig:
                continue
            b, a = optimise(p, CAPS[role(p)])
            done[key] = "%d" % os.path.getsize(p)
            total_before += b
            total_after += a
            changed += 1

    # thumbnails for the service card grid
    svc = os.path.join(IMAGES, "services")
    thumb_dir = os.path.join(svc, "thumb")
    os.makedirs(thumb_dir, exist_ok=True)
    thumbs = 0
    for f in os.listdir(svc):
        if not f.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        src = os.path.join(svc, f)
        dst = os.path.join(thumb_dir, os.path.splitext(f)[0] + ".jpg")
        with Image.open(src) as im:
            w, h = im.size
            side = min(w, h)
            im = im.crop(((w - side) // 2, (h - side) // 2,
                          (w + side) // 2, (h + side) // 2))
            im = im.resize((THUMB_WIDTH, THUMB_WIDTH), Image.LANCZOS).convert("RGB")
            im.save(dst, "JPEG", quality=80, optimize=True, progressive=True)
        thumbs += 1

    json.dump(done, io.open(MARKER, "w", encoding="utf-8"))

    print("optimised %d images: %.1f MB -> %.1f MB (saved %.1f MB)"
          % (changed, total_before / 1048576, total_after / 1048576,
             (total_before - total_after) / 1048576))
    print("generated %d square card thumbnails at %dpx" % (thumbs, THUMB_WIDTH))
    tot = sum(os.path.getsize(os.path.join(dp, f))
              for dp, _d, fs in os.walk(IMAGES) for f in fs)
    print("images/ total now: %.1f MB" % (tot / 1048576))


if __name__ == "__main__":
    main()
