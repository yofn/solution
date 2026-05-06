#!/bin/bash
# Rotate version backups for TikZ diagrams
# Usage: ./rotate_version.sh <basename>
# Example: ./rotate_version.sh c_diagram

BASE="$1"

if [ -z "$BASE" ]; then
    echo "Usage: $0 <basename>"
    exit 1
fi

# Rotate v4 -> v5
if [ -f "${BASE}_v4.tex" ]; then
    cp "${BASE}_v4.tex" "${BASE}_v5.tex"
    cp "${BASE}_v4.pdf" "${BASE}_v5.pdf" 2>/dev/null
    cp "${BASE}_v4.png" "${BASE}_v5.png" 2>/dev/null
fi

# Rotate v3 -> v4
if [ -f "${BASE}_v3.tex" ]; then
    cp "${BASE}_v3.tex" "${BASE}_v4.tex"
    cp "${BASE}_v3.pdf" "${BASE}_v4.pdf" 2>/dev/null
    cp "${BASE}_v3.png" "${BASE}_v4.png" 2>/dev/null
fi

# Rotate v2 -> v3
if [ -f "${BASE}_v2.tex" ]; then
    cp "${BASE}_v2.tex" "${BASE}_v3.tex"
    cp "${BASE}_v2.pdf" "${BASE}_v3.pdf" 2>/dev/null
    cp "${BASE}_v2.png" "${BASE}_v3.png" 2>/dev/null
fi

# Rotate v1 -> v2
if [ -f "${BASE}_v1.tex" ]; then
    cp "${BASE}_v1.tex" "${BASE}_v2.tex"
    cp "${BASE}_v1.pdf" "${BASE}_v2.pdf" 2>/dev/null
    cp "${BASE}_v1.png" "${BASE}_v2.png" 2>/dev/null
fi

# Current -> v1
if [ -f "${BASE}.tex" ]; then
    cp "${BASE}.tex" "${BASE}_v1.tex"
    cp "${BASE}.pdf" "${BASE}_v1.pdf" 2>/dev/null
    cp "${BASE}.png" "${BASE}_v1.png" 2>/dev/null
fi

echo "Rotated ${BASE} backups"
