from typing import List

def get_even_numbers_for_loop(n: int) -> List[int]:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Upper bound N must be an integer, got {type(n).__name__}")
    if n < 2:
        return []
    even_numbers = []
    for num in range(2, n + 1, 2):
        even_numbers.append(num)
    return even_numbers

def get_even_numbers_while_loop(n: int) -> List[int]:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Upper bound N must be an integer, got {type(n).__name__}")
    even_numbers = []
    current = 2
    while current <= n:
        even_numbers.append(current)
        current += 2
    return even_numbers

def test_even_numbers_loop():
    print("--- Running Test Assertions for Task 1 (Even Numbers Loop Completion) ---")
    res_10 = get_even_numbers_for_loop(10)
    w_res_10 = get_even_numbers_while_loop(10)
    assert res_10 == [2, 4, 6, 8, 10], "Test 1 Failed"
    assert res_10 == w_res_10, "For-loop and while-loop mismatch"
    print(f"Assertion 1 Passed: N = 10 -> {res_10} (Both for-loop & while-loop match)")
    
    res_15 = get_even_numbers_for_loop(15)
    assert res_15 == [2, 4, 6, 8, 10, 12, 14], "Test 2 Failed"
    print(f"Assertion 2 Passed: N = 15 -> {res_15}")
    
    assert get_even_numbers_for_loop(1) == [], "Test 3 Failed"
    print("Assertion 3 Passed: N = 1 correctly returns empty list [].")
    
    assert get_even_numbers_for_loop(2) == [2], "Test 4 Failed"
    print("Assertion 4 Passed: N = 2 returns [2].")
    
    try:
        get_even_numbers_for_loop("10")
        assert False, "Failed to catch invalid string"
    except TypeError as e:
        print(f"Assertion 5 Passed: Non-integer input safely rejected ({e}).")
    
    print("All 5 Task 1 Assertions passed successfully!")

if __name__ == "__main__":
    test_even_numbers_loop()
