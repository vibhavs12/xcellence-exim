# -*- coding: utf-8 -*-
"""Generates the redesigned Xcellence Exim static site into ../site/"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parts import (head, header, footer, cta_band, pagehead,
                   IMAGES as I, ICON, SITE, WA, EMAIL_SALES, EMAIL_INFO,
                   EMAIL_DIR, ENQUIRY_ENDPOINT, PHONE)

# Pages are written to the repository root so GitHub Pages can serve
# them directly (Settings -> Pages -> Deploy from branch: main / root).
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
os.makedirs(OUT, exist_ok=True)

def write(name, html):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(html)
    print('  wrote', name, '(%.1f KB)' % (len(html) / 1024.0))


def product_schema(name, desc, img, cat):
    return f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{name}",
  "description": "{desc}",
  "image": "{img}",
  "category": "{cat}",
  "brand": {{ "@type": "Brand", "name": "Xcellence Exim" }},
  "offers": {{
    "@type": "Offer",
    "availability": "https://schema.org/InStock",
    "priceCurrency": "USD",
    "priceSpecification": {{ "@type": "PriceSpecification", "valueAddedTaxIncluded": false }},
    "seller": {{ "@id": "{SITE}/#organization" }}
  }}
}}
</script>
'''


# =========================================================================
# HOME
# =========================================================================
home = head(
    "Xcellence Exim | Indian Exporter of Rice, Coffee, Spices &amp; Sugar ICUMSA 45",
    "Xcellence Exim is an Indian merchant exporter supplying premium Basmati and non-Basmati rice, Arabica and Robusta coffee, Sannam S4 red chilli and Sugar ICUMSA 45 to importers worldwide. IEC, GST, FSSAI, MSME and APEDA registered.",
    "index.html",
    og_image=I['home_rice'],
)
home += header("index.html")

home += f"""
<section class="hero">
  <div class="wrap hero__inner">
    <div class="hero__copy">
      <span class="eyebrow">Merchant Exporter &middot; Kota, India</span>
      <h1>Premium Indian agro commodities, <em>shipped with certainty</em></h1>
      <p class="hero__sub">We supply rice, coffee, spices and refined sugar to importers, distributors and food manufacturers across global markets — sourced from verified mills, inspected against buyer specification, and backed by complete export documentation.</p>
      <div class="hero__badges">
        <span class="pill pill--gold">IEC Registered</span>
        <span class="pill">FSSAI</span>
        <span class="pill">APEDA</span>
        <span class="pill">MSME</span>
        <span class="pill">GST</span>
      </div>
      <div class="btn-row">
        <a class="btn btn--primary" href="contact.html#rfq">Request a Quotation {ICON['arrow']}</a>
        <a class="btn btn--ghost" href="export-process.html">How we ship</a>
      </div>
    </div>
    <div class="hero__media">
      <div class="hero__grid">
        <figure><img src="{I['home_rice']}" alt="Premium Indian basmati rice ready for export" width="600" height="600" fetchpriority="high"></figure>
        <figure><img src="{I['home_coffee']}" alt="Indian Arabica and Robusta coffee beans" width="600" height="600"></figure>
        <figure><img src="{I['home_spices']}" alt="Sannam red chillies and Indian spices" width="600" height="600" loading="lazy"></figure>
        <figure><img src="{I['home_sugar']}" alt="Refined white crystal sugar ICUMSA 45" width="600" height="600" loading="lazy"></figure>
      </div>
    </div>
  </div>
</section>

