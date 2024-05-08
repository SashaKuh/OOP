class Candy:
    def __init__(self, name, manufactur, taste):
        self.name = name
        self.manufactur = manufactur
        self.taste = taste
    def candy_name(self):
        return self.name
    def name_of_manufactur(self):
        return self.manufactur
    def what_a_taste(self):
        if self.taste > 4:
            return "Солодка"
        else:
            return "Кисла"
my_class = Candy("Ліщина", "Roshen", 5)
print(my_class.candy_name())
print(my_class.name_of_manufactur())
print(my_class.what_a_taste())