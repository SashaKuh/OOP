# 1.
class MyEmptyOne:
    pass


# 2.
class Person:
    def __new__(cls, name, age):
        print("Creating a new Person object")
        instance = super().__new__(cls)
        return instance


"""
3.  Буде виведено адресу пам'яті методу
"""

"""
4. Змінна класу є спільною для всіх екземплярів класу і визначається один раз на рівні класу,
 тоді як змінні об'єкта існують окремо для кожного екземпляра і визначаються під час створення кожного об'єкта.
"""