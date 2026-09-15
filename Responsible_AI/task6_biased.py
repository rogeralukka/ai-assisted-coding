APPROVAL_THRESHOLD = 70

def loan_decision(income, age, employment_status, credit_score, loan_amount,
                  gender, religion, race):
    """Demonstration only: this rule uses unrelated sensitive attributes."""
    if income <= 0 or loan_amount <= 0 or not 0 <= credit_score <= 850:
        raise ValueError("Enter positive income/loan values and a credit score from 0 to 850.")

    score = 0
    score += min(income / 1000, 40)
    score += min(credit_score / 10, 40)
    score += 10 if employment_status == "full-time" else 0
    score -= 20 if gender.lower() == "female" else 0
    score -= 15 if religion.lower() == "minority" else 0
    score -= 15 if race.lower() == "minority" else 0
    score -= 10 if loan_amount > income * 3 else 0

    return {
        "decision": "Approved" if score >= APPROVAL_THRESHOLD else "Rejected",
        "score": round(score, 2),
    }

def main():
    print("BIASED DEMONSTRATION - do not use for real lending")
    income = float(input("Annual income: "))
    age = int(input("Age: "))
    employment_status = input("Employment status (full-time/other): ").strip().lower()
    credit_score = float(input("Credit score (0-850): "))
    loan_amount = float(input("Loan amount: "))
    gender = input("Gender: ").strip()
    religion = input("Religion: ").strip()
    race = input("Race: ").strip()
    print(loan_decision(income, age, employment_status, credit_score,
                        loan_amount, gender, religion, race))

if __name__ == "__main__":
    main()
