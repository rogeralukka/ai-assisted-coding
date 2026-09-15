"""
Task 4: Calling a Non-Existent Method
AI Assisted Coding Lab 7.1

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

class Car:
    """
    Comprehensive Car class providing start, drive, and stop methods.
    Addresses both fixing the missing method definition and properly calling existing methods.
    """
    def __init__(self, brand="Tesla", model="Model 3"):
        self.brand = brand
        self.model = model
        self.is_running = False
        self.speed = 0

    def start(self):
        """Starts the car engine."""
        self.is_running = True
        return f"{self.brand} {self.model}: Car started"

    def drive(self, target_speed=40):
        """
        Defines the previously missing drive() method.
        Automatically starts the car if not already running and sets speed.
        """
        if not self.is_running:
            self.start()
        self.speed = target_speed
        return f"{self.brand} {self.model}: Car is driving at {self.speed} km/h"

    def stop(self):
        """Stops the car and resets speed."""
        self.is_running = False
        self.speed = 0
        return f"{self.brand} {self.model}: Car stopped"

def test_car_methods():
    print("--- Running Test Assertions for Task 4 ---")
    my_car = Car("Tesla", "Model 3")

    # Test Case 1: Testing start() method
    assert my_car.start() == "Tesla Model 3: Car started", "Test 1 Failed"
    print("Assertion 1 Passed: my_car.start() -> 'Tesla Model 3: Car started'")

    # Test Case 2: Testing drive() method (previously undefined method)
    assert my_car.drive(60) == "Tesla Model 3: Car is driving at 60 km/h", "Test 2 Failed"
    print("Assertion 2 Passed: my_car.drive(60) -> 'Tesla Model 3: Car is driving at 60 km/h'")

    # Test Case 3: Testing stop() method
    assert my_car.stop() == "Tesla Model 3: Car stopped", "Test 3 Failed"
    print("Assertion 3 Passed: my_car.stop() -> 'Tesla Model 3: Car stopped'")

    # Test Case 4: Default instance
    default_car = Car()
    assert default_car.drive() == "Tesla Model 3: Car is driving at 40 km/h"
    print("Assertion 4 Passed: default_car.drive() works with default values.")
    print("All Assertions passed successfully!")

def main():
    print("=== Task 4: Resolving Undefined Method (AttributeError) ===")
    print("Observed Bug: Calling undefined method 'my_car.drive()' raised AttributeError.")
    print("Applied Fix: Defined comprehensive drive(speed) method inside Car class.\n")
    test_car_methods()

if __name__ == "__main__":
    main()
