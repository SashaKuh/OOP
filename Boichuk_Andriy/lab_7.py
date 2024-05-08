class Building:
    def __init__(self, height, widht):
        self.height = height
        self.widht = widht
    def build_height(self):
        return self.height
    def build_widht(self):
        return self.widht

class School(Building):
    def __init__(self,schoolchildren):
        self.schoolchildren = schoolchildren
    def count_of_schoolchildren(self):
        if self.schoolchildren > 150:
            return "Велика школа"
        else:
            return "Мала школа"
my_class1 = Building(15, 200)
print(my_class1.build_height())
print(my_class1.build_widht())

my_class2 = School(200)
print(my_class2.count_of_schoolchildren())