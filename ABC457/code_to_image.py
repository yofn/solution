#!/usr/bin/env python3
"""Convert C++ code blocks to syntax-highlighted PNG images."""
from PIL import Image, ImageDraw, ImageFont
import re
import os

FONT_PATH = "/System/Library/Fonts/Menlo.ttc"
FONT_SIZE = 14
LINE_HEIGHT = 20
PADDING_X = 24
PADDING_Y = 20
BG_COLOR = "#faf8f5"

COLORS = {
    "kw": "#0066cc",
    "ty": "#0969da",
    "st": "#0a7a3f",
    "nu": "#d73a49",
    "pp": "#6f42c1",
    "fn": "#8250df",
    "default": "#383a42",
}

KEYWORDS = [
    "if", "for", "return", "int", "void", "struct", "push", "pop", "cout", "cin",
    "scanf", "memset", "max", "min", "vector", "queue", "char", "bool", "class",
    "template", "sizeof", "continue", "using", "namespace", "typedef", "const",
    "while", "reverse", "begin", "end", "puts", "printf", "auto", "new", "delete",
    "public", "private", "protected", "typename", "operator", "friend", "inline",
    "static", "extern", "volatile", "mutable", "explicit", "virtual", "override",
    "final", "noexcept", "constexpr", "consteval", "constinit", "decltype",
    "concept", "requires", "co_await", "co_return", "co_yield", "long", "ll",
    "break", "else"
]

TYPE_ALIASES = ["ll", "node"]


def remove_comments(source: str) -> str:
    source = re.sub(r"/\*.*?\*/", "", source, flags=re.DOTALL)
    lines = []
    for line in source.split("\n"):
        if "//" in line:
            line = line[:line.index("//")]
        line = line.rstrip()
        if line:
            lines.append(line)
    return "\n".join(lines)


def highlight_line(line: str):
    intervals = []

    for m in re.finditer(r'"[^"]*"', line):
        intervals.append((m.start(), m.end(), "st"))
    for m in re.finditer(r"'[^']*'", line):
        intervals.append((m.start(), m.end(), "st"))

    for m in re.finditer(r'#\s*(include|define|ifdef|ifndef|endif|pragma|if|else|elif)', line):
        intervals.append((m.start(), m.end(), "pp"))

    for m in re.finditer(r'\blong long\b', line):
        intervals.append((m.start(), m.end(), "ty"))

    for kw in KEYWORDS:
        for m in re.finditer(r'\b' + re.escape(kw) + r'\b', line):
            intervals.append((m.start(), m.end(), "kw"))

    for ta in TYPE_ALIASES:
        for m in re.finditer(r'\b' + re.escape(ta) + r'\b', line):
            intervals.append((m.start(), m.end(), "ty"))

    for m in re.finditer(r'\b\d+\b', line):
        intervals.append((m.start(), m.end(), "nu"))

    for m in re.finditer(r'\b([a-zA-Z_]\w*)\s*(?=\()', line):
        intervals.append((m.start(), m.end(), "fn"))

    intervals.sort(key=lambda x: x[0])
    merged = []
    for s, e, cls in intervals:
        overlap = False
        for ms, me, _ in merged:
            if not (e <= ms or s >= me):
                overlap = True
                break
        if not overlap:
            merged.append((s, e, cls))

    tokens = []
    last = 0
    for s, e, cls in sorted(merged, key=lambda x: x[0]):
        if s > last:
            tokens.append((line[last:s], "default"))
        tokens.append((line[s:e], cls))
        last = e
    if last < len(line):
        tokens.append((line[last:], "default"))
    if not tokens:
        tokens = [(line, "default")]
    return tokens


def render_code(source: str, out_path: str):
    source = remove_comments(source)
    lines = source.split("\n")
    lines = [line.replace("\t", "    ") for line in lines]

    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    max_width = 0
    all_tokens = []
    for line in lines:
        tokens = highlight_line(line)
        all_tokens.append(tokens)
        line_width = sum(font.getlength(t) for t, _ in tokens)
        max_width = max(max_width, line_width)

    img_w = int(max_width + 2 * PADDING_X)
    img_h = int(len(lines) * LINE_HEIGHT + 2 * PADDING_Y)

    img = Image.new("RGB", (img_w, img_h), BG_COLOR)
    draw = ImageDraw.Draw(img)

    y = PADDING_Y
    for tokens in all_tokens:
        x = PADDING_X
        for text, cls in tokens:
            color = COLORS.get(cls, COLORS["default"])
            draw.text((x, y), text, font=font, fill=color)
            x += font.getlength(text)
        y += LINE_HEIGHT

    img.save(out_path)
    print(f"Saved {out_path} ({img_w}x{img_h})")


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    for letter in ["c", "d"]:
        cpp_path = os.path.join(base, f"{letter}.cpp")
        png_path = os.path.join(base, "figures_sel", f"{letter}_code.png")
        with open(cpp_path, "r") as f:
            source = f.read()
        render_code(source, png_path)


if __name__ == "__main__":
    main()
