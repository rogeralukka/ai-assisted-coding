"""
Task 2: Privacy & Security in File Handling
AI Assisted Coding Lab 5

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

import json
import hashlib
import hmac
import os

def hash_password(password, salt=None):
    """Hashes password using PBKDF2-HMAC-SHA256 with cryptographic salt."""
    if salt is None:
        salt = os.urandom(16)
    hashed = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    return salt.hex(), hashed.hex()


def verify_password(password, salt_hex, hash_hex):
    salt = bytes.fromhex(salt_hex)
    _, test_hash = hash_password(password, salt)
    return hmac.compare_digest(test_hash, hash_hex)


def register_user_secure(name, email, password, filepath="users_secure.json"):
    if not name or not email or not password:
        return "Error: All fields are required."
    salt_hex, hash_hex = hash_password(password)
    user_record = {
        "name": name,
        "email": email,
        "salt": salt_hex,
        "password_hash": hash_hex
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(user_record, f, indent=2)
    return "User registered successfully with encrypted password storage."


def test_file_security():
    print("--- Running Test Assertions for Task 2 (Privacy & Security in File Handling) ---")
    test_file = "test_user_secure.json"
    status = register_user_secure("Roger A Raju", "rogeraraju@example.com", "SuperSecret#2026", test_file)

    # Test Case 1: Registration confirmation
    assert "successfully" in status, "Test 1 Failed"
    print("Assertion 1 Passed: User registered with encrypted credentials.")

    # Test Case 2: Verify plaintext password is not saved on disk
    with open(test_file, "r", encoding="utf-8") as f:
        saved_data = json.load(f)
    assert "SuperSecret#2026" not in str(saved_data), "Test 2 Failed (Plaintext leak)"
    assert "password_hash" in saved_data and "salt" in saved_data, "Test 2 Failed"
    print("Assertion 2 Passed: Plaintext password is NEVER stored on disk.")

    # Test Case 3: Correct password authentication
    assert verify_password("SuperSecret#2026", saved_data["salt"], saved_data["password_hash"]) == True, "Test 3 Failed"
    print("Assertion 3 Passed: Valid password authenticated successfully.")

    # Test Case 4: Incorrect password rejection
    assert verify_password("WrongPassword123", saved_data["salt"], saved_data["password_hash"]) == False, "Test 4 Failed"
    print("Assertion 4 Passed: Invalid password rejected.")

    print("All 4 Assertions passed successfully!")

    if os.path.exists(test_file):
        os.remove(test_file)


def main():
    print("=== Task 2: Privacy & Security in File Handling (Password Hashing) ===")
    print("Observed Risk: Plaintext passwords saved to disk violate GDPR and enable catastrophic data leaks.")
    print("Applied Fix: Implemented salted PBKDF2-HMAC-SHA256 one-way hashing with constant-time verification.\n")
    test_file_security()


if __name__ == "__main__":
    main()
