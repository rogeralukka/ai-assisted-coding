"""
Task 2: Loops – Pattern Generation
Lab 6: AI-Based Code Completion – Classes, Loops, and Conditionals
Course: AI Assisted Coding (23CS002PC304)
Student: ROGER A RAJU (Roll No: 2503A52370)
"""

def print_triangle_for_loop(n: int) -> None:
    """
    Prints a right-angled triangle star pattern of height n using a for loop.
    
    Structure:
    - Outer loop iterates over each row (1 to n).
    - Inner loop prints stars for each column (1 to current row).
    """
    print(f"--- Right-Angled Triangle using FOR Loop (n = {n}) ---")
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()


def print_triangle_while_loop(n: int) -> None:
    """
    Prints a right-angled triangle star pattern of height n using a while loop.
    
    Structure:
    - Outer while loop controls the row counter initialized to 1.
    - Inner while loop controls the column counter initialized to 0.
    """
    print(f"--- Right-Angled Triangle using WHILE Loop (n = {n}) ---")
    row = 1
    while row <= n:
        col = 0
        while col < row:
            print("*", end=" ")
            col += 1
        print()
        row += 1


def main():
    print("=" * 60)
    print("Task 2: Pattern Generation using For and While Loops")
    print("=" * 60)

    rows = 5

    # 1. Pattern using for loop
    print_triangle_for_loop(rows)
    print()

    # 2. Pattern using while loop
    print_triangle_while_loop(rows)


if __name__ == "__main__":
    main()
