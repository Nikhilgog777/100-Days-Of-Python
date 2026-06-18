# Problem: Use @property to make balance a readable property (no setter).

## Solution:
- In main.py
## Notes:

## 🧠 Core Concept: The `@property` Decorator

The **`@property`** decorator is a built-in feature in Python that allows you to define a method but access it precisely like a standard **attribute** (without using parentheses `()`). 

When used without a matching `.setter`, it creates a **read-only property**. This allows you to expose private data cleanly while strictly forbidding external code from overwriting it directly.

### Why Use `@property`?
* **Pythonic Syntax**: It replaces clunky getter methods (like `get_balance()`) with clean, natural attribute access (`balance`).
* **Enforced Read-Only Data**: Attempting to assign a value directly (`account.balance = 500`) triggers an automatic `AttributeError`.
* **Backward Compatibility**: If you start with a public attribute and later need to add validation logic, you can convert it to a `@property` without breaking existing code that uses dot notation.

---

## 💻 Code Anatomy & Comparison

### Old Approach (Getter Method)
```python
# Definition
def get_balance(self):
    return self.__balance

# Usage (Requires parentheses)
current_funds = account.get_balance() 
```

### Modern Approach (Property Decorator)
```python
# Definition
@property
def balance(self):
    """Exposes the internal balance safely as a read-only attribute."""
    return self.__balance

# Usage (Accessed exactly like a variable)
current_funds = account.balance 
```

---

## 🚫 Enforcement Mechanics

Because no setter method (`@balance.setter`) is defined for the property, Python acts as a security guard:

```python
account = BankAccount(100.0)

# ✅ This works perfectly
print(account.balance)  # Output: 100.0

# ❌ This crashes and prevents corruption
account.balance = 500.0  
# Raises -> AttributeError: property 'balance' of 'BankAccount' object has no setter
```

---

## 📝 Key Takeaways for OOP Design
1. Use a **private backend variable** (like `self.__balance`) to hold the actual data.
2. Use **`@property`** to safely expose that data for reading.
3. Use **traditional methods** (like `deposit()` and `withdraw()`) when modifications require arguments and complex business logic validation.
