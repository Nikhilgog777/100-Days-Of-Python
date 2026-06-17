#  Write a BankAccount class with private __balance and methods deposit, withdraw, get_balance.

class BankAccount:
    def __init__(self, initial_balance=0.0):
        # Private attribute to prevent direct external access
        self.__balance = float(initial_balance)

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

    def get_balance(self):
        """Provides safe, read-only access to the private balance."""
        return self.__balance


# Create an account with a starting balance of $100
my_account = BankAccount(100.0)

# Check the balance safely
print(f"Initial Balance: ${my_account.get_balance():.2f}") 
# Output: Initial Balance: $100.00

# Perform transactions
my_account.deposit(50.0)    # Output: Successfully deposited: $50.00
my_account.withdraw(30.0)   # Output: Successfully withdrew: $30.00

# Try to overdraw funds
my_account.withdraw(200.0)  # Output: Error: Insufficient funds available.

# Print final status
print(f"Final Balance: ${my_account.get_balance():.2f}") 
# Output: Final Balance: $120.00

# Proof of encapsulation (This will raise an AttributeError)
try:
    print(my_account.__balance)
except AttributeError as e:
    print(f"Access Denied: {e}")
