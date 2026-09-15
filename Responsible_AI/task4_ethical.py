# Task 4 - Ethical Employee Performance Evaluation
EVALUATION_THRESHOLD = 70
WEIGHTS = {
    "project completion": 0.45,
    "teamwork": 0.35,
    "attendance": 0.20,
}

def evaluate_employee_ethical(project_completion, teamwork, attendance):
    """
    Ethical evaluation model:
    - Balanced weighting: project completion (45%) and teamwork (35%) carry primary weight.
    - Attendance is limited to 20% to avoid penalizing employees with approved leaves or medical needs.
    - Full transparency: published weights and score contributions are returned.
    """
    if not all(0 <= score <= 100 for score in (project_completion, teamwork, attendance)):
        raise ValueError("All scores must be between 0 and 100.")

    scores = {
        "project completion": project_completion,
        "teamwork": teamwork,
        "attendance": attendance,
    }

    contributions = {
        factor: round(score * WEIGHTS[factor], 2)
        for factor, score in scores.items()
    }

    total_score = round(sum(contributions.values()), 2)
    rating = "High" if total_score >= EVALUATION_THRESHOLD else "Needs improvement"

    return {
        "rating": rating,
        "total_score": total_score,
        "contributions": contributions,
        "published_weights": WEIGHTS,
    }

def main():
    project_completion = float(input("Project completion rate (0-100): "))
    teamwork = float(input("Teamwork score (0-100): "))
    attendance = float(input("Attendance (0-100): "))
    result = evaluate_employee_ethical(project_completion, teamwork, attendance)
    print(f"Rating: {result['rating']}")
    print(f"Total score: {result['total_score']}/100")
    print(f"Contributions: {result['contributions']}")
    print(f"Published weights: {result['published_weights']}")

if __name__ == "__main__":
    main()
