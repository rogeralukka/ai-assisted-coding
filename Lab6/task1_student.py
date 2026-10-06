class Student:
    """Represents a student with basic attributes and score validation."""

    def __init__(self, name: str, roll_no: int, marks: float):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")

        if not isinstance(roll_no, int) or roll_no <= 0:
            raise ValueError("Roll number must be a positive integer.")

        if not isinstance(marks, (int, float)):
            raise TypeError("Marks must be numeric (int or float).")

        if not (0 <= marks <= 100):
            raise ValueError("Marks must fall between 0 and 100 inclusive.")

        self.name = name.strip()
        self.roll_no = roll_no
        self.marks = float(marks)

    def is_pass(self) -> bool:
        """Determines if student scored the passing threshold (marks >= 40)."""
        return self.marks >= 40

    def __repr__(self) -> str:
        status = "Pass" if self.is_pass() else "Fail"
        return f"Student(name='{self.name}', roll_no={self.roll_no}, marks={self.marks}, status='{status}')"


if __name__ == "__main__":
    s1 = Student("Aarav Sharma", 101, 78.5)
    s2 = Student("Priya Patel", 102, 34.0)

    print(f"{s1.name}: Passed? {s1.is_pass()}")
    print(f"{s2.name}: Passed? {s2.is_pass()}")

    try:
        s3 = Student("Rahul", -5, 105)
    except ValueError as e:
        print(f"Validation Error: {e}")