<section class="trust">
  <div class="wrap">
    <div class="trust__inner">
      <div class="trust__item"><span class="trust__num">4+</span><span class="trust__label">Commodity categories</span></div>
      <div class="trust__item"><span class="trust__num">5</span><span class="trust__label">Statutory registrations</span></div>
      <div class="trust__item"><span class="trust__num">100%</span><span class="trust__label">Lab-tested consignments</span></div>
      <div class="trust__item"><span class="trust__num">24 h</span><span class="trust__label">Quotation turnaround</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Our export range</span>
      <hr class="rule">
      <h2>Four categories, specialised end to end</h2>
      <p class="lead">A focused product range lets us control quality at every stage — from mill selection through grading, testing and export-grade packing.</p>
    </div>

    <div class="grid grid--4 reveal">
      <article class="card">
        <div class="card__media">
          <img src="{I['home_rice']}" alt="Premium Indian basmati rice grains" width="600" height="450" loading="lazy">
          <span class="card__tag">HSN 1006</span>
        </div>
        <div class="card__body">
          <h3>Rice</h3>
          <p>Basmati (1121, 1509, 1718, 1885, 1401, Pusa, Traditional) and non-Basmati varieties including Sona Masoori, IR-64 and PR-26.</p>
          <a class="card__link" href="rice.html">View specifications {ICON['arrow']}</a>
        </div>
      </article>

      <article class="card">
        <div class="card__media">
          <img src="{I['home_coffee']}" alt="Indian arabica and robusta coffee beans" width="600" height="450" loading="lazy">
          <span class="card__tag">HSN 0901</span>
        </div>
        <div class="card__body">
          <h3>Coffee</h3>
          <p>Green, roasted and instant coffee in Arabica and Robusta grades — PL, AC, RC and RP — from selected Indian estates.</p>
          <a class="card__link" href="coffee.html">View specifications {ICON['arrow']}</a>
        </div>
      </article>

      <article class="card">
        <div class="card__media">
          <img src="{I['home_spices']}" alt="Sannam S4 red chilli for export" width="600" height="450" loading="lazy">
          <span class="card__tag">HSN 0904</span>
        </div>
        <div class="card__body">
          <h3>Spices</h3>
          <p>Sannam S4 / S334 red chilli with bright colour and balanced heat, plus turmeric, cumin, cloves and cardamom.</p>
          <a class="card__link" href="spices.html">View specifications {ICON['arrow']}</a>
        </div>
      </article>

      <article class="card">
        <div class="card__media">
          <img src="{I['home_sugar']}" alt="Refined white crystal sugar ICUMSA 45" width="600" height="450" loading="lazy">
          <span class="card__tag">HSN 1701</span>
        </div>
        <div class="card__body">
          <h3>Sugar ICUMSA 45</h3>
          <p>Refined white crystal sugar from certified Indian mills, plus ICUMSA 100–150, brown sugar and raw sugar grades.</p>
          <a class="card__link" href="sugar.html">View specifications {ICON['arrow']}</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="split reveal">
      <div class="split__media split__media--sourcing">
        <img src="{I['about']}" alt="Xcellence Exim supplier and sourcing network across India" width="800" height="600" loading="lazy">
      </div>
      <div>
        <span class="eyebrow">Who we are</span>
        <hr class="rule">
        <h2>A sourcing network built on verified partners</h2>
        <p>Xcellence Exim is a merchant exporter from India supplying a wide range of high-quality agricultural products. We work directly with verified mills, certified processors and trusted farmer groups to ensure consistent quality and reliable supply across every category we handle.</p>
        <p>Our approach is deliberately simple: honest communication, strict quality checks, fair pricing, and close coordination from sourcing through to final shipment. Whether it is rice, sugar, coffee or spices, the commitment stays the same — the right quality, at the right time, with complete transparency.</p>
        <div class="btn-row" style="margin-top:1.6rem">
          <a class="btn btn--outline" href="about.html">More about us</a>
          <a class="btn btn--solid" href="certificates.html">View certificates</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Why buyers trust us</span>
      <hr class="rule">
      <h2>Everything an importer needs, handled</h2>
      <p class="lead">From first enquiry to post-dispatch support, each step is documented so you always know exactly what is arriving and when.</p>
    </div>

    <div class="grid grid--3 reveal">
      <div class="tile"><span class="tile__icon">{ICON['globe']}</span><h3>Export-quality sourcing</h3><p>A vetted network of mills, processors and farmer groups selected for consistency rather than lowest cost.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['lab']}</span><h3>Strict quality inspection</h3><p>Every consignment is cleaned, sorted and tested for purity, moisture and safety parameters before it is released.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['box']}</span><h3>Custom packaging &amp; private label</h3><p>PP, BOPP, jute, non-woven, jumbo bags, valve packs and retail formats — with your branding where required.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['doc']}</span><h3>Complete documentation</h3><p>Commercial invoice, packing list, certificate of origin, COA and every supporting document your customs needs.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['tag']}</span><h3>Focused specialisation</h3><p>A deliberately narrow product range means deeper control over grading, tolerances and shipment consistency.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['talk']}</span><h3>Transparent communication</h3><p>One point of contact from quotation to delivery, with proactive updates at every milestone.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split--media-end reveal">
      <div>
        <span class="eyebrow">Export support</span>
        <hr class="rule">
        <h2>Documentation and logistics, coordinated for you</h2>
        <p>We provide complete export assistance so your clearing agent receives a clean, complete document set on time.</p>
        <ul class="checklist checklist--2" style="margin-top:1.5rem">
          <li>Commercial Invoice</li>
          <li>Packing List</li>
          <li>Certificate of Origin</li>
          <li>Certificate of Analysis (COA)</li>
          <li>Phytosanitary support</li>
          <li>Shipping &amp; logistics coordination</li>
        </ul>
        <div class="btn-row" style="margin-top:1.8rem">
          <a class="btn btn--solid" href="export-process.html">See the full process</a>
        </div>
      </div>
      <div class="split__media">
        <img src="{I['home_logistics']}" alt="Export professional coordinating shipment documents and logistics" width="800" height="600" loading="lazy">
      </div>
    </div>
  </div>
