def evaluate_employee(project_completion, teamwork, attendance):
    """Demonstration of a potentially unfair evaluation model."""
    if not all(0 <= score <= 100 for score in (project_completion, teamwork, attendance)):
        raise ValueError("All scores must be between 0 and 100.")

    # Attendance is overweighted and teamwork is undervalued without explanation.
    total_score = (
        project_completion * 0.30
        + teamwork * 0.10
        + attendance * 0.60
    )
    rating = "High" if total_score >= 70 else "Needs improvement"
    return {"score": round(total_score, 2), "rating": rating}

def main():
    project_completion = float(input("Project completion rate (0-100): "))
    teamwork = float(input("Teamwork score (0-100): "))
    attendance = float(input("Attendance (0-100): "))
    print(evaluate_employee(project_completion, teamwork, attendance))

if __name__ == "__main__":
    main()
