class MyClass:
    def normal_method(self):
        print("This is a normal method.")

obj = MyClass()
obj.normal_method()

class MyClass:
    class_variable = "This is a class variable."


    @classmethod
    def class_method(cls):
        print(cls.class_variable)

    @staticmethod
    def static_method():
        print("This is a static method.")

MyClass.class_method()
MyClass.static_method()

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_string(cls, string):
        x, y = map(int, string.split(','))
        return cls(x, y)

obj = MyClass.from_string("10,20")
print(obj.x, obj.y)
