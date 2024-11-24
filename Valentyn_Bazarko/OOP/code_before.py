class Animal:
    def __init__(self, n, a):
        self.n = n
        self.a = a

    def an_name(self):
        return self.n
    
    def an_age(self):
        return self.a
    
    def __str__(self):
        return f"Ім'я тварини {self.n} а її вік {self.a}"

a = Animal("Кіт", 7)
print(a)
