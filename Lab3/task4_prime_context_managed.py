"""
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
    print("Applied Fix: Strict classification ('Prime', 'Composite', 'Neither Prime nor Composite') and input guards.\n")
    test_prime_context_managed()


if __name__ == "__main__":
    main()
