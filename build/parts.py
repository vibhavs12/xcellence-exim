# -*- coding: utf-8 -*-
"""Shared chrome (head, header, drawer, footer) for the Xcellence Exim site."""

SITE = "https://xcellenceexim.com"
GA4_ID = "G-XFVMBYF6P9"
PHONE = "+91 79859 16897"
WA = "917985916897"
EMAIL_SALES = "sales@xcellenceexim.com"
EMAIL_INFO = "info@xcellenceexim.com"
EMAIL_DIR = "ashwani@xcellenceexim.com"
ENQUIRY_ENDPOINT = "https://script.google.com/macros/s/AKfycbzaIttnTKeeHGlPzfkkl4dVBslXxUuc9k5ZCYf1t_U5cfGaTYDjogVXyJqFi23_q3zXSA/exec"
FB = "https://www.facebook.com/profile.php?id=61578054179792"
IG = "https://www.instagram.com/xcellence_exim"
LI = "https://www.linkedin.com/company/xcellence-exim/"

# Images are served from the client's existing WordPress media library so the
# redesign works the moment you open it. Run tools/download-images.sh to
# self-host them under assets/img/ and swap IMG_BASE to "assets/img".
IMG = SITE + "/wp-content/uploads"

IMAGES = {
    "logo":   IMG + "/2026/07/Screenshot-2026-07-15-180236.png",
    "hero1":  IMG + "/2025/09/spice-shop-37.png",
    "hero2":  IMG + "/2025/09/spice-shop-36.png",
    "hero3":  IMG + "/2025/09/spice-shop-38.png",
    "hero4":  IMG + "/2025/09/spice-shop-40.png",
    "home_rice":   "assets/img/home/rice.jpg",
    "home_coffee": "assets/img/home/coffee.jpg",
    "home_spices": "assets/img/home/spices.jpg",
    "home_sugar":  "assets/img/home/sugar.jpg",
    "home_logistics": "assets/img/home/export-documentation.jpg",
    "order_process": "assets/img/home/order-process.jpg",
    "about":  "assets/img/home/verified-sourcing.jpg",
    "rice1":  IMG + "/2025/07/1.png",
    "rice2":  IMG + "/2025/07/2.png",
    "rice3":  IMG + "/2025/07/3.png",
    "cof1":   IMG + "/2025/07/7.png",
    "cof2":   IMG + "/2025/07/8.png",
    "cof3":   IMG + "/2025/07/9.png",
    "spi1":   IMG + "/2025/07/10.png",
    "spi2":   IMG + "/2025/07/11.png",
    "spi3":   IMG + "/2025/07/12.png",
    "sug1":   IMG + "/2026/05/Paneer-Bhurji-35.png",
    "sug2":   IMG + "/2026/05/Paneer-Bhurji-36.png",
    "sug3":   IMG + "/2026/05/Paneer-Bhurji-37.png",
    "cert1":  IMG + "/2025/09/Screenshot-2025-09-25-194937.png",
    "cert2":  IMG + "/2025/09/Screenshot-2025-09-25-194946.png",
    "cert3":  IMG + "/2025/09/Screenshot-2025-09-25-195001.png",
    "cert4":  IMG + "/2025/09/Screenshot-2025-09-25-195013.png",
    "cert5":  IMG + "/2025/09/Screenshot-2025-09-25-195022.png",
}

