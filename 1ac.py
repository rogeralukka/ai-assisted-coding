def is_happy(n: int) -> bool:
    """Return True if n is a happy number."""
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1


def happy_numbers(limit: int) -> list[int]:
    """Return a list of happy numbers from 1 up to limit."""
    return [num for num in range(1, limit + 1) if is_happy(num)]


def main() -> None:
    try:
        value = int(input("Enter a positive integer: ").strip())
        if value <= 0:
            raise ValueError("The number must be positive.")
    except ValueError as exc:
        print(f"Invalid input: {exc}")
        return

    print(f"{value} is {'a happy' if is_happy(value) else 'not a happy'} number.")
    print("Happy numbers up to", value, ":")
    print(happy_numbers(value))


if __name__ == "__main__":
    main()
