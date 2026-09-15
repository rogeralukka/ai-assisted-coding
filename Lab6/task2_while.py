def print_triangle_while(n: int) -> None:
    """Prints a right-angled triangle pattern of height n using a while loop."""
    if n <= 0:
        return

    i = 1
    while i <= n:
        print("*" * i)
        i += 1


print("--- While Loop Pattern ---")
print_triangle_while(5)
