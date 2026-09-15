import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("users_unsecured.json")

def save_user(name, email, password):
    """Demonstration only: this stores the password in plain text."""
    users = []
    if DATA_FILE.exists():
        with DATA_FILE.open("r", encoding="utf-8") as file:
            users = json.load(file)

    users.append(
        {
            "name": name,
            "email": email,
            "password": password,
        }
    )

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(users, file, indent=2)

def main():
    print("UNSECURED DEMONSTRATION - do not use in production")
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    save_user(name, email, password)
    print(f"User saved to {DATA_FILE}")

if __name__ == "__main__":
    main()
