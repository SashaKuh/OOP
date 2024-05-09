class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Book: {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title, author, file_format):
        super().__init__(title, author)
        self.file_format = file_format

    def display_info(self):
        info = super().display_info()
        return f"{info}, Format: {self.file_format}"
    
class PrintedBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def display_info(self):
        info = super().display_info()
        return f"{info}, Pages: {self.pages}"

class BookStore:
    def __init__(self):
        self.books = []

    def add_ebook(self, title, author, file_format):
        ebook = EBook(title, author, file_format)
        self.books.append(ebook)
        print("EBook added:", ebook.display_info())

    def add_printed_book(self, title, author, pages):
        pbook = PrintedBook(title, author, pages)
        self.books.append(pbook)
        print("Printed Book added:", pbook.display_info())


ebook = EBook("1984", "George Orwell", "PDF")
print(isinstance(ebook, Book))  # True
print(isinstance(ebook, PrintedBook))  # False
print(issubclass(PrintedBook, Book))  # True