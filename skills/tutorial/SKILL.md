---
name: tutorial
description: End-to-end workflow for producing a WeChat tutorial article from an AtCoder contest solution. Orchestrates getcode → figure → code → article steps. Use when the user wants to create a complete CP writeup with diagrams, code images, and styled HTML.
---

# Produce Complete CP Tutorial

End-to-end workflow: from an AtCoder contest to a polished WeChat tutorial article.

## Overview

This skill chains four sub-skills in order:

| Step | Skill | Output |
|------|-------|--------|
| 1 | **getcode** | Contest directory with `README.md` + `.cpp` files |
| 2 | **figure** | `figures/*.png` — algorithm diagrams |
| 3 | **code** | `figures_sel/*_code.png` — syntax-highlighted code fallbacks |
| 4 | **article** | `article.md` + `article.html` — WeChat-ready tutorial |

Run them sequentially. Each step consumes the previous step's output.

---

## Step 1: Get code & problems (`getcode`)

Fetch the AC solution and problem statements from AtCoder.

**Input**: contest name + problem letters + submission URL  
**Output**:
```
ABCxxx/
├── README.md      # problem statements (Chinese)
├── c.cpp          # AC code (preserved as-is)
└── d.cpp
```

**Key decision**: Which problems to cover? Typically C and D (the "educational" problems that separate tiers).

---

## Step 2: Draw figures (`figure`)

Create TikZ diagrams that explain the core insight of each problem.

**Input**: problem statements + AC code  
**Output**:
```
ABCxxx/figures/
├── c_diagram.png
├── d_diagram.png
├── d_state.png
├── d_backtrack.png
└── rotate_version.sh
```

**Principles**:
- One diagram per core concept
- Chinese labels, mobile-friendly sizing
- Use the `figure` skill for TikZ templates and compilation commands

---

## Step 3: Generate code images (`code`)

Render each solution's code into a syntax-highlighted PNG fallback.

**Input**: `.cpp` files from Step 1  
**Output**:
```
ABCxxx/figures_sel/
├── c_code.png
└── d_code.png
```

**Why**: WeChat's editor sometimes strips whitespace from HTML `<pre>` blocks. The PNG guarantees perfect alignment and color consistency on mobile.

**Prerequisites**: Python + Pillow (`python3 -m venv .venv && pip install Pillow`).

Use the `code` skill for the full rendering script and color scheme.

---

## Step 4: Write article (`article`)

Compose the tutorial in Markdown, then convert to WeChat-friendly HTML.

**Input**: `README.md`, `.cpp`, `figures/*.png`, `figures_sel/*_code.png`  
**Output**:
```
ABCxxx/
├── article.md
└── article.html
```

**Structure**:
1. Opening — connect to broader algorithm knowledge
2. Problem C — restatement → insight → diagram → code → explanation
3. Problem D — same structure
4. Closing — encouragement and regular practice

**Rules** (see `article` skill for full details):
- All text in Chinese
- No comments inside code blocks; explanations go in prose
- Use colored `<span>` for emphasis, never `<strong>`
- Embed both HTML code blocks **and** PNG fallbacks

---

## File Organization (Complete)

```
ABCxxx/
├── README.md
├── c.cpp
├── d.cpp
├── article.md
├── article.html
├── figures/
│   ├── c_diagram.tex / .pdf / .png
│   ├── c_diagram_v1...v5.*       # backups
│   ├── d_diagram.tex / .pdf / .png
│   ├── d_state.tex / .pdf / .png
│   ├── d_backtrack.tex / .pdf / .png
│   └── rotate_version.sh
├── figures_sel/                    # article embeddables
│   ├── c_diagram.png
│   ├── d_diagram.png
│   ├── d_state.png
│   ├── d_backtrack.png
│   ├── c_code.png
│   └── d_code.png
└── code_to_image.py              # optional generator script
```

---

## Verification Checklist

- [ ] Code compiles and passes all test cases
- [ ] All diagram PNGs are readable on a phone screen
- [ ] Code block PNGs match article HTML colors exactly
- [ ] `article.html` has no HTML escapes inside `<pre><code>`
- [ ] No personal identifiers anywhere
- [ ] All text in Chinese
- [ ] Article CSS uses `#faf8f5` warm beige for code background
