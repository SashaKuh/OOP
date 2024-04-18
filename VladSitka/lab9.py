class ParentClass:
    def __init__(self, name):
        self.name = name

    def parent_method(self):
        print("Це метод батьківського класу")

    def interact(self, other):
        print(f"{self.name} взаємодіє з {other.name}")
        other.interaction_response()


class ChildClass1(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def child_method(self):
        print("Це метод першого дочірнього класу")

    def interaction_response(self):
        print("Перший дочірній клас реагує")


class ChildClass2(ParentClass):
    def __init__(self, name, gender):
        super().__init__(name)
        self.gender = gender

    def child_method(self):
        print("Це метод другого дочірнього класу")

    def interaction_response(self):
        print("Другий дочірній клас реагує")



parent_obj = ParentClass("Батько")
child1_obj = ChildClass1("Перший", 20)
child2_obj = ChildClass2("Другий", "чоловіча")

parent_obj.interact(child1_obj)
parent_obj.interact(child2_obj)
