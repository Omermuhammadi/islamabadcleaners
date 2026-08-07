"""Service page content — new services group.

Water tank, swimming pool, rug and office chair cleaning. Same schema and
voice as _service_pages.py; `deep-cleaning` is the canonical example.
"""

PAGES = {

    # --------------------------------------------------------- water tank
    "water-tank-cleaning": {
        "h1": "Water Tank Cleaning in Islamabad &amp; Rawalpindi",
        "title": "Water Tank Cleaning in Islamabad & Rawalpindi | Overhead & Underground Tanks",
        "meta": ("Water tank cleaning in Islamabad & Rawalpindi. Overhead & underground "
                 "tanks scrubbed and disinfected. Fixed price on WhatsApp, 24/7. "
                 "WhatsApp 0330 2935777."),
        "hero_p": ("Overhead and underground water tanks emptied, scrubbed down to the "
                   "walls and floor, then disinfected — so the water your family drinks "
                   "and bathes in is not sitting on a layer of sludge."),
        "h2_intro": "Why water tanks here need cleaning every year",
        "h2_included": "What is included in a water tank clean",
        "included_intro": ("This is what every tank clean covers, whether it is a rooftop "
                           "plastic tank on a 5-marla house or a large underground "
                           "concrete tank under a kanal home or plaza."),
        "intro": [
            "The water that reaches homes in Islamabad and Rawalpindi — whether from "
            "CDA or WASA lines, a bore, or tanker deliveries — carries fine sediment "
            "with it. Sand, silt, rust particles from old supply pipes and organic "
            "matter all settle to the bottom of your tank, because a tank is exactly "
            "what a settling basin is: still water in a dark container. Over a year "
            "that becomes a visible layer of sludge on the floor, a slippery biofilm "
            "on the walls, and in warm months a breeding environment for bacteria and "
            "algae. Every glass of water, every shower and every pot of food in the "
            "house passes through that tank.",

            "Most houses here have two tanks working as a pair — an underground tank "
            "that receives the supply, and an overhead tank on the roof that the motor "
            "pumps up to. Both need cleaning, and the underground one is usually worse "
            "because it is lower, darker and never looked at. We clean both types, in "
            "both materials: moulded plastic tanks and cast concrete tanks, which need "
            "different handling because concrete is porous and rough-walled while "
            "plastic scratches if scrubbed with the wrong tools.",

            "The signs people usually notice first are a smell or slight taste in the "
            "water, sediment in the bottom of a glass left standing, staining in "
            "toilets and around taps, or a family member with a stomach bug that keeps "
            "coming back. By that point the tank is overdue. Done yearly — or every "
            "six months where tanker water is used — a tank clean is a quick, "
            "unremarkable job rather than a rescue.",
        ],
        "included": [
            "<strong>Draining</strong> — the tank pumped or drained down, with the "
            "remaining water and sludge removed from the floor rather than left to "
            "dilute back in",
            "<strong>Sludge and sediment removal</strong> — the settled layer on the "
            "tank floor scooped and vacuumed out and taken away, not flushed into "
            "your drainage",
            "<strong>Wall and floor scrubbing</strong> — biofilm, algae and scale "
            "scrubbed off all interior surfaces, with brushes matched to the tank "
            "material so plastic is not scratched and concrete is properly worked",
            "<strong>Corners, joints and fittings</strong> — inlet, outlet, overflow "
            "and float valve areas cleaned by hand, where growth concentrates",
            "<strong>High-pressure rinse</strong> — all loosened material washed off "
            "the surfaces and removed",
            "<strong>Disinfection</strong> — the interior treated with a "
            "chlorine-based disinfectant at drinking-water-safe dosage, left for "
            "contact time, then rinsed",
            "<strong>Final rinse and inspection</strong> — the tank rinsed until the "
            "water runs clear, and you are shown the inside before the lid goes back on",
            "<strong>Lid and surround</strong> — the tank lid cleaned and reseated "
            "properly, and the area around the opening left clean",
        ],
        "excluded": [
            "Repair of cracked tanks, leaking joints or broken lids — we will point "
            "out damage we find, but repair is a plumber's job",
            "Replacement or repair of float valves, motors and supply plumbing",
            "Waterproofing or re-plastering of concrete tanks",
            "Water quality laboratory testing — we clean and disinfect the tank, but "
            "certified testing of the supply itself is a separate specialist service",
            "Unblocking of supply or drainage lines",
            "Cleaning of tanks that are structurally unsafe to enter — we will tell "
            "you on the day if a tank cannot be worked in safely",
        ],
        "process": [
            ("Tell us about your tanks",
             "Send a WhatsApp with how many tanks you have, roughly what size, whether "
             "they are overhead or underground, plastic or concrete, and your area. If "
             "you do not know the sizes, that is fine — a photo of each tank is "
             "usually enough for us to judge."),
            ("You get a fixed price on WhatsApp",
             "We may ask a question or two, then send one fixed price in writing "
             "before any work starts — and it does not change on the day unless the "
             "tanks differ from what you described. If a tank is in good enough "
             "condition that it can wait, we will say so honestly."),
            ("Drain, scrub, disinfect",
             "We time the job so you are without water for as short a period as "
             "possible — usually a few hours. The tank is drained, the sludge removed, "
             "every surface scrubbed and rinsed, then disinfected and rinsed again."),
            ("Refill and check",
             "You see the inside of the tank before it is closed, the tank refills "
             "from your supply as normal, and we advise a brief first flush of the "
             "taps before use."),
        ],
        "price_factors": [
            ("Number and size of tanks",
             "A single rooftop tank on a 5-marla house is a much smaller job than the "
             "paired underground and overhead tanks of a kanal house or a plaza's "
             "large storage tank. Capacity in gallons or litres is the starting point."),
            ("Underground versus overhead",
             "Underground tanks take longer — access is through a small hatch, the "
             "sludge layer is usually heavier, and water and waste have to be pumped "
             "out rather than drained by gravity."),
            ("Condition inside",
             "A tank cleaned every year is a quick scrub. One that has never been "
             "opened since the house was built can carry years of compacted sludge "
             "and needs considerably more time."),
            ("Material",
             "Concrete tanks are porous and rough, so scrubbing and rinsing take "
             "longer than on a smooth plastic tank of the same size."),
            ("Access",
             "Roof access, hatch size, and whether the tank location allows our "
             "pumps and hoses to reach easily all affect the time on site."),
        ],
        "faqs": [
            ("How much does water tank cleaning cost in Islamabad?",
             "It depends on how many tanks you have, their capacity, whether they are "
             "overhead or underground, and the condition inside — a tank cleaned last "
             "year is a very different job from one untouched for a decade. We do not "
             "quote blind: send the tank details and a photo or two on WhatsApp and "
             "we give you one fixed price in writing before any work starts. For most houses, cleaning "
             "both tanks together costs less than booking them separately, so we "
             "usually recommend doing the pair in one visit."),
            ("How often should overhead and underground tanks be cleaned?",
             "Once a year is the sensible minimum for most homes on CDA or WASA "
             "supply. If you receive tanker water regularly, every six months, "
             "because tanker water tends to carry more sediment. The underground "
             "tank generally needs it more than the overhead one — it is the first "
             "stop for incoming water, so most of the silt settles there. Many of our "
             "customers simply book both tanks annually before summer, when water "
             "use and bacterial growth both peak."),
            ("How long is the water off during cleaning?",
             "Usually a few hours per tank. We drain, clean, disinfect and rinse in "
             "one continuous visit, and the tank starts refilling from your supply as "
             "soon as we finish. If your motor and supply timing mean refilling is "
             "slow, tell us and we will schedule the clean around your supply hours "
             "so the tank fills again the same day. For offices and plazas we can "
             "work at night so nobody is affected."),
            ("Is the disinfectant safe for drinking water?",
             "Yes. We use chlorine-based disinfection at dosages meant for potable "
             "water tanks — the same approach used for municipal supply, not "
             "industrial chemicals. The disinfectant is given its contact time and "
             "then rinsed out before the tank is refilled. We advise running the taps "
             "briefly when supply resumes to flush the lines. If anyone in the house "
             "is particularly sensitive to chlorine smell, mention it and we will "
             "rinse more thoroughly and advise on the first day's use."),
            ("Do you clean both plastic and concrete tanks?",
             "Yes, and they are handled differently. Plastic tanks have smooth walls "
             "that clean up well but scratch if attacked with harsh abrasives, so we "
             "use soft-bristle tools on them — scratches give bacteria somewhere to "
             "anchor. Concrete tanks are porous and rough, which means biofilm sits "
             "deeper in the surface and needs firmer scrubbing and a longer rinse. "
             "Both end with the same disinfection step. If your concrete tank's "
             "plaster is failing, we will show you and suggest waterproofing before "
             "it becomes a leak."),
            ("Can you tell how dirty the tank is without opening it?",
             "Not reliably, and neither can you — which is exactly the problem with "
             "tanks. The useful signs are indirect: sediment settling in a glass of "
             "water left standing, a smell from the taps after the water has been off, "
             "or brown staining in cisterns and around fittings. If you can lift the "
             "lid safely, a quick photo of the inside sent on WhatsApp tells us "
             "everything we need — and if the tank does not need cleaning yet, we "
             "will say so rather than clean it for the sake of it."),
            ("Do you clean tanks for offices, plazas and apartment buildings?",
             "Yes. Commercial and shared tanks are a big part of this work — plazas "
             "in Blue Area and Saddar, apartment buildings in E-11 and Bahria Town, "
             "offices, schools and clinics. Shared tanks serve more people and cycle "
             "more water, so they load up with sediment faster than a house tank. We "
             "schedule these jobs at night or on weekends so the building is not left "
             "without water during working hours, and for buildings we can set up a "
             "recurring schedule so it never gets forgotten."),
            ("What happens to the sludge you remove?",
             "It leaves with us. The sludge is scooped and pumped into containers and "
             "taken away, not washed into your drains — a wet sludge load flushed "
             "into a house's drainage is a good way to cause the blockage you were "
             "trying to avoid. The rinse water from the final stages is clean enough "
             "to go to drainage normally. When we leave, the tank area, roof or "
             "basement is left as clean as we found it."),
        ],
        "areas_intro": (
            "We clean water tanks across the whole of Islamabad and Rawalpindi — "
            "houses, apartment buildings, offices and plazas. These are the areas we "
            "work in most often, but if yours is not listed, send us a message and we "
            "will tell you straight away."),
        "closing_h2": "Book a water tank clean in Islamabad or Rawalpindi",
        "closing": [
            "Send us a WhatsApp with your area, how many tanks you have and roughly "
            "their size if you know it — a photo of each tank helps. We will send "
            "one fixed price in writing for the job before any work starts.",
            "We answer messages 24 hours a day, and in most cases you will hear back "
            "within minutes.",
        ],
    },

    # ------------------------------------------------------- swimming pool
    "swimming-pool-cleaning": {
        "h1": "Swimming Pool Cleaning in Islamabad &amp; Rawalpindi",
        "title": "Swimming Pool Cleaning in Islamabad & Rawalpindi | Green Pool Recovery & Weekly Service",
        "meta": ("Swimming pool cleaning in Islamabad & Rawalpindi. Green pool "
                 "recovery after monsoon, weekly service, water balancing. Fixed "
                 "price on WhatsApp. WhatsApp 0330 2935777."),
        "hero_p": ("From a green, algae-filled pool brought back to swimmable, to a "
                   "weekly service that keeps it that way — vacuuming, filters, "
                   "skimming and properly balanced water."),
        "h2_intro": "Why pools here go green, and what it takes to fix",
        "h2_included": "What is included in a pool clean",
        "included_intro": ("A one-off restoration and a regular service visit share the "
                           "same checklist — the difference is how much of each step is "
                           "needed. This is what we cover."),
        "intro": [
            "A swimming pool in Islamabad or Rawalpindi fights two enemies most of "
            "the year: dust and monsoon. The dust that settles on every car and "
            "windowsill here settles on your pool too, sinking to the floor as a "
            "grey film and feeding the filter a constant load. Then the monsoon "
            "arrives — warm water, heavy organic debris washed in by rain, and "
            "humidity — and any pool whose chlorine level slips for even a few days "
            "turns green. Algae does not build up gradually; once it blooms, a pool "
            "can go from clear to opaque green in a weekend.",

            "Bringing a green pool back is a different job from keeping a clear pool "
            "clear. A restoration means shocking the water to kill the bloom, "
            "brushing algae off the walls and floor, vacuuming the dead material out "
            "to waste rather than through the filter, cleaning or backwashing the "
            "filter itself — which will be loaded — and then rebalancing the water "
            "chemistry so the problem does not simply return the following week. "
            "Depending on how far gone the water is, that can take more than one "
            "visit.",

            "Once a pool is clear, keeping it that way is routine: skimming, "
            "vacuuming, emptying skimmer and pump baskets, checking the filter and "
            "testing and adjusting the water. That is the weekly service we run for "
            "houses in DHA, Bahria Town and Bani Gala, guest houses, and gyms and "
            "clubs — so the owner never has to think about the pool except to swim "
            "in it. Most restoration calls we get come right after the first monsoon "
            "rains and just before summer opening; both are avoidable with a regular "
            "schedule.",
        ],
        "included": [
            "<strong>Surface skimming</strong> — leaves, insects and floating debris "
            "netted off before they sink and start to decay",
            "<strong>Wall and floor brushing</strong> — tiles and plaster brushed to "
            "dislodge algae and the dust film before vacuuming",
            "<strong>Pool vacuuming</strong> — the floor vacuumed thoroughly, to "
            "waste rather than through the filter when there is heavy algae or "
            "sediment",
            "<strong>Skimmer and pump baskets</strong> — emptied and rinsed so "
            "circulation is not choked",
            "<strong>Filter service</strong> — sand filters backwashed and cartridge "
            "filters removed and cleaned, with an honest word if the media is due "
            "for replacement",
            "<strong>Water testing and balancing</strong> — chlorine and pH tested "
            "and adjusted, because clear water is chemistry as much as cleaning",
            "<strong>Shock treatment</strong> — chlorine shock dosing for green or "
            "cloudy water, with retesting before the pool is declared swimmable",
            "<strong>Waterline and surrounds</strong> — the scum line at the "
            "waterline scrubbed, and the immediate pool surround left tidy",
        ],
        "excluded": [
            "Repair of pumps, motors, pipework, underwater lights or leaking pools — "
            "we will diagnose what we can see and tell you what a technician needs "
            "to fix",
            "Re-tiling, re-plastering or structural work on the pool shell",
            "Replacement filter media, pumps or parts — we can advise on what to buy "
            "but supply of major parts is quoted separately",
            "Draining and acid-washing of pools, which is quoted as its own job when "
            "a pool is too far gone to recover chemically",
            "Landscaping, lawn or terrace cleaning beyond the immediate pool surround",
            "Fountains and large decorative water bodies — ask us, some we can do, "
            "and we will say honestly if one is outside our scope",
        ],
        "process": [
            ("Tell us about the pool",
             "Send a WhatsApp with the approximate pool size, whether it is "
             "currently clear, cloudy or green, and your area. A photo of the water "
             "tells us more than a paragraph — send one if you can."),
            ("You get a fixed price on WhatsApp",
             "From your photo and details we quote either a one-off restoration or "
             "a weekly service, whichever the pool actually needs — one fixed price "
             "in writing before we start. If the water is too far gone and needs a "
             "drain and acid wash, we say so upfront rather than selling you "
             "chemical treatments that will not work."),
            ("Restore or service",
             "A green pool gets shocked, brushed, vacuumed to waste and rebalanced — "
             "sometimes over two or three visits as the water clears. A maintained "
             "pool gets its full weekly routine in a single visit."),
            ("Keep it that way",
             "Most customers move onto a weekly or twice-weekly schedule after a "
             "restoration, especially through monsoon. We handle everything on a "
             "fixed monthly rate so the pool stays swimmable without you touching it."),
        ],
        "price_factors": [
            ("Pool size and volume",
             "Chemical dosing, brushing and vacuuming time all scale with the "
             "surface area and volume of water. A small residential plunge pool and "
             "a full-length pool at a farmhouse or club are very different jobs."),
            ("Current condition of the water",
             "A clear pool needing routine service is the base case. Cloudy water "
             "costs more, and a fully green pool with an established bloom costs the "
             "most, because it needs shock dosing, repeated brushing and often more "
             "than one visit."),
            ("One-off or regular service",
             "Weekly service is priced as a fixed monthly rate and works out far "
             "cheaper per visit than one-off calls, because a maintained pool never "
             "needs rescue work."),
            ("Filter and equipment condition",
             "A functioning filter does half the work. If the filter media is dead "
             "or the pump barely circulates, cleaning takes longer and results do "
             "not hold — we will tell you honestly if equipment is the real problem."),
            ("Location and access",
             "Rooftop pools, basement pools and pools at farmhouses on the edges of "
             "the cities affect travel and how we get equipment to the waterside."),
        ],
        "faqs": [
            ("How much does swimming pool cleaning cost in Islamabad?",
             "It depends on the pool's size and, above all, the state of the water. "
             "Routine service on a maintained pool is quick and predictable, so "
             "weekly service on a monthly rate is the cheapest way to run a pool. A "
             "green pool restoration costs more because it involves shock chemicals, "
             "repeated brushing and vacuuming, and often two or three visits before "
             "the water is fully clear. Send a photo of the water on WhatsApp and "
             "we give you a fixed price for a restoration, or a fixed monthly rate "
             "for ongoing service, in writing before anything starts."),
            ("My pool has turned green after the rains — can it be saved?",
             "Almost always, yes. Monsoon algae blooms look dramatic but respond "
             "well to a proper shock treatment followed by brushing and vacuuming "
             "the dead algae out to waste. Expect the recovery to take several days "
             "and possibly more than one visit — the water clears in stages, not "
             "hours. The only pools we recommend draining are ones that have been "
             "green for months with heavy debris rotting on the floor; in that case "
             "an acid wash is more honest than an endless chemical battle, and a "
             "photo of the water and the pool floor tells us which situation yours "
             "is."),
            ("How often does a pool need cleaning here?",
             "Through summer and monsoon — roughly April to September — weekly at "
             "minimum, and twice weekly for heavily used pools or those under trees. "
             "The combination of heat, dust and rain-washed debris means chlorine is "
             "consumed fast and a missed week is how blooms start. In winter, when "
             "most pools here are unused, a fortnightly visit keeps the water and "
             "equipment healthy so spring opening is a quick job rather than a full "
             "restoration."),
            ("Are the pool chemicals safe for children?",
             "Yes, when dosed and given time correctly — the chemicals we use are "
             "standard pool chlorine and balancers, the same class of products every "
             "properly run pool in the world uses. What matters is dosage and "
             "waiting time: after a routine service the pool is swimmable almost "
             "immediately, but after a shock treatment it must not be used until the "
             "chlorine level has dropped back into the safe range. We test before "
             "declaring it swimmable and we tell you clearly when the pool can be "
             "used, rather than leaving you to guess."),
            ("Do you clean and service the filter as well?",
             "Yes — the filter is half the pool. Sand filters get backwashed and "
             "rinsed, cartridge filters are removed and cleaned, and skimmer and "
             "pump baskets are emptied every visit. If the sand is exhausted or a "
             "cartridge is beyond cleaning, we tell you and can advise on "
             "replacement. A pool with a dead filter cannot be kept clear no matter "
             "how much chemical goes in, so we would rather flag an equipment "
             "problem early than keep charging you for cleaning that cannot hold."),
            ("Do you offer a regular weekly pool service?",
             "Yes, and it is most of our pool work. A fixed monthly rate covers "
             "scheduled visits — usually weekly, or twice weekly in peak season — "
             "with skimming, brushing, vacuuming, basket and filter care, and water "
             "testing and balancing every time. Houses in DHA, Bahria Town and Bani "
             "Gala, guest houses and gyms all run on this basis. The point of the "
             "schedule is that you never see the pool anything other than clear, and "
             "you never pay for a rescue job again."),
            ("Do you handle pools for gyms, clubs and guest houses?",
             "Yes. Commercial pools carry heavier bather loads, which means faster "
             "chlorine consumption and stricter hygiene requirements than a family "
             "pool. We service these on fixed schedules, keep the water tested and "
             "balanced, and can time visits for early mornings before opening so "
             "guests never see the work happening. For commercial pools we can "
             "arrange a site visit first if photos are not enough to quote from. "
             "If your pool serves paying customers, a documented regular service "
             "is also your answer when anyone asks how the water is maintained."),
            ("Can you get my pool ready before an event or for summer opening?",
             "Yes — pre-summer openings and pre-event calls are our two busiest "
             "kinds of pool booking. The one thing we ask is time: if the pool has "
             "been sitting green all winter, message us a week or more before the "
             "date, not the day before, because water clears chemically over days "
             "and no honest company can turn an opaque green pool into a swimmable "
             "one overnight. Given a reasonable head start, we will have it clear, "
             "balanced and ready on the day."),
        ],
        "areas_intro": (
            "We clean and service swimming pools across Islamabad and Rawalpindi — "
            "houses, farmhouses, guest houses, gyms and clubs. These are the areas "
            "we work in most often, but if yours is not listed, send us a message "
            "and we will tell you straight away."),
        "closing_h2": "Book pool cleaning in Islamabad or Rawalpindi",
        "closing": [
            "Send us a WhatsApp with your area, the approximate pool size and a "
            "photo of the water as it looks now. We will quote either a one-off "
            "restoration or a fixed monthly service in writing — whichever the "
            "pool actually needs.",
            "We answer messages 24 hours a day, and in most cases you will hear "
            "back within minutes.",
        ],
    },

    # ---------------------------------------------------------------- rugs
    "rug-cleaning": {
        "h1": "Rug Cleaning in Islamabad &amp; Rawalpindi",
        "title": "Rug Cleaning in Islamabad & Rawalpindi | Qaleen & Oriental Rug Washing",
        "meta": ("Rug cleaning in Islamabad & Rawalpindi. Qaleen, oriental and "
                 "machine-made rugs colour-tested, at home or with pickup. Fixed "
                 "price on WhatsApp. WhatsApp 0330 2935777."),
        "hero_p": ("Careful cleaning for qaleen, oriental and machine-made rugs — "
                   "colour-tested before anything touches the pile, cleaned at your "
                   "home or collected, and dried properly so the backing never stays "
                   "wet."),
        "h2_intro": "Rugs are not carpets — and should not be cleaned like them",
        "h2_included": "What is included in a rug clean",
        "included_intro": ("Every rug is assessed individually before cleaning. This is "
                           "what the service covers, whether the rug is done at your "
                           "home or collected."),
        "intro": [
            "A rug is not a small carpet, and treating it like one is how rugs get "
            "ruined. Wall-to-wall carpet is a uniform synthetic product, fixed to "
            "the floor, built to take aggressive hot-water extraction. A rug — a "
            "hand-knotted qaleen, an oriental or Afghan piece, a silk-blend runner, "
            "or even a good machine-made rug — is a loose textile with its own "
            "fibres, its own dyes and its own construction. Wool and silk need "
            "gentler chemistry and lower temperatures than nylon. Vegetable and "
            "cheaper synthetic dyes can bleed the moment hot water hits them. A "
            "heavy rug that stays wet in its foundation can develop mildew or dry "
            "stiff. If you have wall-to-wall carpet, see our carpet cleaning "
            "service — this page is about the loose pieces.",

            "Our process starts with identification and testing. We look at the "
            "fibre, the construction and the dyes, and we test a hidden corner for "
            "colour-fastness before any solution touches the visible pile. That "
            "test decides everything that follows: which chemistry we use, how much "
            "moisture the rug can take, and whether it can be cleaned in place at "
            "your home or needs to be collected and washed at our facility where "
            "drying can be controlled properly. An honest company tells you which "
            "your rug needs; a careless one puts a hot extraction wand on a "
            "seventy-year-old qaleen and hopes.",

            "Rugs here take a particular beating. Islamabad's dust settles into the "
            "pile continuously and grinds at the fibre base every time the rug is "
            "walked on, and in most homes rugs sit in the busiest rooms — under "
            "sofas and dining tables, in drawing rooms that fill up at Eid. Most of "
            "the rugs we clean come to us before Eid and family events, after a "
            "spill on a good piece, or when a rug comes out of storage smelling of "
            "damp. Whatever the trigger, the rug is inspected first and you get a "
            "straight answer about what cleaning will and will not achieve.",
        ],
        "included": [
            "<strong>Fibre and dye identification</strong> — wool, silk, cotton "
            "foundation or synthetic, hand-knotted or machine-made, checked before "
            "anything else is decided",
            "<strong>Colour-fastness test</strong> — a hidden corner tested with the "
            "intended solution, so bleeding dyes are found before they can ruin the "
            "visible pile",
            "<strong>Dry soil removal</strong> — thorough dusting and deep vacuuming "
            "of both faces, because the grit at the fibre base does more damage than "
            "any stain",
            "<strong>Stain pre-treatment</strong> — food, drink, oil and traffic "
            "marks treated individually with chemistry matched to the fibre",
            "<strong>Washing or low-moisture cleaning</strong> — full wash for rugs "
            "that can take it, controlled low-moisture extraction for delicate "
            "pieces cleaned in place",
            "<strong>Fringe cleaning</strong> — fringes cleaned and detangled "
            "separately, since they are usually cotton even on a wool rug and "
            "grey first",
            "<strong>Controlled drying</strong> — the rug dried flat or hung with "
            "air movement until the foundation, not just the pile, is dry",
            "<strong>Final grooming and inspection</strong> — pile brushed to lie "
            "correctly, and the rug checked with you on return or before we leave",
        ],
        "excluded": [
            "Repair work — rebinding edges, securing fringes, patching holes or "
            "moth damage; we can point you to repair specialists but do not do the "
            "needlework ourselves",
            "Guaranteed removal of old set stains, dye bleed that has already "
            "happened, or sun fading — fading is fibre damage, not dirt",
            "Restoration of antique or museum-grade pieces beyond careful cleaning — "
            "if a rug is too fragile to clean safely, we will tell you rather than "
            "risk it",
            "Wall-to-wall fitted carpet, which is a separate service with its own "
            "process and pricing",
            "Moth treatment and fumigation, though we will show you the evidence if "
            "we find moth activity",
            "Underlay and floor cleaning beneath the rug, unless booked alongside as "
            "part of a floor or deep cleaning job",
        ],
        "process": [
            ("Tell us about the rug",
             "Send a WhatsApp with the rug's approximate size, what you know about "
             "it — hand-knotted or machine-made, wool or silk — and a photo. Photos "
             "of any stains help us give a realistic answer before we quote."),
            ("You get a fixed price on WhatsApp",
             "From your photos we tell you whether the rug is best cleaned at home "
             "or collected for a full wash, and send one fixed price in writing "
             "either way. On the day we identify the fibre and construction and "
             "test a hidden corner for colour-fastness before anything touches the "
             "visible pile."),
            ("Clean the right way for that rug",
             "Delicate pieces get gentle chemistry and controlled moisture; sturdy "
             "machine-made rugs get a deeper wash. Fringes are done separately, and "
             "stains are treated individually before the main clean."),
            ("Dry fully, then return",
             "The rug is dried until the foundation is dry right through — the step "
             "most often skipped, and the cause of most mildew smells. Collected "
             "rugs are returned rolled and ready to lay; rugs cleaned at home are "
             "left with drying arranged and instructions for when to walk on them."),
        ],
        "price_factors": [
            ("Size of the rug",
             "Measured by area. A small prayer-mat-sized piece and a room-filling "
             "12-by-9 qaleen are priced very differently."),
            ("Fibre and construction",
             "Silk and fine hand-knotted pieces need slower, gentler work than a "
             "synthetic machine-made rug, and that time is reflected in the price."),
            ("Condition and staining",
             "General dust and traffic greying is the base case. Heavy staining, pet "
             "accidents or smoke odour need extra treatment passes."),
            ("At home or collected",
             "In-place cleaning avoids transport but limits how wet the rug can get. "
             "Collection for a full wash includes pickup and delivery and suits rugs "
             "that need deeper work or careful drying."),
            ("Number of rugs",
             "Several rugs done in one booking cost less per rug than separate "
             "visits — many customers do the whole house's rugs before Eid in one go."),
        ],
        "faqs": [
            ("How much does rug cleaning cost in Islamabad?",
             "The main factors are the rug's size, its fibre and construction, and "
             "its condition. A machine-made synthetic rug is quicker and cheaper to "
             "clean than a fine hand-knotted wool or silk piece of the same size, "
             "which needs gentler chemistry and slower work. Whether the rug is "
             "cleaned at home or collected for a full wash also affects the price. "
             "Send photos of the rug on WhatsApp and we give you one fixed price "
             "in writing before anything starts, and if you have several rugs, one "
             "booking for all of them costs less than doing them separately."),
            ("Can you clean the rug at home or do you take it away?",
             "Both, and the rug decides which. Sturdy machine-made and most wool "
             "rugs in reasonable condition can be cleaned in place at your home "
             "with controlled moisture, and dry within the day. Rugs that need a "
             "deeper wash — heavy soiling, pet accidents, odour in the foundation — "
             "and delicate pieces that need careful drying are better collected, "
             "washed at our facility, dried fully and returned. We tell you which "
             "your rug needs when you send the photos, with the reasons, and "
             "collection includes pickup and delivery back to your door."),
            ("Will the colours run?",
             "This is the right question to ask, and the reason we test before we "
             "clean. Some rugs — particularly older pieces and some Afghan and "
             "Iranian dyes — will bleed if hit with hot water or the wrong "
             "chemistry. We test a hidden corner with the intended solution and "
             "wait for the result before touching the visible pile. If the dyes are "
             "not stable, we switch to a gentler cold-process method, and if a rug "
             "cannot be cleaned safely at all, we hand it back and say so. What we "
             "do not do is find out about bleeding dyes in the middle of your rug."),
            ("Do you clean hand-knotted qaleen and oriental rugs?",
             "Yes — they are the reason this is a separate service rather than a "
             "line on the carpet page. Hand-knotted qaleen, Afghan, Iranian and "
             "other oriental pieces are cleaned according to their fibre and dye "
             "behaviour: gentle chemistry, controlled moisture, fringes done "
             "separately by hand, and drying continued until the cotton foundation "
             "is dry right through. We will also tell you honestly if a piece is "
             "too fragile or too valuable to clean without a specialist restorer — "
             "that happens rarely, but when it does you deserve a straight answer."),
            ("How long does a rug take to dry?",
             "A rug cleaned in place with low-moisture methods is walkable the same "
             "day, usually within a few hours. A fully washed rug takes one to two "
             "days to dry properly at our facility, because the foundation holds "
             "water long after the pile feels dry — and returning a rug with a damp "
             "foundation is how mildew smells start. In humid monsoon weeks, drying "
             "takes longer, and we would rather keep the rug an extra day than "
             "return it damp. We give you the expected return date when we collect."),
            ("What is the difference between this and your carpet cleaning service?",
             "Carpet cleaning covers wall-to-wall fitted carpet — a uniform "
             "synthetic surface, cleaned in place with hot-water extraction, dried "
             "where it lies. Rug cleaning covers loose pieces, which vary hugely in "
             "fibre, dye and construction and often cannot take that treatment. The "
             "processes, the chemistry and the risks are different, which is why "
             "they are separate services. If you have both — fitted carpet plus "
             "rugs laid over it, which is common here — we can quote and do both in "
             "one booking."),
            ("Can you remove the smell from a rug that was in storage?",
             "Usually, yes. A musty smell from storage is normally mildew activity "
             "from the rug being stored with some moisture in it, and a full wash "
             "with proper drying removes it in most cases. What we check first is "
             "whether the mildew has damaged the foundation or the dyes — if the "
             "cotton base has rotted, cleaning cannot reverse that, and we will "
             "show you what we find. We also check stored rugs for moth activity, "
             "which is common in wool rugs stored unwrapped, and tell you if we "
             "find it before it spreads to other textiles in the house."),
            ("How often should rugs be cleaned?",
             "For rugs in daily-use rooms, once a year is a good rhythm — the dust "
             "load in Islamabad and Rawalpindi means grit builds at the fibre base "
             "faster than in cleaner climates, and that grit abrades the pile every "
             "time the rug is walked on. Between cleans, vacuum without the beater "
             "bar on delicate pieces and rotate the rug occasionally so wear and "
             "sunlight spread evenly. Most of our customers book all their rugs "
             "once a year, usually in the weeks before Eid or before winter guests."),
        ],
        "areas_intro": (
            "We clean rugs across the whole of Islamabad and Rawalpindi — at your "
            "home or with pickup and delivery. These are the areas we work in most "
            "often, but if yours is not listed, send us a message and we will tell "
            "you straight away."),
        "closing_h2": "Book rug cleaning in Islamabad or Rawalpindi",
        "closing": [
            "Send us a WhatsApp with your area, the number and rough sizes of the "
            "rugs, and a photo or two. We will send one fixed price in writing — "
            "including pickup and delivery if the rugs need a full wash — before "
            "anything starts.",
            "We answer messages 24 hours a day, and in most cases you will hear "
            "back within minutes.",
        ],
    },

    # -------------------------------------------------------- office chairs
    "office-chair-cleaning": {
        "h1": "Office Chair Cleaning in Islamabad &amp; Rawalpindi",
        "title": "Office Chair Cleaning in Islamabad & Rawalpindi | Mesh, Fabric & Leather Chairs",
        "meta": ("Office chair cleaning in Islamabad & Rawalpindi. Mesh, fabric & "
                 "leather chairs cleaned in batches after hours. Fixed "
                 "price on WhatsApp. WhatsApp 0330 2935777."),
        "hero_p": ("Mesh, fabric and leather office chairs deep cleaned where they "
                   "stand — singly or in batches of fifty — with extraction cleaning "
                   "scheduled outside your working hours."),
        "h2_intro": "Why office chairs get dirtier than anything else in the office",
        "h2_included": "What is included in an office chair clean",
        "included_intro": ("Every chair is cleaned as a complete unit, not just the "
                           "seat pad. This is what each chair gets, whether you book "
                           "one chair or a floor of them."),
        "intro": [
            "An office chair is used harder than any sofa. The same person sits in "
            "it eight or nine hours a day, five or six days a week — transferring "
            "body oils and sweat into the seat and backrest continuously, eating "
            "lunch over it, resting forearms on the armrests thousands of times. "
            "Add Islamabad's dust settling into the fabric all day and you get "
            "chairs that turn visibly grey and start to smell within a couple of "
            "years, long before the mechanism wears out. Most offices replace "
            "chairs that only needed cleaning.",

            "The right process depends on the material. Fabric seats and backs get "
            "the same treatment as a sofa — vacuum, pre-treatment of marks, shampoo "
            "agitated in, then hot-water extraction that pulls the solution and the "
            "embedded soil back out under suction. Mesh chairs need a different, "
            "lower-moisture approach, because soaking mesh achieves nothing except "
            "a wet chair; the dirt on mesh sits in the weave and on the frame and "
            "responds to targeted cleaning rather than flooding. Leather and "
            "rexine chairs are cleaned and conditioned rather than extracted. We "
            "sort the batch by material and treat each type correctly.",

            "This is mainly a business-to-business service — banks, software "
            "houses, call centres and clinics across Blue Area, G-9, Saddar and "
            "Bahria Town book us for batches of twenty to a few hundred chairs, "
            "scheduled for evenings or weekends so the office never closes and the "
            "chairs are dry before the next shift sits down. But the same machines "
            "and the same process work at home: we clean dining chairs, study "
            "chairs and single home-office chairs too, often as an add-on to a "
            "sofa cleaning booking.",
        ],
        "included": [
            "<strong>Material check</strong> — each chair identified as fabric, "
            "mesh, leather or mixed, and the batch sorted so every chair gets the "
            "right process",
            "<strong>Deep vacuuming</strong> — seat, backrest, seams and the "
            "crevice between seat and back, where crumbs and grit collect",
            "<strong>Stain pre-treatment</strong> — tea, coffee, ink and food marks "
            "treated individually before the main clean",
            "<strong>Shampoo and hot-water extraction</strong> — for fabric seats "
            "and backs, the solution worked in and extracted back out along with "
            "the embedded soil",
            "<strong>Mesh cleaning</strong> — low-moisture cleaning of mesh panels "
            "and the frame behind them, done so the chair is usable almost "
            "immediately",
            "<strong>Leather cleaning and conditioning</strong> — leather and "
            "rexine chairs wiped down, cleaned and conditioned rather than wet "
            "extracted",
            "<strong>Armrests, base and castors</strong> — armrests degreased, and "
            "the plastic base, stem and wheels wiped down so the whole chair looks "
            "cleaned, not just the cushion",
            "<strong>Deodorising and drying</strong> — odour treated at the source "
            "in the fabric, and air movement used so chairs are dry before the "
            "next working day",
        ],
        "excluded": [
            "Repair of gas lifts, tilt mechanisms, broken castors or wobbly bases — "
            "we will flag broken chairs we find in a batch, but we do not repair them",
            "Re-upholstery, foam replacement or fixing torn fabric and split seams",
            "Guaranteed removal of ink that has spread through fabric, bleach marks "
            "or permanent dye stains — we tell you upfront what will and will "
            "not come out",
            "Workstation, desk and partition cleaning, unless booked alongside as "
            "part of an office deep clean",
            "Carpet cleaning under and around the chairs, which is quoted as its "
            "own service and often booked together",
            "Chairs with active pest problems — those need fumigation first, and we "
            "will tell you if we see the signs",
        ],
        "process": [
            ("Tell us the count and the materials",
             "Send a WhatsApp with roughly how many chairs, what they are — mesh, "
             "fabric, leather or a mix — and your location. For offices, a photo of "
             "a typical chair and the worst chair tells us most of what we need."),
            ("One fixed price on WhatsApp",
             "From your photos and the chair count we quote a fixed per-chair or "
             "per-batch price in writing before any work starts — for very large "
             "batches we can look at the chairs on site first if photos are not "
             "enough. We will also tell you which chairs are beyond cleaning, so "
             "you are not paying to clean a chair that needs replacing."),
            ("We clean outside your working hours",
             "The team comes in the evening, overnight or at the weekend with all "
             "machines and materials, sorts the chairs by type, and works through "
             "the batch — extraction for fabric, low-moisture for mesh, "
             "conditioning for leather."),
            ("Dry and back in service",
             "Air movers run while we work, so fabric chairs are dry before the "
             "next shift and mesh chairs are usable almost immediately. A "
             "supervisor walks the floor with your admin contact before we leave."),
        ],
        "price_factors": [
            ("Number of chairs",
             "The biggest factor, and the per-chair price drops as the batch grows "
             "— cleaning sixty chairs in one night costs far less per chair than "
             "six chairs on six visits."),
            ("Material mix",
             "Fabric chairs take the longest per unit because of extraction and "
             "drying. Mesh is quicker, leather sits in between. A batch's price "
             "reflects its mix."),
            ("Condition",
             "Chairs cleaned annually are routine. Chairs that have gone five years "
             "with daily use, or a batch with heavy staining and odour, need more "
             "pre-treatment and sometimes a second pass."),
            ("Scheduling",
             "Evening, overnight and weekend slots for offices are standard and "
             "built into the quote. Very tight windows — a whole floor between "
             "Friday close and Monday open — may need a larger team."),
            ("Location and access",
             "Which sector or area, which floor, and whether there is lift access "
             "for machines all affect time on site."),
        ],
        "faqs": [
            ("How much does office chair cleaning cost in Islamabad?",
             "Pricing is per chair, and the per-chair rate falls as the batch gets "
             "bigger — a one-off home office chair is priced differently from a "
             "hundred-chair floor done overnight. The material mix matters too, "
             "since fabric chairs take longer than mesh, and condition matters "
             "most of all. Send a photo of a typical chair and the worst chair "
             "along with the count, and we give you one fixed quote for the batch "
             "in writing on WhatsApp — for very large offices we can arrange to "
             "see the chairs first if photos are not enough."),
            ("Do you clean fabric and mesh office chairs?",
             "Yes, both — and differently, which matters. Fabric seats and "
             "backrests get shampoo and hot-water extraction, the same process "
             "that works on sofas, because the dirt is embedded in the cushion "
             "fabric. Mesh cannot be extracted and should never be soaked; the "
             "soil sits in the weave and on the frame, so mesh panels get "
             "targeted low-moisture cleaning instead. Many chairs are a mix — "
             "fabric seat, mesh back — and each part gets its own treatment. "
             "Leather and rexine chairs are cleaned and conditioned rather than "
             "wet cleaned."),
            ("Can you clean the chairs without closing our office?",
             "Yes — that is how almost all our office batches run. We schedule "
             "the work for evenings, overnight or weekends, clean the chairs at "
             "their desks or gathered in one area, whichever suits your floor "
             "plan, and run air movers so fabric chairs are dry before the next "
             "shift arrives. Nobody comes in on Monday to a damp seat. For "
             "24-hour operations like call centres, we work section by section so "
             "part of the floor is always in service."),
            ("How long do the chairs take to dry?",
             "Mesh chairs are usable almost immediately, since the cleaning is "
             "low-moisture. Fabric chairs are dry in roughly four to six hours "
             "with the air movement we use — faster in Islamabad's dry months, a "
             "little slower in monsoon humidity. For overnight office jobs this "
             "is comfortably inside the window between close of business and the "
             "next morning. For a chair cleaned at home in the afternoon, plan on "
             "it being ready to sit on by evening."),
            ("Do you also clean dining chairs at home?",
             "Yes, explicitly — this service is not offices-only. Fabric-seated "
             "dining chairs collect food spills and body oils just like office "
             "chairs, and a set of eight greying dining chairs before Eid is a "
             "job we do constantly. The process is the same extraction cleaning, "
             "priced per chair, and it pairs naturally with sofa cleaning — most "
             "customers book the dining chairs and the sofas in one visit, which "
             "costs less than two separate bookings. Study chairs and single home "
             "office chairs are welcome too."),
            ("Some of our chairs are quite stained — will the marks come out?",
             "Most will. Tea, coffee, food and the general grey of body oil and "
             "dust respond well to pre-treatment and extraction, and the "
             "transformation on a light-coloured chair is usually dramatic. What "
             "we cannot promise is ink that has spread through the fibre, bleach "
             "spots, or dye stains that have chemically changed the fabric "
             "colour. From your photos, and again before we start, we will point "
             "out which chairs fall into which category, so the quote reflects "
             "reality and you are not paying us to attempt the impossible."),
            ("How many chairs can you do in one night?",
             "A standard team works through forty to sixty mixed chairs in an "
             "overnight session, including drying time — more if the batch is "
             "mostly mesh, fewer if the chairs are heavily soiled fabric needing "
             "double passes. For larger offices we bring more teams or split the "
             "job across consecutive nights, section by section, so the whole "
             "floor is never out of service at once. Tell us your chair count and "
             "your deadline and we will tell you honestly what it takes."),
            ("How often should office chairs be cleaned?",
             "Once a year keeps a typical office's chairs in good condition and "
             "is the rhythm most of our contract clients settle into. High-use "
             "environments — call centres running multiple shifts in the same "
             "chairs, clinics, customer-facing seating — benefit from every six "
             "months. The economics are simple: a chair that gets cleaned "
             "annually stays presentable for the whole life of its mechanism, "
             "while an uncleaned one looks and smells finished years before it "
             "actually breaks, and gets replaced early. Cleaning is a fraction of "
             "the replacement cost."),
        ],
        "areas_intro": (
            "We clean office chairs across the whole of Islamabad and Rawalpindi — "
            "offices, call centres, banks, clinics and homes. These are the areas "
            "we work in most often, but if yours is not listed, send us a message "
            "and we will tell you straight away."),
        "closing_h2": "Book office chair cleaning in Islamabad or Rawalpindi",
        "closing": [
            "Send us a WhatsApp with your area, roughly how many chairs, and what "
            "they are made of — a photo of one or two chairs helps. We will quote "
            "the batch at one fixed price in writing, with the work scheduled "
            "outside your working hours.",
            "We answer messages 24 hours a day, and in most cases you will hear "
            "back within minutes.",
        ],
    },
}
