"""Per-service page content.

Only `deep-cleaning` is written out in full for approval. Once the format is
signed off the remaining 14 get the same treatment.

Written for search: each page targets one head keyword plus the Islamabad /
Rawalpindi qualifiers and the sector names people actually type, with real
H2/H3 structure, an inclusions table, pricing factors, area coverage and FAQs.
"""

PAGES = {
    "deep-cleaning": {
        "h1": "Deep Cleaning Services in Islamabad &amp; Rawalpindi",
        "title": "Deep Cleaning Services in Islamabad & Rawalpindi | House & Office Deep Cleaning",
        "meta": ("Professional deep cleaning services in Islamabad and Rawalpindi. "
                 "House and office deep cleaning in DHA, Bahria Town, F & G sectors, "
                 "Saddar and Chaklala. Free inspection, fixed price, available 24/7. "
                 "WhatsApp 0330 2935777."),
        "hero_p": ("A full top-to-bottom clean of your house, apartment or office — "
                   "kitchens, bathrooms, floors, fittings and all the build-up that "
                   "everyday cleaning never reaches. Free inspection first, then one "
                   "fixed price."),
        "h2_intro": "What deep cleaning actually means",
        "h2_included": "What is included in a deep clean",
        "included_intro": ("Every deep clean we quote covers the following as standard. If "
                           "something you need is not on this list, tell us before we quote "
                           "and we will price it in."),
        "intro": [
            "Deep cleaning is not a longer version of your normal weekly clean. It is a "
            "different job. A regular clean keeps surfaces tidy; a deep clean goes after "
            "everything underneath — the grease film on top of kitchen cabinets, the "
            "hard-water scale around taps and shower screens, the grime in tile grout, "
            "the dust sitting on top of fans, vents, skirting boards and door frames, and "
            "the dirt that has worked its way into corners no mop has reached in months.",

            "We provide deep cleaning services across Islamabad and Rawalpindi, for houses, "
            "apartments, offices and commercial units. Most of the deep cleans we do fall "
            "into one of four situations: a home that has not had a thorough clean in six "
            "months or more; a property being prepared before guests, Eid or a family "
            "event; a house that has just been vacated or is about to be moved into; or an "
            "office where the daily cleaner keeps things tidy but the deeper build-up has "
            "never been addressed.",

            "Islamabad and Rawalpindi are dusty cities. Between the construction that never "
            "really stops in the newer sectors and societies, and the dust that blows in "
            "through open windows for most of the year, homes here accumulate a fine grit "
            "on every horizontal surface far faster than they would elsewhere. That is why "
            "a deep clean here needs proper equipment and a systematic room-by-room method, "
            "not a mop and a bottle of surface spray.",
        ],
        "included": [
            "<strong>Kitchen</strong> — cabinets cleaned inside and out, degreasing of "
            "counters, backsplash, hob and extractor hood, sink and taps descaled, "
            "appliance exteriors wiped down, floor scrubbed",
            "<strong>Bathrooms</strong> — full descaling of tiles, grout, glass shower "
            "screens, taps and fittings; WC, basin and tub sanitised; mirrors polished; "
            "drains cleared of surface hair and debris",
            "<strong>Bedrooms and living areas</strong> — dusting from ceiling level down, "
            "including fans, light fittings, vents, curtain rails, door frames, skirting "
            "boards, switches and handles",
            "<strong>Floors</strong> — vacuumed and then machine-scrubbed or mopped "
            "depending on the surface, with grout lines and edges done by hand",
            "<strong>Windows and glass</strong> — interior glass, frames, tracks and sills; "
            "exterior glass where it can be reached safely from inside or from ground level",
            "<strong>Doors, walls and switches</strong> — spot-cleaning of marks and "
            "fingerprints on doors, frames, switch plates and reachable wall areas",
            "<strong>Cobwebs and high dusting</strong> — corners, ceiling edges, and the "
            "tops of wardrobes and cabinets",
            "<strong>Rubbish removal</strong> — all cleaning waste bagged and taken away "
            "with us when we leave",
        ],
        "excluded": [
            "Sofa, carpet, rug and mattress deep cleaning — these need separate machines "
            "and are quoted as their own services",
            "Marble grinding and polishing, which is a heavy machine job",
            "Exterior facade, high-rise or rope-access window cleaning",
            "Water tank cleaning and sewerage or drain unblocking",
            "Moving heavy furniture or appliances — we clean around and behind what can be "
            "moved safely by two people",
            "Painting, plaster repair or any building or handyman work",
            "Pest control and fumigation",
        ],
        "process": [
            ("You tell us the job",
             "Send a WhatsApp or call with the property size in marla or square feet, "
             "how many bedrooms and bathrooms, the area you are in, and roughly when you "
             "need it done. Photos help but are not essential."),
            ("We inspect and quote",
             "For most properties we visit and look at the actual condition before "
             "quoting. That visit is free and there is no obligation. You get one fixed "
             "price covering everything discussed — not an hourly rate that grows."),
            ("We clean, room by room",
             "The team arrives with all machines, chemicals and materials. We work "
             "systematically from the top of each room downwards and finish each room "
             "before moving on, so you can see progress as it happens."),
            ("You check the work",
             "Before the team leaves, you walk through with the supervisor. Anything you "
             "are not happy with gets redone there and then."),
        ],
        "price_factors": [
            ("Size of the property",
             "Measured in marla or square feet, and whether it is single or double storey. "
             "A 5-marla house and a 1-kanal house are very different jobs."),
            ("Condition it is in",
             "A home that is deep cleaned every few months costs less than one that has not "
             "been done in two years, or one where builders have just left."),
            ("Number of kitchens and bathrooms",
             "These two rooms take the longest by a wide margin. A house with four "
             "bathrooms takes far longer than one with two, at the same total area."),
            ("Whether it is furnished or empty",
             "An empty property is quicker — nothing has to be worked around or moved."),
            ("Access and location",
             "Which floor, whether there is a lift, parking availability, and how far the "
             "property is from our base."),
        ],
        "faqs": [
            ("How much does deep cleaning cost in Islamabad?",
             "It depends on the size and condition of the property, so we do not publish a "
             "fixed price list. What we do is come and look at the property free of charge, "
             "then give you one fixed price before any work starts. As a guide, the things "
             "that move the price most are total area in marla, how many kitchens and "
             "bathrooms there are, and whether the property has been maintained or is "
             "coming out of a long period without a proper clean."),
            ("How long does a deep clean take?",
             "For a typical furnished house, expect the better part of a working day. "
             "Smaller apartments are often finished in half a day, while large or badly "
             "neglected properties can run into a second day. We give you a realistic time "
             "estimate with the quote so you can plan around it, and we bring a bigger team "
             "when the deadline is tight."),
            ("Do you bring your own equipment and cleaning materials?",
             "Yes. Machines, chemicals, cloths, mops and protective sheets all come with "
             "the team. You do not need to buy or arrange anything. If you would prefer we "
             "use a specific product you already have — because of an allergy, a delicate "
             "surface or a personal preference — tell us in advance and we will use it."),
            ("Do I need to be at home during the clean?",
             "Someone needs to let the team in and lock up afterwards, and we recommend "
             "you or someone you trust is there at the end for the walkthrough. You do not "
             "need to stay for the whole job. Many customers let us in, go to work, and "
             "come back at the agreed finishing time."),
            ("Are the chemicals safe for children and pets?",
             "Yes. We use standard professional cleaning products and ventilate rooms as we "
             "work. Tell us in advance if anyone in the house has asthma, allergies or "
             "chemical sensitivities, or if you have pets or a baby at home, and we will "
             "adjust what we use and how long the property is aired before you move back in."),
            ("Can you come on the same day?",
             "Often, yes. We work 24 hours a day, seven days a week, and we reply to "
             "WhatsApp messages within minutes during the day. Same-day slots depend on how "
             "many teams are already out, so the earlier you message the better. Urgent "
             "post-construction and move-out deep cleans can usually be arranged at short "
             "notice, including overnight when a handover deadline requires it."),
            ("Do you clean offices as well as homes?",
             "Yes. We deep clean offices, clinics, salons, restaurants and retail units "
             "across both cities. Commercial deep cleans are usually scheduled outside "
             "working hours — evenings, nights or weekends — so your business does not have "
             "to close. If you need regular ongoing cleaning rather than a one-off deep "
             "clean, ask us about janitorial contracts."),
            ("What is the difference between deep cleaning and post-construction cleaning?",
             "A deep clean assumes the property is finished and lived in, and targets "
             "accumulated dirt and grease. Post-construction cleaning deals with a "
             "different problem — fine cement dust in every crack, paint and adhesive "
             "spots, silicone smears on glass, and stickers and protective film on fittings. "
             "It needs more passes and different equipment. If builders have just left the "
             "property, book post-construction cleaning rather than a deep clean."),
        ],
        "areas_intro": (
            "We provide deep cleaning across the whole of Islamabad and Rawalpindi. "
            "These are the areas we work in most often, but if yours is not listed it does "
            "not mean we cannot reach you — send us a message and we will tell you straight "
            "away."),
        "closing_h2": "Book a deep clean in Islamabad or Rawalpindi",
        "closing": [
            "Send us a WhatsApp message with your area, the size of the property and when "
            "you need it done. We will arrange a free inspection, give you one fixed price, "
            "and book a time that works around you — including evenings and weekends.",
            "We answer messages 24 hours a day, and in most cases you will hear back within "
            "minutes.",
        ],
    },
}

