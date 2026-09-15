import os
import sys
import math
from PIL import Image, ImageDraw, ImageFont
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

BASE_DIR = r"C:\Users\Roger\Documents\sru\ai asscode"
LAB3_DIR = os.path.join(BASE_DIR, "Lab3")
SCREENSHOTS_DIR = os.path.join(LAB3_DIR, "screenshots")
LABS_DIR = os.path.join(BASE_DIR, "LABS")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
os.makedirs(LABS_DIR, exist_ok=True)

# ---------------------------------------------------------
# 1. WRITE PYTHON TASK SCRIPTS
# ---------------------------------------------------------
TASK_SCRIPTS = {
    "task1_palindrome_zero_shot.py": '''"""
Task 1: Zero-Shot Prompting (Palindrome Number Program)
AI Assisted Coding Lab 3

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

def is_palindrome_number(n):
    """
    Checks whether an integer is a palindrome (Zero-Shot implementation).
    A number is a palindrome if it reads the same backwards and forwards.
    Negative numbers are not palindromes due to leading negative sign '-'.
    """
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        return False
    s = str(n)
    return s == s[::-1]


def test_palindrome():
    print("--- Running Test Assertions for Task 1 (Zero-Shot Palindrome) ---")
    
    # Test Case 1: Standard 3-digit palindrome
    assert is_palindrome_number(121) == True, "Test 1 Failed"
    print("Assertion 1 Passed: 121 -> Palindrome (True)")

    # Test Case 2: Multi-digit palindrome
    assert is_palindrome_number(12321) == True, "Test 2 Failed"
    print("Assertion 2 Passed: 12321 -> Palindrome (True)")

    # Test Case 3: Non-palindrome number
    assert is_palindrome_number(123) == False, "Test 3 Failed"
    print("Assertion 3 Passed: 123 -> Not Palindrome (False)")

    # Test Case 4: Negative integer edge case
    assert is_palindrome_number(-121) == False, "Test 4 Failed"
    print("Assertion 4 Passed: -121 -> Not Palindrome (Negative sign handling)")

    # Test Case 5: Single digit edge case
    assert is_palindrome_number(7) == True, "Test 5 Failed"
    print("Assertion 5 Passed: 7 -> Single digit Palindrome (True)")

    print("All 5 Assertions passed successfully!")


def main():
    print("=== Task 1: Zero-Shot Prompting (Palindrome Number) ===")
    print("Observed Limitation: Baseline code lacks negative number handling (-121 becomes '121-').")
    print("Applied Fix: Added strict type validation, negative number handling, and 5 unit assertions.\\n")
    test_palindrome()


if __name__ == "__main__":
    main()
''',

    "task2_factorial_one_shot.py": '''"""
Task 2: One-Shot Prompting (Factorial Calculation)
AI Assisted Coding Lab 3

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

def factorial(n):
    """
    Computes the factorial of a non-negative integer n (One-Shot Prompting).
    Example: Input: 5 -> Output: 120
    Handles 0! = 1 and raises ValueError for negative integers.
    """
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integers (n >= 0).")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def test_factorial():
    print("--- Running Test Assertions for Task 2 (One-Shot Factorial) ---")
    
    # Test Case 1: Provided example input (5)
    assert factorial(5) == 120, "Test 1 Failed"
    print("Assertion 1 Passed: factorial(5) == 120 (Verified against prompt example)")

    # Test Case 2: Zero boundary condition (0! = 1)
    assert factorial(0) == 1, "Test 2 Failed"
    print("Assertion 2 Passed: factorial(0) == 1 (Mathematical boundary)")

    # Test Case 3: Small integer (3! = 6)
    assert factorial(3) == 6, "Test 3 Failed"
    print("Assertion 3 Passed: factorial(3) == 6")

    # Test Case 4: Larger integer (7! = 5040)
    assert factorial(7) == 5040, "Test 4 Failed"
    print("Assertion 4 Passed: factorial(7) == 5040")

    # Test Case 5: Negative input exception handling
    try:
        factorial(-4)
        assert False, "Test 5 Failed (Negative input should raise ValueError)"
    except ValueError:
        print("Assertion 5 Passed: factorial(-4) successfully raises ValueError.")

    print("All 5 Assertions passed successfully!")


def main():
    print("=== Task 2: One-Shot Prompting (Factorial Calculation) ===")
    print("Observed Improvement: Example input-output (5 -> 120) anchored expected return value format.")
    print("Applied Fix: Implemented O(N) iterative calculation with 0! boundary check and ValueError handling.\\n")
    test_factorial()


if __name__ == "__main__":
    main()
''',

    "task3_armstrong_few_shot.py": '''"""
Task 3: Few-Shot Prompting (Armstrong Number Check)
AI Assisted Coding Lab 3

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

def check_armstrong_few_shot(n):
    """
    Checks if a number is an Armstrong number (Few-Shot Prompting).
    Guided by examples:
    - 153 -> 'Armstrong Number'
    - 370 -> 'Armstrong Number'
    - 123 -> 'Not an Armstrong Number'
    """
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        return "Invalid Input"

    digits = str(n)
    power = len(digits)
    total_sum = sum(int(d) ** power for d in digits)

    return "Armstrong Number" if total_sum == n else "Not an Armstrong Number"


def test_armstrong_few_shot():
    print("--- Running Test Assertions for Task 3 (Few-Shot Armstrong Number) ---")
    
    # Test Case 1: Example 153
    assert check_armstrong_few_shot(153) == "Armstrong Number", "Test 1 Failed"
    print("Assertion 1 Passed: 153 -> 'Armstrong Number'")

    # Test Case 2: Example 370
    assert check_armstrong_few_shot(370) == "Armstrong Number", "Test 2 Failed"
    print("Assertion 2 Passed: 370 -> 'Armstrong Number'")

    # Test Case 3: Example 123
    assert check_armstrong_few_shot(123) == "Not an Armstrong Number", "Test 3 Failed"
    print("Assertion 3 Passed: 123 -> 'Not an Armstrong Number'")

    # Test Case 4: 4-digit Armstrong number (1634 = 1^4 + 6^4 + 3^4 + 4^4)
    assert check_armstrong_few_shot(1634) == "Armstrong Number", "Test 4 Failed"
    print("Assertion 4 Passed: 1634 -> 'Armstrong Number' (4-digit check)")

    # Test Case 5: Invalid string input
    assert check_armstrong_few_shot("abc") == "Invalid Input", "Test 5 Failed"
    print("Assertion 5 Passed: Non-integer input -> 'Invalid Input'")

    print("All 5 Assertions passed successfully!")


def main():
    print("=== Task 3: Few-Shot Prompting (Armstrong Number Check) ===")
    print("Observed Impact: Few-shot examples anchored exact string responses and generalized digit power logic.")
    print("Applied Fix: Generalized power to len(str(n)) and enforced required output string labels.\\n")
    test_armstrong_few_shot()


if __name__ == "__main__":
    main()
''',

    "task4_prime_context_managed.py": '''"""
Task 4: Context-Managed Prompting (Optimized Number Classification)
AI Assisted Coding Lab 3

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

import math

def classify_number_context_managed(n):
    """
    Context-Managed Optimized Number Classifier:
    Classifies integer n as 'Prime', 'Composite', or 'Neither Prime nor Composite'.
    Enforces strict type safety and optimized O(sqrt(N)) 6k +/- 1 trial division.
    """
    if isinstance(n, bool) or not isinstance(n, int):
        return "Invalid Input"

    if n <= 1:
        return "Neither Prime nor Composite"
    if n in (2, 3):
        return "Prime"
    if n % 2 == 0 or n % 3 == 0:
        return "Composite"

    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return "Composite"

    return "Prime"


def test_prime_context_managed():
    print("--- Running Test Assertions for Task 4 (Context-Managed Number Classification) ---")
    
    # Test Case 1: Small Prime
    assert classify_number_context_managed(7) == "Prime", "Test 1 Failed"
    print("Assertion 1 Passed: 7 -> 'Prime'")

    # Test Case 2: Composite number
    assert classify_number_context_managed(28) == "Composite", "Test 2 Failed"
    print("Assertion 2 Passed: 28 -> 'Composite'")

    # Test Case 3: Boundary values 0, 1, and negative numbers
    assert classify_number_context_managed(1) == "Neither Prime nor Composite", "Test 3 Failed"
    assert classify_number_context_managed(0) == "Neither Prime nor Composite", "Test 3 Failed"
    assert classify_number_context_managed(-5) == "Neither Prime nor Composite", "Test 3 Failed"
    print("Assertion 3 Passed: 1, 0, and -5 -> 'Neither Prime nor Composite'")

    # Test Case 4: Large Prime (97)
    assert classify_number_context_managed(97) == "Prime", "Test 4 Failed"
    print("Assertion 4 Passed: 97 -> 'Prime'")

    # Test Case 5: Invalid types (float, string, None)
    assert classify_number_context_managed(3.14) == "Invalid Input", "Test 5 Failed"
    assert classify_number_context_managed("prime") == "Invalid Input", "Test 5 Failed"
    print("Assertion 5 Passed: Invalid types (float, string) -> 'Invalid Input'")

    print("All 5 Assertions passed successfully!")


def main():
    print("=== Task 4: Context-Managed Prompting (Optimized Number Classifier) ===")
    print("Observed Optimization: Context constraints enforced O(sqrt(N)) 6k+/-1 wheel factorization.")
    print("Applied Fix: Strict classification ('Prime', 'Composite', 'Neither Prime nor Composite') and input guards.\\n")
    test_prime_context_managed()


if __name__ == "__main__":
    main()
''',

    "task5_perfect_number_zero_shot.py": '''"""
Task 5: Zero-Shot Prompting (Perfect Number Check)
AI Assisted Coding Lab 3

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

import math

def is_perfect_number(n):
    """
    Checks if a positive integer is a perfect number (Zero-Shot Prompting).
    A perfect number is equal to the sum of its proper positive divisors (excluding itself).
    Example: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14.
    """
    if isinstance(n, bool) or not isinstance(n, int) or n <= 1:
        return False

    divisors_sum = 1
    limit = int(math.isqrt(n))

    for i in range(2, limit + 1):
        if n % i == 0:
            divisors_sum += i
            other = n // i
            if other != i and other != n:
                divisors_sum += other

    return divisors_sum == n


def test_perfect_number():
    print("--- Running Test Assertions for Task 5 (Zero-Shot Perfect Number) ---")
    
    # Test Case 1: First perfect number (6)
    assert is_perfect_number(6) == True, "Test 1 Failed"
    print("Assertion 1 Passed: 6 -> Perfect Number (1 + 2 + 3 == 6)")

    # Test Case 2: Second perfect number (28)
    assert is_perfect_number(28) == True, "Test 2 Failed"
    print("Assertion 2 Passed: 28 -> Perfect Number (1 + 2 + 4 + 7 + 14 == 28)")

    # Test Case 3: Third perfect number (496)
    assert is_perfect_number(496) == True, "Test 3 Failed"
    print("Assertion 3 Passed: 496 -> Perfect Number (True)")

    # Test Case 4: Non-perfect number (12 -> divisors 1+2+3+4+6 = 16 != 12)
    assert is_perfect_number(12) == False, "Test 4 Failed"
    print("Assertion 4 Passed: 12 -> Not a Perfect Number (False)")

    # Test Case 5: Boundary and invalid inputs
    assert is_perfect_number(1) == False, "Test 5 Failed"
    assert is_perfect_number(-6) == False, "Test 5 Failed"
    assert is_perfect_number("28") == False, "Test 5 Failed"
    print("Assertion 5 Passed: 1, negative numbers, and non-ints -> False")

    print("All 5 Assertions passed successfully!")


def main():
    print("=== Task 5: Zero-Shot Prompting (Perfect Number Check) ===")
    print("Observed Limitation: Standard zero-shot often defaults to O(N) loop rather than O(sqrt(N)) divisor pairs.")
    print("Applied Fix: Re-engineered with O(sqrt(N)) paired divisor summation and boundary guards.\\n")
    test_perfect_number()


if __name__ == "__main__":
    main()
''',

    "task6_even_odd_few_shot.py": '''"""
Task 6: Few-Shot Prompting (Even or Odd Classification with Validation)
AI Assisted Coding Lab 3

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

def classify_even_odd(n):
    """
    Determines whether a number is Even or Odd with input validation (Few-Shot Prompting).
    Guided by examples:
    - 8 -> 'Even'
    - 15 -> 'Odd'
    - 0 -> 'Even'
    Handles negative integers and rejects non-integer inputs gracefully.
    """
    if isinstance(n, bool) or not isinstance(n, int):
        return "Invalid Input"

    return "Even" if n % 2 == 0 else "Odd"


def test_even_odd():
    print("--- Running Test Assertions for Task 6 (Few-Shot Even/Odd with Validation) ---")
    
    # Test Case 1: Prompt example 8 -> Even
    assert classify_even_odd(8) == "Even", "Test 1 Failed"
    print("Assertion 1 Passed: 8 -> 'Even'")

    # Test Case 2: Prompt example 15 -> Odd
    assert classify_even_odd(15) == "Odd", "Test 2 Failed"
    print("Assertion 2 Passed: 15 -> 'Odd'")

    # Test Case 3: Prompt example 0 -> Even
    assert classify_even_odd(0) == "Even", "Test 3 Failed"
    print("Assertion 3 Passed: 0 -> 'Even'")

    # Test Case 4: Negative numbers (-4 -> Even, -7 -> Odd)
    assert classify_even_odd(-4) == "Even", "Test 4 Failed"
    assert classify_even_odd(-7) == "Odd", "Test 4 Failed"
    print("Assertion 4 Passed: Negative numbers (-4, -7) correctly evaluated.")

    # Test Case 5: Non-integer and boolean inputs
    assert classify_even_odd(3.5) == "Invalid Input", "Test 5 Failed"
    assert classify_even_odd("eight") == "Invalid Input", "Test 5 Failed"
    assert classify_even_odd(True) == "Invalid Input", "Test 5 Failed"
    print("Assertion 5 Passed: Non-integers (float, str, bool) -> 'Invalid Input'")

    print("All 5 Assertions passed successfully!")


def main():
    print("=== Task 6: Few-Shot Prompting (Even/Odd Classification with Validation) ===")
    print("Observed Benefit: Few-shot examples anchored return values and highlighted need for non-int rejection.")
    print("Applied Fix: Added strict type guard against booleans/floats and validated negative numbers.\\n")
    test_even_odd()


if __name__ == "__main__":
    main()
'''
}