</section>
"""
home += cta_band()
home += footer()
write('index.html', home)


# =========================================================================
# ABOUT
# =========================================================================
about = head(
    "About Us | Xcellence Exim — Indian Agri-Export Company",
    "Xcellence Exim is an India-based agri-export company delivering products that meet global food safety and quality standards, working closely with farmers, processors and certified facilities.",
    "about.html", og_image=I['about'])
about += header("about.html")
about += pagehead(
    "Who We Are",
    "An India-based agri-export company committed to delivering products that meet global food safety and quality standards.",
    "About Us")

about += f"""
<section class="section">
  <div class="wrap">
    <div class="split reveal">
      <div class="split__media">
        <img src="{I['about']}" alt="Xcellence Exim sourcing network" width="800" height="600">
      </div>
      <div>
        <span class="eyebrow">Our approach</span>
        <hr class="rule">
        <h2>Exports built on relationships, not transactions</h2>
        <p>We work closely with farmers, processors and certified facilities to ensure reliable sourcing, traceability and long-term value for our partners.</p>
        <p>We believe exports are not just transactions — they are relationships built on trust, performance and mutual growth. That belief shapes how we quote, how we inspect, and how we communicate when something needs adjusting.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">What we offer</span>
      <hr class="rule">
      <h2>Our product portfolio</h2>
    </div>
    <div class="grid grid--2 reveal">
      <div class="tile">
        <span class="tile__icon">{ICON['box']}</span>
        <h3>Premium Rice — Basmati &amp; Non-Basmati</h3>
        <p>Premium-grade rice sourced from trusted Indian millers, carefully processed and graded to meet international export standards. Applications: food service, retail packaging, wholesale distribution and institutional supply.</p>
      </div>
      <div class="tile">
        <span class="tile__icon">{ICON['globe']}</span>
        <h3>Coffee</h3>
        <p>High-quality Indian Arabica and Robusta sourced from selected growing regions, processed and graded for global markets. Includes green coffee beans, roasted beans and instant coffee as required.</p>
      </div>
      <div class="tile">
        <span class="tile__icon">{ICON['lab']}</span>
        <h3>Sugar ICUMSA 45</h3>
        <p>Highly refined white crystal sugar suitable for food processing, the beverage industry and direct consumption, meeting international purity standards.</p>
      </div>
      <div class="tile">
        <span class="tile__icon">{ICON['tag']}</span>
        <h3>Premium Red Chilli — Sannam S4 / S334</h3>
        <p>Export-grade red chilli known for vibrant colour, balanced pungency and strong aroma, widely used in spice blending and food processing industries.</p>
      </div>
      <div class="tile">
        <span class="tile__icon">{ICON['ship']}</span>
        <h3>Agro Commodities</h3>
        <p>We export select agricultural products against buyer specification, focusing on consistent quality, proper grading and export-ready packaging.</p>
      </div>
      <div class="tile">
        <span class="tile__icon">{ICON['shield']}</span>
        <h3>Quality Commitment</h3>
        <p>Sourced from verified suppliers, processed under strict hygiene standards, tested for purity, moisture and safety, and packed in export-grade materials that preserve freshness in transit.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split--media-end reveal">
      <div>
        <span class="eyebrow">Quality commitment</span>
        <hr class="rule">
        <h2>Documented, tested, and traceable</h2>
        <p>Quality is at the core of everything we do. We provide Certificates of Analysis and all relevant export documentation to ensure confidence, compliance and transparency in every shipment.</p>
        <ul class="checklist" style="margin-top:1.4rem">
          <li>Sourced from verified and trusted suppliers</li>
          <li>Processed under strict hygiene standards</li>
          <li>Tested for purity, moisture and safety parameters</li>
          <li>Packed in export-grade materials to preserve freshness during transit</li>
        </ul>
      </div>
      <div class="split__media">
        <img src="{I['hero2']}" alt="Quality inspection of export commodities" width="800" height="600" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="grid grid--2 reveal" style="gap:clamp(2rem,1rem+3vw,4rem)">
      <div>
        <span class="eyebrow">Our mission</span>
        <hr class="rule">
        <ul class="checklist">
          <li>To represent Indian agriculture with integrity in global markets.</li>
          <li>To deliver value through quality, reliability and service.</li>
          <li>To grow alongside our customers through collaboration and trust.</li>
        </ul>
      </div>
      <div>
        <span class="eyebrow">Our vision</span>
        <hr class="rule">
        <p>To become a trusted global supplier of Indian agricultural products by delivering consistent quality, building long-term partnerships and promoting sustainable sourcing practices.</p>
        <p style="margin-top:1.2rem">We cater to importers, wholesalers, distributors and food manufacturers across international markets. Our operations are flexible enough to meet regional quality standards, packaging requirements and regulatory compliance.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Why choose us</span>
      <hr class="rule">
      <h2>What working with Xcellence Exim looks like</h2>
    </div>
    <div class="grid grid--3 reveal">
      <div class="tile"><span class="tile__icon">{ICON['ship']}</span><h3>Reliable supply chain</h3><p>Consistent export-quality products backed by a sourcing network we know personally.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['doc']}</span><h3>Complete documentation support</h3><p>Transparent communication and a full document set prepared alongside the shipment.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['box']}</span><h3>Custom &amp; private-label packing</h3><p>Packaging solutions matched to your market, retail format and branding.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['tag']}</span><h3>Competitive pricing</h3><p>Fair, honest pricing structured around long-term partnership rather than one-off margin.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['lab']}</span><h3>Focused product range</h3><p>A narrower catalogue that allows genuinely better quality control.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['shield']}</span><h3>Timely delivery</h3><p>Commitment to agreed shipment windows and buyer satisfaction after dispatch.</p></div>
    </div>
  </div>
</section>
"""
about += cta_band()
about += footer()
write('about.html', about)


# =========================================================================
# PRODUCT PAGE BUILDER
# =========================================================================
def product_page(fname, title, meta_desc, crumb, h1, lead, eyebrow,
                 blocks, gallery, aside_facts, schema, hsn):
    html = head(title, meta_desc, fname, extra_schema=schema, og_image=gallery[0][0])
    html += header(fname)
    html += pagehead(h1, lead, crumb)
    html += '<section class="section"><div class="wrap"><div class="spec-layout">\n<div>\n'
    for b in blocks:
        html += b
    html += '</div>\n'

    facts = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in aside_facts)
    html += f"""
<aside>
  <div class="aside-card">
    <h3>Request pricing</h3>
    <p>Share your quantity, destination port and preferred Incoterms — we reply with a detailed offer within one business day.</p>
    <dl>{facts}</dl>
    <a class="btn btn--primary" href="contact.html#rfq">Request a Quotation</a>
    <a class="btn btn--ghost" href="https://wa.me/{WA}?text={('Hello%20Xcellence%20Exim%2C%20I%20would%20like%20a%20quotation%20for%20' + crumb.replace(' ', '%20').replace('&amp;', 'and'))}" target="_blank" rel="noopener">Enquire on WhatsApp</a>
    <hr>
    <dl translate="no" class="notranslate">
      <dt>HSN Code</dt><dd>{hsn}</dd>
      <dt>Direct line</dt><dd><a href="mailto:{EMAIL_INFO}" style="color:#DFBE4B">{EMAIL_INFO}</a></dd>
    </dl>
  </div>
</aside>
</div></div></section>
"""

    imgs = "".join(f'<img src="{src}" alt="{alt}" width="600" height="600" loading="lazy">' for src, alt in gallery)
    html += f"""
<section class="section section--tint">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">{eyebrow}</span>
      <hr class="rule">
      <h2>Product gallery</h2>
    </div>
    <div class="gallery reveal">{imgs}</div>
  </div>
