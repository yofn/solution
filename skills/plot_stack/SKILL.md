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

The stack **must** grow from bottom to top. The base sits low, the top is high. This matches the physical intuition of "stacking" items.

```
    [ top  ]  ← new items arrive here
    [  ... ]
    [ base ]
```

### 2. Incoming channel sits directly above the stack top

Place the input stream (character boxes or array cells) horizontally above the stack. The "current" element should be vertically aligned with the stack top, with a downward arrow suggesting it "falls into" the stack.

```
[ a ] [ b ] [ c ] ← current
            ↓
          [ c ]   ← stack top
          [ b ]
          [ a ]
```

### 3. Highlight the triggering moment

Show the **exact moment** when a pattern is detected at the stack top:
- Dashed box for the incoming element being pushed
- Brace annotation around the relevant stack-top cells
- "Before / After" side-by-side stacks if a replacement occurs

## TikZ Template

Use this as a starting point. Save as `ABCxxx/figures/<name>.tex`.

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

\begin{document}
\begin{tikzpicture}[font=\large, line cap=round, line join=round]
  % Title
  \node at (5.5,5.2) {\textbf{栈 + 输入通道示意图}};

  % Incoming channel (horizontal boxes above stack)
  \node[gray] at (5.15,4.6) {\small 输入通道};
  % Draw channel boxes; highlight the current one
  \draw[thick, channelborder, fill=channelbg] (2.0,3.8) rectangle ++(0.9,0.7);
  \node at (2.45,4.15) {\texttt{x}};
  % ... more boxes ...
  \draw[thick, highlight, fill=channelbg] (6.4,3.8) rectangle ++(0.9,0.7);
  \node at (6.85,4.15) {\texttt{)}};  % current char

  % Arrow from current channel item down to stack top
  \draw[-{Stealth[length=3mm]}, thick, highlight] (6.85,3.8) -- (6.85,3.0);
  \node[highlight, font=\small] at (7.5,3.4) {当前字符};

  % Stack BEFORE (grows upward: bottom y < top y)
  \node[anchor=west, gray] at (0.3,2.7) {\small 栈（替换前）};
  % bottom cell
  \draw[thick, stackborder, fill=stackbg] (1.0,0.3) rectangle ++(0.9,0.6);
  \node at (1.45,0.6) {\texttt{x}};
  % ... more cells upward ...
  % top cell (incoming)
  \draw[thick, highlight, fill=stackbg, dashed] (1.0,2.7) rectangle ++(0.9,0.6);
  \node[highlight] at (1.45,3.0) {\texttt{)}};

  % Stack AFTER (optional)
  \node[anchor=west, gray] at (5.5,2.7) {\small 栈（替换后）};
  % ... draw result stack ...

  % Bottom note
  \node at (3.6,-0.2) {\small 核心逻辑描述};
\end{tikzpicture}
\end{document}
```

## Compilation

Same as the `figure` skill:

```bash
xelatex -interaction=nonstopmode diagram.tex
pdftoppm -png -r 400 -singlefile diagram.pdf diagram
```

## Key Measurements

| Element | Recommended size |
|---------|------------------|
| Stack cell | `0.9 × 0.6` cm |
| Channel cell | `0.9 × 0.7` cm |
| Vertical gap (stack cells) | `0` (adjacent, shared border) |
| Horizontal gap (channel cells) | `0.2` cm |
| Arrow from channel to stack top | `~0.8` cm vertical |

## Anti-patterns

- **Do NOT** draw the stack growing downward (top at bottom). This inverts the physical metaphor.
- **Do NOT** place the input channel far away from the stack top. Keep them close so the "falling in" visual is immediate.
- **Do NOT** use Python drawing libraries for this. Always use TikZ + xelatex + pdftoppm (400 DPI).