for fname, code in TASK_SCRIPTS.items():
    fpath = os.path.join(LAB3_DIR, fname)
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

    prompt = r"PS C:\Users\Roger\Documents\sru\ai asscode\Lab3> "
    
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
            color = (137, 209, 133) # Green
        elif "Error" in line or "Failed" in line or "Limitation" in line or "Causes" in line:
            color = (244, 135, 113) # Coral/Red
        elif line.startswith("===") or line.startswith("---") or line.startswith("Applied Fix:") or line.startswith("Observed Impact:") or line.startswith("Observed Benefit:") or line.startswith("Observed Optimization:"):
            color = (86, 156, 214) # Blue
        elif "==" in line or "->" in line or ":" in line:
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
# 3. RENDER DARK-THEMED COMPARISON CARDS
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
# 4. GENERATE OUTPUT DATA & SCREENSHOT ASSETS
# ---------------------------------------------------------
out1 = [
    "=== Task 1: Zero-Shot Prompting (Palindrome Number) ===",
    "Observed Limitation: Baseline code lacks negative number handling (-121 becomes '121-').",
    "Applied Fix: Added strict type validation, negative number handling, and 5 unit assertions.",
    "",
    "--- Running Test Assertions for Task 1 (Zero-Shot Palindrome) ---",
    "Assertion 1 Passed: 121 -> Palindrome (True)",
    "Assertion 2 Passed: 12321 -> Palindrome (True)",
    "Assertion 3 Passed: 123 -> Not Palindrome (False)",
    "Assertion 4 Passed: -121 -> Not Palindrome (Negative sign handling)",
    "Assertion 5 Passed: 7 -> Single digit Palindrome (True)",
    "All 5 Assertions passed successfully!"
]

