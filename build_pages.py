"""Rewrite about.html and contact.html with real content.

Reuses the shared header/nav/footer via the same shell approach as the service
pages, so every page stays visually identical.
"""
import io
import json
import os
import re
from urllib.parse import quote

from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")

BRAND = "CleanCrew"
SITE_URL = "https://cleancrew.pk"
PHONE_DISPLAY = "0330 2935777"
PHONE_TEL = "+923302935777"
EMAIL = "mgcleaner364@gmail.com"


def read(p):
    return io.open(p, encoding="utf-8", errors="ignore").read()


def wa(msg):
    return "https://wa.me/923302935777?text=" + quote(msg)


WA_GENERAL = wa("Hi %s, I'd like a quote for cleaning in Islamabad / Rawalpindi." % BRAND)


def shell():
    soup = BeautifulSoup(read(os.path.join(SITE, "index.html")), "lxml")
    head = soup.head
    css = "\n".join(str(t) for t in head.find_all("link", rel="stylesheet"))
    scripts = "\n".join(str(t) for t in soup.find_all("script", src=True))
    return {
        "css": css,
        "header": str(soup.select_one("header.site-header") or ""),
        "nav": str(soup.select_one("nav.navbar") or ""),
        "footer": str(soup.select_one("footer.site-footer") or ""),
        "float": str(soup.select_one(".cc-float") or ""),
        "scripts": scripts,
    }


def page(title, meta, path, hero_title, hero_p, body, schema=None):
    sh = shell()
    schema_tag = ('<script type="application/ld+json">%s</script>' % schema) if schema else ""
    return f"""<!DOCTYPE html>
<html lang="en-PK">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{meta}">
<link rel="canonical" href="{SITE_URL}/{path}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta}">
<meta property="og:url" content="{SITE_URL}/{path}">
{sh["css"]}
{schema_tag}
</head>
<body>
{sh["header"]}
{sh["nav"]}

<section class="svcpage-hero" style="background-image:url('images/services/deep-cleaning.jpg')">
  <div class="container">
    <nav class="svcpage-crumbs" aria-label="Breadcrumb">
      <a href="index.html">Home</a> &rsaquo; <span>{hero_title}</span>
    </nav>
    <h1>{hero_title}</h1>
    <p>{hero_p}</p>
    <a class="cc-btn cc-btn--wa" href="{WA_GENERAL}">
      <i class="bi-whatsapp"></i> Get a free quote on WhatsApp
    </a>
    <a class="cc-btn cc-btn--ghost" href="tel:{PHONE_TEL}">
      <i class="bi-telephone-fill"></i> {PHONE_DISPLAY}
    </a>
  </div>
</section>

{body}

{sh["footer"]}
{sh["float"]}
{sh["scripts"]}
</body>
</html>
"""


