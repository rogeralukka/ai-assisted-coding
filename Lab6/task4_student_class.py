from typing import List, Dict, Any

class Student:
    def __init__(self, name: str, roll_number: str, marks: List[float] = None):
        if not name or not isinstance(name, str):
            raise ValueError("Student name must be a non-empty string.")
        if not roll_number or not isinstance(roll_number, str):
            raise ValueError("Roll number must be a non-empty string.")
            
        self.name = name.strip()
        self.roll_number = roll_number.strip()
        self.marks: List[float] = []
        
        if marks:
            for m in marks:
                self.add_mark(m)
                
    def add_mark(self, mark: float) -> None:
        if not isinstance(mark, (int, float)) or isinstance(mark, bool):
            raise TypeError(f"Mark must be a numerical value, got {type(mark).__name__}.")
        if mark < 0 or mark > 100:
            raise ValueError(f"Mark must be between 0 and 100, got: {mark}")
        self.marks.append(float(mark))
        
    def calculate_total(self) -> float:
        return float(sum(self.marks)) if self.marks else 0.0
        
    def calculate_average(self) -> float:
        if not self.marks:
            return 0.0
        return round(self.calculate_total() / len(self.marks), 2)
        
    def get_grade(self) -> str:
        avg = self.calculate_average()
        if not self.marks:
            return "N/A (No Marks)"
        if avg >= 90:
            return "A+ (Outstanding)"
        elif avg >= 80:
            return "A (Excellent)"
        elif avg >= 70:
            return "B (Very Good)"
        elif avg >= 60:
            return "C (Good)"
        elif avg >= 50:
            return "D (Pass)"
        else:
            return "F (Fail)"
            
    def get_summary(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "roll_number": self.roll_number,
            "subjects_count": len(self.marks),
            "marks": self.marks,
            "total_marks": self.calculate_total(),
            "average_marks": self.calculate_average(),
            "grade": self.get_grade()
        }

def test_student_manager_class():
    print("--- Running Test Assertions for Task 4 (Student Manager Class Completion) ---")
    s1 = Student("Roger A Raju", "2503a52370", [85, 92, 78, 95, 88])
    assert s1.calculate_total() == 438.0, f"Expected 438, got {s1.calculate_total()}"
    assert s1.calculate_average() == 87.6, f"Expected 87.6, got {s1.calculate_average()}"
    assert "A (Excellent)" in s1.get_grade(), "Test 1 Failed"
    print(f"Assertion 1 Passed: Student {s1.name} -> Total: {s1.calculate_total()}, Avg: {s1.calculate_average()}%, Grade: {s1.get_grade()}")
    
    s1.add_mark(90)
    assert s1.calculate_total() == 528.0, "Test 2 Failed"
    assert s1.calculate_average() == 88.0, "Test 2 Failed"
    print(f"Assertion 2 Passed: Dynamic mark added -> New Total: {s1.calculate_total()}, New Avg: {s1.calculate_average()}%")
    
    s2 = Student("Top Performer", "2503A9999", [95, 98, 92, 94])
    assert s2.calculate_average() == 94.75, "Test 3 Failed"
    assert "A+ (Outstanding)" in s2.get_grade(), "Test 3 Failed"
    print(f"Assertion 3 Passed: High performer correctly awarded A+ grade ({s2.calculate_average()}%).")
    
    try:
        Student("BadMarks", "2503A0000", [85, 105])
        assert False, "Failed to reject mark > 100"
    except ValueError as e:
        print(f"Assertion 4 Passed: Out-of-bounds mark (> 100) rejected -> {e}")
        
    s_empty = Student("NewStudent", "2503A1111", [])
    assert s_empty.calculate_total() == 0.0 and s_empty.calculate_average() == 0.0, "Test 5 Failed"
    print("Assertion 5 Passed: Empty marks list handled safely without division by zero.")
    
    print("All 5 Task 4 Assertions passed successfully!")

if __name__ == "__main__":
    test_student_manager_class()
