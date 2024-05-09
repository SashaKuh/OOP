class Plus:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        total = self.num1 + self.num2
        if total >= 15:
            return "Умова виконана"
        else:
            return "Умова не виконана"

my_sum = Plus(10, 5)
print(my_sum.addition())