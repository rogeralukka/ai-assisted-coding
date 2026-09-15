"""
Task 5: TypeError – Mixing Strings and Integers in Addition
AI Assisted Coding Lab 7.1

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

def add_five_numeric(value):
    """
    Solution 1: Type Casting to Numeric (Integer)
    Converts input string or number to integer before adding 5.
    """
    return int(value) + 5

def add_five_string(value):
    """
    Solution 2: String Concatenation
    Converts number or input to string and concatenates '5'.
    """
    return str(value) + "5"

def add_five_flexible(value, mode="numeric"):
    """
    Polymorphic implementation supporting both numeric addition and string concatenation.
    """
    if mode == "numeric":
        return float(value) + 5 if '.' in str(value) else int(value) + 5
    elif mode == "string":
        return str(value) + "5"
    else:
        raise ValueError("Mode must be 'numeric' or 'string'")

def test_type_error_solutions():
    print("--- Running Test Assertions for Task 5 ---")
    
    # Solution 1 Assertions (Type Casting - Numeric Addition)
    print("[Solution 1: Numeric Addition (Type Casting)]")
    assert add_five_numeric("10") == 15, "Numeric Test 1 Failed"
    print("Assertion 1 Passed: add_five_numeric('10') == 15")
    
    assert add_five_numeric(20) == 25, "Numeric Test 2 Failed"
    print("Assertion 2 Passed: add_five_numeric(20) == 25")

    assert add_five_numeric("-5") == 0, "Numeric Test 3 Failed"
    print("Assertion 3 Passed: add_five_numeric('-5') == 0")

    # Solution 2 Assertions (String Concatenation)
    print("\n[Solution 2: String Concatenation]")
    assert add_five_string("10") == "105", "String Test 1 Failed"
    print("Assertion 4 Passed: add_five_string('10') == '105'")

    assert add_five_string(20) == "205", "String Test 2 Failed"
    print("Assertion 5 Passed: add_five_string(20) == '205'")

    assert add_five_string("SRU_") == "SRU_5", "String Test 3 Failed"
    print("Assertion 6 Passed: add_five_string('SRU_') == 'SRU_5'")

    print("\nAll 6 Assertions passed successfully across both solutions!")

def main():
    print("=== Task 5: Resolving TypeError (String + Integer Mixing) ===")
    print("Observed Bug: '10' + 5 causes TypeError due to implicit type mismatch.")
    print("Solution 1 (Numeric Addition): add_five_numeric('10') ->", add_five_numeric("10"))
    print("Solution 2 (String Concatenation): add_five_string('10') ->", add_five_string("10"))
    print()
    test_type_error_solutions()

if __name__ == "__main__":
    main()
