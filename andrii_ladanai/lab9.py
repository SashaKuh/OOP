class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Book: {self.title} by {self.author}"

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

class EBook(Book):
    def __init__(self, title, author, file_format):
        super().__init__(title, author)
        self.file_format = file_format

    def display_info(self):
        info = super().display_info()
        return f"{info}, Format: {self.file_format}"

    def __str__(self):
        return f"EBook: '{self.title}' by {self.author}, Format: {self.file_format}"

    def __repr__(self):
        return f"EBook('{self.title}', '{self.author}', '{self.file_format}')"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.file_format == other.file_format

class PrintedBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def display_info(self):
        info = super().display_info()
        return f"{info}, Pages: {self.pages}"

    def __str__(self):
        return f"Printed Book: '{self.title}' by {self.author}, Pages: {self.pages}"

    def __repr__(self):
        return f"PrintedBook('{self.title}', '{self.author}', {self.pages})"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.pages == other.pages

    def __lt__(self, other):
        if isinstance(other, PrintedBook):
            return self.pages < other.pages
        return NotImplemented

# Приклад використання магічних методів
book1 = EBook("1984", "George Orwell", "PDF")
book2 = PrintedBook("1984", "George Orwell", 328)

print(book1)  # Виклик __str__
print(book2)  # Виклик __str__

print(repr(book1))  # Виклик __repr__
print(repr(book2))  # Виклик __repr__


# Сортування
books = [PrintedBook("Animal Farm", "George Orwell", 112), PrintedBook("1984", "George Orwell", 328)]
print(sorted(books))  # Використовує __lt__ для порівняння
