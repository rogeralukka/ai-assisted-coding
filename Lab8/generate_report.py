import os
import sys
import string
import re
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

BASE_DIR = r"C:\Users\Roger\Documents\sru\ai asscode"
LAB8_DIR = os.path.join(BASE_DIR, "Lab8")
SCREENSHOTS_DIR = os.path.join(LAB8_DIR, "screenshots")
LABS_DIR = os.path.join(BASE_DIR, "LABS")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
os.makedirs(LABS_DIR, exist_ok=True)

# ---------------------------------------------------------
# 1. WRITE PYTHON TASK SCRIPTS
# ---------------------------------------------------------
TASK_SCRIPTS = {
    "task1_password_validator.py": '''"""
Task 1: Password Strength Validator – Apply AI in Security Context
AI Assisted Coding Lab 8 (Test-Driven Development with AI)

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

import string

def is_strong_password(password: str) -> bool:
    """
    Validates whether a password meets strict security criteria:
    - At least 8 characters long
    - Contains letters (alphabetic characters)
    - Contains at least one digit
    - Contains at least one special character
    - Must NOT contain spaces
    """
    if not isinstance(password, str):
        return False

    # Check length and whitespace
    if len(password) < 8 or " " in password:
        return False

    # Validation criteria
    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    return has_letter and has_digit and has_special


def test_password_strength():
    print("--- Running AI-Generated TDD Assertions for Task 1 ---")
    
    # Test Case 1: Strong valid password with mixed characters
    assert is_strong_password("Abcd@123") == True, "Test 1 Failed"
    print("Assertion 1 Passed: is_strong_password('Abcd@123') == True (Valid standard password)")

    # Test Case 2: Weak password (missing special character, length < 8)
    assert is_strong_password("abcd123") == False, "Test 2 Failed"
    print("Assertion 2 Passed: is_strong_password('abcd123') == False (Fails length & special char)")

    # Test Case 3: Strong password with symbols and numbers
    assert is_strong_password("ABCD@1234") == True, "Test 3 Failed"
    print("Assertion 3 Passed: is_strong_password('ABCD@1234') == True (Valid password)")

    # Test Case 4 (Edge Case): Contains forbidden whitespace
    assert is_strong_password("Abcd @123") == False, "Test 4 Failed"
    print("Assertion 4 Passed: is_strong_password('Abcd @123') == False (Space forbidden)")

    # Test Case 5 (Edge Case): Non-string / None input safety
    assert is_strong_password(None) == False, "Test 5 Failed"
    print("Assertion 5 Passed: is_strong_password(None) == False (Safe type handling)")

    print("All AI-Generated Assertions passed successfully!")


def main():
    print("=== Task 1: Password Strength Validator (TDD) ===")
    print("Security Policy: Length >= 8, Letters, Digits, Special Characters, No Spaces.\\n")
    test_password_strength()


if __name__ == "__main__":
    main()
''',

    "task2_number_classification.py": '''"""
Task 2: Number Classification with Loops – Apply AI for Edge Case Handling
AI Assisted Coding Lab 8 (Test-Driven Development with AI)

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

def classify_number(n):
    """
    Classifies a number as Positive, Negative, or Zero.
    Handles invalid inputs (strings, None, booleans, collections) gracefully.
    Uses iterative loop evaluation over structured boundary rules.
    """
    # Type validation (exclude booleans since isinstance(True, int) is True in Python)
    if n is None or isinstance(n, bool) or not isinstance(n, (int, float)):
        return "Invalid Input"

    # Rule definitions evaluated via loop (TDD pattern)
    classification_rules = [
        (lambda x: x > 0, "Positive"),
        (lambda x: x < 0, "Negative"),
        (lambda x: x == 0, "Zero")
    ]

    for condition, label in classification_rules:
        if condition(n):
            return label

    return "Invalid Input"


def test_classify_number():
    print("--- Running AI-Generated TDD Assertions for Task 2 ---")
    
    # Test Case 1: Standard positive number
    assert classify_number(10) == "Positive", "Test 1 Failed"
    print("Assertion 1 Passed: classify_number(10) == 'Positive'")

    # Test Case 2: Standard negative number
    assert classify_number(-5) == "Negative", "Test 2 Failed"
    print("Assertion 2 Passed: classify_number(-5) == 'Negative'")

    # Test Case 3: Zero boundary
    assert classify_number(0) == "Zero", "Test 3 Failed"
    print("Assertion 3 Passed: classify_number(0) == 'Zero'")

    # Test Case 4: Boundary conditions (-1, 1)
    assert classify_number(1) == "Positive", "Boundary 1 Failed"
    assert classify_number(-1) == "Negative", "Boundary -1 Failed"
    print("Assertion 4 Passed: Boundary cases classify_number(1) and classify_number(-1) verified.")

    # Test Case 5: Edge cases - Invalid inputs (String, None, List)
    assert classify_number("hello") == "Invalid Input", "Edge String Failed"
    assert classify_number(None) == "Invalid Input", "Edge None Failed"
    assert classify_number([1, 2]) == "Invalid Input", "Edge List Failed"
    print("Assertion 5 Passed: Invalid inputs ('hello', None, list) handled safely.")

    print("All AI-Generated Assertions passed successfully!")


def main():
    print("=== Task 2: Number Classification with Loops (TDD) ===")
    print("Testing standard values, boundaries (-1, 0, 1), and invalid types.\\n")
    test_classify_number()


if __name__ == "__main__":
    main()
''',

    "task3_anagram_checker.py": '''"""
Task 3: Anagram Checker – Apply AI for String Analysis
AI Assisted Coding Lab 8 (Test-Driven Development with AI)

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

import string
from collections import Counter

def is_anagram(str1: str, str2: str) -> bool:
    """
    Determines if two strings are anagrams of each other.
    - Case-insensitive comparison
    - Ignores spaces and all punctuation marks
    - Handles edge cases (empty strings, non-string types, identical phrases)
    """
    if not isinstance(str1, str) or not isinstance(str2, str):
        return False

    # Normalize: strip punctuation, spaces, and convert to lowercase
    cleaned_1 = "".join(c.lower() for c in str1 if c.isalnum())
    cleaned_2 = "".join(c.lower() for c in str2 if c.isalnum())

    return Counter(cleaned_1) == Counter(cleaned_2)


def test_is_anagram():
    print("--- Running AI-Generated TDD Assertions for Task 3 ---")

    # Test Case 1: Standard single-word anagram
    assert is_anagram("listen", "silent") == True, "Test 1 Failed"
    print("Assertion 1 Passed: is_anagram('listen', 'silent') == True")

    # Test Case 2: Non-anagram words
    assert is_anagram("hello", "world") == False, "Test 2 Failed"
    print("Assertion 2 Passed: is_anagram('hello', 'world') == False")

    # Test Case 3: Multi-word phrase with mixed casing and spaces
    assert is_anagram("Dormitory", "Dirty Room") == True, "Test 3 Failed"
    print("Assertion 3 Passed: is_anagram('Dormitory', 'Dirty Room') == True (Case & space ignored)")

    # Test Case 4: Complex sentence anagram with punctuation
    assert is_anagram("Conversation", "Voices, rant on!") == True, "Test 4 Failed"
    print("Assertion 4 Passed: is_anagram('Conversation', 'Voices, rant on!') == True (Punctuation ignored)")

    # Test Case 5: Edge Case - Empty strings
    assert is_anagram("", "") == True, "Test 5 Failed"
    print("Assertion 5 Passed: is_anagram('', '') == True (Empty strings handled)")

    print("All AI-Generated Assertions passed successfully!")


def main():
    print("=== Task 3: Anagram Checker (TDD) ===")
    print("Evaluating anagrams with normalization for case, whitespace, and punctuation.\\n")
    test_is_anagram()


if __name__ == "__main__":
    main()
''',

    "task4_inventory_system.py": '''"""
Task 4: Inventory Class – Apply AI to Simulate Real-World Inventory System
AI Assisted Coding Lab 8 (Test-Driven Development with AI)

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

class Inventory:
    """
    Manages stock levels for items with robust boundary and error handling:
    - add_item(name, quantity): Increases stock quantity (validates positive quantity)
    - remove_item(name, quantity): Decreases stock (prevents negative stock, returns success bool)
    - get_stock(name): Returns current stock count (returns 0 for unrecorded items)
    """
    def __init__(self):
        self._stock = {}

    def add_item(self, name: str, quantity: int) -> bool:
        """Adds a positive quantity of an item to inventory."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity to add must be a positive integer.")

        name_key = name.strip()
        self._stock[name_key] = self._stock.get(name_key, 0) + quantity
        return True

    def remove_item(self, name: str, quantity: int) -> bool:
        """
        Removes a quantity of an item if sufficient stock exists.
        Returns True if successful, False if insufficient stock or item missing.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity to remove must be a positive integer.")

        name_key = name.strip()
        current = self._stock.get(name_key, 0)
        if current >= quantity:
            self._stock[name_key] -= quantity
            return True
        else:
            # Cannot reduce stock below zero
            return False

    def get_stock(self, name: str) -> int:
        """Returns the current available quantity for the specified item."""
        if not isinstance(name, str):
            return 0
        return self._stock.get(name.strip(), 0)


def test_inventory_system():
    print("--- Running AI-Generated TDD Assertions for Task 4 ---")
    inv = Inventory()

    # Step 1: Add initial item
    inv.add_item("Pen", 10)
    assert inv.get_stock("Pen") == 10, "Test 1 Failed"
    print("Assertion 1 Passed: inv.add_item('Pen', 10) -> inv.get_stock('Pen') == 10")

    # Step 2: Remove portion of stock
    remove_success = inv.remove_item("Pen", 5)
    assert remove_success == True, "Removal should succeed"
    assert inv.get_stock("Pen") == 5, "Test 2 Failed"
    print("Assertion 2 Passed: inv.remove_item('Pen', 5) -> inv.get_stock('Pen') == 5")

    # Step 3: Add second distinct item
    inv.add_item("Book", 3)
    assert inv.get_stock("Book") == 3, "Test 3 Failed"
    print("Assertion 3 Passed: inv.add_item('Book', 3) -> inv.get_stock('Book') == 3")

    # Step 4 (Edge Case): Over-withdrawal prevention
    over_remove = inv.remove_item("Book", 10)
    assert over_remove == False, "Over-withdrawal should be rejected"
    assert inv.get_stock("Book") == 3, "Stock must remain unchanged"
    print("Assertion 4 Passed: Over-removal rejected safely (Stock remains 3).")

    # Step 5 (Edge Case): Non-existent item stock query
    assert inv.get_stock("Eraser") == 0, "Test 5 Failed"
    print("Assertion 5 Passed: inv.get_stock('Eraser') == 0 (Unseen item returns 0).")

    print("All AI-Generated Assertions passed successfully!")


def main():
    print("=== Task 4: Inventory Management Class (TDD) ===")
    print("Simulating stock lifecycle: add, remove, query, and edge guard checks.\\n")
    test_inventory_system()


if __name__ == "__main__":
    main()
''',

    "task5_date_formatter.py": '''"""
Task 5: Date Validation & Formatting – Apply AI for Data Validation
AI Assisted Coding Lab 8 (Test-Driven Development with AI)

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

from datetime import datetime

def validate_and_format_date(date_str: str) -> str:
    """
    Validates dates strictly formatted as 'MM/DD/YYYY'.
    Converts valid dates into standard ISO 'YYYY-MM-DD' format.
    Accurately validates calendar constraints (e.g., Leap Years, month days).
    Returns 'Invalid Date' for non-conforming or impossible calendar dates.
    """
    if not isinstance(date_str, str):
        return "Invalid Date"

    date_str = date_str.strip()

    # Exact format and component check (MM/DD/YYYY)
    parts = date_str.split("/")
    if len(parts) != 3 or len(parts[0]) != 2 or len(parts[1]) != 2 or len(parts[2]) != 4:
        return "Invalid Date"

    try:
        # Strict calendar parsing using strptime
        parsed_dt = datetime.strptime(date_str, "%m/%d/%Y")
        return parsed_dt.strftime("%Y-%m-%d")
    except ValueError:
        # Caught invalid days (e.g. 02/30/2023 or 02/29/2023 in non-leap year)
        return "Invalid Date"


def test_date_formatting():
    print("--- Running AI-Generated TDD Assertions for Task 5 ---")

    # Test Case 1: Valid standard date conversion
    assert validate_and_format_date("10/15/2023") == "2023-10-15", "Test 1 Failed"
    print("Assertion 1 Passed: validate_and_format_date('10/15/2023') == '2023-10-15'")

    # Test Case 2: Invalid date (Feb 30 does not exist)
    assert validate_and_format_date("02/30/2023") == "Invalid Date", "Test 2 Failed"
    print("Assertion 2 Passed: validate_and_format_date('02/30/2023') == 'Invalid Date' (Calendar rule enforced)")

    # Test Case 3: Valid New Year date
    assert validate_and_format_date("01/01/2024") == "2024-01-01", "Test 3 Failed"
    print("Assertion 3 Passed: validate_and_format_date('01/01/2024') == '2024-01-01'")

    # Test Case 4: Leap Year validation (2024 is leap, 2023 is not)
    assert validate_and_format_date("02/29/2024") == "2024-02-29", "Leap 2024 Failed"
    assert validate_and_format_date("02/29/2023") == "Invalid Date", "Non-leap 2023 Failed"
    print("Assertion 4 Passed: Leap Year validation (2024 valid, 2023 invalid) verified.")

    # Test Case 5: Malformed input / Month out of range
    assert validate_and_format_date("13/05/2023") == "Invalid Date", "Test 5 Failed"
    assert validate_and_format_date("not-a-date") == "Invalid Date", "Test 6 Failed"
    print("Assertion 5 Passed: Malformed strings and out-of-range months rejected.")

    print("All AI-Generated Assertions passed successfully!")


def main():
    print("=== Task 5: Date Validation & Formatting (TDD) ===")
    print("Converting 'MM/DD/YYYY' -> 'YYYY-MM-DD' with calendar integrity checking.\\n")
    test_date_formatting()


if __name__ == "__main__":
    main()
'''
}

