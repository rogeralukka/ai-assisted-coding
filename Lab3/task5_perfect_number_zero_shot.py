"""
Task 5: Zero-Shot Prompting (Perfect Number Check)
AI Assisted Coding Lab 3

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

import math

def is_perfect_number(n):
    """
    Checks if a positive integer is a perfect number (Zero-Shot Prompting).
    A perfect number is equal to the sum of its proper positive divisors (excluding itself).
    Example: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14.
    """
    if isinstance(n, bool) or not isinstance(n, int) or n <= 1:
        return False

    divisors_sum = 1
    limit = int(math.isqrt(n))

    for i in range(2, limit + 1):
        if n % i == 0:
            divisors_sum += i
            other = n // i
            if other != i and other != n:
                divisors_sum += other

    return divisors_sum == n


def test_perfect_number():
    print("--- Running Test Assertions for Task 5 (Zero-Shot Perfect Number) ---")
    
    # Test Case 1: First perfect number (6)
    assert is_perfect_number(6) == True, "Test 1 Failed"
    print("Assertion 1 Passed: 6 -> Perfect Number (1 + 2 + 3 == 6)")

    # Test Case 2: Second perfect number (28)
    assert is_perfect_number(28) == True, "Test 2 Failed"
    print("Assertion 2 Passed: 28 -> Perfect Number (1 + 2 + 4 + 7 + 14 == 28)")

    # Test Case 3: Third perfect number (496)
    assert is_perfect_number(496) == True, "Test 3 Failed"
    print("Assertion 3 Passed: 496 -> Perfect Number (True)")

    # Test Case 4: Non-perfect number (12 -> divisors 1+2+3+4+6 = 16 != 12)
    assert is_perfect_number(12) == False, "Test 4 Failed"
    print("Assertion 4 Passed: 12 -> Not a Perfect Number (False)")

    # Test Case 5: Boundary and invalid inputs
    assert is_perfect_number(1) == False, "Test 5 Failed"
    assert is_perfect_number(-6) == False, "Test 5 Failed"
    assert is_perfect_number("28") == False, "Test 5 Failed"
    print("Assertion 5 Passed: 1, negative numbers, and non-ints -> False")

    print("All 5 Assertions passed successfully!")


def main():
    print("=== Task 5: Zero-Shot Prompting (Perfect Number Check) ===")
    print("Observed Limitation: Standard zero-shot often defaults to O(N) loop rather than O(sqrt(N)) divisor pairs.")
    print("Applied Fix: Re-engineered with O(sqrt(N)) paired divisor summation and boundary guards.\n")
    test_perfect_number()


if __name__ == "__main__":
    main()
