#!/bin/bash
# Rotate version backups for a diagram base name
# Usage: ./rotate_version.sh <basename>
# Example: ./rotate_version.sh c_diagram

BASE=$1

if [ -z "$BASE" ]; then
    echo "Usage: $0 <basename>"
    exit 1
fi

for EXT in tex pdf png; do
    FILE="${BASE}.${EXT}"
    if [ -f "$FILE" ]; then
        # Rotate v4 -> v5
        if [ -f "${BASE}_v4.${EXT}" ]; then
            mv "${BASE}_v4.${EXT}" "${BASE}_v5.${EXT}"
        fi
        # Rotate v3 -> v4
        if [ -f "${BASE}_v3.${EXT}" ]; then
            mv "${BASE}_v3.${EXT}" "${BASE}_v4.${EXT}"
        fi
        # Rotate v2 -> v3
        if [ -f "${BASE}_v2.${EXT}" ]; then
            mv "${BASE}_v2.${EXT}" "${BASE}_v3.${EXT}"
        fi
        # Rotate v1 -> v2
        if [ -f "${BASE}_v1.${EXT}" ]; then
            mv "${BASE}_v1.${EXT}" "${BASE}_v2.${EXT}"
        fi
        # Current -> v1
        mv "$FILE" "${BASE}_v1.${EXT}"
    fi
done

echo "Rotated backups for ${BASE}"
