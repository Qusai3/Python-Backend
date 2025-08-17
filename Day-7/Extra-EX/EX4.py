class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return self.title + " by " + self.author + " (ISBN: " + self.isbn + ")"

class Library:
    def __init__(self):  
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added:", book.title)

    def remove_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                self.books.remove(b)
                print("Book removed:", b.title)
                return
        print("Book not found.")

    def list_books(self):
        if not self.books:
            print("No books in library.")
        else:
            for b in self.books:
                print(b.display_info())


lib = Library()
b1 = Book("MVC.NET", "Qusai", "12345")
b2 = Book("Python Fund", "Bassem", "67890")

lib.add_book(b1)
lib.add_book(b2)
lib.list_books()
lib.remove_book("12345")