</section>
"""
    html += cta_band()
    html += footer()
    write(fname, html)


def table(caption, headers, rows):
    th = "".join(f"<th scope='col'>{h}</th>" for h in headers)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"""<div class="table-wrap"><table><caption>{caption}</caption>
<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>"""


def chips(items):
    return '<ul class="chips">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


# ------------------------------- RICE
product_page(
    "rice.html",
    "Premium Indian Rice — Basmati &amp; Non-Basmati | Xcellence Exim",
    "Export-grade Indian rice: 1121, 1509, 1718, 1885 and 1401 Basmati, Sharbati, Sugandha, Sona Masoori, IR-64 and PR-26. Cleaned, sorted, lab-tested and packed to buyer specification.",
    "Rice", "Premium Indian Rice",
    "Basmati and non-Basmati varieties sourced directly from certified and trusted mills — cleaned, sorted, lab-tested and packed to your specification.",
    "Rice",
    [
        f"""<div class="spec-block reveal">
  <h2>Overview</h2>
  <p>We supply a wide range of premium-quality Indian rice sourced directly from certified and trusted mills. Every variety is cleaned, sorted, lab-tested and packed according to buyer specifications, so what arrives at your port matches the sample you approved.</p>
</div>""",
        '<div class="spec-block reveal"><h2>Available varieties</h2>' + table(
            "Basmati, aromatic and non-Basmati varieties available for export.",
            ["Category", "Varieties"],
            [
                ["<strong>Premium Basmati</strong>", "1121 Basmati (Raw / Steam / Sella — Golden &amp; White), 1509 Basmati, 1718 Basmati, 1885 Basmati, 1401 Basmati, Traditional Basmati, Pusa Basmati"],
                ["<strong>Basmati-type aromatic</strong>", "Sharbati, Sugandha"],
                ["<strong>Non-Basmati</strong>", "PR-26, Sona Masoori, IR-64, and other Indian varieties on request"],
            ]) + '</div>',
        '<div class="spec-block reveal"><h2>Packaging options</h2>'
        + chips(["25 kg", "50 kg", "PP bags", "BOPP bags", "Jute bags", "Non-woven bags", "Private label", "Custom branding"])
        + '<p style="margin-top:1.1rem;font-size:.9rem;color:#5C666C">Other bag sizes and retail formats can be arranged against confirmed orders.</p></div>',
        f"""<div class="spec-block reveal">
  <h2>Quality process</h2>
  <ul class="checklist">
    <li>Mill selection against grain length, moisture and broken-percentage tolerances</li>
    <li>Colour sortex and de-stoning before packing</li>
    <li>Lab testing with Certificate of Analysis issued per consignment</li>
    <li>Pre-shipment sample dispatched for approval where required</li>
  </ul>
</div>""",
    ],
    [(I['rice1'], "Indian basmati rice grains, export grade"),
     (I['rice2'], "Sorted premium rice ready for packing"),
     (I['rice3'], "Export packaging for Indian rice")],
    [("HS category", "Cereals — Rice"), ("Bag sizes", "25 kg / 50 kg / custom"), ("Private label", "Available")],
    product_schema("Premium Indian Rice — Basmati &amp; Non-Basmati",
                   "Export-grade Indian Basmati and non-Basmati rice, cleaned, sorted, lab-tested and packed to buyer specification.",
                   I['rice2'], "Rice"),
    "100630",
)

# ------------------------------- COFFEE
product_page(
    "coffee.html",
    "Indian Coffee — Arabica &amp; Robusta, Green, Roasted &amp; Instant | Xcellence Exim",
    "Export-grade Indian coffee: green, roasted and instant. Arabica Plantation (PL), Arabica Cherry (AC), Robusta Cherry AB (RC) and Robusta Parchment (RP) grades with custom packaging.",
    "Coffee", "Premium Indian Coffee",
    "High-quality Arabica and Robusta sourced directly from trusted Indian estates and growers — processed, graded and export-ready packed to your requirement.",
    "Coffee",
    [
        """<div class="spec-block reveal">
  <h2>Overview</h2>
  <p>We supply high-quality Arabica and Robusta coffee sourced directly from trusted Indian estates and growers. All coffee is processed, graded and export-ready packed as per buyer requirements — whether you are a roaster buying green beans in bulk or a brand needing finished retail packs.</p>
</div>""",
        '<div class="spec-block reveal"><h2>Available forms</h2>' + table(
            "Coffee forms available for export.",
            ["Form", "Description"],
            [
                ["<strong>Green Coffee Beans</strong>", "Unroasted raw beans for roasters and bulk industrial use"],
                ["<strong>Roasted Coffee Beans</strong>", "Light, medium and dark roast profiles"],
                ["<strong>Instant Coffee</strong>", "Spray-dried or freeze-dried, with or without chicory"],
            ]) + '</div>',
        '<div class="spec-block reveal"><h2>Grades available</h2>' + table(
            "Standard Indian coffee export grades.",
            ["Code", "Grade"],
            [["<strong>PL</strong>", "Arabica Plantation"],
             ["<strong>AC</strong>", "Arabica Cherry"],
             ["<strong>RC</strong>", "Robusta Cherry AB"],
             ["<strong>RP</strong>", "Robusta Parchment"]]) + '</div>',
        '<div class="spec-block reveal"><h2>HSN codes</h2>' + table(
            "HSN classification by coffee form.",
            ["Product", "HSN"],
            [["Green coffee beans", "090111"],
             ["Roasted coffee beans", "09012190 / 09019090"],
             ["Instant coffee", "21011110 / 21011120"]]) + '</div>',
        '<div class="spec-block reveal"><h2>Packaging options</h2>' + table(
            "Packaging formats by coffee type.",
            ["Type", "Formats"],
            [["Green beans", "60 kg / 70 kg jute bags"],
             ["Roasted beans", "250 g / 500 g / 1 kg valve or foil packs"],
             ["Instant coffee", "50 g / 100 g / 200 g jars or pouches"],
             ["Bulk", "10 kg / 20 kg / 25 kg cartons"]])
        + '<p style="margin-top:1.1rem;font-size:.9rem;color:#5C666C">Private label and custom branding available across all formats.</p></div>',
        """<div class="spec-block reveal">
  <h2>Key features</h2>
  <ul class="checklist checklist--2">
    <li>Clean and sorted beans</li>
    <li>Uniform grading</li>
    <li>Moisture-controlled processing</li>
    <li>Custom packaging available</li>
  </ul>
