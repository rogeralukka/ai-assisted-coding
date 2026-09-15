"""
Task 4: Inventory Class – Apply AI to Simulate Real-World Inventory System
AI Assisted Coding Lab 8 (Test-Driven Development with AI)

Name: Roger A Raju
Roll No: 2503a52370
Batch: 13
"""

class Inventory:
    """
    Manages stock levels for items with robust boundary and error handling:
    - add_item(name, quantity): Increases stock quantity (validates positive quantity)
    - remove_item(name, quantity): Decreases stock (prevents negative stock, returns success bool)
    - get_stock(name): Returns current stock count (returns 0 for unrecorded items)
    """
    def __init__(self):
        self._stock = {}

    def add_item(self, name: str, quantity: int) -> bool:
        """Adds a positive quantity of an item to inventory."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity to add must be a positive integer.")

        name_key = name.strip()
        self._stock[name_key] = self._stock.get(name_key, 0) + quantity
        return True

    def remove_item(self, name: str, quantity: int) -> bool:
        """
        Removes a quantity of an item if sufficient stock exists.
        Returns True if successful, False if insufficient stock or item missing.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity to remove must be a positive integer.")

        name_key = name.strip()
        current = self._stock.get(name_key, 0)
        if current >= quantity:
            self._stock[name_key] -= quantity
            return True
        else:
            # Cannot reduce stock below zero
            return False

    def get_stock(self, name: str) -> int:
        """Returns the current available quantity for the specified item."""
        if not isinstance(name, str):
            return 0
        return self._stock.get(name.strip(), 0)


def test_inventory_system():
    print("--- Running AI-Generated TDD Assertions for Task 4 ---")
    inv = Inventory()

    # Step 1: Add initial item
    inv.add_item("Pen", 10)
    assert inv.get_stock("Pen") == 10, "Test 1 Failed"
    print("Assertion 1 Passed: inv.add_item('Pen', 10) -> inv.get_stock('Pen') == 10")

    # Step 2: Remove portion of stock
    remove_success = inv.remove_item("Pen", 5)
    assert remove_success == True, "Removal should succeed"
    assert inv.get_stock("Pen") == 5, "Test 2 Failed"
    print("Assertion 2 Passed: inv.remove_item('Pen', 5) -> inv.get_stock('Pen') == 5")

    # Step 3: Add second distinct item
    inv.add_item("Book", 3)
    assert inv.get_stock("Book") == 3, "Test 3 Failed"
    print("Assertion 3 Passed: inv.add_item('Book', 3) -> inv.get_stock('Book') == 3")

    # Step 4 (Edge Case): Over-withdrawal prevention
    over_remove = inv.remove_item("Book", 10)
    assert over_remove == False, "Over-withdrawal should be rejected"
    assert inv.get_stock("Book") == 3, "Stock must remain unchanged"
    print("Assertion 4 Passed: Over-removal rejected safely (Stock remains 3).")

    # Step 5 (Edge Case): Non-existent item stock query
    assert inv.get_stock("Eraser") == 0, "Test 5 Failed"
    print("Assertion 5 Passed: inv.get_stock('Eraser') == 0 (Unseen item returns 0).")

    print("All AI-Generated Assertions passed successfully!")


def main():
    print("=== Task 4: Inventory Management Class (TDD) ===")
    print("Simulating stock lifecycle: add, remove, query, and edge guard checks.\n")
    test_inventory_system()


if __name__ == "__main__":
    main()
