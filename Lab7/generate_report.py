import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = r"C:\Users\Roger\Documents\sru\ai asscode"
LAB7_DIR = os.path.join(BASE_DIR, "Lab7")
SCREENSHOTS_DIR = os.path.join(LAB7_DIR, "screenshots")
LABS_DIR = os.path.join(BASE_DIR, "LABS")
os.makedirs(LABS_DIR, exist_ok=True)

OUT_DOCX_1 = os.path.join(LAB7_DIR, "Ai assisted coding lab-7.docx")
OUT_DOCX_2 = os.path.join(LAB7_DIR, "AI_Assisted_Coding_Lab_7_Error_Debugging.docx")
OUT_DOCX_3 = os.path.join(LABS_DIR, "LAB-7-SUB.docx")

def create_lab7_docx(target_path):
    doc = docx.Document()

    # Set page margins (0.75 in)
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # ---------------------------------------------------------
    # Helper Functions
    # ---------------------------------------------------------
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
    add_title("AI ASSISTED CODING LAB-7")
    add_meta("Name: ", "Roger A Raju")
    add_meta("Rollno: ", "2503a52370")
    add_meta("Batch: ", "13")
    
    # ---------------------------------------------------------
    # TASK 1
    # ---------------------------------------------------------
    add_task_heading("Task Description #1 (Syntax Errors – Missing Parentheses in Print Statement)")
    add_prompt("Provide a Python snippet with a missing parenthesis in a print statement (e.g., print \"Hello\"). Use AI to detect and fix the syntax error, explain why it happens in Python 3, and confirm the fix using 3 assert test cases.")
    
    add_subheading("Buggy Code:")
    add_code(
'''# Bug: Missing parentheses in print statement
def greet():
    print "Hello, AI Debugging Lab!"

greet()
# Causes: SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)'''
    )
    
    add_subheading("Corrected Code & Assert Tests:")
    add_code(
'''def greet(name="AI Debugging Lab!"):
    """
    Corrected greet function using valid Python 3 print() syntax.
    In Python 3, print is a built-in function that requires parentheses.
    """
    message = f"Hello, {name}"
    print(message)
    return message

def test_greet():
    print("--- Running Test Assertions for Task 1 ---")
    # Test Case 1: Default lab greeting
    assert greet("AI Debugging Lab!") == "Hello, AI Debugging Lab!", "Test 1 Failed"
    print("Assertion 1 Passed: Default lab greeting verified.")

    # Test Case 2: Custom student name
    assert greet("Roger A Raju") == "Hello, Roger A Raju", "Test 2 Failed"
    print("Assertion 2 Passed: Student name greeting verified.")

    # Test Case 3: Course subject name
    assert greet("Python Programming") == "Hello, Python Programming", "Test 3 Failed"
    print("Assertion 3 Passed: Subject greeting verified.")
    print("All 3 Assertions passed successfully!")

if __name__ == "__main__":
    greet("AI Debugging Lab!")
    test_greet()'''
    )

    add_subheading("output:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "term_t1_syntax.png"), 6.2)

    add_subheading("Comparison:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "comp_t1.png"), 6.2)

    # ---------------------------------------------------------
    # TASK 2
    # ---------------------------------------------------------
    add_task_heading("Task Description #2 (Incorrect condition in an If Statement)")
    add_prompt("Supply a function where an if-condition mistakenly uses = instead of ==. Let AI identify and fix the issue, explain the difference between assignment and comparison operators, and verify with 3 assert test cases.")

    add_subheading("Buggy Code:")
    add_code(
'''# Bug: Using assignment (=) instead of comparison (==)
def check_number(n):
    if n = 10:
        return "Ten"
    else:
        return "Not Ten"
# Causes: SyntaxError: invalid syntax (cannot assign to literal or test clause)'''
    )

    add_subheading("Corrected Code & Assert Tests:")
    add_code(
'''def check_number(n):
    """
    Checks if a given number is equal to 10.
    Fix: Replaced assignment operator (=) with equality comparison operator (==).
    """
    if n == 10:
        return "Ten"
    else:
        return "Not Ten"

def test_check_number():
    print("--- Running Test Assertions for Task 2 ---")
    # Test Case 1: Exact match with 10
    assert check_number(10) == "Ten", "Test 1 Failed"
    print("Assertion 1 Passed: check_number(10) == 'Ten'")

    # Test Case 2: Non-matching positive number
    assert check_number(5) == "Not Ten", "Test 2 Failed"
    print("Assertion 2 Passed: check_number(5) == 'Not Ten'")

    # Test Case 3: Negative number
    assert check_number(-10) == "Not Ten", "Test 3 Failed"
    print("Assertion 3 Passed: check_number(-10) == 'Not Ten'")
    
    # Test Case 4: Floating point 10.0
    assert check_number(10.0) == "Ten", "Test 4 Failed"
    print("Assertion 4 Passed: check_number(10.0) == 'Ten'")
    print("All Assertions passed successfully!")

if __name__ == "__main__":
    test_check_number()'''
    )

    add_subheading("output:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "term_t2_if.png"), 6.2)

    add_subheading("Comparison:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "comp_t2.png"), 6.2)

    # ---------------------------------------------------------
    # TASK 3
    # ---------------------------------------------------------
    add_task_heading("Task Description #3 (Runtime Error – File Not Found)")
    add_prompt("Provide code that attempts to open a non-existent file and crashes. Use AI to apply safe error handling with a try-except block, add user-friendly error messages, and test with at least 3 scenarios: file exists, file missing, and invalid path.")

    add_subheading("Buggy Code:")
    add_code(
'''# Bug: Program crashes if file is missing
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

print(read_file("nonexistent.txt"))
# Causes: FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent.txt\''''
    )

    add_subheading("Corrected Code & Scenario Tests:")
    add_code(
'''import os

def read_file(filename):
    """
    Safely reads file contents using try-except to handle FileNotFoundError
    and other I/O exceptions gracefully without crashing.
    """
    if not filename or not isinstance(filename, str):
        return "Error: Invalid filename provided."
        
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found. Please verify the file path."
    except PermissionError:
        return f"Error: Permission denied while attempting to read '{filename}'."
    except IsADirectoryError:
        return f"Error: '{filename}' is a directory, not a readable file."
    except Exception as e:
        return f"Error: An unexpected error occurred while reading '{filename}': {str(e)}"

def test_file_scenarios():
    print("--- Running Test Scenarios for Task 3 ---")
    test_filename = "sample_test.txt"
    
    # Scenario 1: File exists
    with open(test_filename, "w", encoding="utf-8") as f:
        f.write("SRU University - AI Assisted Coding Lab 7 File Content")
    content = read_file(test_filename)
    assert "SRU University" in content, "Scenario 1 Failed"
    print(f"Scenario 1 (File Exists): Success -> Content: '{content}'")
    if os.path.exists(test_filename):
        os.remove(test_filename)

    # Scenario 2: File missing
    missing_res = read_file("nonexistent.txt")
    assert "was not found" in missing_res, "Scenario 2 Failed"
    print(f"Scenario 2 (File Missing): Handled Gracefully -> '{missing_res}'")

    # Scenario 3: Invalid path / Empty filename
    invalid_res = read_file("")
    assert "Error: Invalid filename" in invalid_res, "Scenario 3 Failed"
    print(f"Scenario 3 (Invalid Filename): Handled Gracefully -> '{invalid_res}'")
    print("All 3 Scenarios tested and verified successfully!")

if __name__ == "__main__":
    test_file_scenarios()'''
    )

    add_subheading("output:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "term_t3_file.png"), 6.2)

    add_subheading("Comparison:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "comp_t3.png"), 6.2)

    # ---------------------------------------------------------
    # TASK 4
    # ---------------------------------------------------------
    add_task_heading("Task Description #4 (Calling a Non-Existent Method)")
    add_prompt("Give a class where a non-existent method is called (e.g., obj.undefined_method()). Use AI to debug, analyze whether to define the missing method or correct the method call, and verify with 3 assert test cases.")

    add_subheading("Buggy Code:")
    add_code(
'''# Bug: Calling an undefined method
class Car:
    def start(self):
        return "Car started"

my_car = Car()
print(my_car.drive()) # drive() is not defined
# Causes: AttributeError: 'Car' object has no attribute 'drive\''''
    )

    add_subheading("Corrected Code & Assert Tests:")
    add_code(
'''class Car:
    """
    Comprehensive Car class providing start, drive, and stop methods.
    Addresses both fixing the missing method definition and properly calling existing methods.
    """
    def __init__(self, brand="Tesla", model="Model 3"):
        self.brand = brand
        self.model = model
        self.is_running = False
        self.speed = 0

    def start(self):
        """Starts the car engine."""
        self.is_running = True
        return f"{self.brand} {self.model}: Car started"

    def drive(self, target_speed=40):
        """
        Defines the previously missing drive() method.
        Automatically starts the car if not already running and sets speed.
        """
        if not self.is_running:
            self.start()
        self.speed = target_speed
        return f"{self.brand} {self.model}: Car is driving at {self.speed} km/h"

    def stop(self):
        """Stops the car and resets speed."""
        self.is_running = False
        self.speed = 0
        return f"{self.brand} {self.model}: Car stopped"

def test_car_methods():
    print("--- Running Test Assertions for Task 4 ---")
    my_car = Car("Tesla", "Model 3")

    # Test Case 1: Testing start() method
    assert my_car.start() == "Tesla Model 3: Car started", "Test 1 Failed"
    print("Assertion 1 Passed: my_car.start() -> 'Tesla Model 3: Car started'")

    # Test Case 2: Testing drive() method (previously undefined method)
    assert my_car.drive(60) == "Tesla Model 3: Car is driving at 60 km/h", "Test 2 Failed"
    print("Assertion 2 Passed: my_car.drive(60) -> 'Tesla Model 3: Car is driving at 60 km/h'")

    # Test Case 3: Testing stop() method
    assert my_car.stop() == "Tesla Model 3: Car stopped", "Test 3 Failed"
    print("Assertion 3 Passed: my_car.stop() -> 'Tesla Model 3: Car stopped'")
    print("All Assertions passed successfully!")

if __name__ == "__main__":
    test_car_methods()'''
    )

    add_subheading("output:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "term_t4_method.png"), 6.2)

    add_subheading("Comparison:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "comp_t4.png"), 6.2)

    # ---------------------------------------------------------
    # TASK 5
    # ---------------------------------------------------------
    add_task_heading("Task Description #5 (TypeError – Mixing Strings and Integers in Addition)")
    add_prompt("Provide code that adds an integer and string (\"5\" + 2) causing a TypeError. Use AI to resolve the bug providing two solutions: type casting (numeric addition) and string concatenation, validated with 3 assert test cases.")

    add_subheading("Buggy Code:")
    add_code(
'''# Bug: TypeError due to mixing string and integer
def add_five(value):
    return value + 5

print(add_five("10"))
# Causes: TypeError: can only concatenate str (not "int") to str OR unsupported operand type(s)'''
    )

    add_subheading("Corrected Code & Dual-Solution Assert Tests:")
    add_code(
'''def add_five_numeric(value):
    """
    Solution 1: Type Casting to Numeric (Integer)
    Converts input string or number to integer before adding 5.
    """
    return int(value) + 5

def add_five_string(value):
    """
    Solution 2: String Concatenation
    Converts number or input to string and concatenates '5'.
    """
    return str(value) + "5"

def test_type_error_solutions():
    print("--- Running Test Assertions for Task 5 ---")
    
    # Solution 1 Assertions (Type Casting - Numeric Addition)
    print("[Solution 1: Numeric Addition (Type Casting)]")
    assert add_five_numeric("10") == 15, "Numeric Test 1 Failed"
    print("Assertion 1 Passed: add_five_numeric('10') == 15")
    assert add_five_numeric(20) == 25, "Numeric Test 2 Failed"
    print("Assertion 2 Passed: add_five_numeric(20) == 25")
    assert add_five_numeric("-5") == 0, "Numeric Test 3 Failed"
    print("Assertion 3 Passed: add_five_numeric('-5') == 0")

    # Solution 2 Assertions (String Concatenation)
    print("\\n[Solution 2: String Concatenation]")
    assert add_five_string("10") == "105", "String Test 1 Failed"
    print("Assertion 4 Passed: add_five_string('10') == '105'")
    assert add_five_string(20) == "205", "String Test 2 Failed"
    print("Assertion 5 Passed: add_five_string(20) == '205'")
    assert add_five_string("SRU_") == "SRU_5", "String Test 3 Failed"
    print("Assertion 6 Passed: add_five_string('SRU_') == 'SRU_5'")
    print("All 6 Assertions passed successfully across both solutions!")

if __name__ == "__main__":
    test_type_error_solutions()'''
    )

    add_subheading("output:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "term_t5_type.png"), 6.2)

    add_subheading("Comparison:")
    add_image_centered(os.path.join(SCREENSHOTS_DIR, "comp_t5.png"), 6.2)

    # Save
    doc.save(target_path)
    print(f"Document successfully created at: {target_path}")

create_lab7_docx(OUT_DOCX_1)
create_lab7_docx(OUT_DOCX_2)
create_lab7_docx(OUT_DOCX_3)
print("All DOCX documents built successfully!")
