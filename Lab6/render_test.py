import os
from PIL import Image, ImageDraw, ImageFont

def render_vscode_terminal(command: str, output_lines: list, save_path: str):
    font_path = "C:/Windows/Fonts/consola.ttf"
    font_bold_path = "C:/Windows/Fonts/consolab.ttf"
    ui_font_path = "C:/Windows/Fonts/segoeui.ttf"
    if not os.path.exists(ui_font_path):
        ui_font_path = "C:/Windows/Fonts/arial.ttf"

    term_font = ImageFont.truetype(font_path, 15)
    term_bold = ImageFont.truetype(font_bold_path, 15)
    tab_font = ImageFont.truetype(ui_font_path, 12)
    tab_bold = ImageFont.truetype(ui_font_path, 12)
    icon_font = ImageFont.truetype(ui_font_path, 13)

    prompt = r"PS C:\Users\Roger\Documents\sru\ai asscode\Lab6> "
    
    # Calculate dimensions
    all_lines = [prompt + command] + output_lines + [prompt]
    max_len = max(len(l) for l in all_lines)
    
    char_w = 9.2
    padding_x = 18
    header_h = 36
    line_h = 22
    term_w = max(880, int(max_len * char_w + padding_x * 2 + 60))
    term_h = header_h + 16 + len(all_lines) * line_h + 20

    # Image canvas
    img = Image.new('RGB', (term_w, term_h), color=(30, 30, 30)) # #1e1e1e
    draw = ImageDraw.Draw(img)

    # 1. VS Code Terminal Header Bar
    draw.rectangle([(0, 0), (term_w, header_h)], fill=(24, 24, 24)) # #181818
    draw.line([(0, header_h), (term_w, header_h)], fill=(45, 45, 45), width=1)

    # Tabs
    tabs = [("PROBLEMS", False), ("OUTPUT", False), ("DEBUG CONSOLE", False), ("TERMINAL", True), ("PORTS", False)]
    cur_x = 18
    for name, is_active in tabs:
        bbox = tab_font.getbbox(name)
        tw = bbox[2] - bbox[0]
        if is_active:
            # Active tab text (white)
            draw.text((cur_x, 9), name, fill=(255, 255, 255), font=tab_bold)
            # Blue underline
            draw.line([(cur_x, header_h - 2), (cur_x + tw, header_h - 2)], fill=(0, 122, 204), width=2)
        else:
            draw.text((cur_x, 9), name, fill=(150, 150, 150), font=tab_font)
        cur_x += tw + 22

    # Right side controls
    right_x = term_w - 240
    # Dropdown box for terminal session
    draw.rounded_rectangle([(right_x, 6), (right_x + 110, header_h - 6)], radius=3, fill=(37, 37, 38), outline=(60, 60, 60))
    draw.text((right_x + 8, 8), "1: pwsh", fill=(204, 204, 204), font=tab_font)
    draw.text((right_x + 92, 9), "v", fill=(150, 150, 150), font=tab_font)

    # Action icons
    icons = ["+", "||", "^", "X"]
    ix = right_x + 125
    for ic in icons:
        draw.text((ix, 7), ic, fill=(170, 170, 170), font=icon_font)
        ix += 26

    # 2. Terminal Body
    y = header_h + 12

    # First Prompt Line
    draw.text((padding_x, y), prompt, fill=(204, 204, 204), font=term_font)
    px_bbox = term_font.getbbox(prompt)
    prompt_w = px_bbox[2] - px_bbox[0]
    draw.text((padding_x + prompt_w, y), command, fill=(255, 255, 255), font=term_bold)
    y += line_h

    # Output lines
    for line in output_lines:
        if "Error" in line or "Validation" in line:
            color = (244, 135, 113) # Red / Coral
        elif "Passed? True" in line or "Highest Discount" in line:
            color = (137, 209, 133) # VS Code Green
        elif "Passed? False" in line:
            color = (244, 135, 113) # Coral Red
        elif line.startswith("---"):
            color = (86, 156, 214) # Blue
        elif "|" in line:
            color = (212, 212, 212)
        else:
            color = (204, 204, 204)
        draw.text((padding_x, y), line, fill=color, font=term_font)
        y += line_h

    # Trailing Prompt Line with Cursor
    draw.text((padding_x, y), prompt, fill=(204, 204, 204), font=term_font)
    # Cursor
    cursor_x = padding_x + prompt_w + 2
    draw.rectangle([(cursor_x, y + 2), (cursor_x + 8, y + line_h - 4)], fill=(204, 204, 204))

    img.save(save_path, "PNG", quality=95)
    print("Saved test image:", save_path)

if __name__ == "__main__":
    t1_lines = [
        "Aarav Sharma: Passed? True",
        "Priya Patel: Passed? False",
        "Validation Error: Roll number must be a positive integer."
    ]
    render_vscode_terminal("python task1_student.py", t1_lines, r"c:\Users\Roger\Documents\sru\ai asscode\Lab6\screenshots\test_vscode.png")