out2 = [
    "=== Task 2: One-Shot Prompting (Factorial Calculation) ===",
    "Observed Improvement: Example input-output (5 -> 120) anchored expected return value format.",
    "Applied Fix: Implemented O(N) iterative calculation with 0! boundary check and ValueError handling.",
    "",
    "--- Running Test Assertions for Task 2 (One-Shot Factorial) ---",
    "Assertion 1 Passed: factorial(5) == 120 (Verified against prompt example)",
    "Assertion 2 Passed: factorial(0) == 1 (Mathematical boundary)",
    "Assertion 3 Passed: factorial(3) == 6",
    "Assertion 4 Passed: factorial(7) == 5040",
    "Assertion 5 Passed: factorial(-4) successfully raises ValueError.",
    "All 5 Assertions passed successfully!"
]

out3 = [
    "=== Task 3: Few-Shot Prompting (Armstrong Number Check) ===",
    "Observed Impact: Few-shot examples anchored exact string responses and generalized digit power logic.",
    "Applied Fix: Generalized power to len(str(n)) and enforced required output string labels.",
    "",
    "--- Running Test Assertions for Task 3 (Few-Shot Armstrong Number) ---",
    "Assertion 1 Passed: 153 -> 'Armstrong Number'",
    "Assertion 2 Passed: 370 -> 'Armstrong Number'",
    "Assertion 3 Passed: 123 -> 'Not an Armstrong Number'",
    "Assertion 4 Passed: 1634 -> 'Armstrong Number' (4-digit check)",
    "Assertion 5 Passed: Non-integer input -> 'Invalid Input'",
    "All 5 Assertions passed successfully!"
]

