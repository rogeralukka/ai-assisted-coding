def check_discount(age: int, is_member: bool) -> str:
    """Determines discount eligibility based on age and membership status

    using nested conditionals.
    """
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a non-negative integer.")

    if not isinstance(is_member, bool):
        raise TypeError("is_member must be a boolean (True/False).")

    if age >= 60:
        if is_member:
            return "Eligible for Senior Discount + Member Bonus (Highest Discount)"
        else:
            return "Eligible for Standard Senior Discount"
    else:
        if is_member:
            return "Eligible for Member Discount"
        else:
            return "No Discount (Standard Rate)"


if __name__ == "__main__":
    test_cases = [
        (65, True),
        (70, False),
        (25, True),
        (30, False),
    ]

    for age, member in test_cases:
        result = check_discount(age, member)
        print(f"Age: {age}, Member: {str(member):<5} -> {result}")
