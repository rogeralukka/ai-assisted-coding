"""
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
    print("Applied Fix: Implemented O(N) iterative calculation with 0! boundary check and ValueError handling.\n")
    test_factorial()


if __name__ == "__main__":
    main()
