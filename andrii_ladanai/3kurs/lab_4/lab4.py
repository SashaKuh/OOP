from abc import ABC, abstractmethod
from typing import List

# Базовий клас для птахів
class Bird(ABC):
    @abstractmethod
    def eat(self) -> str:
        pass

# Птахи, які можуть літати
class FlyingBird(Bird):
    @abstractmethod
    def fly(self) -> str:
        pass

# Конкретна реалізація - Голуб
class Pigeon(FlyingBird):
    def eat(self) -> str:
        return "Голуб їсть зерно"
    
    def fly(self) -> str:
        return "Голуб летить у небі"

# Конкретна реалізація - Орел
class Eagle(FlyingBird):
    def eat(self) -> str:
        return "Орел полює на здобич"
    
    def fly(self) -> str:
        return "Орел ширяє високо в небі"

# Птахи, які не літають
class NonFlyingBird(Bird):
    def eat(self) -> str:
        pass

# Конкретна реалізація - Пінгвін
class Penguin(NonFlyingBird):
    def eat(self) -> str:
        return "Пінгвін їсть рибу"

# Функція, яка працює з птахами
def process_flying_birds(birds: List[FlyingBird]) -> None:
    for bird in birds:
        print(bird.eat())
        print(bird.fly())

def process_birds(birds: List[Bird]) -> None:
    for bird in birds:
        print(bird.eat())

# Приклад використання
def main():
    birds = [Pigeon(), Eagle()]
    all_birds = [Pigeon(), Eagle(), Penguin()]
    
    # Можемо безпечно використовувати FlyingBird
    process_flying_birds(birds)
    
    # Можемо безпечно використовувати всіх птахів
    process_birds(all_birds)

if __name__ == "__main__":
    main()