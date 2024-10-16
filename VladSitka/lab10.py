class MyClass:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Значення не може бути від'ємним")
        self._value = new_value

    @value.deleter
    def value(self):
        print("Видалення значення")
        del self._value




obj = MyClass()


obj.value = 10
print(obj.value)  

try:
    obj.value = -5
except ValueError as e:
    print(e)


del obj.value
