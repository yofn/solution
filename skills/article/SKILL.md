---
name: article
description: Write a complete tutorial article for competitive programming contest solutions, converting from Markdown to a WeChat-friendly HTML page. Covers problem explanations, algorithm insights, code walkthroughs with diagrams, and motivational conclusions.
---

# Write CP Tutorial Article

Generate a complete tutorial article for competitive programming solutions, suitable for publishing on WeChat Official Account (微信公众号).

## Workflow

### 1. Gather materials

Read from the contest directory:
- `README.md` — problem statements
- `<letter>.cpp` — AC solution code
- `figures_sel/` — all embeddable images (diagrams + code block PNGs)

**Note**: Diagram PNGs in `figures_sel/` must be produced by the `figure` skill (TikZ + xelatex + pdftoppm at 400 DPI). Do not accept low-quality images from other sources.

### 2. Plan the article structure

```
1. Opening — why these problems matter
   - Connect to broader algorithm knowledge (e.g., DFS/BFS as tier dividers)
   - Set context and motivation

2. Problem C walkthrough
   - Problem restatement (brief, in Chinese)
   - Key insight / observation
   - Diagram explanation (embed PNG)
   - Code walkthrough (embed code block PNG image)
   - Code explanation in prose

3. Problem D walkthrough
   - Same structure as C

4. Closing — encouragement
   - Summarize what was learned
   - Encourage regular practice (e.g., weekly ABC contests)
```

### 3. Write Markdown

Save as `ABCxxx/article.md`.

**Rules:**
- All text in **Chinese**
- No contestant IDs or personal identifiers
- Code blocks: delete ALL comments from the source; move explanations to surrounding text
- Use **colored font** (`<span style="color:#xxx">text</span>`) for emphasis, NOT bold
- Embed PNG images with local path `![alt](figures_sel/xxx.png)` for Markdown preview
- WeChat publication target: "信奥观察"

### 4. Convert to HTML

Generate `ABCxxx/article.html` with inline CSS styled for WeChat reading.

**Image URLs**: Use **jsDelivr CDN** addresses so WeChat's editor can auto-download images when pasting:

```
https://cdn.jsdelivr.net/gh/<username>/<repo>@main/ABCxxx/figures_sel/<filename>.png
```

Example:
```html
<img src="https://cdn.jsdelivr.net/gh/yofn/solution@main/ABC453/figures_sel/c_diagram.png" alt="C题数轴路径">
```

**Code blocks**: Do NOT use `<pre><code>` HTML blocks. Insert the syntax-highlighted PNG image directly:

```html
<img src="https://cdn.jsdelivr.net/gh/yofn/solution@main/ABC453/figures_sel/c_code.png" alt="C题代码" style="max-width:100%;display:block;margin:14px auto;border-radius:10px;border:1px solid #ece8e0;">
```

This avoids WeChat's editor stripping whitespace or misaligning text from HTML code blocks.

**Key design choices:**

| Element | Design |
|---------|--------|
| Page width | `max-width: 420px` (~20 Chinese chars per line) |
| Body background | `#f0f2f5` light gray |
| Card background | `#fff` white with rounded corners and shadow |
| Code block background | `#faf8f5` warm beige (for occasional inline `<code>` only) |
| h1 | Red left border + gradient background + rounded right corners |
| h2 | Purple gradient dot prefix (with white inner dot) + dashed underline |
| h3 | Light gray gradient rounded pill label with thin border |

**Syntax highlighting color scheme** (used by the `code` skill when rendering code PNGs, keep consistent):

| Class | Color | For |
|-------|-------|-----|
| `.kw` | `#0066cc` | Keywords (if, for, return, int, void...) |
| `.ty` | `#0969da` | Types (int, long long, char, struct, ll, node...) |
| `.st` | `#0a7a3f` | String literals |
| `.nu` | `#d73a49` | Numbers |
| `.pp` | `#6f42c1` | Preprocessor directives |
| `.fn` | `#8250df` | Function names |
| default | `#383a42` | Other text |

**Full CSS template:**

```css
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  font-size: 16px; line-height: 1.85; color: #333;
  background: #f0f2f5; padding: 16px;
}
.container {
  max-width: 420px; margin: 0 auto; background: #fff;
  padding: 24px 20px; border-radius: 10px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
h1 {
  font-size: 22px; color: #2c3e50;
  background: linear-gradient(90deg, #fff0f0 0%, #fff 100%);
  border-left: 5px solid #e74c3c; padding: 14px 16px;
  margin: 32px 0 20px; border-radius: 0 10px 10px 0;
}
h2 {
  font-size: 18px; color: #34495e; position: relative;
  padding: 10px 0 10px 36px; margin: 28px 0 16px;
  border-bottom: 1px dashed #ddd;
}
h2::before {
  content: ""; position: absolute; left: 0; top: 10px;
  width: 26px; height: 26px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 50%; box-shadow: 0 2px 6px rgba(102,126,234,0.35);
}
h2::after {
  content: ""; position: absolute; left: 8px; top: 18px;
  width: 10px; height: 10px; background: #fff; border-radius: 50%;
}
h3 {
  font-size: 15px; color: #555; display: inline-block;
  background: linear-gradient(90deg, #f0f4f8 0%, #f8fafc 100%);
  padding: 5px 16px; border-radius: 20px;
  border: 1px solid #e8ecf1; margin: 20px 0 12px;
}
p { margin: 12px 0; text-align: justify; word-break: break-word; }
img { max-width: 100%; display: block; margin: 16px auto; border-radius: 6px; }
pre {
  background: #faf8f5; color: #2d2d2d; padding: 16px 18px;
  border-radius: 10px; overflow-x: auto; font-size: 13px;
  line-height: 1.65; margin: 14px 0; border: 1px solid #ece8e0;
}
code { font-family: "SF Mono", "Fira Code", Monaco, "Cascadia Code", Consolas, monospace; }
.kw { color: #0066cc; }
.ty { color: #0969da; }
.st { color: #0a7a3f; }
.nu { color: #d73a49; }
.pp { color: #6f42c1; }
.fn { color: #8250df; }
hr { border: none; border-top: 1px solid #e0e0e0; margin: 24px 0; }
```

### 5. Verify

- [ ] All images use jsDelivr CDN URLs, not local paths
- [ ] Code blocks are inserted as `<img>` PNGs, not `<pre><code>` HTML
- [ ] All figures display correctly
- [ ] No comments inside code
- [ ] No personal identifiers
- [ ] Colored `<span>` used for emphasis, NOT `<strong>`/`<b>`
- [ ] h1/h2/h3 have decorative styles distinct from body text
- [ ] Chinese text throughout

### 6. Publish to WeChat

1. Push the repository to GitHub (ensure all PNGs in `figures_sel/` are pushed)
2. Wait 1–2 minutes for jsDelivr cache to refresh
3. Open `article.html` in a browser to confirm all images load
4. Select all and copy the HTML content
5. Paste into WeChat Official Account editor — images will auto-download and be re-hosted on WeChat's CDN
