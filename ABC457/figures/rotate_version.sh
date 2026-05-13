#!/bin/bash
# Rotate versions: v1 <- current, v2 <- v1, ..., up to v5

base="$1"

cd "$(dirname "$0")"

for ext in tex pdf png; do
    if [ -f "${base}_v5.${ext}" ]; then
        rm "${base}_v5.${ext}"
    fi
    for i in 4 3 2 1; do
        j=$((i+1))
        if [ -f "${base}_v${i}.${ext}" ]; then
            mv "${base}_v${i}.${ext}" "${base}_v${j}.${ext}"
        fi
    done
    if [ -f "${base}.${ext}" ]; then
        cp "${base}.${ext}" "${base}_v1.${ext}"
    fi
done

echo "Rotated versions for ${base}"
