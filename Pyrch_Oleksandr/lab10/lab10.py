class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f"Книга: {self.title} автора {self.author}"

    def __str__(self):
        return f"'{self.title}' авторства {self.author}"

    def __repr__(self):
        return f"Книга('{self.title}', '{self.author}')"

class PrintedBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self._pages = pages  

    @property
    def pages(self):
        """Отримати кількість сторінок."""
        return self._pages

    @pages.setter
    def pages(self, value):
        """Встановити кількість сторінок, перевіряючи їх коректність."""
        if isinstance(value, int) and value > 0:
            self._pages = value
        else:
            raise ValueError("Кількість сторінок має бути додатнім цілим числом.")

    @pages.deleter
    def pages(self):
        """Видалити кількість сторінок."""
        print(f"Видалення кількості сторінок для книги '{self.title}'")
        self._pages = None

    def info(self):
        return f"{super().info()}, Кількість сторінок: {self.pages}"

# Приклад використання
try:
    book = PrintedBook("National Geographic", "Susan Goldberg", "January 2024")
    print(book.pages)  # Отримання кількості сторінок (з використанням getter'а)

    book.pages = 200  # Встановлення нової кількості сторінок (з використанням setter'а)
    print(book.pages)

    del book.pages  # Видалення кількості сторінок (з використанням deleter'а)
    print(book.pages)  # None або значення за замовчуванням, яке встановлено за допомогою deleter'а

    book.pages = -100  # Спроба встановлення неприпустимого значення
except ValueError as e:
    print(e)