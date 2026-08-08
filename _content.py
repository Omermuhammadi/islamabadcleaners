"""Real content for both template options.

Single source of truth. `apply_content.py` reads this and rewrites the HTML in
site/ and option-b/, so the two directions always carry identical copy and
can be judged on design alone.
"""

BRAND = "IslamabadCleaners"
TAGLINE = "Cleaning services in Islamabad &amp; Rawalpindi"
PHONE_DISPLAY = "0330 2935777"
PHONE_TEL = "+923302935777"
WHATSAPP = "923302935777"
EMAIL = "mgcleaner364@gmail.com"
CITIES = "Islamabad &amp; Rawalpindi"
YEARS = "10"
HOURS = "Open 24/7"

WA_TEXT = "Hi%20IslamabadCleaners%2C%20I%27d%20like%20a%20quote%20for%20cleaning."
WA_LINK = f"https://wa.me/{WHATSAPP}?text={WA_TEXT}"

HERO_TITLE = "Professional cleaning services in Islamabad &amp; Rawalpindi"
HERO_SUB = (
    "Deep cleaning, post-construction, sofa, carpet and marble — done properly, "
    "quoted after we see the job. Available 24/7."
)

# --- Services ---------------------------------------------------------------
# 8 headline services for card grids; full list of 15 used for nav/footer.
SERVICES = [
    ("Deep Cleaning",
     "A top-to-bottom clean of your home or office, including the built-up dirt "
     "that regular cleaning never reaches."),
    ("Post-Construction Cleaning",
     "Cement dust, paint spots and builder's debris removed so a new build is "
     "ready to move into."),
    ("Sofa Cleaning",
     "Shampoo and hot-water extraction that lifts dirt and odour out of the "
     "fabric, not just off the surface."),
    ("Carpet Cleaning",
     "Deep extraction and stain treatment for carpets and rugs, with controlled "
     "drying so nothing stays damp."),
    ("Marble Polishing",
     "Grinding, honing and polishing that brings dull, scratched marble floors "
     "and stairs back to a proper shine."),
    ("Mattress Cleaning",
     "Deep sanitising that pulls dust, allergens and sweat residue out of the "
     "mattress layers."),
    ("Window &amp; Glass Cleaning",
     "Streak-free glass inside and out, including frames, tracks, and hard-water "
     "marks on shower screens."),
    ("Solar Panel Cleaning",
     "Safe removal of the dust layer that quietly cuts how much power your "
     "panels actually produce."),
]

ALL_SERVICES = [
    "Deep Cleaning", "Post-Construction Cleaning", "Post-Renovation Cleaning",
    "Move-In Cleaning", "Move-Out Cleaning", "Janitorial Services",
    "Carpet Cleaning", "Sofa Cleaning", "Mattress Cleaning",
    "Window Cleaning", "Glass Cleaning", "Marble Polishing",
    "Tile Cleaning", "Floor Care", "Solar Panel Cleaning",
]

# --- Why choose us (homepage radial section) --------------------------------
# (title, blurb, icon key). First 3 render left of the circle, next 3 right,
# last 2 below it.
WHY_US = [
    ("Certified Professional Cleaners",
     "A trained, supervised crew with proper machines &mdash; the same standard "
     "on every job, not whoever was free that day.", "user"),
    ("Environmentally Friendly Cleaning",
     "Professional products that are safe for children and pets, and we "
     "ventilate as we work.", "leaf"),
    ("100% Satisfaction Guaranteed",
     "You walk through the finished job with the supervisor. Anything you "
     "flag is redone on the spot.", "award"),
    ("One-Stop Convenience",
     "Sofas to solar panels, water tanks to full handovers &mdash; one number "
     "for every cleaning job in the twin cities.", "thumb"),
    ("Police-Checked Professionals",
     "Known, vetted staff who work under a named supervisor on every "
     "visit &mdash; never strangers at your door.", "shield"),
    ("24/7 Customer Support",
     "WhatsApp or call at any hour &mdash; a person replies in minutes, day "
     "or night.", "headset"),
    ("Available Evenings & Weekends",
     "Open 24 hours, 7 days. Overnight office jobs and weekend slots are "
     "routine for us.", "cal"),
    ("Book In 60 Seconds",
     "One WhatsApp message books the job. Send photos and you get a fixed "
     "written price in minutes.", "timer"),
]

