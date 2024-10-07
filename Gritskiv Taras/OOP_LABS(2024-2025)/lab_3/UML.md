classDiagram
    Pizza <|-- PizzaDecorator
    PizzaDecorator <|-- CheeseDecorator
    PizzaDecorator <|-- BaconDecorator

    class Pizza {
        +cost(): int
    }

    class PizzaDecorator {
        -_pizza: Pizza
        +__init__(pizza: Pizza)
        +cost(): int
    }

    class CheeseDecorator {
        +cost(): int
    }

    class BaconDecorator {
        +cost(): int
    }
