class Book:
    def __init__(self, title, author, year):
        # Ініціалізуємо атрибути книги: назва, автор, рік видання
        self.title = title
        self.author = author
        self.year = year

    @classmethod
    def create_from_year(cls, title, publication_year, author):
        # Альтернативний конструктор, що створює об'єкт книги на основі року видання
        age = 2024 - publication_year  # Обчислюємо вік книги
        return cls(title, author, age)

# Створюємо книгу за допомогою альтернативного конструктора
book1 = Book.create_from_year("Harry Potter", 2001, "J.K. Rowling")
print(book1.title, book1.year, book1.author)

class Library:
    book_count = 0

    def __init__(self, title, author, year):
        # Ініціалізуємо атрибути книги в бібліотеці та збільшуємо лічильник книг
        self.title = title
        self.author = author
        self.year = year
        Library.book_count += 1

    @classmethod
    def get_books_count(cls):
        # Метод класу, що повертає кількість книг в бібліотеці
        return cls.book_count

# Виводимо кількість книг в бібліотеці
print(Library.get_books_count())
book2 = Library("Lord of the Rings", "J.R.R. Tolkien", 1954)
book3 = Library("The Great Gatsby", "F. Scott Fitzgerald", 1925)
# Виводимо кількість книг після додавання нових книг
print(Library.get_books_count())

class BookParser:
    def __init__(self, title, author, year):
        # Ініціалізуємо атрибути книги
        self.title = title
        self.author = author
        self.year = year

    @classmethod
    def create_from_string(cls, string):
        # Альтернативний конструктор, що створює об'єкт книги з рядка
        title, author, year = string.split(',')
        return cls(title, author, int(year))

# Створюємо книгу з рядка за допомогою альтернативного конструктора
book4 = BookParser.create_from_string("To Kill a Mockingbird,Harper Lee,1960")
print(book4.title, book4.year, book4.author)

class Calculator:
    @staticmethod
    def addition(x, y):
        # Статичний метод, що виконує додавання чисел
        return x + y

# Викликаємо статичний метод додавання
print(Calculator.addition(5, 3))
