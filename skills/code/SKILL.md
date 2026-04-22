---
name: code
description: Convert C++ code blocks to syntax-highlighted PNG images for embedding in WeChat articles. Use when the user needs code screenshots as fallback for HTML copy-paste issues, or wants mobile-friendly code images with consistent syntax highlighting.
---

# Generate Code Block Images

Convert C++ solution code into syntax-highlighted PNG images. These images replace HTML `<pre><code>` blocks in the final WeChat article to prevent whitespace stripping.

## Why PNG Instead of HTML Code Blocks

WeChat's editor sometimes collapses whitespace or misaligns text when copying HTML `<pre><code>` blocks. A PNG image guarantees:
- Exact indentation and monospace alignment
- Consistent syntax highlighting colors
- No font substitution issues on mobile
- No risk of WeChat reformatting the code

## Workflow

### 1. Prepare source code

Read the `.cpp` file and remove **all comments** (`// ...` line comments AND `/* ... */` block comments) and blank lines. Keep only executable code — explanations belong in the article prose, not in the code.

### 2. Syntax highlight

Tokenize each line and apply color classes. **Match in priority order**, then merge non-overlapping intervals (later matches that overlap earlier ones are skipped).

Priority order:
1. String literals `"..."` / `'...'` → `st`
2. Preprocessor directives `#include`, `#define` → `pp`
3. `long long` (before single `long`) → `ty`
4. Keywords (`if`, `for`, `return`, `int`, `void`, `struct`, `push`, `pop`, `cout`, `cin`, `scanf`, `memset`, `max`, `min`, `vector`, `queue`, `char`, `bool`, `class`, `template`, `sizeof`, `continue`, `using`, `namespace`, `typedef`, `const`, `while`, `reverse`, `begin`, `end`, `puts`, `printf`, `auto`, `new`, `delete`, `public`, `private`, `protected`, `typename`, `operator`, `friend`, `inline`, `static`, `extern`, `volatile`, `mutable`, `explicit`, `virtual`, `override`, `final`, `noexcept`, `constexpr`, `consteval`, `constinit`, `decltype`, `concept`, `requires`, `co_await`, `co_return`, `co_yield`) → `kw`
5. Common type aliases (`ll`, `node`) → `ty`
6. Numbers → `nu`
7. Function calls (identifier before `(`) → `fn`

**Color scheme** (must match article HTML exactly):

| Class | Color | For |
|-------|-------|-----|
| `kw` | `#0066cc` | Keywords |
| `ty` | `#0969da` | Types and aliases |
| `st` | `#0a7a3f` | String / char literals |
| `nu` | `#d73a49` | Numbers |
| `pp` | `#6f42c1` | Preprocessor directives |
| `fn` | `#8250df` | Function names |
| default | `#383a42` | Everything else |

**Background**: `#faf8f5` (warm beige, eye-protecting)

### 3. Render with Pillow

```python
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 14)
LINE_HEIGHT = 20
PADDING_X = 24
PADDING_Y = 20
BG_COLOR = "#faf8f5"
```

Measure each token's width with `font.getlength()`, sum per line for image dimensions, then draw token-by-token with the corresponding color.

### 4. Output

Save to `ABCxxx/figures_sel/<letter>_code.png`.

This puts the code image in the same directory as the diagram images, so all article embeddables are in one place.

## File Organization

```
ABCxxx/
├── c.cpp, d.cpp              # original source
├── figures_sel/
│   ├── c_code.png            # generated code image
│   └── d_code.png
└── code_to_image.py          # generation script (optional)
```

After generating, push the repository. The article HTML will reference these images via jsDelivr CDN:

```
https://cdn.jsdelivr.net/gh/<username>/<repo>@main/ABCxxx/figures_sel/c_code.png
```

## Key Gotchas

- **Do NOT generate intermediate HTML `<span>` tags during highlighting** — they can be re-matched by keyword regexes (e.g. `class` inside `<span class="...">`). Highlight by computing non-overlapping intervals directly on the raw source text.
- **`\n` in strings**: When reading `"Yes\n"` from a file, Python sees two characters (`\` and `n`). Ensure the renderer prints them literally on one line, not as an actual line break.
- **Tab characters**: Expand to 4 spaces before measuring/rendering, or indentation will be inconsistent.

## Verification Checklist

- [ ] All comments removed from the source before rendering
- [ ] Syntax colors match the article HTML exactly
- [ ] No HTML tag text visible in the image
- [ ] Escape sequences like `\n` render on a single line
- [ ] Image width fits within mobile screen (≤ 480 px ideal)
- [ ] Output saved to `figures_sel/`, not a separate directory
