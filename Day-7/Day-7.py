class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self): 
        self.books = []  

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print("Book added:", title)

    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print("Title: ",book.title, "Author:", book.author)  

library = Library()

library.add_book("MVC.NET", "Qusai")
library.add_book("Python Fund", "Bassem")



library.show_books() 