# --------------------------------------------------------------------- about
ABOUT_BODY = f"""
<section class="svcbody">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-12">

        <h2>Who we are</h2>
        <p>{BRAND} is a cleaning company working across Islamabad and Rawalpindi. We have
        been doing this for eight years, and in that time the work has settled into three
        kinds of job: one-off cleaning that people book when they need it — deep cleans,
        sofas, carpets, marble; deadline work that comes with building and moving —
        post-construction, post-renovation, move-in and move-out; and regular janitorial
        contracts for offices, clinics and retail units.</p>
        <p>We are not a booking platform or an agency that forwards your job to someone
        else. The people who turn up are our own staff, the equipment is ours, and the
        person who quotes you is the person accountable for the result.</p>

        <h2>How we work</h2>

        <h3>We look before we quote</h3>
        <p>For most jobs we come and see the property before giving a price. It takes half
        an hour and it costs you nothing. The reason is simple: cleaning prices depend on
        size and condition, and condition cannot be judged over the phone. Quoting blind
        means either overcharging you to be safe or revising the number on the day, and we
        would rather do neither.</p>

        <h3>We bring everything</h3>
        <p>Machines, chemicals, cloths, protective sheets — it all comes with the team. You
        do not need to buy anything or have anything ready. If you would prefer we use a
        specific product because of an allergy or a delicate surface, tell us beforehand and
        we will use it.</p>

        <h3>We size the team to the job</h3>
        <p>Most of our cleaners work on call, which means we scale up or down to suit the
        work rather than sending the same two people to every job. A single sofa is one
        person for a couple of hours. A post-construction handover with a fixed deadline
        might be a full crew working through the night. Both are normal for us.</p>

        <h3>We work around the clock</h3>
        <p>We operate 24 hours a day, seven days a week. That is not a slogan — it is what
        makes commercial work possible, because offices, clinics and restaurants generally
        want us in when they are closed, and handover deadlines rarely respect office
        hours. It also means that when you message us at ten at night, someone answers.</p>

        <h2>What we will tell you honestly</h2>
        <p>There are things cleaning cannot fix, and we would rather say so before you pay
        than after. Bleach marks, dye transfer and ink usually do not come out of fabric.
        Marble that is cracked needs replacing, not polishing. Grout that has physically
        eroded cannot be cleaned back. Bed bugs are a pest control problem, not a cleaning
        one. Mould that keeps returning is usually a leak or a ventilation fault.</p>
        <p>Every one of our service pages has a section listing what is not included, for
        exactly this reason. A cleaning company that promises everything is a cleaning
        company that will disappoint you on something.</p>

        <h2>Where we work</h2>
        <p>Both cities, in full. In Islamabad we are most often in DHA, Bahria Town, Bahria
        Enclave, the F and G sectors, E-11, Blue Area, Gulberg Greens and Residencia, PWD
        and Media Town. In Rawalpindi we cover Saddar and Cantt, Chaklala Scheme III,
        Bahria Town Rawalpindi, Askari, Satellite Town and the Adiala Road area. If your
        area is not on that list, message us — it almost certainly does not mean we cannot
        reach you.</p>

        <h2>Get in touch</h2>
        <p>The fastest way to reach us is WhatsApp. Send the service you need, your area,
        and roughly how big the property or item is, and we will come back with a time to
        look at it. We answer messages at any hour, usually within minutes.</p>
        <p>
          <a class="cc-btn cc-btn--wa" href="{WA_GENERAL}" style="color:#10233a">
            <i class="bi-whatsapp"></i> Message us on WhatsApp
          </a>
        </p>

      </div>

      <div class="col-lg-4 col-12">
        <aside class="cc-aside">
          <h3>Talk to us</h3>
          <p>Free inspection, one fixed price, and we work 24/7 across both cities.</p>
          <a class="cc-btn cc-btn--wa" href="{WA_GENERAL}">
            <i class="bi-whatsapp"></i> WhatsApp us
          </a>
          <a class="cc-btn cc-btn--ghost" href="tel:{PHONE_TEL}">
            <i class="bi-telephone-fill"></i> {PHONE_DISPLAY}
          </a>
          <div class="cc-aside-fact"><i class="bi-clock-fill"></i>
            <span>Open 24 hours, 7 days a week</span></div>
          <div class="cc-aside-fact"><i class="bi-tools"></i>
            <span>All machines and materials included</span></div>
          <div class="cc-aside-fact"><i class="bi-geo-alt-fill"></i>
            <span>Islamabad &amp; Rawalpindi</span></div>
          <div class="cc-aside-fact"><i class="bi-envelope-fill"></i>
            <span>{EMAIL}</span></div>
        </aside>
      </div>
    </div>
  </div>
</section>
"""

# ------------------------------------------------------------------- contact
CONTACT_FAQS = [
    ("What is the fastest way to get a quote?",
     "WhatsApp. Send us the service you need, your area, and roughly how big the property "
     "or item is. For smaller jobs like a sofa or a few rugs we can often quote from a "
     "photo without needing to visit at all."),
    ("Do you charge for the inspection?",
     "No. The visit and the quote are free, and there is no obligation to book afterwards. "
     "We would rather see the job and price it accurately than guess over the phone."),
    ("How quickly can you come?",
     "We work 24 hours a day, seven days a week, and reply to messages within minutes. "
     "Same-day slots are often available depending on how many teams are already out, so "
     "the earlier you message the better."),
    ("Do you work on Sundays and public holidays?",
     "Yes. We work every day of the year, including nights, and a lot of our commercial "
     "work happens at weekends precisely because that is when premises are empty."),
    ("Which areas do you cover?",
     "All of Islamabad and Rawalpindi. If you are just outside either city, message us "
     "anyway — depending on the size of the job we can often still come."),
]

CONTACT_SCHEMA = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "LocalBusiness",
            "@id": SITE_URL + "/#organization",
            "name": BRAND,
            "url": SITE_URL,
            "telephone": PHONE_TEL,
            "email": EMAIL,
            "description": ("Cleaning services in Islamabad and Rawalpindi — deep cleaning, "
                            "post-construction, sofa, carpet, marble and janitorial."),
            "additionalType": "http://www.productontology.org/id/Cleaner",
            "areaServed": [
                {"@type": "City", "name": "Islamabad"},
                {"@type": "City", "name": "Rawalpindi"},
            ],
            "openingHoursSpecification": [{
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday",
                              "Friday", "Saturday", "Sunday"],
                "opens": "00:00", "closes": "23:59",
            }],
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in CONTACT_FAQS
            ],
        },
    ],
}, ensure_ascii=False)

CONTACT_FAQ_HTML = "".join(
    '<details%s><summary>%s</summary><div class="cc-faq__a">%s</div></details>'
    % (" open" if i == 0 else "", q, a) for i, (q, a) in enumerate(CONTACT_FAQS))