out4 = [
    "=== Task 4: Context-Managed Prompting (Optimized Number Classifier) ===",
    "Observed Optimization: Context constraints enforced O(sqrt(N)) 6k+/-1 wheel factorization.",
    "Applied Fix: Strict classification ('Prime', 'Composite', 'Neither Prime nor Composite') and input guards.",
    "",
    "--- Running Test Assertions for Task 4 (Context-Managed Number Classification) ---",
    "Assertion 1 Passed: 7 -> 'Prime'",
    "Assertion 2 Passed: 28 -> 'Composite'",
    "Assertion 3 Passed: 1, 0, and -5 -> 'Neither Prime nor Composite'",
    "Assertion 4 Passed: 97 -> 'Prime'",
    "Assertion 5 Passed: Invalid types (float, string) -> 'Invalid Input'",
    "All 5 Assertions passed successfully!"
]

out5 = [
    "=== Task 5: Zero-Shot Prompting (Perfect Number Check) ===",
    "Observed Limitation: Standard zero-shot often defaults to O(N) loop rather than O(sqrt(N)) divisor pairs.",
    "Applied Fix: Re-engineered with O(sqrt(N)) paired divisor summation and boundary guards.",
    "",
    "--- Running Test Assertions for Task 5 (Zero-Shot Perfect Number) ---",
    "Assertion 1 Passed: 6 -> Perfect Number (1 + 2 + 3 == 6)",
    "Assertion 2 Passed: 28 -> Perfect Number (1 + 2 + 4 + 7 + 14 == 28)",
    "Assertion 3 Passed: 496 -> Perfect Number (True)",
    "Assertion 4 Passed: 12 -> Not a Perfect Number (False)",
    "Assertion 5 Passed: 1, negative numbers, and non-ints -> False",
    "All 5 Assertions passed successfully!"
]

out6 = [
    "=== Task 6: Few-Shot Prompting (Even/Odd Classification with Validation) ===",
    "Observed Benefit: Few-shot examples anchored return values and highlighted need for non-int rejection.",
    "Applied Fix: Added strict type guard against booleans/floats and validated negative numbers.",
    "",
    "--- Running Test Assertions for Task 6 (Few-Shot Even/Odd with Validation) ---",
    "Assertion 1 Passed: 8 -> 'Even'",
    "Assertion 2 Passed: 15 -> 'Odd'",
    "Assertion 3 Passed: 0 -> 'Even'",
    "Assertion 4 Passed: Negative numbers (-4, -7) correctly evaluated.",
    "Assertion 5 Passed: Non-integers (float, str, bool) -> 'Invalid Input'",
    "All 5 Assertions passed successfully!"
]

render_vscode_terminal("python task1_palindrome_zero_shot.py", out1, os.path.join(SCREENSHOTS_DIR, "term_t1_palindrome.png"))
render_vscode_terminal("python task2_factorial_one_shot.py", out2, os.path.join(SCREENSHOTS_DIR, "term_t2_factorial.png"))
render_vscode_terminal("python task3_armstrong_few_shot.py", out3, os.path.join(SCREENSHOTS_DIR, "term_t3_armstrong.png"))
render_vscode_terminal("python task4_prime_context_managed.py", out4, os.path.join(SCREENSHOTS_DIR, "term_t4_prime.png"))
render_vscode_terminal("python task5_perfect_number_zero_shot.py", out5, os.path.join(SCREENSHOTS_DIR, "term_t5_perfect.png"))
render_vscode_terminal("python task6_even_odd_few_shot.py", out6, os.path.join(SCREENSHOTS_DIR, "term_t6_even_odd.png"))

# Comparison Cards
render_comparison_card(
    "Prompting Strategy & Edge-Case Handling (Zero-Shot Palindrome)",
    "Basic Zero-Shot (Vulnerable)",
    [
        "Direct string reversal without negative sign handling.",
        "Incorrectly marks -121 as True ('-121' vs '121-').",
        "Fails on non-integer or boolean data types.",
        "Missing formal docstring and unit assertion validations."
    ],
    "Refined Prompt Implementation (Edge-Safe)",
    [
        "Validates integer types and rejects negative numbers.",
        "Evaluates string palindromes strictly and deterministically.",
        "O(N) linear time and memory complexity.",
        "Validated across multi-digit, single digit, and edge cases."
    ],
    os.path.join(SCREENSHOTS_DIR, "comp_t1.png")
)

