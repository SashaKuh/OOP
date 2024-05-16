def check_order(a, b, c):
    if a < b < c:
        return "Значення вірні"
    else:
        return "Значення не вірні"

num1 = 67
num2 = 54
num3 = 89

result = check_order(num1, num2, num3)
print("Результат:", result)

# Функція як параметр у іншій функції
def say_hello(name):
    print("Привіт", name)

def call_function(func):
    func("Олександр")

call_function(say_hello)
