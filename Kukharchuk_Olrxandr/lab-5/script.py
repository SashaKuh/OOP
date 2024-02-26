class MyClass:
    def __init__(self,a,b):
        self.a = a
        self.b = b


    def add(self):
        sum = self.a + self.b
        print(sum)

ob = MyClass(1,2)
print(ob)

ob.add()