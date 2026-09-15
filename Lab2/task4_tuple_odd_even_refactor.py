"""
Lab 2 - Task 4: Student Logic + AI Refactoring (Odd/Even Sum in Tuple)
Student: Roger A Raju (Roll No: 2503A52370, Batch: 13)
"""

from typing import Tuple

# ==========================================
# 1. Original Student Code (Imperative Loop)
# Style: Manual iteration with mutable state
# ==========================================
def calculate_odd_even_sum_student(numbers: tuple):
    """
    Original baseline student implementation using manual for-loop.
    Calculates the sum of even and odd numbers in a tuple.
    """
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum = even_sum + num
        else:
            odd_sum = odd_sum + num
    return even_sum, odd_sum


# ==========================================
# 2. Refactored AI Code (Optimized & Pythonic)
# Tool: Cursor AI / Gemini Refactoring
# Style: Functional generator expressions, type hints, guard clauses
# ==========================================
def calculate_odd_even_sum_refactored(numbers: Tuple[int, ...]) -> Tuple[int, int]:
    """
    Refactored AI implementation using functional generator expressions.
    
    Parameters:
    numbers (Tuple[int, ...]): Tuple of integer values.
    
    Returns:
    Tuple[int, int]: (even_sum, odd_sum)
    
    Raises:
    TypeError: If input is not a tuple or contains non-integer values.
    """
    if not isinstance(numbers, tuple):
        raise TypeError(f"Input must be a tuple, got {type(numbers).__name__}.")
        
    for val in numbers:
        if not isinstance(val, int) or isinstance(val, bool):
            raise TypeError(f"All elements in the tuple must be integers. Found: {val} ({type(val).__name__})")
            
    even_sum = sum(x for x in numbers if x % 2 == 0)
    odd_sum = sum(x for x in numbers if x % 2 != 0)
    
    return even_sum, odd_sum


def test_odd_even_sum_refactoring():
    print("--- Running Test Assertions for Task 4 (Odd/Even Sum Refactoring) ---")
    
    test_tuples = [
        ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), (30, 25), "Standard consecutive range 1-10"),
        ((10, 20, 30, 40), (100, 0), "All even numbers tuple"),
        ((1, 3, 5, 7, 9, 11), (0, 36), "All odd numbers tuple"),
        ((-4, -3, -2, -1, 0, 1, 2, 3, 4), (0, 0), "Symmetric positive and negative integers"),
        ((42,), (42, 0), "Single even element tuple"),
        ((), (0, 0), "Empty tuple edge case")
    ]
    
    for t_in, (exp_even, exp_odd), desc in test_tuples:
        s_even, s_odd = calculate_odd_even_sum_student(t_in)
        r_even, r_odd = calculate_odd_even_sum_refactored(t_in)
        
        assert (s_even, s_odd) == (exp_even, exp_odd), f"Student logic failed on {t_in}"
        assert (r_even, r_odd) == (exp_even, exp_odd), f"Refactored AI logic failed on {t_in}"
        assert (s_even, s_odd) == (r_even, r_odd), "Discrepancy between student and AI logic"
        
        print(f"Assertion Passed: {t_in} -> Even Sum: {r_even}, Odd Sum: {r_odd} ({desc})")

    # Test type error validation on refactored function
    try:
        calculate_odd_even_sum_refactored([1, 2, 3]) # List instead of tuple
        assert False, "Failed to catch non-tuple input"
    except TypeError as e:
        print(f"Assertion Passed: Non-tuple input safely rejected -> {e}")

    try:
        calculate_odd_even_sum_refactored((1, 2, "3", 4))
        assert False, "Failed to catch invalid element type"
    except TypeError as e:
        print(f"Assertion Passed: Non-integer element safely rejected -> {e}")

    print("All 4 Odd/Even Refactoring Assertions passed successfully!")


def main():
    print("=== Task 4: Student Logic + AI Refactoring (Odd/Even Sum) ===")
    print("[AI CAPABILITY] Refactoring Benefit: Reduced imperative boilerplate to memory-efficient C-optimized generator expressions.")
    print("[VERIFICATION] Exact Verification: Exact mathematical parity established across negative, positive, empty, and single tuples.\n")
    test_odd_even_sum_refactoring()


if __name__ == "__main__":
    main()