</div>""",
    ],
    [(I['cof1'], "Green Indian coffee beans for export"),
     (I['cof2'], "Roasted Indian coffee beans"),
     (I['cof3'], "Packaged Indian coffee ready for shipment")],
    [("Origins", "Selected Indian estates"), ("Species", "Arabica &amp; Robusta"), ("Private label", "Available")],
    product_schema("Indian Coffee — Arabica &amp; Robusta",
                   "Green, roasted and instant Indian coffee in PL, AC, RC and RP grades, processed and export-packed to buyer requirement.",
                   I['cof3'], "Coffee"),
    "090111 &middot; 09012190 &middot; 21011110",
)

# ------------------------------- SPICES
product_page(
    "spices.html",
    "Indian Spices &amp; Sannam S4 Red Chilli | Xcellence Exim",
    "Export-grade Sannam S4 / S334 red chilli with bright red colour and medium pungency, plus turmeric, cumin seeds, cloves and cardamom. Cleaned, sortex and stemless options available.",
    "Spices", "Indian Spices &amp; Red Chilli",
    "Premium Sannam S4 red chilli sourced directly from trusted Indian farms, known for medium pungency, bright red colour and balanced heat.",
    "Spices",
    [
        """<div class="spec-block reveal">
  <h2>Overview</h2>
  <p>We supply high-quality Sannam S4 red chilli sourced directly from trusted farms in India. Known for its medium pungency, bright red colour and balanced heat, it is widely used across international markets in spice blending and industrial food processing.</p>
</div>""",
        '<div class="spec-block reveal"><h2>Key specifications</h2>' + table(
            "Sannam S4 red chilli — export specification.",
            ["Parameter", "Specification"],
            [["<strong>Variety</strong>", "Sannam S4 / S334"],
             ["<strong>Heat level</strong>", "Medium"],
             ["<strong>Colour</strong>", "Bright red"],
             ["<strong>Moisture</strong>", "Export standard, controlled"],
             ["<strong>Processing</strong>", "Cleaned / Sortex / Stemless options available"]]) + '</div>',
        '<div class="spec-block reveal"><h2>Applications</h2>'
        + chips(["Spice blending", "Food processing", "Sauces &amp; seasoning", "Retail packaging"]) + '</div>',
        '<div class="spec-block reveal"><h2>Packaging options</h2>'
        + chips(["10 kg PP bags", "25 kg PP bags", "50 kg PP bags", "Jumbo bags", "Vacuum retail packs", "Private label"])
        + '<p style="margin-top:1.1rem;font-size:.9rem;color:#5C666C">Vacuum-packed retail formats prepared to requirement.</p></div>',
        '<div class="spec-block reveal"><h2>Other spices</h2>'
        + chips(["Turmeric", "Cumin seeds", "Cloves", "Cardamom"])
        + '<p style="margin-top:1.1rem;font-size:.9rem;color:#5C666C">Additional spices are sourced against confirmed enquiries — share your specification and volume.</p></div>',
    ],
    [(I['spi1'], "Sannam S4 red chilli, export grade"),
     (I['spi2'], "Indian spices sorted for export"),
     (I['spi3'], "Packed Indian spices ready for shipment")],
    [("Lead variety", "Sannam S4 / S334"), ("Processing", "Cleaned / Sortex / Stemless"), ("Bulk", "Jumbo bags available")],
    product_schema("Sannam S4 Red Chilli &amp; Indian Spices",
                   "Export-grade Sannam S4 red chilli with bright red colour and medium heat, plus turmeric, cumin, cloves and cardamom.",
                   I['spi3'], "Spices"),
    "090421",
)

# ------------------------------- SUGAR
product_page(
    "sugar.html",
    "Sugar ICUMSA 45 &amp; Refined Indian Sugar | Xcellence Exim",
    "Refined and raw Indian sugar from certified mills: ICUMSA 45, ICUMSA 100–150, ICUMSA 200–600 brown sugar and raw sugar. 50 kg PP bags and 1 MT jumbo bags.",
    "Sugar ICUMSA 45", "Sugar ICUMSA 45",
    "High-quality refined and raw sugar sourced from certified Indian sugar mills — processed, tested and export-ready packed to buyer requirement.",
    "Sugar",
    [
        """<div class="spec-block reveal">
  <h2>Overview</h2>
  <p>We supply high-quality refined and raw sugar sourced from certified Indian sugar mills. All sugar is processed, tested and export-ready packed as per buyer requirements, with grade selection matched to your end application.</p>
</div>""",
        '<div class="spec-block reveal"><h2>Available grades</h2>' + table(
            "Sugar grades available for export.",
            ["Grade", "Description"],
            [["<strong>ICUMSA 45</strong>", "Highly refined white crystal sugar for direct consumption and industrial use"],
             ["<strong>ICUMSA 100–150</strong>", "Standard refined white sugar for general food applications"],
             ["<strong>ICUMSA 200–600</strong>", "Light brown sugar with mild molasses content"],
             ["<strong>Raw Sugar</strong>", "Unrefined natural sugar used for further processing"]]) + '</div>',
        """<div class="spec-block reveal">
  <h2>Key features</h2>
  <ul class="checklist checklist--2">
    <li>High purity and consistent grain size</li>
    <li>Low moisture and clean processing</li>
    <li>Suitable for food &amp; beverage industries</li>
    <li>Export-grade quality control</li>
  </ul>
