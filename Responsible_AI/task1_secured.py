import getpass
import hashlib
import hmac
import json
import secrets
from pathlib import Path

DATA_FILE = Path(__file__).with_name("users_secured.json")
HASH_ITERATIONS = 100_000

def load_users():
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as file:
        users = json.load(file)
    if not isinstance(users, list):
        raise ValueError("User data must be a JSON list.")
    return users

def hash_password(password, salt=None):
    salt = salt or secrets.token_bytes(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, HASH_ITERATIONS
    )
    return salt.hex(), password_hash.hex()

def verify_password(password, salt_hex, password_hash_hex):
    salt = bytes.fromhex(salt_hex)
    _, calculated_hash = hash_password(password, salt)
    return hmac.compare_digest(calculated_hash, password_hash_hex)

def save_user(name, email, password):
    users = load_users()
    normalized_email = email.strip().lower()
    if any(user.get("email") == normalized_email for user in users):
        raise ValueError("A user with that email already exists.")

    salt, password_hash = hash_password(password)
    users.append(
        {
            "name": name.strip(),
            "email": normalized_email,
            "salt": salt,
            "password_hash": password_hash,
        }
    )
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(users, file, indent=2)

def main():
    print("SECURED USER REGISTRATION")
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    password = getpass.getpass("Password: ")
    if not name or not email or not password:
        print("Name, email, and password are required.")
        return

    try:
        save_user(name, email, password)
    except (ValueError, json.JSONDecodeError) as error:
        print(f"Could not save user: {error}")
        return
    print(f"User saved to {DATA_FILE}")

if __name__ == "__main__":
    main()
