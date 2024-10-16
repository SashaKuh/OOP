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
    def notify_all(self) -> None:
        pass


class Store(Subject):
    """
    Магазин, який володіє важливим станом і сповіщає спостерігачів, коли стан
    змінюється (наприклад, коли є нові акції).
    """

    _offers: List[str] = ["Знижка 10% на всі товари!", "Купуйте 2, отримуйте 1 безкоштовно!"]  # Початкові акції
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print(f"Магазин: Спостерігача '{observer.name}' підключено.")
        self._observers.append(observer)
        self.notify(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
        print(f"Магазин: Спостерігача '{observer.name}' відключено.")

    def notify(self, observer: Observer) -> None:
        """Повідомляє одного спостерігача одразу після підписки."""
        print(f"Магазин: Повідомлення для {observer.name}...")
        observer.update(self)

    def notify_all(self) -> None:
        """Повідомляє всіх підписників про нову акцію."""
        print("Магазин: Відправка розсилки всім підписникам...")
        for observer in self._observers:
            observer.update(self)

    def add_offer(self, offer: str) -> None:
        """Додає нову акцію і повідомляє всіх підписників."""
        self._offers.append(offer)
        print(f"Магазин: Додано нову акцію: {offer}")


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


def main():
    store = Store()
    customers = {}

    while True:
        print("\nВиберіть дію:")
        print("1 - Підписатися на розсилку акцій")
        print("2 - Відписатися від розсилки")
        print("3 - Додати нову акцію (для магазину)")
        print("4 - Відправити розсилку (для магазину)")
        print("5 - Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            name = input("Введіть ваше ім'я для підписки: ")
            if name not in customers:
                customer = Customer(name)
                customers[name] = customer
                store.attach(customer)  # Підписати користувача і одразу повідомити про акції
            else:
                print(f"{name} вже підписаний на розсилку.")

        elif choice == "2":
            name = input("Введіть ваше ім'я для відписки: ")
            if name in customers:
                store.detach(customers[name])
                del customers[name]
            else:
                print(f"{name} не знайдено серед підписників.")

        elif choice == "3":
            new_offer = input("Введіть нову акцію для магазину: ")
            store.add_offer(new_offer)

        elif choice == "4":
            store.notify_all()

        elif choice == "5":
            print("Завершення програми.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
