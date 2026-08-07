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
    "deep-cleaning", "sofa-cleaning", "carpet-cleaning", "rug-cleaning",
    "mattress-cleaning", "office-chair-cleaning", "solar-panel-cleaning",
    "water-tank-cleaning", "swimming-pool-cleaning", "tile-cleaning",
]

# Trust microcopy shown under primary CTAs.
CTA_TRUST = "Replies in minutes &middot; Free on-site inspection &middot; Fixed written quote"

# The CleanCrew promise — replaces fabricated testimonials with verifiable commitments.
PROMISE = [
    ("A fixed written quote before we start",
     "We look at the job first — free — and give you one number in writing. "
     "That number does not change on the day."),
    ("A walkthrough before we leave",
     "You check the work with the supervisor room by room. Anything you flag "
     "gets redone on the spot, not argued about."),
    ("Straight answers before we start",
     "If a stain won't come out fully, we say so before quoting — not after. "
     "If the cheaper service is enough, we tell you that too."),
]

STEPS = [
    ("Message us on WhatsApp",
     "Tell us the service, your area, and roughly how big the job is. Photos "
     "help but aren't required. We reply within minutes, day or night."),
    ("Free inspection, fixed quote",
     "For most jobs we come and look first, free of charge, then give you one "
     "fixed price in writing before any work starts."),
    ("We clean — you check",
     "The team arrives with all machines and materials, works room by room, "
     "and walks you through the finished job before leaving."),
]