</div>""",
        '<div class="spec-block reveal"><h2>Packaging options</h2>'
        + chips(["50 kg PP bags", "25 kg bags (on request)", "1 MT jumbo bags"]) + '</div>',
    ],
    [(I['sug1'], "Refined white crystal sugar ICUMSA 45"),
     (I['sug2'], "Sugar packed for export"),
     (I['sug3'], "Certified Indian mill sugar in bulk packing")],
    [("Lead grade", "ICUMSA 45"), ("Bulk packing", "1 MT jumbo bags"), ("Source", "Certified Indian mills")],
    product_schema("Sugar ICUMSA 45",
                   "Refined white crystal sugar from certified Indian mills, plus ICUMSA 100–150, brown sugar and raw sugar grades.",
                   I['sug2'], "Sugar"),
    "17019990",
)


# =========================================================================
# EXPORT PROCESS + FAQ
# =========================================================================
FAQS = [
    ("What is your minimum order quantity?",
     "Minimum quantity depends on the commodity and packing format — typically one full 20&nbsp;ft container. Share your requirement and destination port and we will confirm the workable minimum for that specific product."),
    ("Which Incoterms do you work with?",
     "We regularly quote FOB and CIF, and can work to CFR or EXW where it suits your logistics arrangement. Tell us your preference in the enquiry and the quotation will be structured accordingly."),
    ("Can I get a sample before placing an order?",
     "Yes. Pre-shipment samples are dispatched for approval where required, so you can verify grain, colour, moisture and grading against your own standard before the consignment is packed."),
    ("What documents do you provide with each shipment?",
     "Commercial Invoice, Packing List, Certificate of Origin and Certificate of Analysis as standard, along with shipping and logistics coordination. Additional documents required by your customs authority can be arranged on request."),
    ("Do you offer private labelling?",
     "Yes. Private label and custom branding are available across our range — rice bags, coffee valve packs and retail formats, spice packs and sugar bags — subject to artwork approval and order volume."),
    ("How long does it take to receive a quotation?",
     "Our export desk replies within one business day. To get an accurate offer first time, include the product and grade, quantity, destination port, preferred Incoterms and packing format."),
    ("Which markets do you supply?",
     "We supply importers, wholesalers, distributors and food manufacturers across international markets, and adapt to regional quality standards, packaging requirements and regulatory compliance."),
    ("Are your products lab tested?",
     "Yes. Products are tested for purity, moisture and safety parameters, and a Certificate of Analysis is issued per consignment."),
]

faq_schema = '<script type="application/ld+json">\n{\n  "@context": "https://schema.org",\n  "@type": "FAQPage",\n  "mainEntity": [\n'
faq_schema += ",\n".join(
    '    { "@type": "Question", "name": "%s", "acceptedAnswer": { "@type": "Answer", "text": "%s" } }'
    % (q.replace('"', "'"), a.replace('&nbsp;', ' ').replace('"', "'"))
    for q, a in FAQS)
faq_schema += '\n  ]\n}\n</script>\n'

proc = head(
    "Export Process &amp; Buyer FAQ | Xcellence Exim",
    "How Xcellence Exim moves an order from enquiry to delivered container: sourcing, inspection, sampling, packing, documentation and shipment — plus answers to common importer questions.",
    "export-process.html", extra_schema=faq_schema, og_image=I['hero3'])
proc += header("export-process.html")
proc += pagehead(
    "Export Process &amp; Buyer FAQ",
    "From first enquiry to delivered container — every stage documented, so you always know what is coming and when.",
    "Export Process")

steps = [
    ("Understanding buyer requirements", "We start with the specifics: product and grade, quantity, destination port, Incoterms, packing format and any regulatory requirement in your market."),
    ("Product sourcing &amp; quality inspection", "We select the mill or processor best matched to your specification and inspect against agreed tolerances before anything is committed."),
    ("Sampling and approval", "Where required, a pre-shipment sample is dispatched so you can verify quality against your own standard before packing begins."),
    ("Packaging to international standards", "Export-grade materials selected for the commodity and transit route — PP, BOPP, jute, non-woven, jumbo bags, valve packs or retail formats, with private labelling where agreed."),
    ("Documentation &amp; logistics coordination", "Commercial invoice, packing list, certificate of origin and COA prepared alongside booking, so your clearing agent receives a complete set on time."),
    ("Timely shipment &amp; post-dispatch support", "Container despatched within the agreed window, with documents couriered and tracked, and a single point of contact available after shipment."),
]
steps_html = "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in steps)

faq_html = "".join(
    f'<details><summary>{q}</summary><div class="faq__a">{a}</div></details>'
    for q, a in FAQS)

proc += f"""
<section class="section">
  <div class="wrap">
    <div class="split reveal">
      <div>
        <span class="eyebrow">Six stages</span>
        <hr class="rule">
        <h2>How an order moves</h2>
        <ol class="steps">{steps_html}</ol>
      </div>
      <div class="split__media">
        <img src="{I['hero3']}" alt="Export logistics and container shipment" width="800" height="600" loading="lazy">
      </div>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Export support</span>
      <hr class="rule">
      <h2>Documentation we prepare</h2>
      <p class="lead">A complete, clean document set handed over on schedule — the single biggest cause of port delays, removed.</p>
    </div>
    <div class="grid grid--3 reveal">
      <div class="tile"><span class="tile__icon">{ICON['doc']}</span><h3>Commercial Invoice</h3><p>Prepared to match your purchase order, LC terms and customs requirements exactly.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['box']}</span><h3>Packing List</h3><p>Bag counts, net and gross weights, and container stuffing detail per consignment.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['globe']}</span><h3>Certificate of Origin</h3><p>Issued through the relevant authority for preferential or non-preferential treatment.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['lab']}</span><h3>Certificate of Analysis</h3><p>Lab results for purity, moisture and safety parameters, issued per shipment.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['ship']}</span><h3>Shipping coordination</h3><p>Booking, stuffing, bill of lading and courier of original documents, tracked throughout.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['shield']}</span><h3>Compliance support</h3><p>Phytosanitary, fumigation and market-specific documents arranged on request.</p></div>
    </div>
  </div>
