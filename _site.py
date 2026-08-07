"""Site-wide configuration — the single source of truth.

Change BASE_URL here (e.g. when a real domain is bought), run `python build.py`,
and every canonical, og:url, schema id, sitemap entry and robots.txt updates.
"""

BASE_URL = "https://effendii69.github.io/cleancrew"  # no trailing slash

BRAND = "CleanCrew"
PHONE_DISPLAY = "0330 2935777"
PHONE_TEL = "+923302935777"
WHATSAPP = "923302935777"
EMAIL = "mgcleaner364@gmail.com"

# Pre-filled WhatsApp messages (URL-encoded at build time).
WA_GENERIC = "Hi CleanCrew, I'd like a quote for cleaning in Islamabad / Rawalpindi."

# The 10 services featured on the homepage grid, in display order.
HOME_FEATURED = [
    "deep-cleaning", "house-cleaning", "sofa-cleaning", "carpet-cleaning",
    "rug-cleaning", "dining-chair-cleaning", "office-chair-cleaning",
    "mattress-cleaning", "solar-panel-cleaning", "water-tank-cleaning",
    "swimming-pool-cleaning", "tile-cleaning",
]

# Trust microcopy shown under primary CTAs.
CTA_TRUST = "Replies in minutes &middot; Fixed quote on WhatsApp &middot; No hidden charges"

# The CleanCrew promise — replaces fabricated testimonials with verifiable commitments.
PROMISE = [
    ("A fixed written quote before we start",
     "You get one number on WhatsApp, in writing, before we arrive. It does "
     "not change on the day unless the job differs from what you described."),
    ("A walkthrough before we leave",
     "You check the work with the supervisor room by room. Anything you flag "
     "gets redone on the spot, not argued about."),
    ("Straight answers before we start",
     "If a stain won't come out fully, we say so before quoting — not after. "
     "If the cheaper service is enough, we tell you that too."),
]

STEPS = [
    ("Message us on WhatsApp",
     "Tell us the service, your area, and roughly how big the job is. A "
     "couple of photos get you the most accurate price. We reply in minutes."),
    ("Get a fixed price in writing",
     "We quote right there on WhatsApp — one fixed number before any work "
     "starts, not an estimate that grows on the day."),
    ("We clean — you check",
     "The team arrives with all machines and materials, works room by room, "
     "and walks you through the finished job before leaving."),
]
