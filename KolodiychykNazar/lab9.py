class MyClass:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"Value of x: {self.x}"

    def __add__(self, other):
        return self.x + other
obj = MyClass(5)
print(obj) 
result = obj + 3  
print("Result:", result)


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def __add__(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)
num1 = ComplexNumber(3, 2)
num2 = ComplexNumber(1, 4)

print("Sum:", num1 + num2) 
print("Product:", num1 * num2)  
