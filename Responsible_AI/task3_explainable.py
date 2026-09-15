SELECTION_THRESHOLD = 70
WEIGHTS = {
    "entrance exam": 0.50,
    "academic marks": 0.30,
    "interview": 0.20,
}

def admission_decision(entrance_score, academic_marks, interview_score):
    scores = {
        "entrance exam": entrance_score,
        "academic marks": academic_marks,
        "interview": interview_score,
    }
    contributions = {
        factor: round(score * WEIGHTS[factor], 2)
        for factor, score in scores.items()
    }
    total_score = round(sum(contributions.values()), 2)
    selected = total_score >= SELECTION_THRESHOLD
    strongest_factor = max(contributions, key=contributions.get)
    weakest_factor = min(contributions, key=contributions.get)

    if selected:
        reason = (
            f"Selected because the total score was {total_score}/100, "
            f"above the threshold of {SELECTION_THRESHOLD}. "
            f"The strongest factor was {strongest_factor} "
            f"({contributions[strongest_factor]} points)."
        )
    else:
        reason = (
            f"Rejected because the total score was {total_score}/100, "
            f"below the threshold of {SELECTION_THRESHOLD}. "
            f"The lowest contributing factor was {weakest_factor} "
            f"({contributions[weakest_factor]} points)."
        )

    return {
        "decision": "Selected" if selected else "Rejected",
        "total_score": total_score,
        "threshold": SELECTION_THRESHOLD,
        "contributions": contributions,
        "reason": reason,
    }

def main():
    entrance_score = float(input("Entrance exam score (0-100): "))
    academic_marks = float(input("Academic marks (0-100): "))
    interview_score = float(input("Interview score (0-100): "))
    result = admission_decision(entrance_score, academic_marks, interview_score)
    print(result["decision"])
    print(result["reason"])
    print(f"Important factors: {result['contributions']}")

if __name__ == "__main__":
    main()
