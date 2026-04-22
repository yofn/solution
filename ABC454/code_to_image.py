#!/usr/bin/env python3
"""Convert C++ code blocks to syntax-highlighted PNG images."""

import re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Configuration
FONT_PATH = "/System/Library/Fonts/Menlo.ttc"
FONT_SIZE = 14
LINE_HEIGHT = 20
PADDING_X = 24
PADDING_Y = 20
BG_COLOR = "#faf8f5"

COLOR_MAP = {
    "kw": "#0066cc",
    "ty": "#0969da",
    "st": "#0a7a3f",
    "nu": "#d73a49",
    "pp": "#6f42c1",
    "fn": "#8250df",
    None: "#383a42",
}

KW_LIST = [
    "include", "using", "namespace", "typedef", "const", "int", "long", "void",
    "if", "return", "for", "while", "struct", "sizeof", "continue", "push", "pop",
    "front", "empty", "reverse", "begin", "end", "puts", "cout", "cin", "scanf",
    "printf", "memset", "max", "min", "vector", "queue", "string", "char", "bool",
    "auto", "new", "delete", "class", "public", "private", "protected", "template",
    "typename", "operator", "friend", "inline", "static", "extern", "volatile",
    "mutable", "explicit", "virtual", "override", "final", "noexcept", "constexpr",
    "consteval", "constinit", "decltype", "concept", "requires", "co_await",
    "co_return", "co_yield",
]
KW_PATTERN = re.compile(r'\b(' + '|'.join(re.escape(w) for w in KW_LIST) + r')\b')


def remove_comments(code):
    """Remove // comments, /* */ block comments, and blank lines."""
    import re
    # Remove /* ... */ block comments (non-greedy, multiline)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    lines = []
    for line in code.splitlines():
        line = line.split("//")[0].rstrip()
        if line:
            lines.append(line)
    return "\n".join(lines)


def highlight_cpp(code):
    """Syntax-highlight C++ code, returning list of (text, color_class) per line."""
    result = []
    for line in code.splitlines():
        matches = []

        # 1. String literals (highest priority)
        for m in re.finditer(r'"(?:\\.|[^"\\])*"', line):
            matches.append((m.start(), m.end(), m.group(0), "st"))
        for m in re.finditer(r"'(?:\\.|[^'\\])*'", line):
            matches.append((m.start(), m.end(), m.group(0), "st"))

        # 2. Preprocessor directives
        for m in re.finditer(r'#[\t ]*\w+', line):
            matches.append((m.start(), m.end(), m.group(0), "pp"))

        # 3. Type: long long (before single long)
        for m in re.finditer(r'\blong long\b', line):
            matches.append((m.start(), m.end(), m.group(0), "ty"))

        # 4. Keywords
        for m in KW_PATTERN.finditer(line):
            matches.append((m.start(), m.end(), m.group(0), "kw"))

        # 5. Common type aliases
        for m in re.finditer(r'\b(ll|node)\b', line):
            matches.append((m.start(), m.end(), m.group(0), "ty"))

        # 6. Numbers
        for m in re.finditer(r'\b\d+\b', line):
            matches.append((m.start(), m.end(), m.group(0), "nu"))

        # 7. Function calls
        for m in re.finditer(r'\b([a-zA-Z_]\w*)\s*\(', line):
            matches.append((m.start(), m.end(1), m.group(1), "fn"))

        # Sort by start position, then by length descending (longer first)
        matches.sort(key=lambda x: (x[0], -(x[1] - x[0])))

        # Merge: skip overlapping matches (keep earlier/longer)
        merged = []
        for start, end, text, cls in matches:
            if merged and start < merged[-1][1]:
                continue  # overlaps with previous
            merged.append((start, end, text, cls))

        # Build tokens
        tokens = []
        pos = 0
        for start, end, text, cls in merged:
            if start > pos:
                tokens.append((line[pos:start], None))
            tokens.append((text, cls))
            pos = end
        if pos < len(line):
            tokens.append((line[pos:], None))

        result.append(tokens)
    return result


def render_code_to_image(code, out_path):
    """Render C++ code to a PNG image with syntax highlighting."""
    code = remove_comments(code)
    highlighted = highlight_cpp(code)

    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    # Measure max line width
    max_width = 0
    for tokens in highlighted:
        line_width = 0
        for text, _ in tokens:
            line_width += font.getlength(text)
        max_width = max(max_width, line_width)

    img_width = int(max_width) + PADDING_X * 2
    img_height = len(highlighted) * LINE_HEIGHT + PADDING_Y * 2

    img = Image.new("RGB", (img_width, img_height), BG_COLOR)
    draw = ImageDraw.Draw(img)

    for row, tokens in enumerate(highlighted):
        y = PADDING_Y + row * LINE_HEIGHT
        x = PADDING_X
        for text, cls in tokens:
            color = COLOR_MAP.get(cls, COLOR_MAP[None])
            draw.text((x, y), text, font=font, fill=color)
            x += font.getlength(text)

    img.save(out_path, "PNG")
    print(f"Saved {out_path} ({img_width}x{img_height})")


def main():
    base = Path(__file__).parent
    out_dir = base / "figures_sel"
    out_dir.mkdir(exist_ok=True)

    c_code = (base / "c.cpp").read_text()
    render_code_to_image(c_code, out_dir / "c_code.png")

    d_code = (base / "d.cpp").read_text()
    render_code_to_image(d_code, out_dir / "d_code.png")


if __name__ == "__main__":
    main()
