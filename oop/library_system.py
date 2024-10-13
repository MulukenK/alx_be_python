class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, file_size):
        self.file_size = file_size
        super().__init__()
    
    def __str__(self):
        return f"{self.title} by {self.author}, File Size: {self.file_size}"


class PrintBook(Book):
    def __init__(self, page_count):
        self.page_count = page_count
        super().__init__()
    
    def __str__(self):
        return f"{self.title} by {self.author}, Page Count: {self.page_count}"

class Library():
    def __init__(self, book):
        book = []
        self.book = book
    
    def add_book(self, book):
        self.book = book
    
    def list_books(self):
        for items in self.book:
            print(items)