# ---------------------------------------------------------------- icons
ICON = {
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>',
    "caret": '<svg class="nav__caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>',
    "caret_lang": '<svg class="langpick__caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>',
    "caret_p": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>',
    "menu": '<svg class="icon-open" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg><svg class="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>',
    "close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.2-.7.1-.8 1-1 1.2-.4.2-.7 0a8.2 8.2 0 0 1-2.4-1.5 9 9 0 0 1-1.7-2.1c-.2-.3 0-.5.1-.6l.5-.6.3-.5v-.5l-1-2.3c-.2-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.6 3.6 0 0 0-1.1 2.7 6.3 6.3 0 0 0 1.3 3.3 14.3 14.3 0 0 0 5.5 4.8c.8.3 1.4.5 1.8.7a4.4 4.4 0 0 0 2 .1 3.3 3.3 0 0 0 2.1-1.5 2.6 2.6 0 0 0 .2-1.5c-.1-.1-.3-.2-.6-.3zM12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm0 18.3a8.3 8.3 0 0 1-4.2-1.2l-.3-.2-3.1.8.8-3-.2-.3A8.3 8.3 0 1 1 12 20.3z"/></svg>',
    "fb": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0 0 22 12z"/></svg>',
    "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/></svg>',
    "li": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM3 9h4v12H3zM10 9h3.8v1.7h.05a4.2 4.2 0 0 1 3.75-2c4 0 4.75 2.6 4.75 6V21h-4v-5.5c0-1.3 0-3-1.85-3s-2.15 1.44-2.15 2.9V21h-4z"/></svg>',
    "expand": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2 4 5v6c0 5 3.4 9.7 8 11 4.6-1.3 8-6 8-11V5z"/><path d="m9 12 2 2 4-4"/></svg>',
    "ship": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 18a4 4 0 0 0 3.3-1.8L6 15l1.4 1.5a4 4 0 0 0 5.9 0L15 15l1.4 1.5A4 4 0 0 0 22 18"/><path d="M4 15V9l8-4 8 4v6"/><path d="M12 5V2"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H7a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7z"/><path d="M14 2v5h5M9 13h6M9 17h4"/></svg>',
    "box": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="m3 8 9 5 9-5M12 13v8"/></svg>',
    "lab": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 2v6.4L4.4 18A2 2 0 0 0 6.1 21h11.8a2 2 0 0 0 1.7-3L14 8.4V2"/><path d="M8.5 2h7M7 15h10"/></svg>',
    "talk": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 9 9 0 0 1-3.8-.8L3 21l1.9-5.1A8.4 8.4 0 0 1 12 3a8.4 8.4 0 0 1 9 8.5z"/></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a15 15 0 0 1 4 9 15 15 0 0 1-4 9 15 15 0 0 1-4-9 15 15 0 0 1 4-9z"/></svg>',
    "tag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.6 13.4 12 22l-9-9V4a1 1 0 0 1 1-1h8z"/><circle cx="7.5" cy="7.5" r="1.4"/></svg>',
}

PAGE_ROUTES = {
    "index.html": "",
    "about.html": "about-us/",
    "rice.html": "rice/",
    "coffee.html": "tea-coffee/",
    "spices.html": "spices/",
    "sugar.html": "sugar-icumsa-45/",
    "export-process.html": "export-process/",
    "certificates.html": "certificates/",
    "contact.html": "contact-us/",
    "privacy.html": "privacy/",
}


def route_href(page):
    """Root-relative-with-base link used by both home and nested pages."""
    route = PAGE_ROUTES[page]
    return route or "./"


def public_url(page):
    return SITE + "/" + PAGE_ROUTES[page]


def output_path(page):
    route = PAGE_ROUTES[page]
    return "index.html" if not route else route + "index.html"


NAV = [
    ("index.html", "Home", None),
    ("about.html", "About Us", None),
    ("#", "Our Products", [
        ("rice.html", "Rice"),
        ("coffee.html", "Coffee"),
        ("spices.html", "Spices &amp; Red Chilli"),
        ("sugar.html", "Sugar ICUMSA 45"),
    ]),
    ("export-process.html", "Export Process", None),
    ("certificates.html", "Certificates", None),
    ("contact.html", "Contact", None),
]

PAGE_NAMES = {
    "index.html": "Indian Agricultural Exporter",
    "about.html": "About Xcellence Exim",
    "rice.html": "Indian Rice Exporter",
    "coffee.html": "Indian Coffee Exporter",
    "spices.html": "Indian Spices Exporter",
    "sugar.html": "Indian Sugar Exporter",
    "export-process.html": "Export Process and Buyer FAQ",
    "certificates.html": "Export Certificates and Registrations",
    "contact.html": "Request an Export Quotation",
    "privacy.html": "Privacy Notice",
}


def head(title, desc, page, extra_schema="", og_image=None):
    canonical = public_url(page)
    base = "" if page == "index.html" else '<base href="../">\n'
    img = og_image or IMAGES["hero1"]
    if not img.startswith(("http://", "https://")):
        img = SITE + "/" + img.lstrip("/")
    page_name = PAGE_NAMES.get(page, "Xcellence Exim")
    website_schema = ""
    breadcrumb_schema = ""
    if page == "index.html":
        website_schema = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "{SITE}/#website",
  "url": "{SITE}/",
  "name": "Xcellence Exim",
  "alternateName": "Xcellence Exim India",
  "publisher": {{ "@id": "{SITE}/#organization" }},
  "inLanguage": "en-IN"
}}
</script>
'''
    else:
        breadcrumb_schema = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE}/" }},
    {{ "@type": "ListItem", "position": 2, "name": "{page_name}", "item": "{canonical}" }}
  ]
}}
</script>
'''
    return f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{base}<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="theme-color" content="#0F3D2E">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Xcellence Exim">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{img}">