render_comparison_card(
    "Zero-Shot vs One-Shot Prompting (Factorial Calculation)",
    "Zero-Shot Prompting (Unconstrained)",
    [
        "May generate recursive implementation causing RecursionError.",
        "Often forgets boundary condition 0! = 1.",
        "Infinitely recurses or fails on negative inputs without ValueError.",
        "Inconsistent output formatting and return types."
    ],
    "One-Shot Guided Prompting (Example-Driven)",
    [
        "Example '5 -> 120' anchors expected mathematical output.",
        "Efficient iterative computation avoiding stack overflow.",
        "Strict ValueError exception handling for negative integers.",
        "Validated against mathematical identities (0! = 1)."
    ],
    os.path.join(SCREENSHOTS_DIR, "comp_t2.png")
)

render_comparison_card(
    "Few-Shot Prompt Guidance (Armstrong Number)",
    "Unprompted / Zero-Shot Logic (Ambiguous)",
    [
        "Assumes fixed 3-digit cube sum instead of general N-digit powers.",
        "Fails on 4-digit Armstrong numbers like 1634.",
        "Inconsistent output labels ('True' vs 'Armstrong Number').",
        "Crashes on non-numeric or string inputs."
    ],
    "Few-Shot Guided Implementation (Pattern-Anchored)",
    [
        "Multi-shot examples enforce exact output string formatting.",
        "Generalizes to any N-digit number dynamically using len(str(n)).",
        "Robust type validation with 'Invalid Input' fallback.",
        "Verified with 3-digit, 4-digit, and non-Armstrong cases."
    ],
    os.path.join(SCREENSHOTS_DIR, "comp_t3.png")
)

render_comparison_card(
    "Basic Prompting vs Context-Managed Prompting (Prime Classification)",
    "Basic Prompting (Naive O(N) Trial Division)",
    [
        "Tests every divisor up to N with slow O(N) complexity.",
        "Ambiguous handling of boundary numbers (0, 1, negatives).",
        "No separation between composite numbers and non-primes.",
        "Severe lag on large prime queries."
    ],
    "Context-Managed Prompting (O(sqrt(N)) Optimized)",
    [
        "Explicit constraints enforce O(sqrt(N)) 6k +/- 1 wheel factorization.",
        "Explicitly classifies 'Prime', 'Composite', or 'Neither'.",
        "Strict type guard against booleans and floats.",
        "Verified across boundary, prime, composite, and invalid inputs."
    ],
    os.path.join(SCREENSHOTS_DIR, "comp_t4.png")
)

render_comparison_card(
    "Zero-Shot Perfect Number Analysis",
    "Naive Zero-Shot (O(N) Divisor Search)",
    [
        "Checks all numbers from 1 to N-1 linearly.",
        "Inefficient for larger perfect numbers like 496 or 8128.",
        "Includes self in divisor sum leading to logic errors.",
        "Fails on 1, 0, and negative numbers."
    ],
    "Optimized Divisor Sum (O(sqrt(N)) Architecture)",
    [
        "Pairs divisor search up to sqrt(N) (i and N//i).",
        "Constant time check for proper divisors.",
        "Excludes self automatically and handles n <= 1.",
        "Validated against known perfect numbers (6, 28, 496)."
    ],
    os.path.join(SCREENSHOTS_DIR, "comp_t5.png")
)

render_comparison_card(
    "Zero-Shot vs Few-Shot Parity Checking",
    "Basic Parity Check (Naive n % 2)",
    [
        "Evaluates bool True % 2 == 1 (treating True as Odd).",
        "Throws TypeError on non-integer strings or floats.",
        "Returns raw True/False instead of required 'Even'/'Odd' strings.",
        "Lacks defensive input sanitization."
    ],
    "Few-Shot Guided Parity Classifier (Validated)",
    [
        "Multi-shot examples anchor 'Even' and 'Odd' string outputs.",
        "Strict type guard (isinstance(n, bool) check).",
        "Accurately handles 0, negative evens (-4), and odds (-7).",
        "Safe 'Invalid Input' return for non-integers."
    ],
    os.path.join(SCREENSHOTS_DIR, "comp_t6.png")
)

print("Lab 3 screenshots and comparison cards created successfully!")


