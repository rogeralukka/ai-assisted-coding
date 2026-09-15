SELECTION_THRESHOLD = 70

def admission_decision(entrance_score, academic_marks, interview_score):
    total_score = (
        entrance_score * 0.50
        + academic_marks * 0.30
        + interview_score * 0.20
    )
    return "Selected" if total_score >= SELECTION_THRESHOLD else "Rejected"

def main():
    entrance_score = float(input("Entrance exam score (0-100): "))
    academic_marks = float(input("Academic marks (0-100): "))
    interview_score = float(input("Interview score (0-100): "))
    print(admission_decision(entrance_score, academic_marks, interview_score))

if __name__ == "__main__":
    main()