<meta property="og:image:alt" content="{page_name} — Xcellence Exim">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{img}">
<meta name="twitter:image:alt" content="{page_name} — Xcellence Exim">

<link rel="icon" href="{IMAGES['logo']}">
<link rel="apple-touch-icon" href="{IMAGES['logo']}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://cdn.gtranslate.net">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=Noto+Sans+Arabic:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "{SITE}/#organization",
  "name": "Xcellence Exim",
  "description": "Indian agricultural exporter and supplier of Basmati and non-Basmati rice, Arabica and Robusta coffee, Indian spices, Sannam S4 red chilli and sugar ICUMSA 45 for global importers.",
  "url": "{SITE}/",
  "logo": "{IMAGES['logo']}",
  "email": "{EMAIL_SALES}",
  "telephone": "{PHONE}",
  "areaServed": "Worldwide",
  "knowsAbout": ["Indian rice export", "Indian coffee export", "Indian spices export", "Sugar ICUMSA 45 export", "Agricultural export documentation"],
  "contactPoint": {{
    "@type": "ContactPoint",
    "contactType": "export sales",
    "email": "{EMAIL_SALES}",
    "telephone": "{PHONE}",
    "availableLanguage": ["English", "Hindi"],
    "areaServed": "Worldwide"
  }},
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "Ashirwad Neelanchal, B-402, Shrinathpuram",
    "addressLocality": "Kota",
    "addressRegion": "Rajasthan",
    "postalCode": "324010",
    "addressCountry": "IN"
  }},
  "sameAs": ["{FB}", "{IG}", "{LI}"]
}}
</script>
{website_schema}{breadcrumb_schema}
{extra_schema}
<script>
/* Keep the GitHub Pages preview out of search and load analytics only after
   consent on the production domain. Canonicals always point to production. */
(function () {{
  var preview = /\\.(github\\.io|pages\\.dev)$/i.test(location.hostname);
  if (preview) {{
    var robots = document.querySelector('meta[name="robots"]');
    if (robots) robots.content = 'noindex, nofollow';
  }}
  window.XE_GA4_ID = "{GA4_ID}";
  window.XE_IS_PRODUCTION = /(^|\\.)xcellenceexim\\.com$/i.test(location.hostname);
  window.xeLoadAnalytics = function () {{
    if (!window.XE_IS_PRODUCTION || document.querySelector('script[data-xe-ga4]')) return;
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () {{ window.dataLayer.push(arguments); }};
    window.gtag('js', new Date());
    window.gtag('config', window.XE_GA4_ID, {{ anonymize_ip: true }});
    var script = document.createElement('script');
    script.async = true;
    script.dataset.xeGa4 = 'true';
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(window.XE_GA4_ID);
    document.head.appendChild(script);
  }};
  try {{
    if (localStorage.getItem('xe-analytics-consent') === 'granted') window.xeLoadAnalytics();
  }} catch (e) {{ /* storage can be unavailable in privacy modes */ }}
}}());
</script>
<script>window.gtranslateSettings = {{"default_language":"en","detect_browser_language":false,"wrapper_selector":".gtranslate_wrapper","switcher_horizontal_position":"inline"}};</script>
<script src="https://cdn.gtranslate.net/widgets/latest/dropdown.js" defer></script>
<script src="assets/js/languages.js" defer></script>
<script src="assets/js/main.js" defer></script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


def langpick():
    """The language picker.

    Marked `notranslate` / `translate="no"` on purpose — the language names are
    written in their own language (endonyms), so Google Translate must leave
    them alone. Flags come from flagcdn.com and degrade to a lettered chip if
    the image fails to load.

    The list itself is populated at runtime from GTranslate's own <select>, so
    it always matches exactly what the translation service supports.
    """
    return f"""<div class="langpick notranslate" translate="no">
        <button type="button" class="langpick__btn" aria-expanded="false" aria-haspopup="true" aria-label="Choose language">
          <img class="langpick__flag" src="https://flagcdn.com/w20/gb.png" srcset="https://flagcdn.com/w40/gb.png 2x" alt="" width="20" height="15">
          <span class="langpick__current">English</span>
          {ICON['caret_lang']}
        </button>
        <div class="langpick__panel" hidden>
          <div class="langpick__search">
            <input type="search" placeholder="Search language…" aria-label="Search language" autocomplete="off" spellcheck="false">
          </div>
          <div class="langpick__body">
            <p class="langpick__heading">Key export markets</p>
            <div class="langpick__grid" data-lang-priority></div>
            <p class="langpick__heading">All languages</p>
            <ul class="langpick__list" data-lang-list></ul>
            <p class="langpick__empty" data-lang-empty hidden>No language matches that search.</p>
          </div>
          <p class="langpick__note">Machine translation by Google. English remains the reference version for contracts and specifications.</p>
        </div>
      </div>
      <div class="gtranslate_wrapper"></div>"""


