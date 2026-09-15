"""
Task 5: Date Validation & Formatting – Apply AI for Data Validation
AI Assisted Coding Lab 8 (Test-Driven Development with AI)

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

from datetime import datetime

def validate_and_format_date(date_str: str) -> str:
    """
    Validates dates strictly formatted as 'MM/DD/YYYY'.
    Converts valid dates into standard ISO 'YYYY-MM-DD' format.
    Accurately validates calendar constraints (e.g., Leap Years, month days).
    Returns 'Invalid Date' for non-conforming or impossible calendar dates.
    """
    if not isinstance(date_str, str):
        return "Invalid Date"

    date_str = date_str.strip()

    # Exact format and component check (MM/DD/YYYY)
    parts = date_str.split("/")
    if len(parts) != 3 or len(parts[0]) != 2 or len(parts[1]) != 2 or len(parts[2]) != 4:
        return "Invalid Date"

    try:
        # Strict calendar parsing using strptime
        parsed_dt = datetime.strptime(date_str, "%m/%d/%Y")
        return parsed_dt.strftime("%Y-%m-%d")
    except ValueError:
        # Caught invalid days (e.g. 02/30/2023 or 02/29/2023 in non-leap year)
        return "Invalid Date"


def test_date_formatting():
    print("--- Running AI-Generated TDD Assertions for Task 5 ---")

    # Test Case 1: Valid standard date conversion
    assert validate_and_format_date("10/15/2023") == "2023-10-15", "Test 1 Failed"
    print("Assertion 1 Passed: validate_and_format_date('10/15/2023') == '2023-10-15'")

    # Test Case 2: Invalid date (Feb 30 does not exist)
    assert validate_and_format_date("02/30/2023") == "Invalid Date", "Test 2 Failed"
    print("Assertion 2 Passed: validate_and_format_date('02/30/2023') == 'Invalid Date' (Calendar rule enforced)")

    # Test Case 3: Valid New Year date
    assert validate_and_format_date("01/01/2024") == "2024-01-01", "Test 3 Failed"
    print("Assertion 3 Passed: validate_and_format_date('01/01/2024') == '2024-01-01'")

    # Test Case 4: Leap Year validation (2024 is leap, 2023 is not)
    assert validate_and_format_date("02/29/2024") == "2024-02-29", "Leap 2024 Failed"
    assert validate_and_format_date("02/29/2023") == "Invalid Date", "Non-leap 2023 Failed"
    print("Assertion 4 Passed: Leap Year validation (2024 valid, 2023 invalid) verified.")

    # Test Case 5: Malformed input / Month out of range
    assert validate_and_format_date("13/05/2023") == "Invalid Date", "Test 5 Failed"
    assert validate_and_format_date("not-a-date") == "Invalid Date", "Test 6 Failed"
    print("Assertion 5 Passed: Malformed strings and out-of-range months rejected.")

    print("All AI-Generated Assertions passed successfully!")


def main():
    print("=== Task 5: Date Validation & Formatting (TDD) ===")
    print("Converting 'MM/DD/YYYY' -> 'YYYY-MM-DD' with calendar integrity checking.\n")
    test_date_formatting()


if __name__ == "__main__":
    main()
