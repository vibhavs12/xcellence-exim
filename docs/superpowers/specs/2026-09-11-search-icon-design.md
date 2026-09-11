# Xcellence Exim Google Search Icon Design

## Goal

Make Xcellence Exim eligible for a recognisable square icon in Google Search
results and organization surfaces, without changing the existing wide header
and footer logo.

## Chosen visual direction

Use the orange-and-black Xcellence symbol already at the left of the current
wordmark. The image will be cropped to the symbol only and placed on a white
square canvas. This preserves the established brand identity and remains
legible at favicon size.

## Asset and markup

1. Add one square, 512 by 512 pixel PNG at
   `assets/img/brand/favicon.png`.
2. Keep `assets/img/brand/logo.png` as the existing 435 by 104 pixel wide
   wordmark used by the header and footer.
3. Update the shared page generator so every page uses `favicon.png` for
   `rel="icon"` and `rel="apple-touch-icon"`.
4. Update the Organization JSON-LD `logo` value to `favicon.png`.
5. Do not change any navigation, footer, content images, page titles, or
   enquiry form behaviour.

## Delivery and caching

The new icon will be served from `/assets/img/brand/favicon.png`, which is
already covered by the static asset cache policy. The existing wide logo keeps
its current URL, so browser header/footer rendering is unaffected.

## Verification

- The new PNG is square and at least 112 by 112 pixels.
- The generated home page and representative nested pages reference the square
  asset for both favicon link tags and Organization structured data.
- The generated header and footer still reference the wide wordmark.
- Existing logo delivery, enquiry-security, and SEO checks pass.
- The published production URL returns the square image with `image/png`.

## Search expectation

After deployment, request indexing of the homepage in Search Console. Google
will recrawl the favicon and Organization markup on its own schedule; showing
the icon remains Google's decision.
