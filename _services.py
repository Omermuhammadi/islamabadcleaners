"""The 15 services — slug, card copy, photo.

Single source of truth for the home-page grid, the service pages, the footer
and the related-services strips.
"""

SERVICES = [
    {
        "slug": "deep-cleaning",
        "name": "Deep Cleaning",
        "card": "A top-to-bottom clean of the whole property, including the build-up regular cleaning never reaches.",
        "img": "deep-cleaning.jpg",
    },
    {
        "slug": "post-construction-cleaning",
        "name": "Post-Construction Cleaning",
        "card": "Cement dust, paint spots and builder's debris cleared so a new build is ready to move into.",
        "img": "post-construction-cleaning.jpg",
    },
    {
        "slug": "post-renovation-cleaning",
        "name": "Post-Renovation Cleaning",
        "card": "Fine dust and material residue removed after remodelling, including the rooms the builders sealed off.",
        "img": "post-renovation-cleaning.jpg",
    },
    {
        "slug": "move-in-cleaning",
        "name": "Move-In Cleaning",
        "card": "A full clean of an empty house before you move in, while there is no furniture in the way.",
        "img": "move-in-cleaning.jpg",
    },
    {
        "slug": "move-out-cleaning",
        "name": "Move-Out Cleaning",
        "card": "End-of-tenancy cleaning that hands the property back in the condition the landlord expects.",
        "img": "move-out-cleaning.jpg",
    },
    {
        "slug": "sofa-cleaning",
        "name": "Sofa Cleaning",
        "card": "Shampoo and hot-water extraction that lifts dirt and odour out of the fabric, not just off it.",
        "img": "sofa-cleaning.jpg",
    },
    {
        "slug": "carpet-cleaning",
        "name": "Carpet Cleaning",
        "card": "Deep extraction and stain treatment for carpets and rugs, with controlled drying.",
        "img": "carpet-cleaning.jpg",
    },
    {
        "slug": "mattress-cleaning",
        "name": "Mattress Cleaning",
        "card": "Deep sanitising that pulls dust, allergens and sweat residue out of the mattress layers.",
        "img": "mattress-cleaning.jpg",
    },
    {
        "slug": "marble-polishing",
        "name": "Marble Polishing",
        "card": "Grinding, honing and polishing that brings dull, scratched marble floors back to a shine.",
        "img": "marble-polishing.jpg",
    },
    {
        "slug": "tile-cleaning",
        "name": "Tile Cleaning",
        "card": "Machine cleaning for tiles and grout lines, targeting discolouration mopping cannot shift.",
        "img": "tile-cleaning.jpg",
    },
    {
        "slug": "floor-care",
        "name": "Floor Care",
        "card": "Scheduled scrubbing, buffing and sealing that keeps hard floors in condition all year.",
        "img": "floor-care.jpg",
    },
    {
        "slug": "window-cleaning",
        "name": "Window Cleaning",
        "card": "Interior and exterior window cleaning including frames, tracks and sills.",
        "img": "window-cleaning.jpg",
    },
    {
        "slug": "glass-cleaning",
        "name": "Glass Cleaning",
        "card": "Facades, partitions, railings and shower screens, including hard-water and mineral marks.",
        "img": "glass-cleaning.jpg",
    },
    {
        "slug": "solar-panel-cleaning",
        "name": "Solar Panel Cleaning",
        "card": "Safe removal of the dust layer that quietly cuts how much power your panels produce.",
        "img": "solar-panel-cleaning.jpg",
    },
    {
        "slug": "janitorial-services",
        "name": "Janitorial Services",
        "card": "Recurring cleaning staff and supervision for offices, clinics and retail units.",
        "img": "janitorial-services.jpg",
    },
]

BY_SLUG = {s["slug"]: s for s in SERVICES}


def related(slug, n=4):
    """Next n services after `slug`, wrapping around."""
    idx = next((i for i, s in enumerate(SERVICES) if s["slug"] == slug), 0)
    out = []
    i = idx + 1
    while len(out) < n:
        out.append(SERVICES[i % len(SERVICES)])
        i += 1
    return out
