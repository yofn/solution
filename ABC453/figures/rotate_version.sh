#!/bin/bash
# 保存最近5个版本的 tex/pdf/png，自动轮转
# 用法: ./rotate_version.sh <basename>
# 示例: ./rotate_version.sh c_diagram

set -e

BASENAME="$1"
if [ -z "$BASENAME" ]; then
    echo "Usage: $0 <basename>"
    echo "Example: $0 c_diagram"
    exit 1
fi

for EXT in tex pdf png; do
    SRC="${BASENAME}.${EXT}"
    if [ ! -f "$SRC" ]; then
        echo "Warning: $SRC not found, skipping"
        continue
    fi

    # 轮转: v4 -> v5, v3 -> v4, v2 -> v3, v1 -> v2
    for i in 4 3 2 1; do
        j=$((i + 1))
        OLD="${BASENAME}_v${i}.${EXT}"
        NEW="${BASENAME}_v${j}.${EXT}"
        if [ -f "$OLD" ]; then
            cp "$OLD" "$NEW"
        fi
    done

    # 当前 -> v1
    cp "$SRC" "${BASENAME}_v1.${EXT}"
    echo "Saved ${SRC} -> ${BASENAME}_v1.${EXT} (rotated older versions)"
done

echo "Done. Versions kept: v1 (latest backup) .. v5 (oldest backup)"
