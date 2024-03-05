#приклад простої функції та її виклик
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


#приклад передачі функції в якості параметра
def square(x):
    return x * x

def apply_operation(func, y):
    return func(y)

result = apply_operation(square, 4)