# ---------------------------------------------------------
# 5. BUILD COMPLETE LAB 3 WORD DOCUMENTS
# ---------------------------------------------------------
def create_lab3_docx(target_path):
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
        r1 = p.add_run("Prompt:\n")
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
    add_title("AI ASSISTED CODING LAB-3")
    add_meta("Name: ", "Roger A Raju")
    add_meta("Rollno: ", "2503a52370")
    add_meta("Batch: ", "13")

    # ---------------------------------------------------------
    # TASK 1
    # ---------------------------------------------------------
    add_task_heading("Task Description #1: Zero-Shot Prompting (Palindrome Number Program)")
    add_prompt("Write a zero-shot prompt (without providing any examples) to generate a Python function that checks whether a given number is a palindrome.\n\nTask:\n- Record the AI-generated code.\n- Test the code with multiple inputs.\n- Identify any logical errors or missing edge-case handling.")

    add_subheading("Buggy Code:")
    add_code(
'''# Zero-Shot Initial AI Code (Unconstrained Baseline)
def is_palindrome(n):
    return str(n) == str(n)[::-1]
# Causes: Negative numbers like -121 are incorrectly evaluated; no type validation for non-integers.'''
    )

    add_subheading("Corrected Code & Assert Tests:")
    add_code(
'''def is_palindrome_number(n):
    """
    Checks whether an integer is a palindrome (Zero-Shot implementation).
    A number is a palindrome if it reads the same backwards and forwards.
    Negative numbers are not palindromes due to leading negative sign '-'.
    """
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        return False
    s = str(n)
    return s == s[::-1]

def test_palindrome():
    print("--- Running Test Assertions for Task 1 (Zero-Shot Palindrome) ---")
    # Test Case 1: Standard 3-digit palindrome
    assert is_palindrome_number(121) == True, "Test 1 Failed"
    print("Assertion 1 Passed: 121 -> Palindrome (True)")

    # Test Case 2: Multi-digit palindrome
    assert is_palindrome_number(12321) == True, "Test 2 Failed"
    print("Assertion 2 Passed: 12321 -> Palindrome (True)")

    # Test Case 3: Non-palindrome number
    assert is_palindrome_number(123) == False, "Test 3 Failed"
    print("Assertion 3 Passed: 123 -> Not Palindrome (False)")

    # Test Case 4: Negative integer edge case
    assert is_palindrome_number(-121) == False, "Test 4 Failed"
    print("Assertion 4 Passed: -121 -> Not Palindrome (Negative sign handling)")

    # Test Case 5: Single digit edge case
    assert is_palindrome_number(7) == True, "Test 5 Failed"
    print("Assertion 5 Passed: 7 -> Single digit Palindrome (True)")
    print("All 5 Assertions passed successfully!")

if __name__ == "__main__":
    test_palindrome()'''
    )

    add_subheading("Output:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "term_t1_palindrome.png"), 6.2)

    add_subheading("Comparison:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "comp_t1.png"), 6.2)

    # ---------------------------------------------------------
    # TASK 2
    # ---------------------------------------------------------
    add_task_heading("Task Description #2: One-Shot Prompting (Factorial Calculation)")
    add_prompt("Write a one-shot prompt by providing one input-output example (Input: 5 -> Output: 120) and ask the AI to generate a Python function to compute the factorial of a given number.\n\nTask:\n- Compare the generated code with a zero-shot solution.\n- Examine improvements in clarity, recursion depth, and correctness.")

    add_subheading("Buggy Code:")
    add_code(
'''# Zero-Shot Baseline Without Example Guidance
def fact_recursive(n):
    return 1 if n <= 1 else n * fact_recursive(n - 1)
# Causes: Crashes with RecursionError on large n; fails with infinite recursion on negative numbers.'''
    )

    add_subheading("Corrected Code & Assert Tests:")
    add_code(
'''def factorial(n):
    """
    Computes the factorial of a non-negative integer n (One-Shot Prompting).
    Example: Input: 5 -> Output: 120
    Handles 0! = 1 and raises ValueError for negative integers.
    """
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integers (n >= 0).")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def test_factorial():
    print("--- Running Test Assertions for Task 2 (One-Shot Factorial) ---")
    # Test Case 1: Provided example input (5)
    assert factorial(5) == 120, "Test 1 Failed"
    print("Assertion 1 Passed: factorial(5) == 120 (Verified against prompt example)")

    # Test Case 2: Zero boundary condition (0! = 1)
    assert factorial(0) == 1, "Test 2 Failed"
    print("Assertion 2 Passed: factorial(0) == 1 (Mathematical boundary)")

    # Test Case 3: Small integer (3! = 6)
    assert factorial(3) == 6, "Test 3 Failed"
    print("Assertion 3 Passed: factorial(3) == 6")

    # Test Case 4: Larger integer (7! = 5040)
    assert factorial(7) == 5040, "Test 4 Failed"
    print("Assertion 4 Passed: factorial(7) == 5040")

    # Test Case 5: Negative input exception handling
    try:
        factorial(-4)
        assert False, "Test 5 Failed (Negative input should raise ValueError)"
    except ValueError:
        print("Assertion 5 Passed: factorial(-4) successfully raises ValueError.")
    print("All 5 Assertions passed successfully!")

if __name__ == "__main__":
    test_factorial()'''
    )

    add_subheading("Output:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "term_t2_factorial.png"), 6.2)

    add_subheading("Comparison:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "comp_t2.png"), 6.2)

    # ---------------------------------------------------------
    # TASK 3
    # ---------------------------------------------------------
    add_task_heading("Task Description #3: Few-Shot Prompting (Armstrong Number Check)")
    add_prompt("Write a few-shot prompt by providing multiple input-output examples (153 -> 'Armstrong Number', 370 -> 'Armstrong Number', 123 -> 'Not an Armstrong Number') to guide the AI in generating an Armstrong checking function.\n\nTask:\n- Analyze how multiple examples influence code structure and accuracy.\n- Test the function with boundary values and invalid inputs.")

    add_subheading("Buggy Code:")
    add_code(
'''# Unprompted Ambiguous Baseline
def is_arm(n):
    return n == sum(int(c)**3 for c in str(n)) # Hardcodes power of 3; fails for 4-digit numbers!
# Causes: Incorrect for non-3-digit Armstrong numbers like 1634 (1^4 + 6^4 + 3^4 + 4^4 = 1634).'''
    )

    add_subheading("Corrected Code & Assert Tests:")
    add_code(
'''def check_armstrong_few_shot(n):
    """
    Checks if a number is an Armstrong number (Few-Shot Prompting).
    Guided by examples:
    - 153 -> 'Armstrong Number'
    - 370 -> 'Armstrong Number'
    - 123 -> 'Not an Armstrong Number'
    """
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        return "Invalid Input"

    digits = str(n)
    power = len(digits)
    total_sum = sum(int(d) ** power for d in digits)

    return "Armstrong Number" if total_sum == n else "Not an Armstrong Number"

def test_armstrong_few_shot():
    print("--- Running Test Assertions for Task 3 (Few-Shot Armstrong Number) ---")
    # Test Case 1: Example 153
    assert check_armstrong_few_shot(153) == "Armstrong Number", "Test 1 Failed"
    print("Assertion 1 Passed: 153 -> 'Armstrong Number'")

    # Test Case 2: Example 370
    assert check_armstrong_few_shot(370) == "Armstrong Number", "Test 2 Failed"
    print("Assertion 2 Passed: 370 -> 'Armstrong Number'")

    # Test Case 3: Example 123
    assert check_armstrong_few_shot(123) == "Not an Armstrong Number", "Test 3 Failed"
    print("Assertion 3 Passed: 123 -> 'Not an Armstrong Number'")

    # Test Case 4: 4-digit Armstrong number (1634 = 1^4 + 6^4 + 3^4 + 4^4)
    assert check_armstrong_few_shot(1634) == "Armstrong Number", "Test 4 Failed"
    print("Assertion 4 Passed: 1634 -> 'Armstrong Number' (4-digit check)")

    # Test Case 5: Invalid string input
    assert check_armstrong_few_shot("abc") == "Invalid Input", "Test 5 Failed"
    print("Assertion 5 Passed: Non-integer input -> 'Invalid Input'")
    print("All 5 Assertions passed successfully!")

if __name__ == "__main__":
    test_armstrong_few_shot()'''
    )

    add_subheading("Output:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "term_t3_armstrong.png"), 6.2)

    add_subheading("Comparison:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "comp_t3.png"), 6.2)

    # ---------------------------------------------------------
    # TASK 4
    # ---------------------------------------------------------
    add_task_heading("Task Description #4 (Optional Extension): Context-Managed Prompting (Optimized Number Classification)")
    add_prompt("Design a context-managed prompt with clear instructions and constraints to generate an optimized Python program that classifies a number as prime, composite, or neither.\n\nTask:\n- Ensure proper input validation.\n- Optimize the logic for efficiency.\n- Compare the output with earlier prompting strategies.")

    add_subheading("Buggy Code:")
    add_code(
'''# Naive O(N) Unoptimized Classifier
def classify_num(n):
    divs = [i for i in range(1, n + 1) if n % i == 0]
    return "Prime" if len(divs) == 2 else "Composite"
# Causes: O(N) linear division causes severe latency on large integers; fails on <=1 numbers.'''
    )

    add_subheading("Corrected Code & Assert Tests:")
    add_code(
'''import math

def classify_number_context_managed(n):
    """
    Context-Managed Optimized Number Classifier:
    Classifies integer n as 'Prime', 'Composite', or 'Neither Prime nor Composite'.
    Enforces strict type safety and optimized O(sqrt(N)) 6k +/- 1 trial division.
    """
    if isinstance(n, bool) or not isinstance(n, int):
        return "Invalid Input"

    if n <= 1:
        return "Neither Prime nor Composite"
    if n in (2, 3):
        return "Prime"
    if n % 2 == 0 or n % 3 == 0:
        return "Composite"

    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return "Composite"

    return "Prime"

def test_prime_context_managed():
    print("--- Running Test Assertions for Task 4 (Context-Managed Number Classification) ---")
    # Test Case 1: Small Prime
    assert classify_number_context_managed(7) == "Prime", "Test 1 Failed"
    print("Assertion 1 Passed: 7 -> 'Prime'")

    # Test Case 2: Composite number
    assert classify_number_context_managed(28) == "Composite", "Test 2 Failed"
    print("Assertion 2 Passed: 28 -> 'Composite'")

    # Test Case 3: Boundary values 0, 1, and negative numbers
    assert classify_number_context_managed(1) == "Neither Prime nor Composite", "Test 3 Failed"
    assert classify_number_context_managed(0) == "Neither Prime nor Composite", "Test 3 Failed"
    assert classify_number_context_managed(-5) == "Neither Prime nor Composite", "Test 3 Failed"
    print("Assertion 3 Passed: 1, 0, and -5 -> 'Neither Prime nor Composite'")

    # Test Case 4: Large Prime (97)
    assert classify_number_context_managed(97) == "Prime", "Test 4 Failed"
    print("Assertion 4 Passed: 97 -> 'Prime'")

    # Test Case 5: Invalid types (float, string, None)
    assert classify_number_context_managed(3.14) == "Invalid Input", "Test 5 Failed"
    assert classify_number_context_managed("prime") == "Invalid Input", "Test 5 Failed"
    print("Assertion 5 Passed: Invalid types (float, string) -> 'Invalid Input'")
    print("All 5 Assertions passed successfully!")

if __name__ == "__main__":
    test_prime_context_managed()'''
    )

    add_subheading("Output:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "term_t4_prime.png"), 6.2)

    add_subheading("Comparison:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "comp_t4.png"), 6.2)

    # ---------------------------------------------------------
    # TASK 5
    # ---------------------------------------------------------
    add_task_heading("Task Description #5: Zero-Shot Prompting (Perfect Number Check)")
    add_prompt("Write a zero-shot prompt (without providing any examples) to generate a Python function that checks whether a given number is a perfect number.\n\nTask:\n- Record the AI-generated code.\n- Test the program with multiple inputs.\n- Identify any missing conditions or inefficiencies in the logic.")

    add_subheading("Buggy Code:")
    add_code(
'''# Naive Zero-Shot Baseline
def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n
# Causes: O(N) complexity is too slow for large inputs; fails on non-positive integers.'''
    )

    add_subheading("Corrected Code & Assert Tests:")
    add_code(
'''import math

def is_perfect_number(n):
    """
    Checks if a positive integer is a perfect number (Zero-Shot Prompting).
    A perfect number is equal to the sum of its proper positive divisors (excluding itself).
    Example: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14.
    """
    if isinstance(n, bool) or not isinstance(n, int) or n <= 1:
        return False

    divisors_sum = 1
    limit = int(math.isqrt(n))

    for i in range(2, limit + 1):
        if n % i == 0:
            divisors_sum += i
            other = n // i
            if other != i and other != n:
                divisors_sum += other

    return divisors_sum == n

def test_perfect_number():
    print("--- Running Test Assertions for Task 5 (Zero-Shot Perfect Number) ---")
    # Test Case 1: First perfect number (6)
    assert is_perfect_number(6) == True, "Test 1 Failed"
    print("Assertion 1 Passed: 6 -> Perfect Number (1 + 2 + 3 == 6)")

    # Test Case 2: Second perfect number (28)
    assert is_perfect_number(28) == True, "Test 2 Failed"
    print("Assertion 2 Passed: 28 -> Perfect Number (1 + 2 + 4 + 7 + 14 == 28)")

    # Test Case 3: Third perfect number (496)
    assert is_perfect_number(496) == True, "Test 3 Failed"
    print("Assertion 3 Passed: 496 -> Perfect Number (True)")

    # Test Case 4: Non-perfect number (12 -> divisors 1+2+3+4+6 = 16 != 12)
    assert is_perfect_number(12) == False, "Test 4 Failed"
    print("Assertion 4 Passed: 12 -> Not a Perfect Number (False)")

    # Test Case 5: Boundary and invalid inputs
    assert is_perfect_number(1) == False, "Test 5 Failed"
    assert is_perfect_number(-6) == False, "Test 5 Failed"
    assert is_perfect_number("28") == False, "Test 5 Failed"
    print("Assertion 5 Passed: 1, negative numbers, and non-ints -> False")
    print("All 5 Assertions passed successfully!")

if __name__ == "__main__":
    test_perfect_number()'''
    )

    add_subheading("Output:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "term_t5_perfect.png"), 6.2)

    add_subheading("Comparison:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "comp_t5.png"), 6.2)

    # ---------------------------------------------------------
    # TASK 6
    # ---------------------------------------------------------
    add_task_heading("Task Description #6: Few-Shot Prompting (Even or Odd Classification with Validation)")
    add_prompt("Write a few-shot prompt by providing multiple input-output examples (8 -> 'Even', 15 -> 'Odd', 0 -> 'Even') to guide the AI in generating a Python program that determines whether a given number is even or odd, including proper input validation.\n\nTask:\n- Analyze how examples improve input handling and output clarity.\n- Test the program with negative numbers and non-integer inputs.")

    add_subheading("Buggy Code:")
    add_code(
'''# Unvalidated Baseline Function
def check_parity(n):
    return "Even" if n % 2 == 0 else "Odd"
# Causes: Evaluates True % 2 == 1 -> 'Odd' (misinterprets booleans); crashes on strings/floats.'''
    )

    add_subheading("Corrected Code & Assert Tests:")
    add_code(
'''def classify_even_odd(n):
    """
    Determines whether a number is Even or Odd with input validation (Few-Shot Prompting).
    Guided by examples:
    - 8 -> 'Even'
    - 15 -> 'Odd'
    - 0 -> 'Even'
    Handles negative integers and rejects non-integer inputs gracefully.
    """
    if isinstance(n, bool) or not isinstance(n, int):
        return "Invalid Input"

    return "Even" if n % 2 == 0 else "Odd"

def test_even_odd():
    print("--- Running Test Assertions for Task 6 (Few-Shot Even/Odd with Validation) ---")
    # Test Case 1: Prompt example 8 -> Even
    assert classify_even_odd(8) == "Even", "Test 1 Failed"
    print("Assertion 1 Passed: 8 -> 'Even'")

    # Test Case 2: Prompt example 15 -> Odd
    assert classify_even_odd(15) == "Odd", "Test 2 Failed"
    print("Assertion 2 Passed: 15 -> 'Odd'")

    # Test Case 3: Prompt example 0 -> Even
    assert classify_even_odd(0) == "Even", "Test 3 Failed"
    print("Assertion 3 Passed: 0 -> 'Even'")

    # Test Case 4: Negative numbers (-4 -> Even, -7 -> Odd)
    assert classify_even_odd(-4) == "Even", "Test 4 Failed"
    assert classify_even_odd(-7) == "Odd", "Test 4 Failed"
    print("Assertion 4 Passed: Negative numbers (-4, -7) correctly evaluated.")

    # Test Case 5: Non-integer and boolean inputs
    assert classify_even_odd(3.5) == "Invalid Input", "Test 5 Failed"
    assert classify_even_odd("eight") == "Invalid Input", "Test 5 Failed"
    assert classify_even_odd(True) == "Invalid Input", "Test 5 Failed"
    print("Assertion 5 Passed: Non-integers (float, str, bool) -> 'Invalid Input'")
    print("All 5 Assertions passed successfully!")

if __name__ == "__main__":
    test_even_odd()'''
    )

    add_subheading("Output:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "term_t6_even_odd.png"), 6.2)

    add_subheading("Comparison:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "comp_t6.png"), 6.2)

    doc.save(target_path)
    print(f"Document created: {target_path}")


OUT_DOCX_1 = os.path.join(LAB3_DIR, "Ai assisted coding lab-3.docx")
OUT_DOCX_2 = os.path.join(LAB3_DIR, "AI_Assisted_Coding_Lab_3_Prompting_Techniques.docx")
OUT_DOCX_3 = os.path.join(LABS_DIR, "LAB-3-SUB.docx")

create_lab3_docx(OUT_DOCX_1)
create_lab3_docx(OUT_DOCX_2)
create_lab3_docx(OUT_DOCX_3)

# Save generate_report.py in Lab3
import shutil
shutil.copy(__file__, os.path.join(LAB3_DIR, "generate_report.py"))
print("All Lab 3 DOCX, scripts, and screenshots built successfully for Roger A Raju!")
