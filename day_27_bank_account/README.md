# Problem: Write a BankAccount class with private __balance and methods deposit, withdraw, get_balance.
## Solution:
- In main.py
## 🧠 Core Challenge Concept: Encapsulation

**Encapsulation** is one of the four fundamental principles of Object-Oriented Programming. It refers to the practice of bundling data (attributes) and methods (functions) that operate on that data into a single unit (a class) while **restricting direct access** to some of the object's components.

### Why Encapsulation Matters
* **Data Protection**: It prevents external code from accidentally or maliciously modifying internal object states into an invalid configuration (e.g., setting a bank balance to a negative number).
* **Controlled Access**: Changes to internal data can only happen through specific, well-defined pathways (methods) that enforce business logic rules.
* **Maintainability**: The internal implementation can be changed without breaking code that relies on the class, as long as the public interface remains identical.

---

## 💻 Code Architecture Breakdown

### 1. Name Mangling (Private Attributes)
In Python, there is no strict `private` keyword like in Java or C++. Instead, privacy is enforced conceptually using underscores:
* **`self._balance` (Single Underscore)**: A convention indicating an attribute is intended for internal use. It does not actively block access.
* **`self.__balance` (Double Underscore)**: Triggers Python's **Name Mangling** mechanism. Python automatically changes the variable name internally to `_ClassName__VariableName` (e.g., `_BankAccount__balance`). This prevents direct external lookup via standard dot notation.

### 2. Guard Clauses & Input Validation
Public methods act as "gatekeepers" to the private data. 
* **Deposits**: Ensure that only positive values are added to the balance.
* **Withdrawals**: Ensure the transaction amount is positive and that the account possesses sufficient funds to cover the request.

---

## 📝 Syntax Reference & Explanation

| Component | Code Implementation | Purpose / Responsibility |
| :--- | :--- | :--- |
| **Constructor** | `def __init__(self, initial_balance=0.0):` | Initializes new instances and enforces a standard starting state. |
| **Private Field** | `self.__balance = float(initial_balance)` | Holds the state securely; hidden via Python name mangling. |
| **Setter / Modifier** | `def deposit(self, amount):` | Public entry point to safely increment the private data. |
| **Setter / Modifier** | `def withdraw(self, amount):` | Public entry point to safely decrement data after passing rule checks. |
| **Getter Method** | `def get_balance(self):` | Provides standard, read-only visualization of internal data. |

---

## 🚫 Common Mistakes & Anti-Patterns

```python
# ❌ ANTI-PATTERN: Direct Modification
# This circumvents all security rules and introduces bugs
my_account.__balance = -50000.00 

# ❌ ANTI-PATTERN: Bypassing Mangling
# While technically possible via mangled names, this breaks encapsulation design rules
my_account._BankAccount__balance = -50000.00 

#  BEST PRACTICE: Use Designed Accessors
my_account.deposit(50.00)
current_funds = my_account.get_balance()
```
