from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    """
    Інтерфейс Суб'єкта оголошує набір методів для управління підписниками.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Store(Subject):
    """
    Магазин, який володіє важливим станом і сповіщає спостерігачів, коли стан
    змінюється (наприклад, коли є нові акції).
    """

    _offers: List[str] = []
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Магазин: Спостерігача підключено.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
        print("Магазин: Спостерігача відключено.")

    def notify(self) -> None:
        print("Магазин: Повідомлення спостерігачів про нові акції...")
        for observer in self._observers:
            observer.update(self)

    def add_offer(self, offer: str) -> None:
        self._offers.append(offer)
        print(f"Магазин: Додано нову акцію: {offer}")
        self.notify()


class Observer(ABC):
    """
    Інтерфейс Спостерігача оголошує метод update, який використовується
    суб'єктами для сповіщення.
    """

    @abstractmethod
    def update(self, subject: Store) -> None:
        """Отримати оновлення від суб'єкта."""
        pass


class Customer(Observer):
    """Клієнт, який підписується на акції магазину."""

    def __init__(self, name: str):
        self.name = name

    def update(self, subject: Store) -> None:
        if subject._offers:
            print(f"{self.name}: Я отримав повідомлення про нову акцію: {subject._offers[-1]}")
        else:
            print(f"{self.name}: Немає нових акцій.")


if __name__ == "__main__":
    # Код клієнта

    store = Store()

    # Створюємо клієнтів (спостерігачів)
    customer_a = Customer("Анна")
    store.attach(customer_a)

    customer_b = Customer("Богдан")
    store.attach(customer_b)

    # Додаємо акції
    store.add_offer("Знижка 20% на всі товари!")
    store.add_offer("Безкоштовна доставка при замовленні від 500 грн!")

    # Відключаємо одного зі спостерігачів
    store.detach(customer_a)

    # Додаємо ще одну акцію
    store.add_offer("Купуйте 1, отримуйте 1 безкоштовно!")
