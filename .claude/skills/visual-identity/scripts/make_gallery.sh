#!/usr/bin/env bash
# Build a visual gallery of every style in the Lemo-Opuscar library.
# Usage: make_gallery.sh <outdir> [libdir]
# Gets the library (clone, or update) if needed, downloads each style's demo frame,
# and writes <outdir>/style_gallery.html (one card per style, grouped by category).
set -euo pipefail
OUT="$1"; LIB="${2:-$HOME/lemo-opuscar}"
mkdir -p "$OUT/frames" "$OUT/frames_small"
if [ -d "$LIB/.git" ]; then git -C "$LIB" pull -q --ff-only || true
else git clone -q --depth 1 https://github.com/lemomo-ai/lemo-opuscar.git "$LIB"; fi
grep -o 'src="docs/frames/[^"]*"' "$LIB/README.md" | cut -d'"' -f2 | while read -r p; do
  f="$OUT/frames/$(basename "$p")"
  [ -s "$f" ] || [ -s "$LIB/$p" ] && cp -n "$LIB/$p" "$f" 2>/dev/null || true
  [ -s "$f" ] || curl -sfL -o "$f" "https://raw.githubusercontent.com/lemomo-ai/lemo-opuscar/main/$p" || echo "missing frame: $p"
  [ -s "$f" ] && ffmpeg -nostdin -v error -y -i "$f" -vf scale=480:-1 -q:v 5 "$OUT/frames_small/$(basename "$p")"
done
python3 -I "$(dirname "$0")/build_gallery.py" "$LIB" "$OUT"
echo "gallery: $OUT/style_gallery.html"
