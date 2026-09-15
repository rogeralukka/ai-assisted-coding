from typing import List, Dict

def count_even_odd(numbers: List[int]) -> Dict[str, int]:
    if not isinstance(numbers, (list, tuple)):
        raise TypeError(f"Input must be a list or tuple, got {type(numbers).__name__}")
    even_count = 0
    odd_count = 0
    for num in numbers:
        if not isinstance(num, int) or isinstance(num, bool):
            raise TypeError(f"List elements must be integers, found: {num} ({type(num).__name__})")
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return {
        "even_count": even_count,
        "odd_count": odd_count,
        "total_elements": len(numbers)
    }

def test_even_odd_counter():
    print("--- Running Test Assertions for Task 2 (Even/Odd Counter with Loop & Conditionals) ---")
    data1 = [12, 7, 9, 14, 22, 33, 40]
    res1 = count_even_odd(data1)
    assert res1["even_count"] == 4, f"Expected 4 even, got {res1['even_count']}"
    assert res1["odd_count"] == 3, f"Expected 3 odd, got {res1['odd_count']}"
    print(f"Assertion 1 Passed: {data1} -> Even: {res1['even_count']}, Odd: {res1['odd_count']}")
    
    data2 = [2, 4, 6, 8, 10, 100]
    res2 = count_even_odd(data2)
    assert res2["even_count"] == 6 and res2["odd_count"] == 0, "Test 2 Failed"
    print("Assertion 2 Passed: All-even list correctly counted (6 even, 0 odd).")
    
    data3 = [1, 3, 5, 7, 9, 11]
    res3 = count_even_odd(data3)
    assert res3["even_count"] == 0 and res3["odd_count"] == 6, "Test 3 Failed"
    print("Assertion 3 Passed: All-odd list correctly counted (0 even, 6 odd).")
    
    data4 = [-5, -4, -3, -2, -1, 0, 1, 2]
    res4 = count_even_odd(data4)
    assert res4["even_count"] == 4 and res4["odd_count"] == 4, "Test 4 Failed"
    print("Assertion 4 Passed: Negative integers and zero classified correctly.")
    
    assert count_even_odd([]) == {"even_count": 0, "odd_count": 0, "total_elements": 0}, "Test 5 Failed"
    print("Assertion 5 Passed: Empty list returns zero counts.")
    
    print("All 5 Task 2 Assertions passed successfully!")

if __name__ == "__main__":
    test_even_odd_counter()
