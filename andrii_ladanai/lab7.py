class Book:
    total_books = 0  # Класова змінна для підрахунку книг

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        Book.total_books += 1

    @classmethod
    def from_year(cls, title, year_published):
        current_year = 2023
        pages = current_year - year_published + 1  # Кожен рік додає одну сторінку
        return cls(title, pages)

    @classmethod
    def get_total_books(cls):
        print(f"Total books created: {cls.total_books}")

    @staticmethod
    def is_even_pages(pages):
        return pages % 2 == 0

# Приклад використання класу
book1 = Book("Python Programming", 250)
book2 = Book.from_year("History of Ukraine", 2010)
print(f"Book: {book2.title}, Pages: {book2.pages}")

Book.get_total_books()

print("Is the number of pages even?:", Book.is_even_pages(book1.pages))
