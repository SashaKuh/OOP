def hello():
    print("Привіт, світ!")
hello()

#Поняття параметрів та аргументів функції 
def greet(name):
    print("Привіт, " + name + "!")
greet("Назар")

#Методи роботи з функціями
def square(x):
    return x * x

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

print(my_map(square, [1, 2, 3, 4, 5]))
print(my_map(cube, [1, 2, 3, 4, 5]))

#Розв'язання задачі
def find_max(numbers):
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

numbers_list = [3, 6, 2, 8, 1, 10, 5]
print("Максимальне число у списку:", find_max(numbers_list))

