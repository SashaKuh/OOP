class SoccerEntity:
    def act(self):
        pass

class Player(SoccerEntity):
    def act(self):
        print("Гравець")

class Coach(SoccerEntity):
    def act(self):
        print("Тренер")

class Referee(SoccerEntity):
    def act(self):
        print("Арбітр")

class SoccerEntityFactory:
    def create_entity(self, entity_type):
        if entity_type == "player":
            return Player()
        elif entity_type == "coach":
            return Coach()
        elif entity_type == "referee":
            return Referee()
        else:
            raise ValueError("Невідомий тип футбольного об'єкта")

# Використання фабрики
factory = SoccerEntityFactory()
player = factory.create_entity("player")
coach = factory.create_entity("coach")
referee = factory.create_entity("referee")

player.act()
coach.act()
referee.act()    


