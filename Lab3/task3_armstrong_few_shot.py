"""
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
    print("Applied Fix: Generalized power to len(str(n)) and enforced required output string labels.\n")
    test_armstrong_few_shot()


if __name__ == "__main__":
    main()
