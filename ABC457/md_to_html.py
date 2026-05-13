#!/usr/bin/env python3
"""Convert article.md to WeChat-friendly article.html."""
import re

CDN_BASE = "https://cdn.jsdelivr.net/gh/yofn/solution@main/ABC457/figures_sel"

CSS = """
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
""".strip()


def md_to_html(md_path: str, html_path: str):
    with open(md_path, "r", encoding="utf-8") as f:
        md = f.read()

    lines = md.split("\n")
    html_lines = []
    in_code_block = False
    code_lang = None
    code_buffer = []
    problem_letter = None

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            if not in_code_block:
                in_code_block = True
                code_lang = stripped[3:].strip()
                code_buffer = []
            else:
                in_code_block = False
                letter = problem_letter if problem_letter else "c"
                html_lines.append(
                    f'<img src="{CDN_BASE}/{letter}_code.png" alt="{letter.upper()}题代码" '
                    f'style="max-width:100%;display:block;margin:14px auto;border-radius:10px;border:1px solid #ece8e0;">'
                )
                code_buffer = []
            continue

        if in_code_block:
            continue

        if stripped == "---":
            html_lines.append("<hr>")
            continue

        if stripped.startswith("# "):
            title = stripped[2:]
            html_lines.append(f"<h1>{title}</h1>")
            continue
        if stripped.startswith("## "):
            title = stripped[3:]
            html_lines.append(f"<h2>{title}</h2>")
            if "C 题" in title or "C题" in title:
                problem_letter = "c"
            elif "D 题" in title or "D题" in title:
                problem_letter = "d"
            continue
        if stripped.startswith("### "):
            title = stripped[4:]
            html_lines.append(f"<h3>{title}</h3>")
            continue

        m = re.match(r'!\[(.*?)\]\((.*?)\)', stripped)
        if m:
            alt, path = m.groups()
            filename = path.split("/")[-1]
            html_lines.append(
                f'<img src="{CDN_BASE}/{filename}" alt="{alt}" style="max-width:100%;display:block;margin:14px auto;border-radius:6px;">'
            )
            continue

        if stripped:
            html_lines.append(f"<p>{stripped}</p>")

    body = "\n".join(html_lines)
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ABC457 题解</title>
<style>
{CSS}
</style>
</head>
<body>
<div class="container">
{body}
</div>
</body>
</html>
"""
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Saved {html_path}")


if __name__ == "__main__":
    md_to_html("article.md", "article.html")
