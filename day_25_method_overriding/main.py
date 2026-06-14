# Override the __str__ method for Book and EBook to display nicely.

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        """Initializes a new book instance with core attributes."""
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str :
        """Returns a formatted string representing the book."""
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"
    
class Ebook(Book):
    def __init__(self, title: str, author: str, isbn: str, size: str):
        super().__init__(title,author,isbn)
        self.size = size

    def __str__(self) -> str:
        """Returns the size of the ebook."""
        return f"'{self.title}' by {self.author}' (ISBN: {self.isbn}, File size: {self.size} kb)"

if __name__ == "__main__":
    # Create Instances
    physical_book = Book("The Hobbit", "J.R.R. Tolkien", "978-0048230706")
    digital_book = Ebook("Digital Minimalism", "Cal Newport", "978-0525536543", "302")

    # Print objects (this automatically triggers the __str__ method)
    print("Physical Book Display:")
    print(physical_book)
    
    print("\nEBook Display:")
    print(digital_book)