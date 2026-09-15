"""
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
    print("Applied Fix: Added strict type guard against booleans/floats and validated negative numbers.\n")
    test_even_odd()


if __name__ == "__main__":
    main()
