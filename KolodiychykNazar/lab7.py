#Різниця між звичайними методами, методами класу та статичними методами
class MyClass:
    class_variable = 10  
    def __init__(self, x):
        self.x = x  
    def instance_method(self):
        return self.x  
    @classmethod
    def class_method(cls):
        return cls.class_variable 

    @staticmethod
    def static_method():
        return "This is a static method"  

#Створення альтернативних конструкторів
class MyClass:
    def __init__(self, x):
        self.x = x
    @classmethod
    def from_string(cls, string):
        parts = string.split('-')
        return cls(int(parts[0]), int(parts[1]))

#Реалізація "методу класу"
class MyClass:
    class_variable = 10
    @classmethod
    def class_method(cls):
        return cls.class_variable

#Реалізація альтернативного конструктора за допомогою методу класу
class MyClass:
    def __init__(self, x):
        self.x = x
    @classmethod
    def from_list(cls, lst):
         return cls(sum(lst))  