def header(active):
    def link(href, label, sub):
        if sub:
            is_active = active in [s[0] for s in sub]
            items = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in sub)
            cur = ' aria-current="page"' if is_active else ''
            return (f'<li class="has-dropdown"><button type="button" class="nav__link" '
                    f'aria-expanded="false" aria-haspopup="true"{cur}>{label}{ICON["caret"]}</button>'
                    f'<ul class="dropdown">{items}</ul></li>')
        cur = ' aria-current="page"' if href == active else ''
        return f'<li><a class="nav__link" href="{href}"{cur}>{label}</a></li>'

    menu = "".join(link(h, l, s) for h, l, s in NAV)

    return f"""
<div class="topbar">
  <div class="wrap topbar__inner">
    <div class="topbar__contact">
      <span translate="no" class="notranslate">{ICON['phone']}<a href="tel:+917985916897">{PHONE}</a></span>
      <span translate="no" class="notranslate">{ICON['mail']}<a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a></span>
    </div>
    <div class="topbar__right">
      <span class="topbar__social">
        <a href="{FB}" target="_blank" rel="noopener" aria-label="Xcellence Exim on Facebook">{ICON['fb']}</a>
        <a href="{IG}" target="_blank" rel="noopener" aria-label="Xcellence Exim on Instagram">{ICON['ig']}</a>
        <a href="{LI}" target="_blank" rel="noopener" aria-label="Xcellence Exim on LinkedIn">{ICON['li']}</a>
      </span>
    </div>
  </div>
</div>

<header class="site-header">
  <nav class="wrap nav" aria-label="Primary">
    <a class="brand" href="index.html" aria-label="Xcellence Exim — home">
      <img src="{IMAGES['logo']}" alt="Xcellence Exim — Indian Agro Exporter" width="180" height="46">
    </a>

    <ul class="nav__menu">{menu}</ul>

    <div class="nav__actions">
      <span data-lang-desktop>{langpick()}</span>
      <a class="btn btn--primary btn--desktop" href="contact.html#rfq"><span>Request a Quote</span></a>
      <button type="button" class="nav__toggle" aria-expanded="false" aria-controls="drawer" aria-label="Open menu">{ICON['menu']}</button>
    </div>
  </nav>
</header>

<div class="drawer" id="drawer" aria-hidden="true">
  <div class="drawer__scrim" data-drawer-close></div>
  <div class="drawer__panel" role="dialog" aria-modal="true" aria-label="Site menu">
    <div class="drawer__head">
      <span class="brand__name">Menu</span>
      <button type="button" class="drawer__close" data-drawer-close aria-label="Close menu">{ICON['close']}</button>
    </div>
    <div class="drawer__body">
      <div class="drawer__lang">
        <span data-lang-mobile></span>
        <p data-lang-fallback hidden class="hint" style="font-size:.78rem;color:#808C93;margin:.5rem 0 0">
          Translation service unavailable — please check your connection.
        </p>
      </div>

      <ul class="drawer__nav">
        <li><a href="index.html"{' aria-current="page"' if active == 'index.html' else ''}>Home</a></li>
        <li><a href="about.html"{' aria-current="page"' if active == 'about.html' else ''}>About Us</a></li>
        <li>
          <button type="button" class="drawer__acc" aria-expanded="false" aria-controls="drawer-products">
            Our Products {ICON['caret_p']}
          </button>
          <ul class="drawer__sub" id="drawer-products">
            <li><a href="rice.html"{' aria-current="page"' if active == 'rice.html' else ''}>Rice</a></li>
            <li><a href="coffee.html"{' aria-current="page"' if active == 'coffee.html' else ''}>Coffee</a></li>
            <li><a href="spices.html"{' aria-current="page"' if active == 'spices.html' else ''}>Spices &amp; Red Chilli</a></li>
            <li><a href="sugar.html"{' aria-current="page"' if active == 'sugar.html' else ''}>Sugar ICUMSA 45</a></li>
          </ul>
        </li>
        <li><a href="export-process.html"{' aria-current="page"' if active == 'export-process.html' else ''}>Export Process &amp; FAQ</a></li>
        <li><a href="certificates.html"{' aria-current="page"' if active == 'certificates.html' else ''}>Certificates</a></li>
        <li><a href="contact.html"{' aria-current="page"' if active == 'contact.html' else ''}>Contact</a></li>
      </ul>

      <div class="drawer__cta">
        <a class="btn btn--primary" href="contact.html#rfq">Request a Quote</a>
        <a class="btn btn--outline" href="https://wa.me/{WA}" target="_blank" rel="noopener">Chat on WhatsApp</a>
      </div>

      <div class="drawer__meta" translate="no">
        <a href="tel:+917985916897">{PHONE}</a>
        <a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a>
      </div>
    </div>
  </div>
</div>

<main id="main">
"""


