"""
Task 3: Runtime Error – File Not Found
AI Assisted Coding Lab 7.1

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

import os

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
    
    # Clean up test file
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

def main():
    print("=== Task 3: Safe File Handling with Try-Except ===")
    print("Observed Bug: Opening missing files throws unhandled FileNotFoundError and crashes.")
    print("Applied Fix: Wrapped file I/O in try-except block with user-friendly error messages.\n")
    test_file_scenarios()

if __name__ == "__main__":
    main()
