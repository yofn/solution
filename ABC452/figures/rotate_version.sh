#!/bin/bash
# Rotate versions for a figure basename (e.g., ./rotate_version.sh c_diagram)

base="$1"

# rotate v4 -> v5
if [ -f "${base}_v4.tex" ]; then
    mv "${base}_v4.tex" "${base}_v5.tex"
    mv "${base}_v4.pdf" "${base}_v5.pdf" 2>/dev/null
    mv "${base}_v4.png" "${base}_v5.png" 2>/dev/null
fi

# rotate v3 -> v4
if [ -f "${base}_v3.tex" ]; then
    mv "${base}_v3.tex" "${base}_v4.tex"
    mv "${base}_v3.pdf" "${base}_v4.pdf" 2>/dev/null
    mv "${base}_v3.png" "${base}_v4.png" 2>/dev/null
fi

# rotate v2 -> v3
if [ -f "${base}_v2.tex" ]; then
    mv "${base}_v2.tex" "${base}_v3.tex"
    mv "${base}_v2.pdf" "${base}_v3.pdf" 2>/dev/null
    mv "${base}_v2.png" "${base}_v3.png" 2>/dev/null
fi

# rotate v1 -> v2
if [ -f "${base}_v1.tex" ]; then
    mv "${base}_v1.tex" "${base}_v2.tex"
    mv "${base}_v1.pdf" "${base}_v2.pdf" 2>/dev/null
    mv "${base}_v1.png" "${base}_v2.png" 2>/dev/null
fi

# rotate current -> v1
if [ -f "${base}.tex" ]; then
    cp "${base}.tex" "${base}_v1.tex"
    cp "${base}.pdf" "${base}_v1.pdf" 2>/dev/null
    cp "${base}.png" "${base}_v1.png" 2>/dev/null
fi

echo "Rotated ${base}"
