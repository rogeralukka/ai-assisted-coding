"""
Task 2: Incorrect condition in an If Statement
AI Assisted Coding Lab 7.1

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

def check_number(n):
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

def main():
    print("=== Task 2: If Statement Assignment vs Comparison ===")
    print("Observed Bug: 'if n = 10:' raises SyntaxError because '=' is an assignment operator.")
    print("Applied Fix: Used equality operator '==' to evaluate equality.")
    print(f"Sample Run check_number(10): {check_number(10)}")
    print(f"Sample Run check_number(25): {check_number(25)}\n")
    test_check_number()

if __name__ == "__main__":
    main()