</section>

<section class="section" id="faq">
  <div class="wrap wrap--narrow">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Buyer FAQ</span>
      <hr class="rule">
      <h2>Questions importers ask us</h2>
    </div>
    <div class="faq reveal">{faq_html}</div>
  </div>
</section>
"""
proc += cta_band("Still have a question?",
                 "Our export desk answers enquiries within one business day — including specification queries, sampling requests and documentation questions.")
proc += footer()
write('export-process.html', proc)


# =========================================================================
# CERTIFICATES
# =========================================================================
certs = head(
    "Certificates &amp; Registrations | Xcellence Exim",
    "Xcellence Exim is registered and compliant: IEC, GST, FSSAI, MSME and APEDA. View our statutory certificates and registrations.",
    "certificates.html", og_image=I['cert1'])
certs += header("certificates.html")
certs += pagehead(
    "Certificates &amp; Registrations",
    "Registered, compliant and export-ready. Select any certificate to view it full size.",
    "Certificates")

cert_items = [
    (I['cert1'], "Registration certificate 1"),
    (I['cert2'], "Registration certificate 2"),
    (I['cert3'], "Registration certificate 3"),
    (I['cert4'], "Registration certificate 4"),
    (I['cert5'], "Registration certificate 5"),
]
cert_html = "".join(
    f'''<a class="cert" href="{src}" data-lightbox="{src}" aria-label="View {alt} full size">
      <img src="{src}" alt="{alt}" width="600" height="800" loading="lazy">
      <span class="cert__cap">{alt} {ICON['expand']}</span>
    </a>''' for src, alt in cert_items)

certs += f"""
<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Registered &amp; compliant</span>
      <hr class="rule">
      <h2>Our statutory registrations</h2>
      <p class="lead">Xcellence Exim holds IEC, GST, FSSAI, MSME and APEDA registrations. We are export-ready and committed to delivering quality Indian products through a transparent and professional process.</p>
    </div>
    <div class="cert-grid reveal">{cert_html}</div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="grid grid--4 reveal">
      <div class="tile"><span class="tile__icon">{ICON['globe']}</span><h3>IEC</h3><p>Importer Exporter Code issued by the DGFT — the statutory licence to trade internationally from India.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['doc']}</span><h3>GST</h3><p>GST No: 08AAAFX5073E1Z6 — registered for Goods and Services Tax in Rajasthan, India.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['shield']}</span><h3>FSSAI</h3><p>Food Safety and Standards Authority of India registration covering food-grade handling.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['tag']}</span><h3>APEDA &amp; MSME</h3><p>Agricultural &amp; Processed Food Products Export Development Authority registration, plus MSME registration.</p></div>
    </div>
  </div>
