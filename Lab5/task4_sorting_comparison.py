"""
Task 4: Transparency in Algorithm Comparison
AI Assisted Coding Lab 5

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

def bubble_sort(arr):
    """
    Bubble Sort Algorithm:
    Iteratively compares adjacent elements and swaps them if in wrong order.
    Time Complexity: O(N^2) | Space: O(1) in-place | Stability: Stable
    """
    a = list(arr)
    n = len(a)
    comparisons, swaps = 0, 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return a, comparisons, swaps


def quick_sort(arr):
    """
    QuickSort Algorithm:
    Divide-and-conquer partitioning around a chosen pivot element.
    Time Complexity: O(N log N) average | Space: O(log N) stack | Stability: Unstable
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def test_sorting_comparison():
    print("--- Running Test Assertions for Task 4 (Algorithm Comparison) ---")
    data = [64, 34, 25, 12, 22, 11, 90]
    expected_sorted = [11, 12, 22, 25, 34, 64, 90]

    # Test Case 1: BubbleSort correctness
    b_res, b_comp, b_swaps = bubble_sort(data)
    assert b_res == expected_sorted, "Test 1 Failed"
    print(f"Assertion 1 Passed: BubbleSort correctly sorted list ({b_comp} comparisons, {b_swaps} swaps).")

    # Test Case 2: QuickSort correctness
    q_res = quick_sort(data)
    assert q_res == expected_sorted, "Test 2 Failed"
    print(f"Assertion 2 Passed: QuickSort correctly sorted list.")

    # Test Case 3: Empty and single-item lists
    assert quick_sort([]) == [] and bubble_sort([])[0] == [], "Test 3 Failed"
    assert quick_sort([42]) == [42] and bubble_sort([42])[0] == [42], "Test 3 Failed"
    print("Assertion 3 Passed: Edge cases (empty, single-element) handled accurately.")

    # Test Case 4: Presorted array efficiency in BubbleSort
    presorted = [1, 2, 3, 4, 5]
    _, p_comp, p_swaps = bubble_sort(presorted)
    assert p_swaps == 0 and p_comp == 4, "Test 4 Failed"
    print(f"Assertion 4 Passed: Presorted list optimized by early termination (0 swaps).")

    print("All 4 Assertions passed successfully!")


def main():
    print("=== Task 4: Transparency in Algorithm Comparison (Sorting Analysis) ===")
    print("Observed Limitation: Black-box algorithm selection leads to choosing O(N^2) algorithms for big data.")
    print("Applied Fix: Documented QuickSort vs BubbleSort with runtime metrics and complexity profiles.\n")
    test_sorting_comparison()


if __name__ == "__main__":
    main()
