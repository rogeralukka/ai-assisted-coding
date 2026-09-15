import json
from datetime import datetime, timezone
from pathlib import Path

FEEDBACK_FILE = Path(__file__).with_name("feedback_accessible.json")
VALID_RATINGS = {"1", "2", "3", "4", "5"}

def ask_rating():
    while True:
        answer = input("How would you rate your experience from 1 to 5? ").strip()
        if answer in VALID_RATINGS:
            return int(answer)
        print("Please enter a whole number from 1 to 5.")

def ask_required(prompt):
    while True:
        answer = input(prompt).strip()
        if answer:
            return answer
        print("This field is required, or type 'prefer not to say'.")

def collect_feedback():
    print("User feedback form")
    print("Use short answers if helpful. Optional questions may be left blank.")
    return {
        "name": input("Name (optional): ").strip() or None,
        "contact": input("Email or other contact (optional): ").strip() or None,
        "rating": ask_rating(),
        "helpful": ask_required("What was helpful? "),
        "improvement": ask_required("What could we improve? "),
        "access_needs": input(
            "Access needs or barriers (optional): "
        ).strip() or None,
        "identity_details": input(
            "Identity details (optional, or prefer not to say): "
        ).strip() or None,
        "submitted_at": datetime.now(timezone.utc).isoformat(),
    }

def main():
    feedback = collect_feedback()
    with FEEDBACK_FILE.open("w", encoding="utf-8") as file:
        json.dump(feedback, file, indent=2)
    print("Thank you. Your feedback was saved.")

if __name__ == "__main__":
    main()