</section>
"""
certs += cta_band("Need copies for your compliance file?",
                  "We can share certificate copies, specification sheets and a Certificate of Analysis for any consignment on request.")
certs += footer()
certs = certs.replace('</body>', f'''
<div class="lightbox" aria-hidden="true" role="dialog" aria-modal="true" aria-label="Certificate viewer">
  <button type="button" class="lightbox__close" aria-label="Close certificate viewer">{ICON['close']}</button>
  <img src="" alt="">
</div>
</body>''')
write('certificates.html', certs)


# =========================================================================
# CONTACT
# =========================================================================
contact = head(
    "Contact Us | Xcellence Exim — Request a Quotation",
    "Contact Xcellence Exim for export quotations on Indian rice, coffee, spices and Sugar ICUMSA 45. WhatsApp +91 79859 16897 or email sales@xcellenceexim.com.",
    "contact.html", og_image=I['hero1'])
contact += header("contact.html")
contact += pagehead(
    "Contact Us",
    "Tell us the product, quantity, destination port and Incoterms — you will have a detailed offer from our export desk within one business day.",
    "Contact")

contact += f"""
<section class="section">
  <div class="wrap">
    <div class="spec-layout">
      <div id="rfq">
        <div class="section-head reveal">
          <span class="eyebrow">Request for quotation</span>
          <hr class="rule">
          <h2>Send us your enquiry</h2>
          <p class="lead">The more detail you give, the more accurate the first offer — and the fewer emails it takes to close.</p>
        </div>

        <div class="form-card reveal">
          <form id="rfq-form" novalidate method="POST"
                action="{ENQUIRY_ENDPOINT}"
                data-endpoint="{ENQUIRY_ENDPOINT}"
                data-to="{EMAIL_SALES}"
                data-cc="{EMAIL_DIR}"
                data-whatsapp="{WA}">
            <!-- Enquiries are sent through the company's Google Workspace Apps
                 Script endpoint. The action is also the no-JavaScript fallback;
                 no email client or third-party form relay is used. -->
            <div class="field-grid">
              <div class="field">
                <label for="f-name">Full name <span class="req" aria-hidden="true">*</span></label>
                <input type="text" id="f-name" name="name" autocomplete="name" required>
                <span class="err"></span>
              </div>
              <div class="field">
                <label for="f-company">Company</label>
                <input type="text" id="f-company" name="company" autocomplete="organization">
              </div>
              <div class="field">
                <label for="f-email">Email address <span class="req" aria-hidden="true">*</span></label>
                <input type="email" id="f-email" name="email" autocomplete="email" inputmode="email" required>
                <span class="err"></span>
              </div>
              <div class="field">
                <label for="f-phone">Phone / WhatsApp</label>
                <input type="tel" id="f-phone" name="phone" autocomplete="tel" inputmode="tel">
              </div>
              <div class="field">
                <label for="f-country">Destination country <span class="req" aria-hidden="true">*</span></label>
                <input type="text" id="f-country" name="country" autocomplete="country-name" required>
                <span class="err"></span>
              </div>
              <div class="field">
                <label for="f-port">Destination port</label>
                <input type="text" id="f-port" name="port" placeholder="e.g. Jebel Ali, Durban, Santos">
              </div>
              <div class="field">
                <label for="f-product">Product <span class="req" aria-hidden="true">*</span></label>
                <select id="f-product" name="product" required>
                  <option value="">Select a product…</option>
                  <option>Rice — Basmati</option>
                  <option>Rice — Non-Basmati</option>
                  <option>Coffee — Green beans</option>
                  <option>Coffee — Roasted beans</option>
                  <option>Coffee — Instant</option>
                  <option>Spices — Sannam S4 red chilli</option>
                  <option>Spices — Other</option>
                  <option>Sugar ICUMSA 45</option>
                  <option>Sugar — Other grade</option>
                  <option>Other agro commodity</option>
                </select>
                <span class="err"></span>
              </div>
              <div class="field">
                <label for="f-qty">Quantity required</label>
                <input type="text" id="f-qty" name="quantity" placeholder="e.g. 1 x 20 ft FCL / 25 MT">
              </div>
              <div class="field">
                <label for="f-incoterm">Preferred Incoterm</label>
                <select id="f-incoterm" name="incoterm">
                  <option value="">No preference</option>
                  <option>FOB</option>
                  <option>CIF</option>
                  <option>CFR</option>
                  <option>EXW</option>
                </select>
              </div>
              <div class="field">
                <label for="f-packing">Packing preference</label>
                <input type="text" id="f-packing" name="packing" placeholder="e.g. 25 kg BOPP, private label">
              </div>
              <div class="field field--full">
                <label for="f-msg">Message <span class="req" aria-hidden="true">*</span></label>
                <textarea id="f-msg" name="message" required placeholder="Specification, grade, target price, delivery window, or any certification you need."></textarea>
                <span class="err"></span>
              </div>
            </div>

            <div class="hp" aria-hidden="true">
              <label for="f-hp">Leave this field empty</label>
              <input type="text" id="f-hp" name="company_website" tabindex="-1" autocomplete="off">
            </div>

            <div class="form-actions">
              <button type="submit" class="btn btn--primary">Send enquiry {ICON['arrow']}</button>
              <button type="button" class="btn btn--outline" id="rfq-whatsapp">Send via WhatsApp</button>
            </div>
            <p class="form-note">We use your details only to prepare and follow up on this quotation. No marketing lists, no sharing with third parties.</p>
            <div class="form-status" id="form-status" role="status" aria-live="polite"></div>
          </form>
        </div>
      </div>

      <aside>
        <div class="aside-card">
          <h3>Export desk</h3>
          <p>Reach us directly — we typically reply the same working day.</p>
          <dl translate="no" class="notranslate">
            <dt>WhatsApp / Phone</dt>
            <dd><a href="https://wa.me/{WA}" target="_blank" rel="noopener" style="color:#DFBE4B">{PHONE}</a></dd>
            <dt>Sales</dt>
            <dd><a href="mailto:{EMAIL_SALES}" style="color:#DFBE4B">{EMAIL_SALES}</a></dd>
            <dt>Director</dt>
            <dd><a href="mailto:{EMAIL_DIR}" style="color:#DFBE4B">{EMAIL_DIR}</a></dd>
            <dt>Address</dt>
            <dd>Ashirwad Neelanchal, B-402,<br>Shrinathpuram, Kota — 324010,<br>Rajasthan, India</dd>
            <dt>Registered &amp; compliant</dt>
            <dd>IEC &middot; GST &middot; FSSAI &middot; MSME &middot; APEDA</dd>
            <dt>GST No.</dt>
            <dd>08AAAFX5073E1Z6</dd>
          </dl>
          <a class="btn btn--primary" href="https://wa.me/{WA}" target="_blank" rel="noopener">Chat on WhatsApp</a>
          <a class="btn btn--ghost" href="tel:+917985916897">Call the export desk</a>
        </div>
      </aside>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Before you write</span>
      <hr class="rule">
      <h2>Four details that get you a firm price fastest</h2>
    </div>
    <div class="grid grid--4 reveal">
      <div class="tile"><span class="tile__icon">{ICON['tag']}</span><h3>Product &amp; grade</h3><p>e.g. 1121 Sella Golden Basmati, or Robusta Cherry AB.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['box']}</span><h3>Quantity &amp; packing</h3><p>Container count or tonnage, and preferred bag size or retail format.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['ship']}</span><h3>Destination port</h3><p>The discharge port determines freight and therefore your landed cost.</p></div>
      <div class="tile"><span class="tile__icon">{ICON['doc']}</span><h3>Incoterms</h3><p>FOB, CIF, CFR or EXW — plus any certificates your customs authority requires.</p></div>
    </div>
  </div>
</section>
"""
contact += footer()
write('contact.html', contact)


# =========================================================================
# sitemap / robots
# =========================================================================
pages = ["", "about.html", "rice.html", "coffee.html", "spices.html",
         "sugar.html", "export-process.html", "certificates.html", "contact.html"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for p in pages:
    pr = "1.0" if p == "" else ("0.9" if p in ("contact.html", "about.html") else "0.8")
    sm += f"  <url><loc>{SITE}/{p}</loc><changefreq>monthly</changefreq><priority>{pr}</priority></url>\n"
sm += "</urlset>\n"
write('sitemap.xml', sm)
write('robots.txt', f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

print('\nDone.')
