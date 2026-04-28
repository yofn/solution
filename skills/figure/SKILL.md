---
name: figure
description: Generate TikZ illustrations for competitive programming problem solutions. Use when the user wants to create visual diagrams, figures, or charts to explain an algorithm, data structure, or problem scenario. Outputs LaTeX/TikZ source, PDF, and high-resolution PNG suitable for mobile viewing.
---

# Generate CP Solution Figures with TikZ

Create clear, mobile-friendly illustrations for competitive programming problem solutions.

## Prerequisites

- LaTeX with `ctex` package (use `xelatex` for Chinese support)
- `pdftoppm` for PNG conversion

## Workflow

### 1. Understand the problem

Read the problem statement and the user's code to identify what needs to be visualized:
- Data structures (arrays, trees, graphs)
- Algorithm steps (sorting, searching, DP transitions)
- Geometric scenarios (number lines, grids, coordinates)
- State transitions or flow diagrams

### 2. Design the diagram

Keep it **simple and focused**. Mobile screens are small.

**Principles:**
- One diagram per core concept
- Use **Chinese labels** where possible
- Use **color coding** to distinguish states/operations
- Avoid text clutter — remove coordinate labels unless essential
- Ensure no overlapping elements

**Common patterns:**

| Problem Type | Visualization | Sub-skill |
|-------------|---------------|-----------|
| Number line / coordinate | Horizontal axis with arrows for moves | — |
| Grid / maze | Matrix with colored cells and path arrows | — |
| Tree / graph | Nodes and edges with labels | — |
| Array operations | Vertical bars or sequence diagram | — |
| State comparison | Side-by-side grid layout showing why extra dimension is needed | — |
| Stack + incoming stream | Stack growing upward with channel above top | `plot_stack` |

**State comparison diagrams** (e.g., `(x,y)` vs `(x,y,d)`):
- Use a 2x2 grid layout: left=insufficient state, right=sufficient state
- Top row = one cell type (e.g., `o` = go straight), bottom row = another (e.g., `x` = must turn)
- Left side: show question marks or forbidden symbols to indicate indeterminacy
- Right side: show clear arrows with direction labels (e.g., 面朝 = R, 直行 → R)
- Use horizontal line to separate rows, dashed vertical line to separate columns

### 3. Version roll before editing

**Before modifying an existing `.tex` file, you MUST roll the current version.**

Use the `rotate_version.sh` script in the `figures/` directory:

```bash
cd ABCxxx/figures
./rotate_version.sh c_diagram
```

This rotates backups automatically (`v1` ← current, `v2` ← old `v1`, ... up to `v5`). Keeps 5 versions of `.tex`, `.pdf`, and `.png`.

### 4. Write TikZ code

Use this template as starting point:

```latex
\documentclass[tikz,border=10pt]{standalone}
\usepackage{ctex}
\usepackage{tikz}
\usetikzlibrary{arrows.meta, matrix, calc}

\begin{document}
\begin{tikzpicture}[font=\large]
  % diagram content
\end{tikzpicture}
\end{document}
```

**Key settings for mobile clarity:**
- `font=\large` or larger for all text
- `minimum width/height=1.5cm+` for grid cells
- Use `-{Stealth[length=3mm]}` for arrow tips
- Define colors with `\definecolor` for consistency

**Overlapping avoidance:**
- When multiple arrows pass through the same cell/region, offset them slightly using `+(-0.25,0)` or `+(0.25,0)`
- Use `matrix` with `row sep=-\pgflinewidth, column sep=-\pgflinewidth` for aligned grids

**Color scheme for directions:**
- Up: blue `RGB{30,144,255}`
- Down: green `RGB{34,139,34}`
- Left: orange `RGB{255,140,0}`
- Right: purple `RGB{138,43,226}`

**Color design principles for text and emphasis:**
- Do NOT use a single pure color (e.g., pure green `#2ecc71`, pure red `#ff0000`) for emphasis text, titles, or key insights. Pure monochromatic colors look cheap on mobile screens and provide poor contrast against white backgrounds.
- For emphasis, use **gradient or muted accent colors** instead, such as:
  - Soft indigo `RGB{102,126,234}` (a desaturated blue-purple)
  - Muted coral `RGB{231,76,60}` (already used for highlight/warn)
  - Steel blue `RGB{52,152,219}`
- When creating "before vs after" or "intuitive vs insightful" comparison diagrams, avoid overly wide horizontal layouts that exceed mobile screen width. Prefer vertical stacking or a compact single-column layout.
- Always ensure text labels do not overlap with nodes, arrows, or other text elements. Leave adequate horizontal and vertical gaps.

### 5. Compile and convert

```bash
# Compile with xelatex (required for ctex Chinese support)
xelatex -interaction=nonstopmode diagram.tex

# Convert to high-res PNG (400 DPI for mobile clarity)
pdftoppm -png -r 400 -singlefile diagram.pdf diagram
```

### 6. Verify

Open the PNG and check:
- [ ] All text is readable at phone screen size
- [ ] No overlapping labels or arrows
- [ ] Colors are distinguishable
- [ ] Chinese characters render correctly

### 7. Save version backup (important)

Before making the next edit, save the current version to keep a rollback history.

Use the `rotate_version.sh` script in the `figures/` directory:

```bash
cd ABCxxx/figures
./rotate_version.sh c_diagram
```

This script rotates backups automatically:
- `v1` ← current file (latest backup)
- `v2` ← previous `v1`
- ...up to `v5` (oldest)

Keeps **5 versions** of `.tex`, `.pdf`, and `.png` for each diagram.

### 8. Copy to `figures_sel/`

After verification, copy the final PNGs to `figures_sel/` so all article embeddables are in one place:

```bash
cp figures/c_diagram.png figures_sel/
cp figures/d_diagram.png figures_sel/
cp figures/d_state.png figures_sel/
cp figures/d_backtrack.png figures_sel/
```

These PNGs will be pushed to GitHub and referenced in the article HTML via jsDelivr CDN.

**Critical**: `article.md` references `figures/` for local Markdown preview, but `article.html` uses CDN links pointing to `figures_sel/`. If you edit a diagram and forget to re-copy it to `figures_sel/`, the Markdown preview will show the new image while the published HTML still serves the stale one from CDN. Always sync before generating HTML.

## File Organization

Place TikZ source and intermediate files in the contest's `figures/` subdirectory. Final PNGs for the article live in `figures_sel/`:

```
ABCxxx/
├── figures/
│   ├── c_diagram.tex
│   ├── c_diagram.pdf
│   ├── c_diagram.png
│   ├── c_diagram_v1.tex / .pdf / .png   # latest backup
│   ├── c_diagram_v2.tex / .pdf / .png   # older backup
│   ├── ...
│   ├── d_diagram.tex / .pdf / .png
│   ├── d_diagram_v1.tex / .pdf / .png
│   ├── ...
│   └── rotate_version.sh
└── figures_sel/                          # article embeddables
    ├── c_diagram.png
    ├── d_diagram.png
    ├── d_state.png
    └── d_backtrack.png
```

Clean up intermediate files (`.aux`, `.log`) after verification.
