"""
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
    print("Testing standard values, boundaries (-1, 0, 1), and invalid types.\n")
    test_classify_number()


if __name__ == "__main__":
    main()
