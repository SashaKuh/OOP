# Приклад 1: Брудний код - довгий метод з поганими іменами змінних
def calc(x, y, op):
    if op == 1:
        r = x + y
        return r
    elif op == 2:
        r = x - y
        return r
    elif op == 3:
        r = x * y
        return r
    elif op == 4:
        if y == 0:
            return "Error"
        r = x / y
        return r
    else:
        return "Invalid operation"

# Рефакторинг: Розділення на менші методи, кращі імена, використання enum
from enum import Enum

class Operation(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4

def calculate(first_number: float, second_number: float, operation: Operation) -> float:
    operations = {
        Operation.ADD: lambda: add(first_number, second_number),
        Operation.SUBTRACT: lambda: subtract(first_number, second_number),
        Operation.MULTIPLY: lambda: multiply(first_number, second_number),
        Operation.DIVIDE: lambda: divide(first_number, second_number)
    }
    return operations.get(operation, lambda: "Invalid operation")()

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

# Приклад 2: Брудний код - великий клас з поганою зв'язністю
class UserManager:
    def __init__(self):
        self.users = []
        self.logged_in = []
        self.db_connection = None
    
    def add_user(self, name, email, password):
        if not name or not email or not password:
            return False
        if '@' not in email:
            return False
        if len(password) < 6:
            return False
        user = {'name': name, 'email': email, 'password': password}
        self.users.append(user)
        self.save_to_db(user)
        self.send_welcome_email(email)
        return True
    
    def save_to_db(self, user):
        # Уявімо, що тут код для збереження в базу даних
        pass
    
    def send_welcome_email(self, email):
        # Уявімо, що тут код для відправки email
        pass

# Рефакторинг: Розділення відповідальності на окремі класи
class User:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

class UserValidator:
    @staticmethod
    def validate_user(name: str, email: str, password: str) -> bool:
        return (bool(name) and 
                bool(email) and 
                '@' in email and 
                bool(password) and 
                len(password) >= 6)

class UserRepository:
    def __init__(self):
        self.users = []
    
    def save(self, user: User) -> None:
        self.users.append(user)

class EmailService:
    @staticmethod
    def send_welcome_email(email: str) -> None:
        # Логіка відправки email
        pass

class RefactoredUserManager:
    def __init__(self):
        self.validator = UserValidator()
        self.repository = UserRepository()
        self.email_service = EmailService()
    
    def add_user(self, name: str, email: str, password: str) -> bool:
        if not UserValidator.validate_user(name, email, password):
            return False
        
        user = User(name, email, password)
        self.repository.save(user)
        self.email_service.send_welcome_email(email)
        return True

# Приклад використання
if __name__ == "__main__":
    # Тестування калькулятора
    print("Брудний калькулятор:", calc(10, 5, 1))
    print("Чистий калькулятор:", calculate(10, 5, Operation.ADD))
    
    # Тестування менеджера користувачів
    dirty_manager = UserManager()
    clean_manager = RefactoredUserManager()
    
    # Порівняння викликів
    dirty_result = dirty_manager.add_user("John", "john@example.com", "password123")
    clean_result = clean_manager.add_user("John", "john@example.com", "password123")
    
    print("Результат брудного коду:", dirty_result)
    print("Результат чистого коду:", clean_result)
