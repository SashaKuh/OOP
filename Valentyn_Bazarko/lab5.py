class Plus:
    def __init__ (self, a, b):
        self.a = a
        self.b = b

    def dodavannya(self):
        suma = self.a + self.b
        if suma >= 15:
            return "Умова  виконана"
        else:
            return "Умова не виконана"
    

my_plus = Plus(10, 5)
print(my_plus.dodavannya())

