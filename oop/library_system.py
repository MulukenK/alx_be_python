class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
class EBook(Book):
    def __init__(self, file_size):
        self.file_size = file_size
        super().__init__()

class PrintBook(Book):
    def __init__(self, page_count):
        self.page_count = page_count
        super().__init__()

class Library():
    def __init__(self, book):
        book = []
        self.book = book
    
    def add_book(self, book):
        self.book = book
    
    def list_books(self):
        for items in self.book:
            print(items)