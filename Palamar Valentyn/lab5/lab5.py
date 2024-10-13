class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        result = self.x + self.y
        print(result)

obj = MyClass(5, 6)
print(obj)

obj.add()