CONTACT_BODY = f"""
<section class="svcbody">
  <div class="container">
    <div class="row">
      <div class="col-lg-8 col-12">

        <h2>Message us and we will come back within minutes</h2>
        <p>The quickest way to reach us is WhatsApp. Tell us three things — the service you
        need, the area you are in, and roughly how big the property or item is — and we will
        reply with a time to come and look at it. For smaller jobs like a sofa, a few rugs
        or a mattress, a photo is usually enough for us to quote without visiting.</p>
        <p>We answer messages 24 hours a day. If you would rather talk, call the same
        number.</p>

        <div class="cc-panel">
          <h3>Contact details</h3>
          <ul>
            <li><strong>WhatsApp and phone</strong> — <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
            <li><strong>Email</strong> — <a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li><strong>Hours</strong> — open 24 hours, 7 days a week, including public holidays</li>
            <li><strong>Areas covered</strong> — all of Islamabad and Rawalpindi</li>
          </ul>
          <p>
            <a class="cc-btn cc-btn--wa" href="{WA_GENERAL}" style="color:#10233a">
              <i class="bi-whatsapp"></i> Message us on WhatsApp
            </a>
          </p>
        </div>

        <h2>What to tell us when you message</h2>
        <p>You do not need to know exactly what service you want — describing the problem is
        fine, and we will tell you which service fits. What genuinely speeds up an accurate
        quote is:</p>
        <ul>
          <li><strong>The service or the problem</strong> — "deep clean", "builders just
          left", "sofa smells", "marble has gone dull"</li>
          <li><strong>Your area</strong> — the sector or society is enough</li>
          <li><strong>Size</strong> — marla or square feet for a property, number of seats
          for a sofa, number of panels for solar</li>
          <li><strong>When you need it</strong> — including if there is a fixed handover or
          inspection date</li>
          <li><strong>A photo</strong> — optional, but it often removes the need for a visit
          on smaller jobs</li>
        </ul>

        <h2>Common questions</h2>
        <div class="cc-faq">{CONTACT_FAQ_HTML}</div>

        <h2>Commercial and contract enquiries</h2>
        <p>For offices, clinics, restaurants, showrooms and schools, we set up janitorial
        contracts with a written scope of work, assigned staff and a fixed monthly price.
        Message us the size of the premises, the type of business and the hours you want the
        cleaning done, and we will arrange a site visit.</p>
        <p>We can also handle one-off commercial work — post-construction handovers, fit-out
        cleans, carpet extraction and floor restoration — outside your business hours so
        nothing disrupts your operation.</p>

      </div>

      <div class="col-lg-4 col-12">
        <aside class="cc-aside">
          <h3>Get a free quote</h3>
          <p>Tell us the service, your area and the size. Free inspection, then one fixed
          price that does not move.</p>
          <a class="cc-btn cc-btn--wa" href="{WA_GENERAL}">
            <i class="bi-whatsapp"></i> WhatsApp us
          </a>
          <a class="cc-btn cc-btn--ghost" href="tel:{PHONE_TEL}">
            <i class="bi-telephone-fill"></i> {PHONE_DISPLAY}
          </a>
          <div class="cc-aside-fact"><i class="bi-clock-fill"></i>
            <span>Open 24 hours, 7 days a week</span></div>
          <div class="cc-aside-fact"><i class="bi-lightning-fill"></i>
            <span>We usually reply within minutes</span></div>
          <div class="cc-aside-fact"><i class="bi-geo-alt-fill"></i>
            <span>All of Islamabad &amp; Rawalpindi</span></div>
          <div class="cc-aside-fact"><i class="bi-envelope-fill"></i>
            <span>{EMAIL}</span></div>
        </aside>
      </div>
    </div>
  </div>
</section>
"""


def main():
    about = page(
        title="About CleanCrew | Cleaning Company in Islamabad & Rawalpindi",
        meta=("About CleanCrew — a cleaning company working across Islamabad and "
              "Rawalpindi for eight years. Our own staff, our own equipment, free "
              "inspection and one fixed price. Open 24/7."),
        path="about.html",
        hero_title="About " + BRAND,
        hero_p=("Eight years cleaning homes, offices and new builds across Islamabad and "
                "Rawalpindi. Our own staff, our own equipment, and a price we agree "
                "before we start."),
        body=ABOUT_BODY,
    )
    io.open(os.path.join(SITE, "about.html"), "w", encoding="utf-8").write(about)
    print("built about.html")

    contact = page(
        title="Contact CleanCrew | Cleaning Services Islamabad & Rawalpindi",
        meta=("Contact CleanCrew for cleaning in Islamabad and Rawalpindi. WhatsApp or "
              "call 0330 2935777, open 24 hours a day. Free inspection and a fixed price "
              "before we start."),
        path="contact.html",
        hero_title="Contact us",
        hero_p=("WhatsApp or call 0330 2935777 — any hour, any day. Tell us the service, "
                "your area and the size, and we will come and quote free of charge."),
        body=CONTACT_BODY,
        schema=CONTACT_SCHEMA,
    )
    io.open(os.path.join(SITE, "contact.html"), "w", encoding="utf-8").write(contact)
    print("built contact.html")


if __name__ == "__main__":
    main()
