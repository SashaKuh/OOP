class Game:
    def __init__(self, title, gameplay):
        self.title = title
        self.gameplay = int(gameplay)
        
    def title_definition(self):
        return self.title
    def interesting_gameplay(self):
        if self.gameplay >= 7:
            return "Супер"
        else:
            return "Погано"
my_Game = Game("Hollow Knight", "9")
print(my_Game.title_definition())
print(my_Game.interesting_gameplay())
print("__________________________________________")
class Studio(Game):
    def __init__(self, name):
        self.name = name
    def studio_name(self):
        return self.name
    
studios = Studio("Team Cherry")
print(studios.studio_name())