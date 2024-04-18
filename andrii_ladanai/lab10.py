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

class PrintedBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self._pages = pages  # Інкапсуляція: змінна тепер є приватною

    @property
    def pages(self):
        """Getter для кількості сторінок."""
        return self._pages

    @pages.setter
    def pages(self, value):
        """Setter для кількості сторінок, який перевіряє, чи значення є допустимим."""
        if isinstance(value, int) and value > 0:
            self._pages = value
        else:
            raise ValueError("Кількість сторінок має бути додатним цілим числом.")

    @pages.deleter
    def pages(self):
        """Deleter, який "видаляє" кількість сторінок, насправді встановлюючи значення в None."""
        print(f"Видалення кількості сторінок для книги '{self.title}'")
        self._pages = None

    def display_info(self):
        return f"{super().display_info()}, Pages: {self.pages}"

# Приклад використання
try:
    book = PrintedBook("1984", "George Orwell", 328)
    print(book.pages)  # Використання getter'а

    book.pages = 200  # Використання setter'а
    print(book.pages)

    del book.pages  # Використання deleter'а
    print(book.pages)  # None або дефолтне значення, яке встановлено deleter'ом

    book.pages = -100  # Спроба встановити недопустиме значення
except ValueError as e:
    print(e)
