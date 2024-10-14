class Publisher:
    def __init__(self):
        self._subscribers = [] 

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self._subscribers:
            subscriber.update(message)


class Subscriber:
    def update(self, message):
        raise NotImplementedError("Subclasses must implement update method")


class EmailSubscriber(Subscriber):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"Email to {self.name}: {message}")


class SMSSubscriber(Subscriber):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def update(self, message):
        print(f"SMS to {self.phone_number}: {message}")

store = Publisher()

email_subscriber = EmailSubscriber("sasha@gmail.com")
sms_subscriber = SMSSubscriber("+1234567890")

store.subscribe(email_subscriber)
store.subscribe(sms_subscriber)

store.notify("Новий товар доступний в магазині!")

store.unsubscribe(sms_subscriber)

store.notify("Інше повідомлення для залишених підписників.")
