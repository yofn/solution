#!/usr/bin/env python3
"""Generate diagram images for ABC454 article."""

from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_PATH_EN = "/System/Library/Fonts/Menlo.ttc"

def draw_c_diagram():
    """C题：有向图DFS示意图"""
    W, H = 420, 280
    img = Image.new("RGB", (W, H), "#ffffff")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, 14)
    font_sm = ImageFont.truetype(FONT_PATH, 12)
    font_en = ImageFont.truetype(FONT_PATH_EN, 14)

    # Title
    draw.text((W//2, 10), "C题：有向图与DFS遍历", fill="#333", font=font, anchor="mt")

    # Nodes positions
    nodes = {
        1: (80, 80),
        2: (200, 60),
        3: (320, 80),
        4: (200, 140),
        5: (320, 180),
    }

    # Draw edges (directed)
    edges = [(1,2), (2,3), (2,4), (4,3), (5,2)]
    for u, v in edges:
        x1, y1 = nodes[u]
        x2, y2 = nodes[v]
        # Arrow line
        draw.line([(x1, y1), (x2, y2)], fill="#666", width=2)
        # Arrow head
        import math
        angle = math.atan2(y2-y1, x2-x1)
        arr_len = 10
        arr_angle = 0.4
        ax = x2 - arr_len * math.cos(angle - arr_angle)
        ay = y2 - arr_len * math.sin(angle - arr_angle)
        bx = x2 - arr_len * math.cos(angle + arr_angle)
        by = y2 - arr_len * math.sin(angle + arr_angle)
        draw.polygon([(x2, y2), (ax, ay), (bx, by)], fill="#666")

    # Draw nodes
    for nid, (x, y) in nodes.items():
        r = 18
        color = "#e74c3c" if nid == 1 else "#3498db"
        draw.ellipse([(x-r, y-r), (x+r, y+r)], fill=color, outline="#fff", width=2)
        draw.text((x, y), str(nid), fill="#fff", font=font_en, anchor="mm")

    # Labels
    draw.text((80, 120), "起点(物品1)", fill="#e74c3c", font=font_sm, anchor="mt")
    draw.text((W//2, 240), "DFS从节点1出发，能到达的节点即为可获得物品", fill="#555", font=font_sm, anchor="mt")
    draw.text((W//2, 260), "ans = 可达节点数（包含起点）", fill="#555", font=font_sm, anchor="mt")

    img.save("figures_sel/c_diagram.png")
    print("Saved figures_sel/c_diagram.png")


def draw_d_diagram():
    """D题：栈简化示意图"""
    W, H = 420, 340
    img = Image.new("RGB", (W, H), "#ffffff")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, 14)
    font_sm = ImageFont.truetype(FONT_PATH, 12)
    font_en = ImageFont.truetype(FONT_PATH_EN, 13)

    draw.text((W//2, 10), "D题：栈简化字符串", fill="#333", font=font, anchor="mt")

    # Show stack states step by step
    steps = [
        ("输入: x ( x x ) x", [], "入栈x"),
        ("", ['x'], ""),
        ("输入: (", ['x', '('], "入栈("),
        ("输入: x", ['x', '(', 'x'], "入栈x"),
        ("输入: x", ['x', '(', 'x', 'x'], "入栈x → 检测到(x x)"),
        ("", ['x', 'x', 'x'], "弹栈并替换为x x"),
        ("输入: )", ['x', 'x', 'x'], "入栈)... 等等不对"),
    ]

    # Simpler: show before/after
    y = 50
    draw.text((20, y), "原字符串:", fill="#333", font=font)
    draw.text((100, y), "x(xx)x", fill="#e74c3c", font=font_en)

    y += 30
    draw.text((20, y), "简化过程:", fill="#333", font=font)

    # Stack visualization
    stack_y = y + 30
    stack_x = 60
    box_w, box_h = 36, 32
    states = [
        ([], "初始"),
        (['x'], "入x"),
        (['x','('], "入("),
        (['x','(','x'], "入x"),
        (['x','(','x','x'], "入x"),
        (['x','x','x'], "替换"),
    ]

    for i, (st, label) in enumerate(states):
        x = stack_x + i * 58
        # Draw stack boxes from bottom
        for j, ch in enumerate(st):
            by = stack_y + (3-j) * box_h
            draw.rectangle([(x, by), (x+box_w, by+box_h)], fill="#f0f4f8", outline="#3498db", width=1)
            draw.text((x+box_w//2, by+box_h//2), ch, fill="#333", font=font_en, anchor="mm")
        # Label
        draw.text((x+box_w//2, stack_y + 4*box_h + 8), label, fill="#666", font=font_sm, anchor="mt")
        # Arrow between states
        if i < len(states) - 1:
            draw.text((x+box_w+10, stack_y+box_h*1.5), "→", fill="#999", font=font, anchor="mm")

    # Result
    draw.text((20, stack_y + 4*box_h + 40), "简化结果:", fill="#333", font=font)
    draw.text((100, stack_y + 4*box_h + 40), "xxx", fill="#e74c3c", font=font_en)

    # Key insight
    draw.text((W//2, H-30), "核心：用栈检测末尾的 '(xx)' 并替换为 'xx'", fill="#555", font=font_sm, anchor="mt")

    img.save("figures_sel/d_diagram.png")
    print("Saved figures_sel/d_diagram.png")


if __name__ == "__main__":
    draw_c_diagram()
    draw_d_diagram()
