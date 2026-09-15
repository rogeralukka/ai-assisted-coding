APPROVAL_THRESHOLD = 70

def loan_decision(income, age, employment_status, credit_score, loan_amount):
    """Use relevant financial factors only; never use protected attributes."""
    if income <= 0 or loan_amount <= 0:
        raise ValueError("Income and loan amount must be positive.")
    if not 18 <= age <= 100:
        raise ValueError("Age must be between 18 and 100.")
    if not 0 <= credit_score <= 850:
        raise ValueError("Credit score must be between 0 and 850.")

    employment_points = {
        "full-time": 15,
        "part-time": 8,
        "self-employed": 10,
        "unemployed": 0,
    }

    status = employment_status.strip().lower()
    if status not in employment_points:
        raise ValueError("Use full-time, part-time, self-employed, or unemployed.")

    income_points = min(income / 1000, 35)
    credit_points = (credit_score / 850) * 35
    employment_score = employment_points[status]
    affordability_points = 15 if loan_amount <= income * 2 else 0
    total_score = income_points + credit_points + employment_score + affordability_points

    return {
        "decision": "Approved" if total_score >= APPROVAL_THRESHOLD else "Rejected",
        "score": round(total_score, 2),
        "factors": {
            "income": round(income_points, 2),
            "credit_score": round(credit_points, 2),
            "employment_status": employment_score,
            "loan_affordability": affordability_points,
        },
        "sensitive_attributes_used": False,
    }

def main():
    print("FAIRER LOAN APPROVAL DEMONSTRATION")
    income = float(input("Annual income: "))
    age = int(input("Age: "))
    employment_status = input(
        "Employment status (full-time/part-time/self-employed/unemployed): "
    )
    credit_score = float(input("Credit score (0-850): "))
    loan_amount = float(input("Loan amount: "))
    result = loan_decision(income, age, employment_status, credit_score, loan_amount)
    print(result)

if __name__ == "__main__":
    main()
