#!/usr/bin/env bash
# Rewrites every remote image URL in the HTML to the local copies created by
# download-images.sh. Run from the site root, after download-images.sh.
set -euo pipefail
B="https://xcellenceexim.com/wp-content/uploads"
for f in *.html; do
  sed -i.bak \
    -e "s#$B/2026/07/Screenshot-2026-07-15-180236.png#assets/img/brand/logo.png#g" \
    -e "s#$B/2026/07/Supplier-Network-Strength-4.png#assets/img/product/Supplier-Network-Strength-4.png#g" \
    -e "s#$B/2025/09/spice-shop-#assets/img/product/spice-shop-#g" \
    -e "s#$B/2025/09/Screenshot-2025-09-25-#assets/img/cert/Screenshot-2025-09-25-#g" \
    -e "s#$B/2025/07/#assets/img/product/#g" \
    -e "s#$B/2026/05/#assets/img/product/#g" \
    "$f"
  rm -f "$f.bak"
done
echo "HTML now points at assets/img/."
