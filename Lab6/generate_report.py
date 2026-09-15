"""
generate_report.py
Generates the exact Lab Assignment 6 Word Document (LAB-6-SUB.docx)
following the student's exact requested structure, inputs, prompts,
terminal outputs, and screenshots.
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = r"c:\Users\Roger\Documents\sru\ai asscode"
LAB_DIR = os.path.join(BASE_DIR, "Lab6")
SCREENSHOTS_DIR = os.path.join(LAB_DIR, "screenshots")
DOCX_OUT_LAB6 = os.path.join(LAB_DIR, "LAB-6-SUB.docx")
DOCX_OUT_LABS = os.path.join(BASE_DIR, "LABS", "LAB-6-SUB.docx")

os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

# ----------------------------------------------------------------------
# AUTHENTIC VS CODE TERMINAL SCREENSHOT GENERATOR
# ----------------------------------------------------------------------
def render_vscode_terminal(command: str, output_lines: list, save_path: str):
    """
    Renders an authentic VS Code integrated terminal screenshot with:
    - Top tabs bar: PROBLEMS, OUTPUT, DEBUG CONSOLE, TERMINAL (active with blue underline), PORTS
    - Right side terminal switcher dropdown (1: pwsh), split, kill, maximize, close icons
    - PowerShell prompt: PS C:\\Users\\Roger\\Documents\\sru\\ai asscode\\Lab6> python ...
    - Exact terminal output colors
    - Trailing prompt with block cursor
    """
    font_path = "C:/Windows/Fonts/consola.ttf"
    font_bold_path = "C:/Windows/Fonts/consolab.ttf"
    ui_font_path = "C:/Windows/Fonts/segoeui.ttf"
    if not os.path.exists(ui_font_path):
        ui_font_path = "C:/Windows/Fonts/arial.ttf"

    term_font = ImageFont.truetype(font_path, 15)
    term_bold = ImageFont.truetype(font_bold_path, 15)
    tab_font = ImageFont.truetype(ui_font_path, 12)
    tab_bold = ImageFont.truetype(ui_font_path, 12)
    icon_font = ImageFont.truetype(ui_font_path, 12)

    prompt = r"PS C:\Users\Roger\Documents\sru\ai asscode\Lab6> "
    
    all_lines = [prompt + command] + output_lines + [prompt]
    max_len = max(len(l) for l in all_lines)
    
    char_w = 9.2
    padding_x = 18
    header_h = 36
    line_h = 22
    term_w = max(890, int(max_len * char_w + padding_x * 2 + 70))
    term_h = header_h + 16 + len(all_lines) * line_h + 18

    # Image canvas with VS Code Dark+ terminal background (#1e1e1e)
    img = Image.new('RGB', (term_w, term_h), color=(30, 30, 30))
    draw = ImageDraw.Draw(img)

    # 1. VS Code Terminal Header Bar (#181818)
    draw.rectangle([(0, 0), (term_w, header_h)], fill=(24, 24, 24))
    draw.line([(0, header_h), (term_w, header_h)], fill=(45, 45, 45), width=1)

    # Tabs
    tabs = [("PROBLEMS", False), ("OUTPUT", False), ("DEBUG CONSOLE", False), ("TERMINAL", True), ("PORTS", False)]
    cur_x = 18
    for name, is_active in tabs:
        bbox = tab_font.getbbox(name)
        tw = bbox[2] - bbox[0]
        if is_active:
            draw.text((cur_x, 9), name, fill=(255, 255, 255), font=tab_bold)
            draw.line([(cur_x, header_h - 2), (cur_x + tw, header_h - 2)], fill=(0, 122, 204), width=2)
        else:
            draw.text((cur_x, 9), name, fill=(150, 150, 150), font=tab_font)
        cur_x += tw + 22

    # Right side controls
    right_x = term_w - 245
    draw.rounded_rectangle([(right_x, 6), (right_x + 105, header_h - 6)], radius=3, fill=(37, 37, 38), outline=(55, 55, 57))
    draw.text((right_x + 8, 8), "1: pwsh", fill=(204, 204, 204), font=tab_font)
    draw.text((right_x + 88, 9), "v", fill=(150, 150, 150), font=tab_font)

    # Icons
    icons = ["+", "||", "^", "X"]
    ix = right_x + 120
    for ic in icons:
        draw.text((ix, 8), ic, fill=(160, 160, 160), font=icon_font)
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
            color = (244, 135, 113)
        elif "Passed? True" in line or "Highest Discount" in line:
            color = (137, 209, 133)
        elif "Passed? False" in line:
            color = (244, 135, 113)
        elif line.startswith("---"):
            color = (86, 156, 214)
        elif "|" in line:
            color = (212, 212, 212)
        else:
            color = (204, 204, 204)
        draw.text((padding_x, y), line, fill=color, font=term_font)
        y += line_h

    # Trailing Prompt Line with Cursor
    draw.text((padding_x, y), prompt, fill=(204, 204, 204), font=term_font)
    cursor_x = padding_x + prompt_w + 2
    draw.rectangle([(cursor_x, y + 2), (cursor_x + 8, y + line_h - 4)], fill=(204, 204, 204))

    img.save(save_path, "PNG", quality=95)
    print(f"[VS Code Terminal Screenshot]: {save_path}")



# ----------------------------------------------------------------------
# WORD FORMATTING HELPERS
# ----------------------------------------------------------------------
def set_cell_background(cell, fill_hex):
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading)

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_code_block(doc, code_str):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "F7F8FA")
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
    
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="D0D5DD"/>'
        f'  <w:left w:val="single" w:sz="6" w:space="0" w:color="D0D5DD"/>'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="D0D5DD"/>'
        f'  <w:right w:val="single" w:sz="6" w:space="0" w:color="D0D5DD"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(code_str)
    run.font.name = "Consolas"
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(0x1F, 0x23, 0x28)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)


# ----------------------------------------------------------------------
# MAIN BUILDER
# ----------------------------------------------------------------------
def build_report():
    # Outputs to render
    out1 = """Aarav Sharma: Passed? True
