class Book: 
    def init(self, title, author, pages):
        self.title = title 
        self.author = author
        self.pages = pages

        def get_info(self):
            return f"{self.title} by {self.author}"

class Fiction(Book):
    def init(self, title, author, pages, genre):
        super().init(title, author, pages)
        self.genre = genre 

    def get_info(self):
        return f"{super().get_info()}, Genre: {self.genre}"
    
class NonFiction(Book):
    def init(self, title, author, pages, topic):
        super().init(title, author, pages) 
        self.topic = topic

    def get_info(self):
        return f"{super().get_info()}, Topic: {self.topic}" 
    
fiction_book = Fiction("The Great Gatsby", "F. Scott Fitzerland", 180, "Classic")
non_fiction_book = NonFiction("Sapiens", "Yuval Noah Harari", 400, "History")

print(fiction_book.get_info())
print(non_fiction_book.get_info())