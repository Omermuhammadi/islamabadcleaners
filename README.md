# Cleaning Services Website — Islamabad & Rawalpindi

Static marketing site for a cleaning services company operating in Islamabad and
Rawalpindi. Plain HTML/CSS/JS (Bootstrap 5) — no build step required to deploy,
and it runs on any free static host.

**Working brand name is `CleanCrew` — this is a placeholder.** Changing it is a
one-line edit in each build script's `BRAND` constant, then re-running the pipeline.

---

## Structure

```
site/                  The live website — deploy this folder
  index.html           Home
  services.html        Services index
  services/*.html      15 service pages
  about.html
  contact.html
  page-404.html
  css/custom.css       All of our overrides (the vendor CSS is untouched)
  images/

superclean-alt/        Alternative template kept for reference (the "5003" option)

*.py                   Content + build scripts (see below)
```

`site/` is fully static. Nothing in it depends on the Python scripts at runtime —
those only regenerate the HTML.

---

## Running locally

```bash
cd site && python -m http.server 5004
```

Then open <http://localhost:5004>.

The alternative template:

```bash
cd superclean-alt && python -m http.server 5003
```

---

## Regenerating the site

Content lives in Python data files so that copy edits do not mean hand-editing 20
HTML pages. Install the one dependency, then run the pipeline **in this order**:

```bash
pip install beautifulsoup4 lxml
python apply_content.py && python build_services.py && python build_service_page.py && python build_pages.py && python finalize.py && python fix_a11y.py
```

| Script | What it does |
|---|---|
| `apply_content.py` | Swaps template demo content for the real business content |
| `build_services.py` | Builds the oval services grid on the home and services pages |
| `build_service_page.py` | Generates the 15 service pages from `_service_pages.py` |
| `build_pages.py` | Generates `about.html` and `contact.html` |
| `finalize.py` | Nav, footer, testimonials, areas strip, WhatsApp CTAs, favicon, 404 |
| `fix_a11y.py` | Heading order, alt attributes, accessible link names |

### Where the content lives

| File | Contents |
|---|---|
| `_services.py` | The 15 services — slug, card copy, photo. Single source of truth for nav, footer, grids and related links |
| `_service_pages.py` | Deep cleaning page copy, plus merges the four modules below |
| `_pages_property.py` | Post-construction, post-renovation, move-in, move-out |
| `_pages_furniture.py` | Sofa, carpet, mattress |
| `_pages_surfaces.py` | Marble, tile, floor care |
| `_pages_exterior.py` | Window, glass, solar panel, janitorial |
| `finalize.py` | Testimonials, footer areas, contact details |

---

## Deploying

`site/` is static, so any of these work on a free tier:

- **Cloudflare Pages** — recommended. Free tier permits commercial use. Point it
  at this repo and set the output directory to `site`.
- **Netlify** — same approach, publish directory `site`.
- **GitHub Pages** — works, but serves from a subpath unless a custom domain is set.

Both Cloudflare Pages and Netlify serve `/services/deep-cleaning` without the
`.html`, which is why the internal links use `.html` and the canonicals do not.

> Vercel's free Hobby tier is **not** suitable here — its terms restrict it to
> personal, non-commercial projects.

---

## Before this goes live

1. **Replace the testimonials.** The four reviews in `finalize.py` are written,
   not real. Fabricated reviews breach Google's policies and would invalidate
   review schema. Collect real ones via Google Business Profile first.
2. **Set the real brand name, domain and logo.** Update `BRAND` and `SITE_URL`
   in the build scripts; the logo is currently the template's bubble icon.
3. **Replace the photography.** All images are template stock.
4. **Add `sitemap.xml` and `robots.txt`**, then submit to Search Console.
5. **Set up the Google Business Profile.** For local search this matters more
   than the website — the local pack sits above organic results for nearly every
   query in this category.

## Known state

- 20 pages, 925 internal links, 0 broken, 0 missing assets
- 111 WhatsApp deep links, each pre-filled with the relevant service context
- Lighthouse (home, services, about, contact, service pages):
  **Accessibility 100 · Best Practices 100 · SEO 100**
- Performance is not yet optimised — the template ships jQuery and Bootstrap, and
  images are unoptimised. Worth addressing after the design is signed off.
