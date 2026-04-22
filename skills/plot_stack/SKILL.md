---
name: plot_stack
description: Generate TikZ diagrams for stack-based algorithms with an incoming character/channel stream. Use when a problem solution involves pushing elements onto a stack while scanning a sequence (string, array, etc.), such as bracket matching, string normalization, expression evaluation, or monotone stack problems.
---

# Plot Stack + Incoming Channel Diagrams

Generate TikZ illustrations for algorithms that process an input stream using a stack. This is a common pattern in competitive programming (bracket matching, string reduction, expression parsing, monotone stack, etc.).

## When to Use

Activate this skill when the solution involves:
- Scanning a sequence left-to-right
- Pushing elements onto a stack
- Conditionally popping / replacing based on stack top state

Examples: ABC454-D `(xx)` normalization, bracket matching, postfix evaluation, monotone stack for NGE/NLE.

## Design Principles

### 1. Stack grows upward

The stack **must** grow from bottom to top. The base sits low, the top is high.

```
    [ top  ]  ← new items arrive here
    [  ... ]
    [ base ]
```

### 2. Input stream layout: three elements in a horizontal row

Above the stack, display **three horizontally-aligned** visual elements:

| Left | Center | Right |
|------|--------|-------|
| **已处理** (gray) | **当前** (red/highlight) | **待处理** (yellow/channel) |
| Characters already consumed | Character being processed now | Characters not yet read |

- All three labels and boxes must sit on the **same horizontal baseline**.
- The **current** element must be vertically aligned with the stack top.

### 3. Current element hovers above stack top (NO overlap)

The current-character box sits **directly above** the stack top with a small, visible gap. A short downward arrow connects it to the stack top, creating a "falling in" visual without actual overlap.

```
[已处理]   [ 当前 ]   [待处理]
            ↓ 压栈
          [ top ]   ← dashed box for incoming element
          [ ... ]
          [base ]
```

### 4. Highlight the triggering moment

Show the **exact moment** when a pattern is detected at the stack top:
- Dashed box for the incoming element being pushed
- Brace annotation around the relevant stack-top cells
- "Before / After" side-by-side stacks if a replacement occurs

## TikZ Template

```latex
\documentclass[tikz,border=10pt]{standalone}
\usepackage{ctex}
\usepackage{tikz}
\usetikzlibrary{arrows.meta, decorations.pathreplacing}

\definecolor{stackbg}{RGB}{240,244,248}
\definecolor{stackborder}{RGB}{52,152,219}
\definecolor{highlight}{RGB}{231,76,60}
\definecolor{channelbg}{RGB}{255,250,240}
\definecolor{channelborder}{RGB}{230,180,100}
\definecolor{donegray}{RGB}{160,160,160}

\begin{document}
\begin{tikzpicture}[font=\large, line cap=round, line join=round]
  % Title
  \node at (5.5,5.2) {\textbf{Stack + Input Stream}};

  % ===== Top row: processed | current | pending =====
  \node[donegray, font=\small] at (1.5,4.5) {已处理};
  \node[donegray] at (1.5,4.1) {\texttt{...}};

  \node[highlight, font=\small] at (4.9,4.5) {当前};
  \draw[thick, highlight, fill=highlight!10] (4.45,3.9) rectangle ++(0.9,0.6);
  \node[highlight] at (4.9,4.2) {\texttt{c}};

  \node[channelborder, font=\small] at (8.3,4.5) {待处理};
  \draw[thick, channelborder, fill=channelbg] (7.85,3.9) rectangle ++(0.9,0.6);
  \node at (8.3,4.2) {\texttt{...}};

  % Short arrow from current down to stack top
  \draw[-{Stealth[length=3mm]}, thick, highlight] (4.9,3.85) -- (4.9,3.35);
  \node[highlight, font=\small] at (5.4,3.6) {压栈};

  % ===== Stack (grows upward) =====
  \node[anchor=west, gray] at (3.3,2.9) {\small 栈};
  \def\sx{4.0}
  \draw[thick, stackborder, fill=stackbg] (\sx,0.3) rectangle ++(0.9,0.6);
  \node at (\sx+0.45,0.6) {\texttt{a}};
  % ... more cells upward ...
  \draw[thick, highlight, fill=stackbg, dashed] (\sx,2.7) rectangle ++(0.9,0.6);
  \node[highlight] at (\sx+0.45,3.0) {\texttt{c}};
\end{tikzpicture}
\end{document}
```

## Compilation

Handled by the parent `figure` skill:

```bash
xelatex -interaction=nonstopmode diagram.tex
pdftoppm -png -r 400 -singlefile diagram.pdf diagram
```

## Key Measurements

| Element | Recommended size |
|---------|------------------|
| Stack cell | `0.9 × 0.6` cm |
| Top-row cell (current/pending) | `0.9 × 0.6` cm |
| Vertical gap: current box → stack top | `0.25` cm |
| Horizontal gap between top-row cells | `2.5+` cm |

## Anti-patterns

- **Do NOT** draw the stack growing downward.
- **Do NOT** place processed characters inside the "pending" channel. Keep them in separate left/center/right elements.
- **Do NOT** overlap the current-character box with the stack top. Maintain a visible gap with a short arrow.
- **Do NOT** use Python drawing libraries. Always use TikZ + xelatex + pdftoppm (400 DPI).
