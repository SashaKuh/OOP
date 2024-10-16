class MyClass:
    class_variable = 0

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    def instance_method(self):
        print("Це метод екземпляру класу")

    @classmethod
    def class_method(cls):
        print("Це метод класу")
        cls.class_variable += 1

    @classmethod
    def alternative_constructor(cls, value):
        return cls(value)

    @staticmethod
    def static_method():
        print("Це статичний метод")


obj1 = MyClass(10)
obj1.instance_method()

MyClass.class_method()
print(MyClass.class_variable)

obj2 = MyClass.alternative_constructor(20)
print(obj2.instance_variable)

MyClass.static_method()