# --- merge the rest of the catalogue ---------------------------------------
from _pages_property import PAGES as _P_PROPERTY      # noqa: E402
from _pages_furniture import PAGES as _P_FURNITURE    # noqa: E402
from _pages_surfaces import PAGES as _P_SURFACES      # noqa: E402
from _pages_exterior import PAGES as _P_EXTERIOR      # noqa: E402

PAGES.update(_P_PROPERTY)
PAGES.update(_P_FURNITURE)
PAGES.update(_P_SURFACES)
PAGES.update(_P_EXTERIOR)


AREAS_ISB = [
    "DHA Phase I &amp; II", "Bahria Town Phase 1–8", "Bahria Enclave",
    "F-6", "F-7", "F-8", "F-10", "F-11", "G-9", "G-10", "G-11", "E-11",
    "I-8", "Blue Area", "Gulberg Greens", "Gulberg Residencia",
    "PWD Colony", "Media Town", "Soan Gardens", "Park Road", "Bani Gala",
]

AREAS_RWP = [
    "Saddar", "Rawalpindi Cantt", "Chaklala Scheme III", "Bahria Town Rawalpindi",
    "Askari 10", "Askari 14", "Adiala Road", "Gulraiz", "Satellite Town",
    "Peshawar Road", "Morgah", "Westridge",
]