def cta_band(title="Ready to discuss your next shipment?",
             text="Send us your product, quantity, destination port and preferred Incoterms — you will have a detailed offer from our export desk within one business day."):
    return f"""
<section class="section">
  <div class="wrap">
    <div class="cta-band reveal">
      <div>
        <h2>{title}</h2>
        <p>{text}</p>
      </div>
      <div class="btn-row">
        <a class="btn btn--primary" href="contact.html#rfq">Request a Quote</a>
        <a class="btn btn--ghost" href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp Us</a>
      </div>
    </div>
  </div>
</section>
"""


def footer():
    return f"""
</main>

<footer class="site-footer footer">
  <div class="wrap footer__main">
    <div class="footer__brand">
      <img src="{IMAGES['logo']}" alt="Xcellence Exim" width="180" height="44" loading="lazy">
      <p>A merchant exporter from India supplying premium agricultural commodities to importers, distributors and food manufacturers worldwide.</p>
      <div class="footer__badges" translate="no">
        <span>IEC</span><span>GST</span><span>FSSAI</span><span>MSME</span><span>APEDA</span>
      </div>
      <div class="footer__social">
        <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{ICON['fb']}</a>
        <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{ICON['ig']}</a>
        <a href="{LI}" target="_blank" rel="noopener" aria-label="LinkedIn">{ICON['li']}</a>
      </div>
    </div>

    <div>
      <h4>Products</h4>
      <ul>
        <li><a href="rice.html">Rice — Basmati &amp; Non-Basmati</a></li>
        <li><a href="coffee.html">Coffee — Arabica &amp; Robusta</a></li>
        <li><a href="spices.html">Spices &amp; Red Chilli</a></li>
        <li><a href="sugar.html">Sugar ICUMSA 45</a></li>
      </ul>
    </div>

    <div>
      <h4>Company</h4>
      <ul>
        <li><a href="about.html">About Us</a></li>
        <li><a href="export-process.html">Export Process</a></li>
        <li><a href="export-process.html#faq">Buyer FAQ</a></li>
        <li><a href="certificates.html">Certificates</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>

    <div>
      <h4>Get in touch</h4>
      <address translate="no">
        Ashirwad Neelanchal, B-402,<br>
        Shrinathpuram, Kota — 324010,<br>
        Rajasthan, India
      </address>
      <ul style="margin-top:1rem" translate="no">
        <li><a href="mailto:{EMAIL_SALES}">{EMAIL_SALES}</a></li>
        <li><a href="mailto:{EMAIL_DIR}">{EMAIL_DIR}</a></li>
        <li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp {PHONE}</a></li>
      </ul>
    </div>
  </div>

  <div class="wrap">
    <div class="footer__bottom">
      <p>&copy; <span data-year>2026</span> Xcellence Exim. All rights reserved. &middot; <a href="privacy.html">Privacy Notice</a></p>
      <p translate="no" class="notranslate">GST No: 08AAAFX5073E1Z6</p>
    </div>
  </div>
</footer>

<aside class="consent" data-consent-banner hidden aria-label="Analytics privacy choices">
  <div>
    <strong>Privacy choices</strong>
    <p>We use optional Google Analytics cookies to understand website usage. The site works without them. Read our <a href="privacy.html">Privacy Notice</a>.</p>
  </div>
  <div class="consent__actions">
    <button type="button" class="btn btn--outline" data-consent="denied">Decline</button>
    <button type="button" class="btn btn--primary" data-consent="granted">Accept analytics</button>
  </div>
</aside>

<a class="wa-float" href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="Chat with Xcellence Exim on WhatsApp">{ICON['wa']}</a>

</body>
</html>
"""


def pagehead(title, lead, crumb):
    return f"""
<section class="pagehead">
  <div class="wrap pagehead__inner">
    <ol class="crumbs">
      <li><a href="index.html">Home</a></li>
      <li aria-current="page">{crumb}</li>
    </ol>
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>
"""
