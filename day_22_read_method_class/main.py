# Add a read() method to Book that changes a is_read flag and prints a message.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_read = False # Default Method 

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")    
    
    def read(self): 
        self.is_read = True # Method after reading
        print(f"You have succesfully read {self.title} by {self.author}")


book1 = Book("1984", "George Orwell", 1949)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
book3 = Book("Pride and Prejudice", "Jane Austen", 1813)

book1.read() # Read function used to tell that the book is read.

print(book1.is_read)  # Outputs True because user have read the book
print(book2.is_read)  # Outputs False because book2 is still unread
