"""
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
    print("Security Policy: Length >= 8, Letters, Digits, Special Characters, No Spaces.\n")
    test_password_strength()


if __name__ == "__main__":
    main()
