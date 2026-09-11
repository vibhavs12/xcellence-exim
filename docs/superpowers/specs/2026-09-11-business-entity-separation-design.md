# Xcellence Exim Business Entity Separation Design

## Goal

Help search engines distinguish Xcellence Exim, the Kota-based Indian agricultural merchant exporter, from similarly named logistics businesses without representing unverified legal or registration details.

## Scope

1. Keep the existing public company name, Xcellence Exim, as the Organization name.
2. Clarify the Organization structured data with the factual business identity already published on the website:
   - Indian agricultural merchant exporter;
   - Kota, Rajasthan, India postal address;
   - export-sales contact point;
   - worldwide service area;
   - existing Facebook, Instagram, and LinkedIn profile URLs;
   - existing square brand icon.
3. Permanently redirect the malformed nested contact route
   `/sugar-icumsa-45/contact-us/` to `/contact-us/`.
4. Add regression checks for the Organization identity data and the redirect.

## Non-goals

- Do not add a legal name, incorporation date, IEC number, APEDA number, GST number, or other identifier unless the user supplies it and it is verified.
- Do not create, claim, or edit third-party directory or business-profile listings.
- Do not change visitor-facing content, the company name, the footer address, or product URLs.
- Do not attempt to remove the different company from Google results.

## Design

`build/parts.py` remains the single owner of global Organization JSON-LD. Its
description will explicitly call the business an Indian agricultural merchant
exporter, and its existing address, contact point, logo, and social identities
will remain in the same JSON-LD object. This makes the business's location,
specialism, and official profiles machine-readable without making claims that
cannot be established from the site.

`_redirects` will add one exact Cloudflare Pages redirect for the malformed
nested route. The redirect is permanent (301), so Google can consolidate the
incorrect URL with the canonical contact page while normal product and contact
routes stay unchanged.

`tools/seo-audit.py` will parse the generated JSON-LD and validate the expected
Organization fields on every canonical page. It will also validate the exact
malformed-route redirect. The test is intentionally data-focused: it guards
the entity signals rather than relying on a search-ranking outcome that cannot
be deterministically tested.

## Error handling and verification

- Invalid or missing JSON-LD continues to fail the SEO audit.
- A missing or wrongly targeted nested-route redirect fails the audit.
- The generated site will be rebuilt before checking its canonical URLs,
  schema, sitemap, and enquiry regression suite.
- Production verification will request the public malformed URL and confirm a
  301 response to the canonical contact page after deployment.

## Success criteria

- Every generated canonical page declares the same, valid Xcellence Exim
  Organization identity with its Kota address and export-sales contact.
- `/sugar-icumsa-45/contact-us/` returns a 301 redirect to `/contact-us/`.
- Existing generated-page SEO checks, logo checks, and enquiry-security checks
  pass after the build.
