class Animal:
    def __init__(self, speed, weight, voice):
        self.speed = speed
        self.weight = weight
        self.voice = voice
    def animal_speed(self):
        return self.speed
    def animal_weight(self):
        return self.weight
    def animal_voice(self):
        return self.voice
my_class1 = Animal(70, 30, "який небуть")
print(my_class1.animal_speed())
print(my_class1.animal_weight())
print(my_class1.animal_voice())
class Pig(Animal):
    def __init__(self, voice):
        self.voice = voice
    def pig_voice(self):
        return self.voice
my_class2 = Pig("хрю хрю")
print(my_class2.pig_voice())
