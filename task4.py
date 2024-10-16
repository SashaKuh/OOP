
def add_numbers(a, b):
    return a + b


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def greet(name):
    return "Привіт, " + name + "!"

print(add_numbers(5, 3))  # Виведе 8

print(factorial(5))  # Виведе 120
print(greet("Вася"))  # Виведе "Привіт, Вася!"