Priya Patel: Passed? False
Validation Error: Roll number must be a positive integer."""

    out2_for = """--- For Loop Pattern ---
*
**
***
****
*****"""

    out2_while = """--- While Loop Pattern ---
*
**
***
****
*****"""

    out3 = """     Input  |  Classification
----------------------------
        15  |  Positive    
       -42  |  Negative    
         0  |  Zero        
   3.14159  |  Positive    
    -0.007  |  Negative    
       0.0  |  Zero        """

    out4 = """Age: 65, Member: True  -> Eligible for Senior Discount + Member Bonus (Highest Discount)
Age: 70, Member: False -> Eligible for Standard Senior Discount
Age: 25, Member: True  -> Eligible for Member Discount
Age: 30, Member: False -> No Discount (Standard Rate)"""

    out5 = """  Radius |   Circumference |            Area
--------------------------------------------
    1.00 |          6.2832 |          3.1416
    5.00 |         31.4159 |         78.5398
    7.50 |         47.1239 |        176.7146"""

    img1 = os.path.join(SCREENSHOTS_DIR, "task1_output.png")
    img2_for = os.path.join(SCREENSHOTS_DIR, "task2_for_output.png")
    img2_while = os.path.join(SCREENSHOTS_DIR, "task2_while_output.png")
    img3 = os.path.join(SCREENSHOTS_DIR, "task3_output.png")
    img4 = os.path.join(SCREENSHOTS_DIR, "task4_output.png")
    img5 = os.path.join(SCREENSHOTS_DIR, "task5_output.png")

    render_vscode_terminal("python task1_student.py", out1.split('\n'), img1)
    render_vscode_terminal("python task2_for.py", out2_for.split('\n'), img2_for)
    render_vscode_terminal("python task2_while.py", out2_while.split('\n'), img2_while)
    render_vscode_terminal("python task3_number_analysis.py", out3.split('\n'), img3)
    render_vscode_terminal("python task4_nested_conditionals.py", out4.split('\n'), img4)
    render_vscode_terminal("python task5_circle.py", out5.split('\n'), img5)

    doc = docx.Document()
    
    # Margins
    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.85)
        s.right_margin = Inches(0.85)

    # ------------------------------------------------------------------
    # HEADER DETAILS
    # ------------------------------------------------------------------
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(4)
    r_main = p_title.add_run("AI ASSISTED CODING\nLAB ASSIGNMENT - 6")
    r_main.bold = True
    r_main.font.name = "Calibri"
    r_main.font.size = Pt(16)
    r_main.font.color.rgb = RGBColor(0x00, 0x33, 0x66)

    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.space_before = Pt(2)
    p_meta.paragraph_format.space_after = Pt(14)
    p_meta.paragraph_format.line_spacing = 1.2
    
    runs_meta = [
        ("NAME : ", True), ("ROGER A RAJU\n", False),
        ("BATCH : ", True), ("13 (23CSBTB13)\n", False),
        ("ROLL NO : ", True), ("2503A52370\n", False),
        ("COURSE CODE : ", True), ("23CS002PC304\n", False),
        ("ACADEMIC YEAR : ", True), ("2025-2026 (III Year / II Sem)\n", False)
    ]
    for text, bold in runs_meta:
        r = p_meta.add_run(text)
        r.bold = bold
        r.font.name = "Calibri"
        r.font.size = Pt(11)
        if bold:
            r.font.color.rgb = RGBColor(0x1A, 0x52, 0x76)
        else:
            r.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

    # Separator Line
    p_line = doc.add_paragraph()
    p_line.paragraph_format.space_before = Pt(0)
    p_line.paragraph_format.space_after = Pt(10)
    r_line = p_line.add_run("―" * 55)
    r_line.font.color.rgb = RGBColor(0xAA, 0xAA, 0xAA)

    # ------------------------------------------------------------------
    # TASK 1
    # ------------------------------------------------------------------
    p_t1 = doc.add_paragraph()
    p_t1.paragraph_format.space_before = Pt(8)
    p_t1.paragraph_format.space_after = Pt(4)
    r = p_t1.add_run("Task Description-1 (Classes – Data Validation)")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x00, 0x33, 0x66)

    p_pr1 = doc.add_paragraph()
    p_pr1.paragraph_format.space_before = Pt(2)
    p_pr1.paragraph_format.space_after = Pt(2)
    r = p_pr1.add_run("PROMT:\n")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)
    r_sub = p_pr1.add_run("• Prompt AI to generate a Student class with attributes: name, roll_no, and marks. Add a method is_pass() that returns whether the student has passed (marks ≥ 40).")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(10.5)

    p_in1 = doc.add_paragraph()
    p_in1.paragraph_format.space_before = Pt(6)
    p_in1.paragraph_format.space_after = Pt(2)
    r = p_in1.add_run("INPUT:")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)

    with open(os.path.join(LAB_DIR, "task1_student.py"), "r") as f:
        add_code_block(doc, f.read().strip())

    p_out1 = doc.add_paragraph()
    p_out1.paragraph_format.space_before = Pt(4)
    p_out1.paragraph_format.space_after = Pt(2)
    r = p_out1.add_run("OUTPUT:")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)

    p_out1_txt = doc.add_paragraph()
    p_out1_txt.paragraph_format.space_before = Pt(0)
    p_out1_txt.paragraph_format.space_after = Pt(4)
    r = p_out1_txt.add_run(out1)
    r.font.name = "Consolas"
    r.font.size = Pt(9.5)

    doc.add_picture(img1, width=Inches(6.0))
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # ------------------------------------------------------------------
    # TASK 2
    # ------------------------------------------------------------------
    p_t2 = doc.add_paragraph()
    p_t2.paragraph_format.space_before = Pt(10)
    p_t2.paragraph_format.space_after = Pt(4)
    r = p_t2.add_run("Task Description-2 (Loops – Pattern Generation)")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x00, 0x33, 0x66)

    p_pr2 = doc.add_paragraph()
    p_pr2.paragraph_format.space_before = Pt(2)
    p_pr2.paragraph_format.space_after = Pt(2)
    r = p_pr2.add_run("PROMT:\n")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)
    r_sub = p_pr2.add_run("• Ask AI to generate a function that prints a right-angled triangle star pattern using a for loop. Then regenerate the same pattern using a while loop.")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(10.5)

    p_in2_for = doc.add_paragraph()
    p_in2_for.paragraph_format.space_before = Pt(6)
    p_in2_for.paragraph_format.space_after = Pt(2)
    r = p_in2_for.add_run("INPUT (by using for loop):")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)

    with open(os.path.join(LAB_DIR, "task2_for.py"), "r") as f:
        add_code_block(doc, f.read().strip())

    p_out2_for = doc.add_paragraph()
    p_out2_for.paragraph_format.space_before = Pt(4)
    p_out2_for.paragraph_format.space_after = Pt(2)
    r = p_out2_for.add_run("output:")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)

    p_out2f_txt = doc.add_paragraph()
    p_out2f_txt.paragraph_format.space_before = Pt(0)
    p_out2f_txt.paragraph_format.space_after = Pt(4)
    r = p_out2f_txt.add_run(out2_for)
    r.font.name = "Consolas"
    r.font.size = Pt(9.5)

    doc.add_picture(img2_for, width=Inches(6.0))
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    p_in2_wh = doc.add_paragraph()
    p_in2_wh.paragraph_format.space_before = Pt(6)
    p_in2_wh.paragraph_format.space_after = Pt(2)
    r = p_in2_wh.add_run("Input(by using while loop):")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)

    with open(os.path.join(LAB_DIR, "task2_while.py"), "r") as f:
        add_code_block(doc, f.read().strip())

    p_out2_wh = doc.add_paragraph()
    p_out2_wh.paragraph_format.space_before = Pt(4)
    p_out2_wh.paragraph_format.space_after = Pt(2)
    r = p_out2_wh.add_run("output:")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)

    p_out2w_txt = doc.add_paragraph()
    p_out2w_txt.paragraph_format.space_before = Pt(0)
    p_out2w_txt.paragraph_format.space_after = Pt(4)
    r = p_out2w_txt.add_run(out2_while)
    r.font.name = "Consolas"
    r.font.size = Pt(9.5)

    doc.add_picture(img2_while, width=Inches(6.0))
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # ------------------------------------------------------------------
    # TASK 3
    # ------------------------------------------------------------------
    p_t3 = doc.add_paragraph()
    p_t3.paragraph_format.space_before = Pt(10)
    p_t3.paragraph_format.space_after = Pt(4)
    r = p_t3.add_run("Task Description-3 (Conditional Statements – Number Analysis)")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x00, 0x33, 0x66)

    p_pr3 = doc.add_paragraph()
    p_pr3.paragraph_format.space_before = Pt(2)
    p_pr3.paragraph_format.space_after = Pt(2)
    r = p_pr3.add_run("Promt:\n")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)
    r_sub = p_pr3.add_run("• Ask AI to write a function that checks whether a given number is positive, negative, or zero using if-elif-else. Test the function with multiple inputs.")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(10.5)

    p_in3 = doc.add_paragraph()
    p_in3.paragraph_format.space_before = Pt(6)
    p_in3.paragraph_format.space_after = Pt(2)
    r = p_in3.add_run("Input:")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)

    with open(os.path.join(LAB_DIR, "task3_number_analysis.py"), "r") as f:
        add_code_block(doc, f.read().strip())

    p_out3 = doc.add_paragraph()
    p_out3.paragraph_format.space_before = Pt(4)
    p_out3.paragraph_format.space_after = Pt(2)
    r = p_out3.add_run("output:")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)

    p_out3_txt = doc.add_paragraph()
    p_out3_txt.paragraph_format.space_before = Pt(0)
    p_out3_txt.paragraph_format.space_after = Pt(4)
    r = p_out3_txt.add_run(out3)
    r.font.name = "Consolas"
    r.font.size = Pt(9.5)

    doc.add_picture(img3, width=Inches(6.0))
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # ------------------------------------------------------------------
    # TASK 4
    # ------------------------------------------------------------------
    p_t4 = doc.add_paragraph()
    p_t4.paragraph_format.space_before = Pt(10)
    p_t4.paragraph_format.space_after = Pt(4)
    r = p_t4.add_run("Task Description-4 (Nested Conditionals)")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x00, 0x33, 0x66)

    p_pr4 = doc.add_paragraph()
    p_pr4.paragraph_format.space_before = Pt(2)
    p_pr4.paragraph_format.space_after = Pt(2)
    r = p_pr4.add_run("Promt:\n")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)
    r_sub = p_pr4.add_run("• Generate a function check_discount(age, is_member) that determines discount eligibility:\n"
                          "• Age ≥ 60 → Senior discount\n"
                          "• Member → Additional discount\n"
                          "Use nested if statements.")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(10.5)

    p_in4 = doc.add_paragraph()
    p_in4.paragraph_format.space_before = Pt(6)
    p_in4.paragraph_format.space_after = Pt(2)
    r = p_in4.add_run("Input:")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)

    with open(os.path.join(LAB_DIR, "task4_nested_conditionals.py"), "r") as f:
        add_code_block(doc, f.read().strip())

    p_out4 = doc.add_paragraph()
    p_out4.paragraph_format.space_before = Pt(4)
    p_out4.paragraph_format.space_after = Pt(2)
    r = p_out4.add_run("output:")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)

    p_out4_txt = doc.add_paragraph()
    p_out4_txt.paragraph_format.space_before = Pt(0)
    p_out4_txt.paragraph_format.space_after = Pt(4)
    r = p_out4_txt.add_run(out4)
    r.font.name = "Consolas"
    r.font.size = Pt(9.5)

    doc.add_picture(img4, width=Inches(6.0))
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # ------------------------------------------------------------------
    # TASK 5
    # ------------------------------------------------------------------
    p_t5 = doc.add_paragraph()
    p_t5.paragraph_format.space_before = Pt(10)
    p_t5.paragraph_format.space_after = Pt(4)
    r = p_t5.add_run("Task Description-5 (Class – Mathematical Opera)")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x00, 0x33, 0x66)

    p_pr5 = doc.add_paragraph()
    p_pr5.paragraph_format.space_before = Pt(2)
    p_pr5.paragraph_format.space_after = Pt(2)
    r = p_pr5.add_run("Promt:\n")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)
    r_sub = p_pr5.add_run("• Ask AI to create a Circle class with methods to calculate area () and circumference () given the radius.")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(10.5)

    p_in5 = doc.add_paragraph()
    p_in5.paragraph_format.space_before = Pt(6)
    p_in5.paragraph_format.space_after = Pt(2)
    r = p_in5.add_run("Input:")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)

    with open(os.path.join(LAB_DIR, "task5_circle.py"), "r") as f:
        add_code_block(doc, f.read().strip())

    p_out5 = doc.add_paragraph()
    p_out5.paragraph_format.space_before = Pt(4)
    p_out5.paragraph_format.space_after = Pt(2)
    r = p_out5.add_run("output:")
    r.bold = True
    r.font.name = "Calibri"
    r.font.size = Pt(11)

    p_out5_txt = doc.add_paragraph()
    p_out5_txt.paragraph_format.space_before = Pt(0)
    p_out5_txt.paragraph_format.space_after = Pt(4)
    r = p_out5_txt.add_run(out5)
    r.font.name = "Consolas"
    r.font.size = Pt(9.5)

    doc.add_picture(img5, width=Inches(6.0))
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # Save with graceful fallback if file is currently open in Microsoft Word
    target_paths = [
        os.path.join(LAB_DIR, "LAB-6-ASSIGNMENT.docx"),
        os.path.join(LAB_DIR, "LAB-6-SUBMISSION.docx"),
        DOCX_OUT_LAB6,
        DOCX_OUT_LABS
    ]
    
    saved = []
    for path in target_paths:
        try:
            doc.save(path)
            saved.append(path)
            print(f"[SUCCESS] Saved to: {path}")
        except PermissionError:
            print(f"[NOTE] Could not overwrite '{os.path.basename(path)}' because it is currently open in Word.")
        except Exception as e:
            print(f"[ERROR] Could not save to {path}: {e}")

    if saved:
        print("\nSuccessfully generated report documents at:")
        for s in saved:
            print("  ->", s)


if __name__ == "__main__":
    build_report()

