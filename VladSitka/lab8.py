class ParentClass:
    def __init__(self, name):
        self.name = name

    def parent_method(self):
        print("Це метод батьківського класу")

class ChildClass1(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def child1_method(self):
        print("Це метод першого дочірнього класу")

class ChildClass2(ParentClass):
    def __init__(self, name, gender):
        super().__init__(name)
        self.gender = gender

    def child2_method(self):
        print("Це метод другого дочірнього класу")

    def interact_with_child1(self, child1_instance):
        print(f"{self.name} взаємодіє з {child1_instance.name}")
        child1_instance.child1_method()



parent_obj = ParentClass("Батько")
child1_obj = ChildClass1("Перший", 20)
child2_obj = ChildClass2("Другий", "чоловіча")

print(parent_obj.name)
parent_obj.parent_method()

print(child1_obj.name, child1_obj.age)
child1_obj.parent_method()
child1_obj.child1_method()

print(child2_obj.name, child2_obj.gender)
child2_obj.parent_method()
child2_obj.child2_method()

child2_obj.interact_with_child1(child1_obj)
