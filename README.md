# IslamabadCleaners — cleaning services in Islamabad & Rawalpindi

Static site, live at **https://effendii69.github.io/cleancrew/** (GitHub Pages
serves the `docs/` folder on `main`).

## How it works

Everything in `docs/` is generated. Edit the data files, then rebuild:

```
pip install pillow
python build.py      # regenerates all 24 pages + sitemap.xml + robots.txt
python verify.py     # bulletproof gate: links, meta, schema, weights — must pass
```

| File | What lives there |
|---|---|
| `_site.py` | **Config**: BASE_URL, brand, phone/WhatsApp, email, featured services, promise/steps copy |
| `_services.py` | The 19 services — slug, name, card copy |
| `_service_pages.py` + `_pages_*.py` | Long-form service page content (intro, inclusions, FAQs…) |
| `_content.py` | Homepage FAQs, about copy, features, area lists |
| `build.py` | Templates + generator (also holds the short meta descriptions) |
| `make_images.py` | Rebuilds optimized images from `raw-images/` (not in git) |
| `verify.py` | The QA gate — run it before every push |

## Common tasks

- **New phone number / domain**: change it in `_site.py`, run `python build.py`,
  commit `docs/`. When a real domain is bought, set `BASE_URL`, rebuild, and
  configure the custom domain in the GitHub Pages settings.
- **Edit service copy**: find the dict in `_pages_*.py` / `_pages_new.py`,
  edit, rebuild.
- **Replace a photo**: drop a JPG named `{slug}.jpg` into `raw-images/`, run
  `python make_images.py`, rebuild. Replace stock photos with real job photos
  whenever you can — image credits are in `docs/images/CREDITS.txt`.
- **Deploy**: commit and push `main`; GitHub Pages redeploys automatically.

## Before-launch notes

- Testimonials were removed deliberately — the previous ones were placeholders,
  and fabricated reviews violate Google's policies. Collect real ones.
- Set up a **Google Business Profile** for Islamabad/Rawalpindi — it matters
  more for local search than anything on this site.
- Analytics are not installed (needs the owner's Google account).
