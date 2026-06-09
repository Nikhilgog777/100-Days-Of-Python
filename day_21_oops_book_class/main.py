# Define a Book class with attributes title, author, and year. Print a book’s info.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")

book1 = Book("1984", "George Orwell", 1949)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
book3 = Book("Pride and Prejudice", "Jane Austen", 1813)

Book.display_info(book2)
Book.display_info(book3)