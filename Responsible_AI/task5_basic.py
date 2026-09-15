import json
from pathlib import Path

FEEDBACK_FILE = Path(__file__).with_name("feedback_basic.json")

def main():
    print("Customer Feedback")
    name = input("Full name: ")
    gender = input("Gender (Male/Female): ")
    has_disability = input("Do you have a disability? (Yes/No): ")
    rating = input("Rate us from 1 to 5: ")
    comments = input("Additional comments: ")

    feedback = {
        "name": name,
        "gender": gender,
        "has_disability": has_disability,
        "rating": rating,
        "comments": comments,
    }

    with FEEDBACK_FILE.open("w", encoding="utf-8") as file:
        json.dump(feedback, file, indent=2)
    print("Feedback saved.")

if __name__ == "__main__":
    main()
