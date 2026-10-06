from typing import Union


def analyze_number(num: Union[int, float]) -> str:
    """Classifies a given number as 'Positive', 'Negative', or 'Zero'.

    Args:
        num: A numeric value (int or float).

    Returns:
        A string indicating the sign of the number.
    """
    if not isinstance(num, (int, float)):
        raise TypeError(f"Expected int or float, got {type(num).__name__}")

    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


if __name__ == "__main__":
    test_cases = [15, -42, 0, 3.14159, -0.007, 0.0]

    print(f"{'Input':>10}  |  {'Classification':<12}")
    print("-" * 28)
    for value in test_cases:
        result = analyze_number(value)
        print(f"{value:>10}  |  {result:<12}")
