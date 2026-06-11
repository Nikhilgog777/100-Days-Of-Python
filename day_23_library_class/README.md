# Problem: Create a Library class that can add, remove, and list books (use a list of Book objects).
## Solution: 
- In main.py
## Notes:
- OOP Relationship: Demonstrates Composition where a Library object contains and manages a list of individual Book objects.
- Encapsulation: Keeps data safe by forcing all modifications (adding/removing) through official class methods rather than modifying the list directly.

##### 1. Book Class
  - Data Storage: Holds three core properties for every book: title, author, and isbn.
  - String Formatting: Uses __str__ to automatically format how the book details look when printed.
##### 2. Library Class
  - Initialization: Creates an empty internal list (self.books) to store the book objects.
  - `add_book` Method: Appends a new Book instance directly to the end of the collection list.
  - `remove_book` Method: Searches the list by a unique ISBN identifier; deletes the item if found.
  - `list_books` Method: Loops through the list to print every item, or prints a fallback message if empty.
