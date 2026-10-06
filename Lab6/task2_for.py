def print_triangle_for(n: int) -> None:
    """Prints a right-angled triangle pattern of height n using a for loop."""
    if n <= 0:
        return

    for i in range(1, n + 1):
        print("*" * i)


print("--- For Loop Pattern ---")
print_triangle_for(5)
