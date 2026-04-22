#!/bin/bash
# Rotate backup versions for a diagram base name
# Usage: ./rotate_version.sh c_diagram

BASE="$1"

for ext in tex pdf png; do
    for i in 4 3 2 1; do
        j=$((i+1))
        if [ -f "${BASE}_v${i}.${ext}" ]; then
            mv "${BASE}_v${i}.${ext}" "${BASE}_v${j}.${ext}"
        fi
    done
    if [ -f "${BASE}.${ext}" ]; then
        cp "${BASE}.${ext}" "${BASE}_v1.${ext}"
    fi
done
