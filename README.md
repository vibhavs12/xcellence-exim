# Xcellence Exim — redesigned website

A complete static rebuild of xcellenceexim.com. No build step, no framework, no
dependencies — open `index.html` locally, or upload the folder to any host.

## Pages

| Canonical path | Page |
|---|---|
| `/` | Home |
| `/about-us/` | About Us |
| `/rice/` | Rice — Basmati & Non-Basmati |
| `/tea-coffee/` | Coffee — Arabica & Robusta |
| `/spices/` | Spices & Sannam S4 Red Chilli |
| `/sugar-icumsa-45/` | Sugar ICUMSA 45 |
| `/export-process/` | Export Process + Buyer FAQ |
| `/certificates/` | Certificates & Registrations |
| `/contact-us/` | Contact + RFQ form |
| `/privacy/` | Privacy Notice |

Plus `sitemap.xml` and `robots.txt`.

## Deploying

**To share a preview with someone:** see `DEPLOY-GITHUB.md` — the repository is
already committed, so it is a push plus one settings toggle.

**Other options:** drag the folder onto **Netlify Drop** (app.netlify.com/drop),
or push to **Vercel** or **Cloudflare Pages**. On traditional hosting
(cPanel / Hostinger), upload the contents into `public_html/`.

## SEO launch requirements

The production domain must serve this build before its SEO changes can affect
Google results. Do not leave the redesigned site only on the GitHub Pages
preview: every canonical URL and the sitemap intentionally point to
`https://xcellenceexim.com`.

At launch:

1. Replace the current WordPress site with this build, or connect
   `xcellenceexim.com` as the GitHub Pages custom domain.
2. Keep the `.htaccess` redirects when deploying to Apache. Existing WordPress
   paths are the canonical content locations; redirects only consolidate the
   temporary redesign-preview `.html` URLs.
3. Verify `https://xcellenceexim.com/robots.txt` and
   `https://xcellenceexim.com/sitemap.xml` after cutover.
4. Add the domain property in Google Search Console, submit `sitemap.xml`, and
   request indexing for the home page and four product pages.
5. Keep redirects active for at least one year and update profile or directory
   links to their final canonical clean URLs.

Run `python3 tools/seo-audit.py` after rebuilding to check titles, descriptions,
canonicals, headings, structured data, image alt text, internal links and the
sitemap.

To replace the WordPress site on the same domain, upload the repository contents
to the web root and remove or rename the WordPress install. The build preserves
the existing public URL paths, so the cutover does not require old-to-new page
redirects. Apache redirects are included only for previously shared `.html`
preview links.

## Images

Images currently load from the existing WordPress media library, so the site
works immediately. To make it fully self-contained, run from this folder:

```bash
bash tools/download-images.sh   # fetch the images locally
bash tools/use-local-images.sh  # point the HTML at the local copies
```

## The enquiry form

`/contact-us/` has a structured RFQ form — product, quantity, destination port,
Incoterms, packing. The visitor never leaves the site; on submit it emails a
formatted enquiry to the sales desk with the director copied in:

| | |
|---|---|
| **To** | sales@xcellenceexim.com |
| **CC** | ashwani@xcellenceexim.com |
| **Subject** | `Export enquiry — {product} — {country} — {name}` |
| **Reply-To** | the buyer's own address, so hitting Reply answers them directly |
| **Body** | every field as a labelled table row |

Both addresses are set on the `<form>` tag, so changing them is a one-line edit:

```html
<form id="rfq-form" data-to="sales@xcellenceexim.com"
                    data-cc="ashwani@xcellenceexim.com" ...>
```

The form requires acknowledgement of the site Privacy Notice. Update and
redeploy `integrations/google-apps-script/Code.gs` so the server-side endpoint
enforces the same requirement.

## Analytics and preview indexing

GA4 property `G-XFVMBYF6P9` loads only on `xcellenceexim.com` and only after the
visitor accepts optional analytics. GitHub Pages previews do not load analytics
and switch their rendered robots directive to `noindex, nofollow`; all canonical
URLs continue to point to production.

### ⚠️ One-time activation — do this before going live

Delivery runs through the Google Workspace Apps Script web app in
`integrations/google-apps-script/`. The deployed Workspace account sends a
formatted email directly to sales@xcellenceexim.com, copies the director, and
sets Reply-To to the buyer's address. The endpoint validates every field,
limits request volume, and fixes the recipient so it cannot be used as an open
mail relay.

If the endpoint is unreachable, the visitor stays on the page and sees a clear
error instead of having a desktop mail application opened. There is also a
**Send via WhatsApp** button that composes the same summary.

## Languages

Translation is still GTranslate, the same service the old site used, so the full
language list is preserved. What changed is the interface: instead of a bare
dropdown of 100+ English names, there's a picker showing

- the **flag and the language's own name** — Español, العربية, Tiếng Việt — not
  the English label, which is what a non-English speaker is actually scanning for
- a **Key export markets** row of twelve one-tap tiles (Gulf, LATAM, Africa,
  SE Asia, Europe, East Asia)
- a **search box** covering all languages, matching either the English or the
  native name
- a footnote noting these are machine translations and English governs contracts

Edit the twelve featured markets in `assets/js/languages.js`
(`XE_PRIORITY_LANGUAGES`). The rest of the list builds itself from whatever
GTranslate supports, so it never drifts out of sync.

Flags come from flagcdn.com and fall back to a lettered chip if an image fails
or the language has no meaningful single flag (Esperanto, Latin). They mark a
representative market, not a claim that a language belongs to one country.

Right-to-left languages (Arabic, Hebrew, Urdu, Farsi, Kurdish, Pashto, Uyghur)
flip the whole layout — navigation, tables, forms, drawer and icons.

The picker is mounted once and *moved* between the header and the mobile menu
rather than duplicated, so translation state survives a resize — the usual cause
of a half-translated page.

### Header fitting

Translated menu labels can run two to three times longer than the English ones.
Rather than guess a breakpoint, the header measures what the row actually needs
and collapses to the hamburger the moment it stops fitting — in any language, at
any zoom level, re-checking whenever the translation swaps the text in.

## Editing

- **Colours, spacing, type** — all tokens sit at the top of `assets/css/styles.css`.
- **Contact details** — search and replace in the HTML, or edit `build/parts.py`
  and re-run `python3 build/build.py` from this folder to regenerate every page
  consistently.
- **Behaviour** — `assets/js/main.js`, vanilla JS, no dependencies.
