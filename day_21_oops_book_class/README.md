# Problem: Define a Book class with attributes title, author, and year. Print a book’s info.
## Solution:
- In main.py
## Notes:
- ```class``` is a template or schema used to define the structure of data and behavior.
  
   - class Book: creates the blueprint. It doesn’t create a real book yet; it just defines what a book looks like.
- `__init__()` is a special initialization method that runs automatically when a new object is born.
  
  - ```def __init__(self, title, author, year)``` : acts as the configuration screen, forcing you to provide data when making a book.
- `self` is a keyword that points to the specific, individual object you are dealing with right now.
  
  - ```self.title = title``` means "Take the title passed into this specific book instance and save it."
- Attributes are variables tied to an object that hold data or states.

  - `self.title`, `self.author`, and `self.year` are instance attributes.
- `book1 = Book("1984", "George Orwell", 1949)` creates a real, memory-allocated object.
