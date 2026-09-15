"""
Task 3: Anagram Checker – Apply AI for String Analysis
AI Assisted Coding Lab 8 (Test-Driven Development with AI)

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

import string
from collections import Counter

def is_anagram(str1: str, str2: str) -> bool:
    """
    Determines if two strings are anagrams of each other.
    - Case-insensitive comparison
    - Ignores spaces and all punctuation marks
    - Handles edge cases (empty strings, non-string types, identical phrases)
    """
    if not isinstance(str1, str) or not isinstance(str2, str):
        return False

    # Normalize: strip punctuation, spaces, and convert to lowercase
    cleaned_1 = "".join(c.lower() for c in str1 if c.isalnum())
    cleaned_2 = "".join(c.lower() for c in str2 if c.isalnum())

    return Counter(cleaned_1) == Counter(cleaned_2)


def test_is_anagram():
    print("--- Running AI-Generated TDD Assertions for Task 3 ---")

    # Test Case 1: Standard single-word anagram
    assert is_anagram("listen", "silent") == True, "Test 1 Failed"
    print("Assertion 1 Passed: is_anagram('listen', 'silent') == True")

    # Test Case 2: Non-anagram words
    assert is_anagram("hello", "world") == False, "Test 2 Failed"
    print("Assertion 2 Passed: is_anagram('hello', 'world') == False")

    # Test Case 3: Multi-word phrase with mixed casing and spaces
    assert is_anagram("Dormitory", "Dirty Room") == True, "Test 3 Failed"
    print("Assertion 3 Passed: is_anagram('Dormitory', 'Dirty Room') == True (Case & space ignored)")

    # Test Case 4: Complex sentence anagram with punctuation
    assert is_anagram("Conversation", "Voices, rant on!") == True, "Test 4 Failed"
    print("Assertion 4 Passed: is_anagram('Conversation', 'Voices, rant on!') == True (Punctuation ignored)")

    # Test Case 5: Edge Case - Empty strings
    assert is_anagram("", "") == True, "Test 5 Failed"
    print("Assertion 5 Passed: is_anagram('', '') == True (Empty strings handled)")

    print("All AI-Generated Assertions passed successfully!")


def main():
    print("=== Task 3: Anagram Checker (TDD) ===")
    print("Evaluating anagrams with normalization for case, whitespace, and punctuation.\n")
    test_is_anagram()


if __name__ == "__main__":
    main()
