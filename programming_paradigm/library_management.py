class Book:
    def __init__(self, title, author, is_checked_out = False):
        self.title = title
        self.author = author
        self._is_checked_out = is_checked_out
    
    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self, books):
        self._books = list(books)
    
    def add_book(self, book):
        self._books = self._books.append(book)
    
    def check_out_book(self, book):
        self._books = self._books.remove(book)
    
    def return_book(self, book):
        self._books = self._books.append(book)
    
    def list_available_books(self):
        print(self._books)




    