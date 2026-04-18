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
- `figures/` — diagrams (PNG files)

### 2. Plan the article structure

```
1. Opening — why these problems matter
   - Connect to broader algorithm knowledge (e.g., DFS/BFS as tier dividers)
   - Set context and motivation

2. Problem C walkthrough
   - Problem restatement (brief, in Chinese)
   - Key insight / observation
   - Diagram explanation (embed PNG)
   - Code walkthrough (no comments in code; explain in prose)

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
- Code must NOT use HTML escape sequences (`&lt;`, `&gt;`, etc.); keep raw `< >`
- Use **colored font** (`<span style="color:#xxx">text</span>`) for emphasis, NOT bold
- Embed PNG images directly with `![alt](figures/xxx.png)`
- WeChat publication target: "信奥观察"

### 4. Convert to HTML

Generate `ABCxxx/article.html` with inline CSS styled for WeChat reading:

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  body { font-family: -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif; font-size: 16px; line-height: 1.8; color: #333; max-width: 600px; margin: 0 auto; padding: 20px; background: #f5f5f5; }
  .content { background: #fff; padding: 24px; border-radius: 8px; }
  h1 { font-size: 22px; color: #2c3e50; border-left: 4px solid #e74c3c; padding-left: 12px; margin: 28px 0 16px; }
  h2 { font-size: 18px; color: #34495e; margin: 24px 0 12px; }
  h3 { font-size: 16px; color: #555; margin: 18px 0 10px; }
  p { margin: 12px 0; }
  img { max-width: 100%; display: block; margin: 16px auto; border-radius: 4px; }
  pre { background: #1e1e1e; color: #d4d4d4; padding: 16px; border-radius: 6px; overflow-x: auto; font-size: 13px; line-height: 1.5; }
  code { font-family: "SF Mono", Monaco, "Cascadia Code", Consolas, monospace; }
  .highlight-red { color: #e74c3c; }
  .highlight-blue { color: #2980b9; }
  .highlight-green { color: #27ae60; }
  .highlight-purple { color: #8e44ad; }
  .highlight-orange { color: #e67e22; }
  blockquote { border-left: 3px solid #ddd; padding-left: 12px; color: #666; margin: 12px 0; }
</style>
</head>
<body><div class="content">
  <!-- article content -->
</div></body>
</html>
```

### 5. Verify

- [ ] All 4 figures display correctly
- [ ] Code blocks render without escaped characters
- [ ] No comments inside code
- [ ] No personal identifiers
- [ ] Colored emphasis used instead of bold
- [ ] Chinese text throughout
