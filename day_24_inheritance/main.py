#  Use inheritance: make EBook (subclass of Book) with an extra file_size attribute.

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        """Initializes a new book instance with core attributes."""
        self.title = title
        self.author = author
        self.isbn = isbn

    def get_info(self):
        """Returns a formatted string representing the book."""
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"
    
class Ebook(Book):
    def __init__(self, title: str, author: str, isbn: str, size: str):
        super().__init__(title,author,isbn)
        self.size = size

    def get_info(self):
        """Returns the size of the ebook."""
        return f"'{self.title}' by {self.author}' (ISBN: {self.isbn}, File size: {self.size} kb)"

book1 = Book("The Hobbit", "J.R.R. Tolkien", "978-0261102217")
book2 = Book("1984", "George Orwell", "978-0451524935")
book3 = Ebook("To Kill a Mockingbird", "Harper Lee", "978-0061120084", "300")
book4 = Ebook("The Alchemist", "Paulo Coelho", "978-0061122415", "565")

print(book1.get_info())
print(book3.get_info())
print(book4.get_info())