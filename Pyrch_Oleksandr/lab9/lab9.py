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

class Magazine(Book):
    def __init__(self, title, editor, issue):
        super().__init__(title, editor)
        self.issue = issue

    def display_info(self):
        info = super().display_info()
        return f"{info}, Issue: {self.issue}"

    def __str__(self):
        return f"Magazine: '{self.title}' edited by {self.author}, Issue: {self.issue}"

    def __repr__(self):
        return f"Magazine('{self.title}', '{self.author}', {self.issue})"

class Journal(Book):
    def __init__(self, title, editor, volume):
        super().__init__(title, editor)
        self.volume = volume

    def display_info(self):
        info = super().display_info()
        return f"{info}, Volume: {self.volume}"

    def __str__(self):
        return f"Journal: '{self.title}' edited by {self.author}, Volume: {self.volume}"

    def __repr__(self):
        return f"Journal('{self.title}', '{self.author}', {self.volume})"

# Приклад використання
book1 = Magazine("National Geographic", "Susan Goldberg", "January 2024")
book2 = Journal("Science", "Jeremy M. Berg", "Volume 382")

print(book1)  # Виклик __str__
print(book2)  # Виклик __str__

print(repr(book1))  # Виклик __repr__
print(repr(book2))  # Виклик __repr__