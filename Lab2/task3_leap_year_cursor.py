"""
Lab 2 - Task 3: Leap Year Validation Using Cursor AI
Tool: Cursor AI (Dual-Prompt Evaluation)
Student: Roger A Raju (Roll No: 2503A52370, Batch: 13)
"""

# ==========================================
# Version 1: Prompt 1 (Basic Conditional Logic)
# Prompt: "Write a Python function to check whether a given year is a leap year using standard if-else conditions."
# ==========================================
def is_leap_year_basic(year: int) -> bool:
    """Basic leap year check using nested if-else rules."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# ==========================================
# Version 2: Prompt 2 (Cursor AI Refactored for Production Backend)
# Prompt: "Refactor leap year validation for a backend production calendar module with type safety, comprehensive docstring, boundary validation, and boolean simplification."
# ==========================================
def is_leap_year_production(year: int) -> bool:
    """
    Validates whether a given calendar year is a leap year in the Gregorian calendar.
    
    A leap year occurs on every year that is evenly divisible by 4,
    except for end-of-century years (multiples of 100), which must also be divisible by 400.
    
    Parameters:
    year (int): Positive Gregorian calendar year (>= 1).
    
    Returns:
    bool: True if leap year, False otherwise.
    
    Raises:
    TypeError: If year is not an integer or is a boolean.
    ValueError: If year is less than 1 (AD calendar boundary).
    """
    if not isinstance(year, int) or isinstance(year, bool):
        raise TypeError(f"Year must be an integer, got {type(year).__name__}.")
        
    if year < 1:
        raise ValueError(f"Year must be a positive integer >= 1 (Gregorian calendar boundary), got {year}.")
        
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def test_leap_year_cursor():
    print("--- Running Test Assertions for Task 3 (Leap Year Validation: Cursor AI) ---")
    
    test_cases = [
        (2024, True, "Divisible by 4 and not 100 -> Leap Year"),
        (2000, True, "Century year divisible by 400 -> Leap Year"),
        (1900, False, "Century year divisible by 100 but not 400 -> Non-Leap Year"),
        (2023, False, "Common year not divisible by 4 -> Non-Leap Year"),
        (2026, False, "Current year not divisible by 4 -> Non-Leap Year"),
        (2400, True, "Future century year divisible by 400 -> Leap Year"),
        (1600, True, "Historical century year divisible by 400 -> Leap Year")
    ]
    
    for yr, expected, explanation in test_cases:
        basic_res = is_leap_year_basic(yr)
        prod_res = is_leap_year_production(yr)
        assert basic_res == expected, f"Basic logic failed on {yr}"
        assert prod_res == expected, f"Production logic failed on {yr}"
        print(f"Assertion Passed: Year {yr} -> {prod_res} ({explanation})")

    # Test boundary / invalid input handling on production version
    try:
        is_leap_year_production(-50)
        assert False, "Failed to catch negative year"
    except ValueError as e:
        print(f"Assertion Passed: Negative year caught safely -> {e}")

    try:
        is_leap_year_production("2024")
        assert False, "Failed to catch string input"
    except TypeError as e:
        print(f"Assertion Passed: Invalid type caught safely -> {e}")

    print("All Leap Year Assertions passed successfully!")


def main():
    print("=== Task 3: Leap Year Validation (Cursor AI Multi-Prompting) ===")
    print("[AI CAPABILITY] Prompt Impact: Prompt 1 produced nested if-else logic; Prompt 2 produced production-grade guard clauses.")
    print("[VERIFICATION] Backend Readiness: Verified century leap rules (1600, 2000, 2400) and strict non-leap century rules (1900).\n")
    test_leap_year_cursor()


if __name__ == "__main__":
    main()
