students = {}


def add_student():
    student_id = input("Student ID: ")
    name = input("Student name: ")
    students[student_id] = {"name": name, "attendance": []}
    print("Student added.")


def mark_attendance():
    student_id = input("Student ID: ")
    if student_id not in students:
        print("Student not found.")
        return

    status = input("Status (Present/Absent): ").title()
    if status not in ("Present", "Absent"):
        print("Enter Present or Absent.")
        return

    students[student_id]["attendance"].append(status)
    print("Attendance marked.")


def show_report():
    if not students:
        print("No students registered.")
        return

    for student_id, student in students.items():
        records = student["attendance"]
        present = records.count("Present")
        total = len(records)
        percentage = present / total * 100 if total else 0
        print(f"{student_id} - {student['name']}: {percentage:.1f}% attendance")


while True:
    print("\n1. Add student\n2. Mark attendance\n3. Show report\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        show_report()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")