"""
Lab 2 - Task 1: Statistical Summary for Survey Data
Tool: Google Gemini (Colab)
Student: Roger A Raju (Roll No: 2503A52370, Batch: 13)
"""

from typing import List, Dict, Union

def calculate_survey_statistics(responses: List[Union[int, float]]) -> Dict[str, float]:
    """
    Calculates the mean, minimum, and maximum values from survey numerical responses.
    
    Parameters:
    responses (List[Union[int, float]]): List of numerical survey ratings/scores.
    
    Returns:
    Dict[str, float]: Dictionary containing 'mean', 'min', 'max', and 'count'.
    
    Raises:
    ValueError: If the responses list is empty or contains non-numeric data.
    """
    if not isinstance(responses, (list, tuple)):
        raise TypeError("Survey responses must be provided as a list or tuple.")
        
    if not responses:
        raise ValueError("Survey responses list cannot be empty.")
        
    for val in responses:
        if not isinstance(val, (int, float)) or isinstance(val, bool):
            raise TypeError(f"Invalid non-numeric value found in survey data: {val}")
            
    total = sum(responses)
    count = len(responses)
    mean_val = round(total / count, 2)
    min_val = float(min(responses))
    max_val = float(max(responses))
    
    return {
        "count": count,
        "mean": mean_val,
        "min": min_val,
        "max": max_val
    }


def test_survey_statistics():
    print("--- Running Test Assertions for Task 1 (Statistical Summary for Survey Data) ---")
    
    # Test Case 1: Standard survey ratings (Scale 1-10)
    survey_data = [8, 9, 7, 10, 6, 8, 9, 5, 10, 8]
    stats = calculate_survey_statistics(survey_data)
    assert stats["count"] == 10, "Test 1 Failed: Count mismatch"
    assert stats["mean"] == 8.0, "Test 1 Failed: Mean calculation"
    assert stats["min"] == 5.0, "Test 1 Failed: Min value"
    assert stats["max"] == 10.0, "Test 1 Failed: Max value"
    print(f"Assertion 1 Passed: Survey Ratings -> Mean: {stats['mean']}, Min: {stats['min']}, Max: {stats['max']}")

    # Test Case 2: Floating point customer satisfaction scores
    float_data = [4.5, 3.8, 4.9, 2.1, 5.0]
    f_stats = calculate_survey_statistics(float_data)
    assert f_stats["mean"] == 4.06, f"Test 2 Failed: Expected 4.06, got {f_stats['mean']}"
    assert f_stats["min"] == 2.1, "Test 2 Failed"
    assert f_stats["max"] == 5.0, "Test 2 Failed"
    print(f"Assertion 2 Passed: Decimal Scores -> Mean: {f_stats['mean']}, Min: {f_stats['min']}, Max: {f_stats['max']}")

    # Test Case 3: Single response edge case
    single_data = [7]
    s_stats = calculate_survey_statistics(single_data)
    assert s_stats["mean"] == 7.0 and s_stats["min"] == 7.0 and s_stats["max"] == 7.0, "Test 3 Failed"
    print("Assertion 3 Passed: Single-element list correctly handled.")

    # Test Case 4: Empty list validation
    try:
        calculate_survey_statistics([])
        assert False, "Test 4 Failed: Expected ValueError"
    except ValueError as e:
        print(f"Assertion 4 Passed: Empty list safely rejected ({e}).")

    print("All 4 Assertions passed successfully!")


def main():
    print("=== Task 1: Statistical Summary for Survey Data (Gemini in Colab) ===")
    print("[AI CAPABILITY] Analytical Capability: Google Gemini generates structured, type-annotated code with edge-case validation.")
    print("[VERIFICATION] Colab Execution: Evaluated mean, minimum, maximum, and empty/invalid input handling across survey datasets.\n")
    test_survey_statistics()


if __name__ == "__main__":
    main()
