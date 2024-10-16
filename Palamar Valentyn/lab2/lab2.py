from random import randint

# Створюю дві змінні
a = 50
b = 'Python'

# Використання динамічної типізації
b = str(b)
print(type(b))

# Базові операції
c = 50
d = 5
print(f'+: {c + d}\n-: {c - d}\n*: {c * d}\n/:{c / d} \n//: {c // 3} \n%: {d % 3}')

# Створюю список, який містить різні типи даних
my_list = [50, False, True, 'Python', 5.0, 'Programming']
print(f"Список: {my_list}\nРандомний елемент: {my_list[randint(0, 5)]}")

# Операції над списками
my_list.append('New Element')
print(my_list)
copy_list = my_list.copy()
print(copy_list)
print(copy_list.count(True))
print(copy_list.pop())
copy_list.clear()
print(copy_list)

# Робота зі стрічками
my_str = 'Python is great'
print(my_str * 2)
print(my_str + ' ' + 'Programming')
print(my_str[0])
print(my_str[0:6])
count = 0
for i in my_str:
    if i == 't':
        count += 1
print(f'Кількість "t": {count}')

# Робота зі словниками
my_dict = {
    'Language': 5,
    'Platform': 4,
    'Library': 3
}
print(my_dict)
print(my_dict['Platform'])
my_dict.pop('Platform')
print(my_dict)
print(my_dict.get('Library'))