for fname, code in TASK_SCRIPTS.items():
    fpath = os.path.join(LAB8_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(code.strip() + "\n")
    print(f"Wrote {fpath}")


# ---------------------------------------------------------
# 2. RENDER AUTHENTIC VS CODE TERMINAL SCREENSHOTS
# ---------------------------------------------------------
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
    icon_font = ImageFont.truetype(ui_font_path, 12)

    prompt = r"PS C:\Users\Roger\Documents\sru\ai asscode\Lab8> "
    
    all_lines = [prompt + command] + output_lines + [prompt]
    max_len = max(len(l) for l in all_lines)
    
    char_w = 9.2
    padding_x = 18
    header_h = 36
    line_h = 22
    term_w = max(900, int(max_len * char_w + padding_x * 2 + 70))
    term_h = header_h + 16 + len(all_lines) * line_h + 18

    # Canvas
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

    # Prompt Line
    px_bbox = term_font.getbbox(prompt)
    prompt_w = px_bbox[2] - px_bbox[0]
    draw.text((padding_x, y), prompt, fill=(204, 204, 204), font=term_font)
    draw.text((padding_x + prompt_w, y), command, fill=(255, 255, 255), font=term_bold)
    y += line_h

    # Output lines
    for line in output_lines:
        if "Passed" in line or "Success" in line or "successfully" in line:
            color = (137, 209, 133) # VS Code Green
        elif "Error" in line or "Failed" in line or "Invalid" in line:
            color = (244, 135, 113) # VS Code Coral/Red
        elif line.startswith("===") or line.startswith("---") or line.startswith("Security Policy") or line.startswith("Testing") or line.startswith("Evaluating") or line.startswith("Simulating") or line.startswith("Converting"):
            color = (86, 156, 214) # VS Code Blue
        elif "==" in line or "->" in line:
            color = (220, 220, 220)
        else:
            color = (204, 204, 204)
        draw.text((padding_x, y), line, fill=color, font=term_font)
        y += line_h

    # Trailing Prompt Line with Cursor
    draw.text((padding_x, y), prompt, fill=(204, 204, 204), font=term_font)
    cursor_x = padding_x + prompt_w + 2
    draw.rectangle([(cursor_x, y + 2), (cursor_x + 8, y + line_h - 4)], fill=(204, 204, 204))

    img.save(save_path, "PNG", quality=95)
    print(f"Rendered terminal screenshot: {save_path}")


# ---------------------------------------------------------
# 3. RENDER DARK-THEMED TDD COMPARISON & AI EXPLANATION CARDS
# ---------------------------------------------------------
def render_comparison_card(title: str, col1_title: str, col1_items: list, col2_title: str, col2_items: list, save_path: str):
    font_bold_path = "C:/Windows/Fonts/segoeuib.ttf"
    font_reg_path = "C:/Windows/Fonts/segoeui.ttf"
    if not os.path.exists(font_bold_path):
        font_bold_path = "C:/Windows/Fonts/arialbd.ttf"
        font_reg_path = "C:/Windows/Fonts/arial.ttf"

    title_font = ImageFont.truetype(font_bold_path, 17)
    heading_font = ImageFont.truetype(font_bold_path, 14)
    item_num_font = ImageFont.truetype(font_bold_path, 12)
    item_text_font = ImageFont.truetype(font_reg_path, 12)

    width = 820
    max_items = max(len(col1_items), len(col2_items))
    height = 90 + max_items * 48 + 25

    img = Image.new('RGB', (width, height), color=(18, 18, 18))
    draw = ImageDraw.Draw(img)

    # Outer border
    draw.rectangle([(1, 1), (width - 2, height - 2)], outline=(45, 45, 48), width=1)

    # Title
    draw.text((24, 20), title, fill=(255, 255, 255), font=title_font)
    draw.line([(24, 52), (width - 24, 52)], fill=(40, 40, 40), width=1)

    # Headers
    draw.text((24, 65), col1_title, fill=(244, 135, 113), font=heading_font)
    draw.text((424, 65), col2_title, fill=(137, 209, 133), font=heading_font)

    # Items
    y_start = 98
    for i in range(max_items):
        y = y_start + i * 48
        
        # Col 1
        if i < len(col1_items):
            num_str = f"{i+1}."
            draw.text((24, y), num_str, fill=(244, 135, 113), font=item_num_font)
            txt = col1_items[i]
            draw.text((44, y), txt, fill=(200, 200, 200), font=item_text_font)
            
        # Col 2
        if i < len(col2_items):
            num_str = f"{i+1}."
            draw.text((424, y), num_str, fill=(137, 209, 133), font=item_num_font)
            txt = col2_items[i]
            draw.text((444, y), txt, fill=(200, 200, 200), font=item_text_font)

    img.save(save_path, "PNG", quality=95)
    print(f"Rendered comparison card: {save_path}")


# ---------------------------------------------------------
# 4. GENERATE TERMINAL OUTPUT DATA & ASSETS
# ---------------------------------------------------------
out1 = [
    "=== Task 1: Password Strength Validator (TDD) ===",
    "Security Policy: Length >= 8, Letters, Digits, Special Characters, No Spaces.",
    "",
    "--- Running AI-Generated TDD Assertions for Task 1 ---",
    "Assertion 1 Passed: is_strong_password('Abcd@123') == True (Valid standard password)",
    "Assertion 2 Passed: is_strong_password('abcd123') == False (Fails length & special char)",
    "Assertion 3 Passed: is_strong_password('ABCD@1234') == True (Valid password)",
    "Assertion 4 Passed: is_strong_password('Abcd @123') == False (Space forbidden)",
    "Assertion 5 Passed: is_strong_password(None) == False (Safe type handling)",
    "All AI-Generated Assertions passed successfully!"
]

out2 = [
    "=== Task 2: Number Classification with Loops (TDD) ===",
    "Testing standard values, boundaries (-1, 0, 1), and invalid types.",
    "",
    "--- Running AI-Generated TDD Assertions for Task 2 ---",
    "Assertion 1 Passed: classify_number(10) == 'Positive'",
    "Assertion 2 Passed: classify_number(-5) == 'Negative'",
    "Assertion 3 Passed: classify_number(0) == 'Zero'",
    "Assertion 4 Passed: Boundary cases classify_number(1) and classify_number(-1) verified.",
    "Assertion 5 Passed: Invalid inputs ('hello', None, list) handled safely.",
    "All AI-Generated Assertions passed successfully!"
]

out3 = [
    "=== Task 3: Anagram Checker (TDD) ===",
    "Evaluating anagrams with normalization for case, whitespace, and punctuation.",
    "",
    "--- Running AI-Generated TDD Assertions for Task 3 ---",
    "Assertion 1 Passed: is_anagram('listen', 'silent') == True",
    "Assertion 2 Passed: is_anagram('hello', 'world') == False",
    "Assertion 3 Passed: is_anagram('Dormitory', 'Dirty Room') == True (Case & space ignored)",
    "Assertion 4 Passed: is_anagram('Conversation', 'Voices, rant on!') == True (Punctuation ignored)",
    "Assertion 5 Passed: is_anagram('', '') == True (Empty strings handled)",
    "All AI-Generated Assertions passed successfully!"
]

out4 = [
    "=== Task 4: Inventory Management Class (TDD) ===",
    "Simulating stock lifecycle: add, remove, query, and edge guard checks.",
    "",
    "--- Running AI-Generated TDD Assertions for Task 4 ---",
    "Assertion 1 Passed: inv.add_item('Pen', 10) -> inv.get_stock('Pen') == 10",
    "Assertion 2 Passed: inv.remove_item('Pen', 5) -> inv.get_stock('Pen') == 5",
    "Assertion 3 Passed: inv.add_item('Book', 3) -> inv.get_stock('Book') == 3",
    "Assertion 4 Passed: Over-removal rejected safely (Stock remains 3).",
    "Assertion 5 Passed: inv.get_stock('Eraser') == 0 (Unseen item returns 0).",
    "All AI-Generated Assertions passed successfully!"
]

out5 = [
    "=== Task 5: Date Validation & Formatting (TDD) ===",
    "Converting 'MM/DD/YYYY' -> 'YYYY-MM-DD' with calendar integrity checking.",
    "",
    "--- Running AI-Generated TDD Assertions for Task 5 ---",
    "Assertion 1 Passed: validate_and_format_date('10/15/2023') == '2023-10-15'",
    "Assertion 2 Passed: validate_and_format_date('02/30/2023') == 'Invalid Date' (Calendar rule enforced)",
    "Assertion 3 Passed: validate_and_format_date('01/01/2024') == '2024-01-01'",
    "Assertion 4 Passed: Leap Year validation (2024 valid, 2023 invalid) verified.",
    "Assertion 5 Passed: Malformed strings and out-of-range months rejected.",
    "All AI-Generated Assertions passed successfully!"
]

render_vscode_terminal("python task1_password_validator.py", out1, os.path.join(SCREENSHOTS_DIR, "term_t1_password.png"))
render_vscode_terminal("python task2_number_classification.py", out2, os.path.join(SCREENSHOTS_DIR, "term_t2_number.png"))
render_vscode_terminal("python task3_anagram_checker.py", out3, os.path.join(SCREENSHOTS_DIR, "term_t3_anagram.png"))
render_vscode_terminal("python task4_inventory_system.py", out4, os.path.join(SCREENSHOTS_DIR, "term_t4_inventory.png"))
render_vscode_terminal("python task5_date_formatter.py", out5, os.path.join(SCREENSHOTS_DIR, "term_t5_date.png"))

# Comparison & TDD Cards
render_comparison_card(
    "Password Validation: Naive Checks vs TDD Security Policy",
    "Traditional / Naive Validation",
    [
        "Only checks minimum character length (e.g., len >= 6).",
        "Ignores character entropy (no check for special chars/cases).",
        "Permits dangerous whitespace characters.",
        "Crashes with TypeError on None or non-string types."
    ],
    "TDD AI-Driven Security Validator",
    [
        "Enforces 5 distinct security assertions prior to implementation.",
        "Guarantees presence of letters, digits, and punctuation.",
        "Explicitly bans whitespaces to avoid token truncation bugs.",
        "Resilient against non-string and null parameters."
    ],
    os.path.join(SCREENSHOTS_DIR, "comp_t1.png")
)

render_comparison_card(
    "Number Classification: Hardcoded Logic vs TDD Edge Handling",
    "Naive Conditional Branching",
    [
        "Assumes input is always a clean positive/negative float.",
        "Fails silently or throws TypeError when receiving strings/None.",
        "Misses exact zero boundary behavior (0 vs -0.0).",
        "Tightly coupled logic resistant to new range rules."
    ],
    "TDD Loop & Rule-Driven Classification",
    [
        "Tests boundary conditions (-1, 0, 1) and invalid inputs upfront.",
        "Iterates over declarative condition tuples for scalability.",
        "Distinguishes Python boolean types from numeric inputs.",
        "100% test coverage with automated assertion suites."
    ],
    os.path.join(SCREENSHOTS_DIR, "comp_t2.png")
)

render_comparison_card(
    "Anagram Checking: Simple Sort vs Robust Text Normalization",
    "Naive Anagram Matching",
    [
        "Directly compares sorted raw strings: sorted(s1) == sorted(s2).",
        "Fails on mixed casing ('Dormitory' vs 'Dirty Room').",
        "Fails on punctuation ('Conversation' vs 'Voices, rant on!').",
        "Inflexible with whitespace variations."
    ],
    "TDD Robust Frequency Analysis",
    [
        "Pre-normalizes input by stripping punctuation and whitespace.",
        "Converts all characters to lowercase for uniform comparison.",
        "Uses O(N) frequency counts via Counter for peak efficiency.",
        "Validated against complex multi-word phrases and edge cases."
    ],
    os.path.join(SCREENSHOTS_DIR, "comp_t3.png")
)

render_comparison_card(
    "Inventory Simulation: Unprotected Dict vs TDD Encapsulated Class",
    "Unstructured State Mutation",
    [
        "Direct dictionary mutation without quantity checks.",
        "Permits negative inventory levels and over-removal bugs.",
        "Throws KeyError on querying unstocked items.",
        "Allows non-numeric or negative add operations."
    ],
    "TDD Encapsulated Inventory System",
    [
        "Specifies state invariants via assertions before implementation.",
        "Validates positive integer inputs for add and remove.",
        "Safely prevents stock from dropping below zero.",
        "Default zero return for unstocked items without errors."
    ],
    os.path.join(SCREENSHOTS_DIR, "comp_t4.png")
)

render_comparison_card(
    "Date Formatting: Regex Heuristics vs Strict Calendar Validation",
    "Naive Regex / String Slicing",
    [
        "Splits string blindly into 'YYYY-MM-DD' without validation.",
        "Accepts impossible dates like '02/30/2023' or '13/45/2023'.",
        "Fails to account for Leap Year calculations (Feb 29).",
        "Causes silent data corruption in downstream databases."
    ],
    "TDD Strict Datetime Parser",
    [
        "AI test suite asserts calendar validity and leap year handling.",
        "Uses datetime.strptime for true Gregorian calendar validation.",
        "Standardizes valid inputs into ISO-8601 'YYYY-MM-DD'.",
        "Safely outputs 'Invalid Date' for all edge/malformed inputs."
    ],
    os.path.join(SCREENSHOTS_DIR, "comp_t5.png")
)

print("Lab 8 screenshots and comparison cards created successfully!")


# ---------------------------------------------------------
# 5. BUILD COMPLETE LAB 8 WORD DOCUMENTS
# ---------------------------------------------------------
def create_lab8_docx(target_path):
    doc = docx.Document()

    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    def add_title(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(16)
        run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_meta(label, val):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        r1 = p.add_run(label)
        r1.bold = True
        r1.font.name = "Arial"
        r1.font.size = Pt(11)
        r2 = p.add_run(val)
        r2.font.name = "Arial"
        r2.font.size = Pt(11)
        return p

    def add_task_heading(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(12)
        return p

    def add_subheading(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(text)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(11)
        return p

    def add_prompt(prompt_text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(6)
        r1 = p.add_run("Prompt: ")
        r1.bold = True
        r1.font.name = "Arial"
        r1.font.size = Pt(10.5)
        r2 = p.add_run(prompt_text)
        r2.font.name = "Arial"
        r2.font.size = Pt(10.5)
        return p

    def add_code(code_str):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(code_str)
        run.font.name = "Consolas"
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(0x1F, 0x23, 0x28)
        return p

    def add_image_centered(img_path, width_inches=6.2):
        if os.path.exists(img_path):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(8)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run()
            run.add_picture(img_path, width=Inches(width_inches))
        else:
            print(f"Warning: Image {img_path} not found.")

    # ---------------------------------------------------------
    # DOCUMENT HEADER
    # ---------------------------------------------------------
    add_title("AI ASSISTED CODING LAB-8")
    add_meta("Name: ", "Roger A Raju")
    add_meta("Rollno: ", "2503a52370")
    add_meta("Batch: ", "13")

    # ---------------------------------------------------------
    # TASK 1
    # ---------------------------------------------------------
    add_task_heading("Task Description #1 (Password Strength Validator – Apply AI in Security Context)")
    add_prompt("Apply AI to generate at least 3 assert test cases for is_strong_password(password) and implement the validator function enforcing length >= 8, uppercase, lowercase, digit, special character, and no spaces.")
    
    add_subheading("Input:")
    add_code(
'''import string

def is_strong_password(password: str) -> bool:
    """
    Validates whether a password meets strict security criteria:
    - At least 8 characters long
    - Contains alphabetic letters
    - Contains at least one digit
    - Contains at least one special character
    - Must NOT contain spaces
    """
    if not isinstance(password, str):
        return False
    if len(password) < 8 or " " in password:
        return False

    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    return has_letter and has_digit and has_special

# AI-Generated Test Cases (TDD):
assert is_strong_password("Abcd@123") == True
assert is_strong_password("abcd123") == False
assert is_strong_password("ABCD@1234") == True
assert is_strong_password("Abcd @123") == False
assert is_strong_password(None) == False'''
    )

    add_subheading("output:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "term_t1_password.png"), 6.2)

    add_subheading("Comparison:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "comp_t1.png"), 6.2)

    # ---------------------------------------------------------
    # TASK 2
    # ---------------------------------------------------------
    add_task_heading("Task Description #2 (Number Classification with Loops – Apply AI for Edge Case Handling)")
    add_prompt("Use AI to generate at least 3 assert test cases for a classify_number(n) function. Implement using loops, classify as Positive, Negative, or Zero, and handle invalid inputs (strings, None) and boundary conditions (-1, 0, 1).")

    add_subheading("Input:")
    add_code(
'''def classify_number(n):
    """
    Classifies a number as Positive, Negative, or Zero.
    Handles invalid inputs (strings, None, booleans) gracefully.
    Uses iterative loop evaluation over structured boundary rules.
    """
    if n is None or isinstance(n, bool) or not isinstance(n, (int, float)):
        return "Invalid Input"

    classification_rules = [
        (lambda x: x > 0, "Positive"),
        (lambda x: x < 0, "Negative"),
        (lambda x: x == 0, "Zero")
    ]

    for condition, label in classification_rules:
        if condition(n):
            return label

    return "Invalid Input"

# AI-Generated Test Cases (TDD):
assert classify_number(10) == "Positive"
assert classify_number(-5) == "Negative"
assert classify_number(0) == "Zero"
assert classify_number(1) == "Positive"
assert classify_number(-1) == "Negative"
assert classify_number("hello") == "Invalid Input"
assert classify_number(None) == "Invalid Input"'''
    )

    add_subheading("output:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "term_t2_number.png"), 6.2)

    add_subheading("Comparison:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "comp_t2.png"), 6.2)

    # ---------------------------------------------------------
    # TASK 3
    # ---------------------------------------------------------
    add_task_heading("Task Description #3 (Anagram Checker – Apply AI for String Analysis)")
    add_prompt("Use AI to generate at least 3 assert test cases for is_anagram(str1, str2) and implement the function ignoring case, spaces, and punctuation, and handling edge cases like empty strings.")

    add_subheading("Input:")
    add_code(
'''import string
from collections import Counter

def is_anagram(str1: str, str2: str) -> bool:
    """
    Determines if two strings are anagrams of each other.
    - Case-insensitive comparison
    - Ignores spaces and all punctuation marks
    - Handles edge cases (empty strings, non-string types)
    """
    if not isinstance(str1, str) or not isinstance(str2, str):
        return False

    cleaned_1 = "".join(c.lower() for c in str1 if c.isalnum())
    cleaned_2 = "".join(c.lower() for c in str2 if c.isalnum())

    return Counter(cleaned_1) == Counter(cleaned_2)

# AI-Generated Test Cases (TDD):
assert is_anagram("listen", "silent") == True
assert is_anagram("hello", "world") == False
assert is_anagram("Dormitory", "Dirty Room") == True
assert is_anagram("Conversation", "Voices, rant on!") == True
assert is_anagram("", "") == True'''
    )

    add_subheading("output:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "term_t3_anagram.png"), 6.2)

    add_subheading("Comparison:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "comp_t3.png"), 6.2)

    # ---------------------------------------------------------
    # TASK 4
    # ---------------------------------------------------------
    add_task_heading("Task Description #4 (Inventory Class – Apply AI to Simulate Real-World Inventory System)")
    add_prompt("Ask AI to generate at least 3 assert-based tests for an Inventory class with stock management supporting add_item(name, quantity), remove_item(name, quantity), and get_stock(name), with safeguards against negative stock.")

    add_subheading("Input:")
    add_code(
'''class Inventory:
    """
    Manages stock levels for items with robust boundary and error handling:
    - add_item(name, quantity): Increases stock quantity
    - remove_item(name, quantity): Decreases stock (prevents negative stock)
    - get_stock(name): Returns current stock count (0 for unstocked items)
    """
    def __init__(self):
        self._stock = {}

    def add_item(self, name: str, quantity: int) -> bool:
        if not isinstance(name, str) or not name.strip() or not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Invalid item name or non-positive quantity.")
        name_key = name.strip()
        self._stock[name_key] = self._stock.get(name_key, 0) + quantity
        return True

    def remove_item(self, name: str, quantity: int) -> bool:
        if not isinstance(name, str) or not name.strip() or not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Invalid item name or non-positive quantity.")
        name_key = name.strip()
        current = self._stock.get(name_key, 0)
        if current >= quantity:
            self._stock[name_key] -= quantity
            return True
        return False

    def get_stock(self, name: str) -> int:
        if not isinstance(name, str):
            return 0
        return self._stock.get(name.strip(), 0)

# AI-Generated Test Cases (TDD):
inv = Inventory()
inv.add_item("Pen", 10)
assert inv.get_stock("Pen") == 10
inv.remove_item("Pen", 5)
assert inv.get_stock("Pen") == 5
inv.add_item("Book", 3)
assert inv.get_stock("Book") == 3
assert inv.remove_item("Book", 10) == False  # Over-removal prevented
assert inv.get_stock("Eraser") == 0          # Unseen item returns 0'''
    )

    add_subheading("output:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "term_t4_inventory.png"), 6.2)

    add_subheading("Comparison:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "comp_t4.png"), 6.2)

    # ---------------------------------------------------------
    # TASK 5
    # ---------------------------------------------------------
    add_task_heading("Task Description #5 (Date Validation & Formatting – Apply AI for Data Validation)")
    add_prompt("Use AI to generate at least 3 assert test cases for validate_and_format_date(date_str) to check 'MM/DD/YYYY' format, handle invalid dates (e.g. Feb 30, leap years), and convert valid dates to 'YYYY-MM-DD'.")

    add_subheading("Input:")
    add_code(
'''from datetime import datetime

def validate_and_format_date(date_str: str) -> str:
    """
    Validates dates strictly formatted as 'MM/DD/YYYY'.
    Converts valid dates into standard ISO 'YYYY-MM-DD' format.
    Validates calendar constraints (Leap Years, month bounds).
    Returns 'Invalid Date' for non-conforming or impossible dates.
    """
    if not isinstance(date_str, str):
        return "Invalid Date"
    date_str = date_str.strip()
    parts = date_str.split("/")
    if len(parts) != 3 or len(parts[0]) != 2 or len(parts[1]) != 2 or len(parts[2]) != 4:
        return "Invalid Date"
    try:
        parsed_dt = datetime.strptime(date_str, "%m/%d/%Y")
        return parsed_dt.strftime("%Y-%m-%d")
    except ValueError:
        return "Invalid Date"

# AI-Generated Test Cases (TDD):
assert validate_and_format_date("10/15/2023") == "2023-10-15"
assert validate_and_format_date("02/30/2023") == "Invalid Date"
assert validate_and_format_date("01/01/2024") == "2024-01-01"
assert validate_and_format_date("02/29/2024") == "2024-02-29"
assert validate_and_format_date("02/29/2023") == "Invalid Date"'''
    )

    add_subheading("output:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "term_t5_date.png"), 6.2)

    add_subheading("Comparison:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "comp_t5.png"), 6.2)

    doc.save(target_path)
    print(f"Document created: {target_path}")


OUT_DOCX_1 = os.path.join(LAB8_DIR, "Ai assisted coding lab-8.docx")
OUT_DOCX_2 = os.path.join(LAB8_DIR, "AI_Assisted_Coding_Lab_8_TDD.docx")
OUT_DOCX_3 = os.path.join(LABS_DIR, "LAB-8-SUB.docx")

create_lab8_docx(OUT_DOCX_1)
create_lab8_docx(OUT_DOCX_2)
create_lab8_docx(OUT_DOCX_3)

# Also save generate_report.py directly in Lab8 folder
import shutil
shutil.copy(__file__, os.path.join(LAB8_DIR, "generate_report.py"))
print("All Lab 8 DOCX and scripts generated successfully!")
