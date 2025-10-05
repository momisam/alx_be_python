# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize the account balance (default = 0)
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if enough balance."""
        if amount > self._account_balance:
            return False  # Not enough funds
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self._account_balance -= amount
            return True  # Withdrawal successful

    def display_balance(self):
        """Show the current account balance."""
        print(f"Current Balance: ${self._account_balance}")
