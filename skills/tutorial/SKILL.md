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
| 2 | **figure** | `figures/*.png` — algorithm diagrams (then copied to `figures_sel/`) |
| 3 | **code** | `figures_sel/*_code.png` — syntax-highlighted code block images |
| 4 | **article** | `article.md` + `article.html` — WeChat-ready tutorial with CDN image URLs |

Run them sequentially. Each step consumes the previous step's output.

**Critical**: When executing this workflow, you must **actively read and follow** each sub-skill (`getcode`, `figure`, `code`, `article`) rather than improvising your own implementation. In particular, the `figure` step requires TikZ + LaTeX compilation — do not substitute with Python drawing libraries.

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

## Step 2: Draw figures (`figure`) — **MANDATORY**

**You MUST invoke the `figure` skill** to generate diagram PNGs. Do NOT use Pillow, Matplotlib, or any other non-LaTeX method to draw diagrams — those produce low-quality images that do not meet publication standards.

Create TikZ diagrams that explain the core insight of each problem.

**Input**: problem statements + AC code  
**Output**:
```
ABCxxx/figures/
├── c_diagram.tex / .pdf / .png
├── c_diagram_v1...v5.*           # backups managed by rotate_version.sh
├── d_diagram.tex / .pdf / .png
├── d_state.tex / .pdf / .png
├── d_backtrack.tex / .pdf / .png
└── rotate_version.sh
```

**Workflow**:
1. Read the `figure` skill (`skills/figure/SKILL.md`) for TikZ templates, color schemes, and compilation commands (`xelatex` + `pdftoppm -r 400`).
2. Write `.tex` files in `ABCxxx/figures/`.
3. Compile with `xelatex -interaction=nonstopmode` and convert with `pdftoppm -png -r 400 -singlefile`.
4. Verify the PNG is readable on a phone screen.
5. Use `rotate_version.sh` before edits to keep backups.
6. Copy final PNGs to `figures_sel/` for article embedding.

**Principles**:
- One diagram per core concept
- Chinese labels, mobile-friendly sizing
- **Always use TikZ + xelatex + pdftoppm (400 DPI)** for all diagrams
- If the algorithm involves a stack processing an input stream (e.g., bracket matching, string normalization), invoke the **`plot_stack`** sub-skill for the diagram template and layout rules

---

## Step 3: Generate code images (`code`)

Render each solution's code into a syntax-highlighted PNG image.

**Input**: `.cpp` files from Step 1  
**Output**:
```
ABCxxx/figures_sel/
├── c_code.png
└── d_code.png
```

**Why**: WeChat's editor strips whitespace from HTML `<pre>` blocks. PNG images guarantee perfect alignment and color consistency on mobile. The article inserts these as `<img>` elements, not `<pre><code>` blocks.

**Prerequisites**: Python + Pillow (`python3 -m venv .venv && pip install Pillow`).

Use the `code` skill for the full rendering script and color scheme.

---

## Step 4: Write article (`article`)

Compose the tutorial in Markdown, then convert to WeChat-friendly HTML.

**Input**: `README.md`, `.cpp`, `figures_sel/*.png`  
**Output**:
```
ABCxxx/
├── article.md
└── article.html
```

**Image URLs**: All images in `article.html` must use **jsDelivr CDN** addresses:

```
https://cdn.jsdelivr.net/gh/<username>/<repo>@main/ABCxxx/figures_sel/<filename>.png
```

This allows WeChat's editor to auto-download images when pasting HTML.

**Code blocks**: Do NOT use `<pre><code>`. Insert the PNG image directly:

```html
<img src="https://cdn.jsdelivr.net/gh/yofn/solution@main/ABC453/figures_sel/c_code.png"
     alt="C题代码"
     style="max-width:100%;display:block;margin:14px auto;border-radius:10px;border:1px solid #ece8e0;">
```

**Structure**:
1. Opening — connect to broader algorithm knowledge
2. Problem C — restatement → insight → diagram → code PNG → explanation
3. Problem D — same structure
4. Closing — encouragement and regular practice

**Rules** (see `article` skill for full details):
- All text in Chinese
- No comments inside code blocks; explanations go in prose
- Use colored `<span>` for emphasis, never `<strong>`

---

## Step 5: Git commit (agent does NOT push)

The agent performs `git add -A` and `git commit`, then **reminds the user to push**:

```bash
git add -A
git commit -m "Add ABCxxx tutorial with TikZ diagrams and AC code"
```

> ⚠️ **The agent must NOT run `git push` by default**. The user decides when to publish. If the user explicitly asks the agent to push, the agent may attempt it.

## Step 6: Publish

1. **Push** the repository to GitHub (ensure the repo is **public**)
2. Wait **1–2 minutes** for jsDelivr cache to refresh
3. Open `article.html` in a browser to confirm all images load from CDN
4. Select all and copy the HTML content
5. Paste into WeChat Official Account editor — images will auto-download and be re-hosted on WeChat's CDN

---

## File Organization (Complete)

```
ABCxxx/
├── README.md
├── c.cpp
├── d.cpp
├── article.md
├── article.html
├── figures/                          # TikZ source + intermediate files
│   ├── c_diagram.tex / .pdf / .png
│   ├── c_diagram_v1...v5.*           # backups
│   ├── d_diagram.tex / .pdf / .png
│   ├── d_state.tex / .pdf / .png
│   ├── d_backtrack.tex / .pdf / .png
│   └── rotate_version.sh
├── figures_sel/                      # all article embeddables (push these)
│   ├── c_diagram.png
│   ├── d_diagram.png
│   ├── d_state.png
│   ├── d_backtrack.png
│   ├── c_code.png
│   └── d_code.png
└── code_to_image.py                  # optional generator script
```

---

## Verification Checklist

- [ ] Code compiles and passes all test cases
- [ ] All diagram PNGs are readable on a phone screen
- [ ] Code block PNGs match article HTML colors exactly
- [ ] All images in `article.html` use jsDelivr CDN URLs, not local paths
- [ ] Code blocks are `<img>` PNGs, not `<pre><code>` HTML
- [ ] Repository is public so jsDelivr can serve files
- [ ] No personal identifiers anywhere
- [ ] All text in Chinese
- [ ] Article CSS uses `#faf8f5` warm beige background
