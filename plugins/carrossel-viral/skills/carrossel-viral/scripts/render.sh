#!/usr/bin/env bash
# Renderiza slides HTML em PNG e junta tudo num PDF.
# Uso: render.sh <pasta-slides> [largura] [altura]
set -euo pipefail

SLIDES_DIR="${1:?uso: render.sh <pasta-slides> [largura] [altura]}"
W="${2:-1080}"
H="${3:-1350}"
SLIDES_DIR="$(cd "$SLIDES_DIR" && pwd)"
OUT_DIR="$(dirname "$SLIDES_DIR")"
PNG_DIR="$OUT_DIR/png"
mkdir -p "$PNG_DIR"

CHROME=""
for c in \
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  "/Applications/Chromium.app/Contents/MacOS/Chromium" \
  "$(command -v google-chrome 2>/dev/null || true)" \
  "$(command -v chromium 2>/dev/null || true)" \
  "$(command -v chromium-browser 2>/dev/null || true)"; do
  if [ -n "$c" ] && [ -x "$c" ]; then CHROME="$c"; break; fi
done
[ -n "$CHROME" ] || { echo "Chrome/Chromium não encontrado." >&2; exit 1; }

shopt -s nullglob
files=("$SLIDES_DIR"/slide-*.html)
[ ${#files[@]} -gt 0 ] || { echo "Nenhum slide-*.html em $SLIDES_DIR" >&2; exit 1; }

for f in "${files[@]}"; do
  name="$(basename "$f" .html)"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=1 --window-size="$W,$H" \
    --virtual-time-budget=4000 \
    --screenshot="$PNG_DIR/$name.png" "file://$f" >/dev/null 2>&1
  echo "PNG: $PNG_DIR/$name.png"
done

# PDF: uma página por slide, no tamanho exato (impresso pelo próprio Chrome).
PDF_HTML="$PNG_DIR/.pdf.html"
{
  echo "<!doctype html><html><head><meta charset=utf-8><style>@page{size:${W}px ${H}px;margin:0}html,body{margin:0}img{display:block;width:${W}px;height:${H}px;page-break-after:always}</style></head><body>"
  for f in "${files[@]}"; do echo "<img src=\"$(basename "$f" .html).png\">"; done
  echo "</body></html>"
} > "$PDF_HTML"
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$OUT_DIR/carrossel.pdf" "file://$PDF_HTML" >/dev/null 2>&1
rm -f "$PDF_HTML"
echo "PDF: $OUT_DIR/carrossel.pdf"
