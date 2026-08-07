# IslamabadCleaners — cleaning services in Islamabad & Rawalpindi

Static site, live at **https://www.islamabadcleaners.com** — Vercel deploys the
`docs/` folder from `main` on every push.

## URLs

Pages use clean, extensionless URLs — `/services`, `/about`, `/contact`,
`/services/sofa-cleaning`. Each one is a real `index.html` inside its own
folder (`docs/services/about/index.html` → `/about`), so the clean URL works on
any static host, not just Vercel.

`vercel.json` (generated into both the repo root and `docs/`, so it applies
whichever one Vercel treats as the project root) adds:

- `trailingSlash: false` — `/services/` redirects to `/services`
- permanent **308 redirects** from every legacy `.html` URL, so old links and
  anything Google already indexed land on the clean URL instead of a 404

All internal links and asset paths are **site-absolute** (`/css/main.css`), so
they resolve identically at every depth. To preview locally, serve the folder —
opening the files directly with `file://` will not work:

```
python -m http.server 8000 --directory docs
```

## How it works

Everything in `docs/` is generated. Edit the data files, then rebuild:

```
pip install pillow
python build.py      # regenerates all 26 pages + sitemap + robots + vercel.json
python verify.py     # bulletproof gate: links, meta, schema, redirects, weights
```

`build.py` prunes any `.html` left behind by a previous layout, so the output
folder never accumulates stale pages.

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
  commit `docs/`. `BASE_URL` must match the host Vercel actually serves —
  currently `www`, since the bare domain 308-redirects to it. If that ever
  flips, change `BASE_URL` and rebuild, or every canonical points at a redirect.
- **Edit service copy**: find the dict in `_pages_*.py` / `_pages_new.py`,
  edit, rebuild.
- **Replace a photo**: drop a JPG named `{slug}.jpg` into `raw-images/`, run
  `python make_images.py`, rebuild. Replace stock photos with real job photos
  whenever you can — image credits are in `docs/images/CREDITS.txt`.
- **Deploy**: commit and push `main`; Vercel redeploys automatically.

## Before-launch notes

- Testimonials were removed deliberately — the previous ones were placeholders,
  and fabricated reviews violate Google's policies. Collect real ones.
- Set up a **Google Business Profile** for Islamabad/Rawalpindi — it matters
  more for local search than anything on this site.
- Analytics are not installed (needs the owner's Google account).
