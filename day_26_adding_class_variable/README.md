# Problem: Add a class variable total_books to Book that counts every instance created.
## Solution:
- In main.py
## Core Concepts

*   **Class Variable**: A variable declared directly inside a class body (outside any methods) that is shared by all instances of that class.
*   **Instance Variable**: Variables tied to specific objects (like `self.title`), where each object holds its own independent data.
*   **Shared State**: Modifying a class variable updates the value for the entire class and all its objects simultaneously.

---

## Code Architecture Notes

### 1. Defining the Counter
*   `total_books = 0` is initialized at the top of the `Book` class. 
*   It acts as a global counter restricted to the scope of the `Book` blueprint.

### 2. The No-`super()` Increment Mechanic
Because `EBook` does not call `super().__init__()`, the parent constructor is bypassed entirely. To count instances accurately, the tracking must be split:
*   **Inside `Book.__init__`**: `Book.total_books += 1` fires when physical books are made.
*   **Inside `EBook.__init__`**: `Book.total_books += 1` must be typed manually to ensure digital books are also tracked.

---

## Visual Data Flow

```text
[ Book.total_books = 0 ]
        │
        ├──► Create physical_book ──► Triggers Book.__init__  ──► Count becomes 1
        │
        └──► Create digital_book  ──► Triggers EBook.__init__ ──► Count becomes 2
```

---

## Key Rules for Usage

*   **Access via Class Name**: Always read or modify the variable using `Book.total_books` instead of `self.total_books` to avoid accidentally creating unintended instance overrides.
*   **Shared Inheritance**: Since `EBook` inherits from `Book`, calling `EBook.total_books` will show the exact same count as `Book.total_books`.
