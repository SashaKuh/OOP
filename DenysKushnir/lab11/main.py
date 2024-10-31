class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Демонстрація роботи
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 == singleton2)  # True, обидва посилаються на той самий об'єкт
print(id(singleton1), id(singleton2))  # Ідентифікатори об'єктів однакові
