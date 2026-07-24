#!/usr/bin/env bash
# Self-host the site images instead of loading them from the old WordPress
# install. Run once from the site root:  bash tools/download-images.sh
# Then run:  bash tools/use-local-images.sh   to rewrite the HTML.
set -euo pipefail
B="https://xcellenceexim.com/wp-content/uploads"
mkdir -p assets/img/brand assets/img/product assets/img/cert
get() { echo "  -> $2"; curl -fsSL "$1" -o "$2"; }
get "$B/2026/07/Screenshot-2026-07-15-180236.png" assets/img/brand/logo.png
for n in 1 2 3 7 8 9 10 11 12; do get "$B/2025/07/$n.png" "assets/img/product/$n.png"; done
for n in 35 36 37; do get "$B/2026/05/Paneer-Bhurji-$n.png" "assets/img/product/Paneer-Bhurji-$n.png"; done
for n in 36 37 38 40; do get "$B/2025/09/spice-shop-$n.png" "assets/img/product/spice-shop-$n.png"; done
get "$B/2026/07/Supplier-Network-Strength-4.png" assets/img/product/Supplier-Network-Strength-4.png
for s in 194937 194946 195001 195013 195022; do get "$B/2025/09/Screenshot-2025-09-25-$s.png" "assets/img/cert/Screenshot-2025-09-25-$s.png"; done
echo "Done. Now run: bash tools/use-local-images.sh"
