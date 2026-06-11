#  Create a Library class that can add, remove, and list books (use a list of Book objects).

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        """Initializes a new book instance with core attributes."""
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        """Returns a formatted string representing the book."""
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        """Initializes the library with an empty list of books."""
        self.books = []

    def add_book(self, book: Book):
        """Adds a Book object to the internal list."""
        self.books.append(book)
        print(f"Added: {book}")

    def remove_book(self, isbn: str):
        """Removes a Book object from the list using its unique ISBN."""
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed: {book}")
                return True
        print(f"Error: No book found with ISBN {isbn}.")
        return False

    def list_books(self):
        """Prints all the books currently stored in the library."""
        if not self.books:
            print("The library is currently empty.")
            return

        print(f"\n--- Library Catalog ({len(self.books)} books) ---")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book}")

# 1. Initialize the library
my_library = Library()

# 2. Instantiate some Book objects
book1 = Book("The Hobbit", "J.R.R. Tolkien", "978-0261102217")
book2 = Book("1984", "George Orwell", "978-0451524935")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")

# 3. Add the books to the library
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# 4. List all available books
my_library.list_books()

# 5. Remove a book by its unique ISBN identifier
my_library.remove_book("978-0451524935")

# 6. Verify the updated book list
my_library.list_books()
