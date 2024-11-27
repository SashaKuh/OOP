class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

    def set_state(self, state):
        self._state = state
        self.notify()

    def get_state(self):
        return self._state


class Observer:
    def update(self):
        pass


class ConcreteObserver(Observer):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def update(self):
        print(f"{self.name} отримав оновлення: {self.subject.get_state()}")


subject = Subject()

observer1 = ConcreteObserver("Спостерігач 1", subject)
observer2 = ConcreteObserver("Спостерігач 2", subject)

subject.attach(observer1)
subject.attach(observer2)

subject.set_state(10)  

subject.detach(observer1)
subject.set_state(20)  