# --- Why us -----------------------------------------------------------------
FEATURES = [
    ("Available 24/7",
     "Call or WhatsApp at any hour. We usually reply within minutes and can "
     "often be there the same day."),
    ("We bring everything",
     "Our own machines, chemicals and supplies come with the team. You don't "
     "have to arrange or buy anything."),
    ("The right size crew",
     "We scale the team to the job — one cleaner for a sofa, a full crew for a "
     "post-construction handover."),
]

ABOUT_TITLE = f"{YEARS} years cleaning homes and offices across the twin cities"
ABOUT_BODY = [
    "We are a cleaning company based in Islamabad, working across both "
    "Islamabad and Rawalpindi. We handle one-off jobs like deep cleans, sofas, "
    "carpets and marble, the deadline work that comes with moving or building, "
    "and regular janitorial contracts for offices and clinics.",
    "We bring our own equipment and materials to every job, and we quote in "
    "writing on WhatsApp from your photos and details — so the price we give "
    "you is the price you pay.",
]

# --- FAQ --------------------------------------------------------------------
FAQS = [
    ("Which areas do you cover?",
     "We cover all of Islamabad and Rawalpindi — including DHA, Bahria Town, "
     "Bahria Enclave, the F and G sectors, E-11, Blue Area, Gulberg, PWD and "
     "Media Town, plus Saddar, Cantt, Chaklala Scheme III, Askari and the "
     "Adiala Road area. Message us if your area isn't listed and we'll tell you "
     "straight away."),
    ("How do I get a price?",
     "Send us a WhatsApp with the service you need, your area, roughly how "
     "big the property or item is, and a photo or two if you can. We quote "
     "right there on WhatsApp — one fixed price in writing before any work "
     "starts."),
    ("Why don't you show prices on the website?",
     "Because the same service can cost very differently depending on size and "
     "condition. A 5-marla house cleaned regularly and a 5-marla house after "
     "building work are not the same job. We would rather quote your actual "
     "job from your photos and details than advertise a low figure and change "
     "it on the day."),
    ("Do you bring your own equipment and supplies?",
     "Yes. Machines, chemicals, cloths and everything else comes with the team. "
     "You don't need to provide anything."),
    ("How quickly can you come?",
     "We work 24/7 and reply to messages within minutes during the day. "
     "Same-day slots are often available, and urgent post-construction or "
     "move-out jobs can usually be arranged at short notice."),
    ("Are the chemicals safe for children and pets?",
     "Yes. We use standard professional cleaning products and ventilate as we "
     "work. Tell us in advance if anyone in the house has allergies or "
     "sensitivities and we'll adjust what we use."),
]

# --- Areas ------------------------------------------------------------------
AREAS = [
    "DHA Islamabad", "Bahria Town", "Bahria Enclave", "F-6, F-7 &amp; F-8",
    "F-10 &amp; F-11", "G-9, G-10 &amp; G-11", "E-11", "Blue Area",
    "Gulberg Greens &amp; Residencia", "PWD &amp; Media Town",
    "Saddar &amp; Cantt", "Chaklala Scheme III", "Bahria Town Rawalpindi",
    "Askari &amp; Adiala Road",
]

# --- Testimonials -----------------------------------------------------------
# ⚠️ PLACEHOLDER. These are written to look realistic for the design review.
# They MUST be replaced with real reviews before launch — fabricated reviews
# breach Google's policies and invalidate Review schema.
TESTIMONIALS = [
    ("Ayesha K.", "F-11, Islamabad",
     "Booked a deep clean before Eid. Team arrived on time, brought everything "
     "with them, and the kitchen looked better than when we moved in."),
    ("Bilal R.", "Bahria Town",
     "We had them in after the builders finished. There was cement dust "
     "everywhere and they cleared all of it in a day. Fair price, no arguing."),
    ("Hina M.", "DHA Phase 2",
     "Two sofas and a carpet. The smell from the sofas is completely gone and "
     "the colour came back. Replied on WhatsApp within a few minutes."),
    ("Usman T.", "Chaklala, Rawalpindi",
     "Used them for our office. They come regularly now. Reliable, and the "
     "supervisor actually checks the work."),
    ("Ayesha S.", "F-10, Islamabad",
     "Very professional team. They cleaned the whole house in one visit and "
     "the price was exactly what they quoted on WhatsApp."),
    ("Basit A.", "G-9, Islamabad",
     "Quick reply on WhatsApp and the team came the same day. Sofa cleaning "
     "was done in two hours. Highly recommended."),
]

STATS = [
    ("24/7", "Available every day"),
    (YEARS + "+", "Years in the twin cities"),
    ("15", "Cleaning services"),
    ("2", "Cities covered"),
]
