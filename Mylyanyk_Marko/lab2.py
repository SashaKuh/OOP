"""
1. Ідентація - це відступи на початку рядка. В Пайтоні використовуються для розрізнення блоків коду.
"""

# 2.
variable: str = "25"
variable_dict = dict()
one, two = 1, 2

"""
3. Прості змінні - це Integer, Float, Boolean, String
"""

# 4.
variable_int = int(variable)

"""
5. List - це структура даних, яка мітить в собі впорядкований набір елементів
"""
example = [1, 2, 3]
new_num = 4
example.append(new_num) # noqa :add new value in end of list
example.sort(reverse=True) # noqa: Sort list values in given order
example.index(2) # noqa: returns the index of the specified element in the list

# 6.
x, y = 1, 2
suma = x + y
difference = x - y
product = x * y
quotient = x / y
remainder = x % y
in_pow = x ** y

# 7.
line = "Hello World!"

line.upper() # noqa: capitalize all letters
line.lower() # noqa: lower case all letters
line.title() # noqa: makes first character in every word upper case
line.split() # noqa: splits a string into a list

name = "Marko"
surname = "Mylyanyk"
start = "My name is {name} {surname}"

type_1 = f"My name is {name} {surname}"
type_2 = "My name is %s %s" % (name, surname)
type_3 = start.format(name=name, surname=surname)

print(type_1)
print(type_2)
print(type_2)

"""
8. Dicts - структура даних на базі хеш таблиць, яка містить в собі key/value пари
"""

d_1 = dict(name="Marko", surname="Mylyanyk")
d_2 = {
    "name": "Marko",
    "surname": "Mylyanyk"
}

d_3 = dict()
d_3["name"] = "Marko"
d_3["surname"] = "Mylyanyk"


"""
9. Головна різниця в тому, що в списку елементи зберігають порядок, а в словнику - ні.
Важко визначити який більш універсальний, так як кожеш з типів даних має своє призначення
Можна зімітувати словник за допомогою списку, треба написати кастомні getitem та setitem і тд.

"""








