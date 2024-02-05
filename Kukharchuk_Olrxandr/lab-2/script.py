import random

# Створюємо дві змінні
number = 2
greeting = 'Hello world!'
print(greeting, number)

# Використання динамічної типізації
strings = int(len(greeting))
print(type(strings))

# Базові операції
num1 = 100
num2 = 10
print(f'Додавання: {num1 + num2}\nВіднімання: {num1 - num2}\nМноження: {num1 * num2}\nДілення: {num1 / num2} \nДілення націло: {num1 // 3} \nОстача від ділення: {num2 % 3}')

# Список, що містить різні типи даних
my_list = [1, 2, 3, 4, True, '4', '5', True, '6', 7.2, 8.984, 9, True, False, 'Like', 'Day']
print(f"Весь список: {my_list}\nВиведення випадкового елементу зі списку: {my_list[random.randint(0, 15)]}")

# Операції над рядками
my_str = 'OOP'
print(my_str * 5)
print(my_str + ' ' + 'Супер')
print(my_str[0])
print(my_str[0:3])

# Підрахунок кількості букв "о" у рядку
count = 0
for char in my_str:
    if char == 'о':
        count += 1
print(f'У рядку міститься {count} букв "о"')

# Робота із словниками
my_dict = {
    'Саша': 5,
    'Назар': 4,
    'Влад': 3
}
print(my_dict)
print(my_dict['Саша'])
my_dict.pop('Саша')
print(my_dict)
print(my_dict.get('Влад'))
