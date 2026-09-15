"""
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
    print("Applied Fix: Added strict type validation, negative number handling, and 5 unit assertions.\n")
    test_palindrome()


if __name__ == "__main__":
    main()
