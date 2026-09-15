"""
Task 3: Transparency in Algorithm Design
AI Assisted Coding Lab 5

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

def is_armstrong_number(number):
    """
    Transparent, step-by-step Armstrong (Narcissistic) number validator:
    An Armstrong number equals the sum of its own digits each raised to the power of the total number of digits.
    Example for 153: (1^3) + (5^3) + (3^3) = 1 + 125 + 27 = 153.
    """
    if not isinstance(number, int) or number < 0:
        return {"is_armstrong": False, "explanation": "Input must be a non-negative integer."}

    num_str = str(number)
    num_digits = len(num_str)
    digit_powers = []
    total_sum = 0

    for char in num_str:
        digit = int(char)
        power_val = digit ** num_digits
        digit_powers.append(f"{digit}^{num_digits} ({power_val})")
        total_sum += power_val

    is_armstrong = (total_sum == number)
    explanation = f"Sum of digits: {' + '.join(digit_powers)} = {total_sum} {'==' if is_armstrong else '!='} {number}"

    return {
        "number": number,
        "is_armstrong": is_armstrong,
        "total_sum": total_sum,
        "explanation": explanation
    }


def test_armstrong_transparency():
    print("--- Running Test Assertions for Task 3 (Transparency in Algorithm Design) ---")
    
    # Test Case 1: 3-digit Armstrong number (153)
    res_153 = is_armstrong_number(153)
    assert res_153["is_armstrong"] == True, "Test 1 Failed"
    print(f"Assertion 1 Passed: 153 is Armstrong -> {res_153['explanation']}")

    # Test Case 2: 3-digit Armstrong number (370)
    res_370 = is_armstrong_number(370)
    assert res_370["is_armstrong"] == True, "Test 2 Failed"
    print(f"Assertion 2 Passed: 370 is Armstrong -> {res_370['explanation']}")

    # Test Case 3: Non-Armstrong number (123)
    res_123 = is_armstrong_number(123)
    assert res_123["is_armstrong"] == False, "Test 3 Failed"
    print(f"Assertion 3 Passed: 123 is Not Armstrong -> {res_123['explanation']}")

    # Test Case 4: Single digit Armstrong number (9)
    assert is_armstrong_number(9)["is_armstrong"] == True, "Test 4 Failed"
    print("Assertion 4 Passed: 9 is Armstrong (9^1 == 9).")

    print("All 4 Assertions passed successfully!")


def main():
    print("=== Task 3: Transparency in Algorithm Design (Armstrong Number) ===")
    print("Observed Limitation: Uncommented compressed code creates cognitive burden and auditing difficulties.")
    print("Applied Fix: Created explainable function returning step-by-step mathematical proof.\n")
    test_armstrong_transparency()


if __name__ == "__main__":
    main()
