'''
def privitania(name):
    return "Hello, " + name + "!"

dokogo = privitania("python")
print(dokogo)
'''

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def peredacha(operation, x, y):
    return operation(x, y)

result = peredacha(add, 5, 3)
print(":", result)

result1 = peredacha(multiply, 5, 3)
print(":", result1)
