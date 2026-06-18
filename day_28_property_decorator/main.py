# – Use @property to make balance a readable property (no setter).

class BankAccount:
    def __init__(self, initial_balance=0.0):
        # Private attribute to prevent direct external access
        self.__balance = float(initial_balance)

    @property
    def balance(self):
        """Makes balance readable as an attribute, but blocks direct writing."""
        return self.__balance

    def deposit(self, amount):
        """Adds a valid, positive amount to the account balance."""
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited: ${amount:.2f}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deducts funds if amount is valid and coverage is available."""
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Error: Insufficient funds available.")
        else:
            self.__balance -= amount
            print(f"Successfully withdrew: ${amount:.2f}")

account = BankAccount(100.0)

# ✅ Read access looks clean (no parentheses needed)
print(account.balance)  # Output: 100.0

# ❌ Direct modifications are blocked by Python automatically
try:
    account.balance = 5000.0
except AttributeError as e:
    print(f"Blocked: {e}")  # Output: Blocked: property 'balance' of 'BankAccount' object has no setter
