''' Коментарі-милиці (Code Comments Smells)
# Поганий приклад
# Збільшуємо лічильник на 1
counter += 1

# Створюємо список користувачів
users = []

# Перевіряємо чи список порожній
if len(users) == 0:
    print("Немає користувачів")


# Покращений варіант
counter += 1
users = []
if not users:
    print("Немає користувачів")

'''

'''Магічні числа (Magic Numbers)
# Поганий приклад
def calculate_total(price):
    return price * 1.2

# Покращений варіант
TAX_RATE = 0.2

def calculate_total(price):
    return price * (1 + TAX_RATE)
'''

'''Порушення інкапсуляції (Broken Encapsulation)
# Поганий приклад
class BankAccount:
    def __init__(self):
        self.balance = 0

# Покращений варіант
class BankAccount:
    def __init__(self):
        self._balance = 0
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
'''

'''Великі класи (Large Classes)
# Поганий приклад
class Order:
    def calculate_total(self): pass
    def validate(self): pass
    def save(self): pass
    def load(self): pass
    def send_email(self): pass
    def generate_invoice(self): pass
    # ... ще 20 методів

# Покращений варіант
class Order:
    def calculate_total(self): pass
    def validate(self): pass

class OrderStorage:
    def save(self, order): pass
    def load(self, order_id): pass

class OrderNotification:
    def send_email(self, order): pass

class InvoiceGenerator:
    def generate(self, order): pass

'''

'''Дублювання коду (Duplicate Code)
# Приклад дублювання
def calculate_total_price(items):
    total = 0
    for item in items:
        total += item.price * 1.2  # Податок 20%
    return total

def calculate_wholesale_price(items):
    total = 0
    for item in items:
        total += item.price * 1.2  # Той самий код
    return total

# Покращений варіант
def apply_tax(price):
    return price * 1.2

def calculate_price(items):
    return sum(apply_tax(item.price) for item in items)
'''

'''Параметри-прапорці (Flag Parameters)
# Поганий приклад
def format_text(text, is_uppercase=False, add_exclamation=False):
    result = text
    if is_uppercase:
        result = result.upper()
    if add_exclamation:
        result += "!"
    return result

# Використання
text = format_text("hello", is_uppercase=True, add_exclamation=True)  # "HELLO!"
text = format_text("hello", is_uppercase=True)  # "HELLO"
text = format_text("hello", add_exclamation=True)  # "hello!"

# Покращений варіант
def to_uppercase(text):
    return text.upper()

def add_exclamation_mark(text):
    return text + "!"

# Використання
text = add_exclamation_mark(to_uppercase("hello"))  # "HELLO!"
text = to_uppercase("hello")  # "HELLO"
text = add_exclamation_mark("hello")  # "hello!"
'''