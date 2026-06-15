# Add a class variable total_books to Book that counts every instance created.

class Book:
    # Class variable shared by all instances
    total_books = 0

    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        # Increment the counter every time a new Book is initialized
        Book.total_books += 1

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author} ({self.pages} pages)"


class EBook(Book):
    def __init__(self, title: str, author: str, pages: int, file_format: str):
        # Explicitly assign attributes (No super() used)
        self.title = title
        self.author = author
        self.pages = pages
        self.file_format = file_format
        # Manually increment parent class counter since super().__init__() is not called
        Book.total_books += 1

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author} ({self.pages} pages) [Format: {self.file_format}]"


# --- Example Usage ---
if __name__ == "__main__":
    print(f"Books before creation: {Book.total_books}")  # Outputs: 0

    book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
    book2 = EBook("Digital Minimalism", "Cal Newport", 302, "EPUB")

    print(f"Books after creation: {Book.total_books}")   # Outputs: 2
