"""
Task 1: Syntax Errors – Missing Parentheses in Print Statement
AI Assisted Coding Lab 7.1

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

def greet(name="AI Debugging Lab!"):
    """
    Corrected greet function using valid Python 3 print() syntax.
    In Python 3, print is a built-in function that requires parentheses.
    """
    message = f"Hello, {name}"
    print(message)
    return message

def test_greet():
    print("--- Running Test Assertions for Task 1 ---")
    # Test Case 1: Default lab greeting
    assert greet("AI Debugging Lab!") == "Hello, AI Debugging Lab!", "Test 1 Failed"
    print("Assertion 1 Passed: Default lab greeting verified.")

    # Test Case 2: Custom student name
    assert greet("Roger A Raju") == "Hello, Roger A Raju", "Test 2 Failed"
    print("Assertion 2 Passed: Student name greeting verified.")

    # Test Case 3: Course subject name
    assert greet("Python Programming") == "Hello, Python Programming", "Test 3 Failed"
    print("Assertion 3 Passed: Subject greeting verified.")
    print("All 3 Assertions passed successfully!")

def main():
    print("=== Task 1: Syntax Error Debugging ===")
    print("Observed Bug: Missing parentheses in Python 2 print statement causes SyntaxError in Python 3.")
    print("Applied Fix: Replaced 'print ...' with 'print(...)'.\n")
    test_greet()

if __name__ == "__main__":
    main()
