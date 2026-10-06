from typing import List, Dict, Any

class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        if not account_holder or not isinstance(account_holder, str):
            raise ValueError("Account holder name must be a non-empty string.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
            
        self.account_holder = account_holder
        self.balance = float(initial_balance)
        self.transactions: List[Dict[str, Any]] = []
        self._record_transaction("OPENING_BALANCE", self.balance, self.balance, "Account created")
        
    def _record_transaction(self, tx_type: str, amount: float, current_bal: float, status: str) -> None:
        self.transactions.append({
            "id": len(self.transactions) + 1,
            "type": tx_type,
            "amount": amount,
            "balance_after": current_bal,
            "status": status
        })
        
    def deposit(self, amount: float) -> bool:
        if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount <= 0:
            self._record_transaction("DEPOSIT_FAILED", amount, self.balance, "Invalid deposit amount")
            return False
        self.balance += float(amount)
        self._record_transaction("DEPOSIT", float(amount), self.balance, "Success")
        return True
        
    def withdraw(self, amount: float) -> bool:
        if not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount <= 0:
            self._record_transaction("WITHDRAW_FAILED", amount, self.balance, "Invalid withdrawal amount")
            return False
        if amount > self.balance:
            self._record_transaction("WITHDRAW_REJECTED", float(amount), self.balance, "Insufficient funds")
            return False
            
        self.balance -= float(amount)
        self._record_transaction("WITHDRAWAL", float(amount), self.balance, "Success")
        return True
        
    def process_batch_operations(self, operations: List[Dict[str, Any]]) -> Dict[str, int]:
        success_count = 0
        failed_count = 0
        for op in operations:
            op_type = op.get("type", "").upper()
            amt = op.get("amount", 0.0)
            if op_type == "DEPOSIT":
                if self.deposit(amt):
                    success_count += 1
                else:
                    failed_count += 1
            elif op_type == "WITHDRAW":
                if self.withdraw(amt):
                    success_count += 1
                else:
                    failed_count += 1
            else:
                failed_count += 1
        return {
            "total_processed": len(operations),
            "successful_operations": success_count,
            "failed_operations": failed_count,
            "final_balance": self.balance
        }

def test_bank_account_system():
    print("--- Running Test Assertions for Task 5 (Bank Account System Completion Review) ---")
    account = BankAccount("Roger A Raju", 1000.0)
    assert account.balance == 1000.0, "Test 1 Failed"
    assert len(account.transactions) == 1, "Test 1 Failed"
    print(f"Assertion 1 Passed: Account opened for '{account.account_holder}' with Rs. {account.balance}")
    
    assert account.deposit(500.0) is True, "Deposit failed"
    assert account.balance == 1500.0, "Balance mismatch after deposit"
    assert account.withdraw(300.0) is True, "Withdrawal failed"
    assert account.balance == 1200.0, "Balance mismatch after withdrawal"
    print(f"Assertion 2 Passed: Deposit (+Rs. 500) & Withdrawal (-Rs. 300) -> Balance: Rs. {account.balance}")
    
    assert account.withdraw(5000.0) is False, "Test 3 Failed: Overdraft permitted"
    assert account.balance == 1200.0, "Test 3 Failed: Balance modified on overdraft"
    print("Assertion 3 Passed: Overdraft of Rs. 5000 safely rejected by conditional check.")
    
    batch_ops = [
        {"type": "DEPOSIT", "amount": 200.0},
        {"type": "WITHDRAW", "amount": 400.0},
        {"type": "WITHDRAW", "amount": 9999.0},
        {"type": "DEPOSIT", "amount": -50.0},
        {"type": "UNKNOWN", "amount": 100.0}
    ]
    summary = account.process_batch_operations(batch_ops)
    assert summary["successful_operations"] == 2, "Test 4 Failed"
    assert summary["failed_operations"] == 3, "Test 4 Failed"
    assert summary["final_balance"] == 1000.0, "Test 4 Failed"
    print(f"Assertion 4 Passed: Batch Operations Processed -> Success: {summary['successful_operations']}, Failed: {summary['failed_operations']}, Final Bal: Rs. {summary['final_balance']}")
    
    print("All 4 Task 5 Assertions passed successfully!")

if __name__ == "__main__":
    test_bank_account_system()
