# Існуючий інтерфейс, який ми хочемо адаптувати
class OldPrinter:
    def print_old(self, text):
        return f"Друк старим методом: {text}"

# Цільовий інтерфейс, який очікує клієнт
class ModernPrinter:
    def print_modern(self, text):
        pass

# Адаптер, який дозволяє використовувати старий принтер через новий інтерфейс
class PrinterAdapter(ModernPrinter):
    def __init__(self, old_printer: OldPrinter):
        self.old_printer = old_printer
    
    def print_modern(self, text):
        # Адаптуємо виклик старого методу до нового інтерфейсу
        return self.old_printer.print_old(text)

# Клієнтський код
def client_code(modern_printer: ModernPrinter):
    # Отримуємо текст від користувача
    user_text = input("Введіть текст для друку: ")
    return modern_printer.print_modern(user_text)

# Демонстрація роботи
if __name__ == "__main__":
    while True:
        # Створюємо екземпляр старого принтера
        old_printer = OldPrinter()
        
        # Створюємо адаптер, який обгортає старий принтер
        printer_adapter = PrinterAdapter(old_printer)
        
        # Використовуємо адаптер через новий інтерфейс
        result = client_code(printer_adapter)
        print(result)
        
        # Питаємо користувача чи хоче він продовжити
        continue_printing = input("\nБажаєте надрукувати ще щось? (так/ні): ")
        if continue_printing.lower() not in ['так', 'yes', 'y', 'т']:
            break