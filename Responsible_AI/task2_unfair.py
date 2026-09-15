APPROVAL_THRESHOLD = 70
LOCATION_BONUS = {"urban": 0, "rural": 10}

def check_eligibility(academic_score, family_income, location):
    location = location.strip().lower()
    if location not in LOCATION_BONUS:
        raise ValueError("Location must be urban or rural.")
    if not 0 <= academic_score <= 100 or family_income < 0:
        raise ValueError("Enter a valid academic score and family income.")

    academic_points = academic_score * 0.5
    income_points = max(0, 40 - (family_income / 60_000) * 40)
    location_points = LOCATION_BONUS[location]
    total_score = academic_points + income_points + location_points

    return {
        "eligible": total_score >= APPROVAL_THRESHOLD,
        "score": round(total_score, 2),
        "location_points": location_points,
    }

def main():
    academic_score = float(input("Academic score (0-100): "))
    family_income = float(input("Family income: "))
    location = input("Location (urban/rural): ")
    result = check_eligibility(academic_score, family_income, location)
    print("Eligible" if result["eligible"] else "Not eligible")
    print(result)

if __name__ == "__main__":
    main()
