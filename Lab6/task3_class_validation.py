import re
from typing import Dict, Any

class User:
    EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    
    def __init__(self, username: str, email: str, age: int):
        self.username = self._validate_username(username)
        self.email = self._validate_email(email)
        self.age = self._validate_age(age)
        
    def _validate_username(self, username: str) -> str:
        if not isinstance(username, str) or not username.strip():
            raise ValueError("Username must be a non-empty string.")
        return username.strip()
        
    def _validate_email(self, email: str) -> str:
        if not isinstance(email, str):
            raise TypeError("Email must be a string.")
        email_clean = email.strip()
        if not self.EMAIL_REGEX.match(email_clean):
            raise ValueError(f"Invalid email format: '{email}'. Must contain valid username, '@', and domain.")
        return email_clean.lower()
        
    def _validate_age(self, age: int) -> int:
        if not isinstance(age, int) or isinstance(age, bool):
            raise TypeError(f"Age must be an integer, got {type(age).__name__}.")
        if age < 0 or age > 120:
            raise ValueError(f"Age must be between 0 and 120 years. Provided: {age}")
        return age
        
    def get_profile(self) -> Dict[str, Any]:
        return {
            "username": self.username,
            "email": self.email,
            "age": self.age,
            "is_adult": self.age >= 18
        }
        
    def update_email(self, new_email: str) -> None:
        self.email = self._validate_email(new_email)
        
    def update_age(self, new_age: int) -> None:
        self.age = self._validate_age(new_age)

def test_user_validation_class():
    print("--- Running Test Assertions for Task 3 (User Class Attribute Validation) ---")
    u1 = User("Roger A Raju", "roger@example.com", 20)
    profile = u1.get_profile()
    assert profile["username"] == "Roger A Raju", "Test 1 Failed"
    assert profile["email"] == "roger@example.com", "Test 1 Failed"
    assert profile["age"] == 20 and profile["is_adult"] is True, "Test 1 Failed"
    print(f"Assertion 1 Passed: Valid User created -> {profile}")
    
    invalid_emails = ["invalid-email", "user@", "@domain.com", "user@domain"]
    for bad_email in invalid_emails:
        try:
            User("TestUser", bad_email, 25)
            assert False, f"Failed to reject bad email: {bad_email}"
        except ValueError:
            pass
    print("Assertion 2 Passed: Malformed email formats successfully rejected by regex conditional.")
    
    try:
        User("JohnDoe", "john@gmail.com", -5)
        assert False, "Failed to reject negative age"
    except ValueError as e:
        print(f"Assertion 3 Passed: Negative age rejected -> {e}")
        
    try:
        User("AncientOne", "ancient@history.org", 150)
        assert False, "Failed to reject age > 120"
    except ValueError as e:
        print(f"Assertion 4 Passed: Unrealistic age (> 120) rejected -> {e}")
        
    u2 = User("Alice", "alice@school.edu", 15)
    assert u2.get_profile()["is_adult"] is False, "Test 5 Failed"
    u2.update_age(19)
    assert u2.get_profile()["is_adult"] is True, "Test 5 Failed"
    print("Assertion 5 Passed: Dynamic attribute update and is_adult conditional evaluation verified.")
    
    print("All 5 Task 3 Assertions passed successfully!")

if __name__ == "__main__":
    test_user_validation_class()
