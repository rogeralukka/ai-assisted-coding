"""
Task 1: Privacy in API Usage
AI Assisted Coding Lab 5

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

import os

def get_weather_secure(city, api_key=None):
    """
    Fetches weather data securely using environment variables.
    Prevents hardcoded API credentials from leaking into repositories.
    """
    if api_key is None:
        api_key = os.environ.get("OPENWEATHER_API_KEY")

    if not api_key:
        return "Error: Missing API Key. Set 'OPENWEATHER_API_KEY' environment variable."

    if not city or not isinstance(city, str):
        return "Error: Invalid city name provided."

    masked_key = f"{api_key[:4]}****{api_key[-4:]}" if len(api_key) >= 8 else "****"
    return f"Securely connecting to Weather API for '{city}' using key '{masked_key}'."


def test_weather_privacy():
    print("--- Running Test Assertions for Task 1 (Privacy in API Usage) ---")
    
    # Test Case 1: Missing API key handling
    os.environ.pop("OPENWEATHER_API_KEY", None)
    res_missing = get_weather_secure("Hyderabad")
    assert "Error: Missing API Key" in res_missing, "Test 1 Failed"
    print("Assertion 1 Passed: Missing environment variable caught safely.")

    # Test Case 2: Environment variable injection
    os.environ["OPENWEATHER_API_KEY"] = "sk_weather_secret_key_998877"
    res_secure = get_weather_secure("Hyderabad")
    assert "Securely connecting" in res_secure, "Test 2 Failed"
    print("Assertion 2 Passed: Successfully loaded key from environment variable.")

    # Test Case 3: Key masking in logs
    assert "sk_w****8877" in res_secure, "Test 3 Failed"
    print("Assertion 3 Passed: Secret key masked in log output.")

    # Test Case 4: Invalid city validation
    assert "Error: Invalid city" in get_weather_secure("", "dummy_key"), "Test 4 Failed"
    print("Assertion 4 Passed: Invalid city parameter handled gracefully.")

    print("All 4 Assertions passed successfully!")


def main():
    print("=== Task 1: Privacy in API Usage (Environment Variables) ===")
    print("Observed Risk: Hardcoded API credentials expose account quota and secrets in code repositories.")
    print("Applied Fix: Loaded credentials dynamically via os.environ with fallback validation and masking.\n")
    test_weather_privacy()


if __name__ == "__main__":
    main()
