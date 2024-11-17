# Single Responsibility Principle (SRP) - кожен клас виконує одну задачу
class FileHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return f"Помилка: файл {self.file_name} не знайдено."

    def write_file(self, content):
        try:
            with open(self.file_name, 'w', encoding='utf-8') as file:
                file.write(content)
            return "Файл успішно записано."
        except Exception as e:
            return f"Помилка запису файлу: {e}"

# Open/Closed Principle (OCP) - класи відкриті для розширення, але закриті для зміни
class TextTransformer:
    def transform(self, text):
        raise NotImplementedError("Метод 'transform' має бути реалізований у підкласі.")

class ToUpperCase(TextTransformer):
    def transform(self, text):
        return text.upper()

class RemoveExtraSpaces(TextTransformer):
    def transform(self, text):
        return " ".join(text.split())

class AddPrefix(TextTransformer):
    def __init__(self, prefix):
        self.prefix = prefix

    def transform(self, text):
        return f"{self.prefix} {text}"

# Liskov Substitution Principle (LSP) - підкласи повинні замінювати базові класи
class TextProcessor:
    def __init__(self, transformers):
        self.transformers = transformers

    def process_text(self, text):
        results = {}
        for transformer in self.transformers:
            results[transformer.__class__.__name__] = transformer.transform(text)
        return results

# Interface Segregation Principle (ISP) - розділення інтерфейсів
class DataSaver:
    def save(self, data):
        raise NotImplementedError("Метод 'save' має бути реалізований у підкласі.")

class ConsoleSaver(DataSaver):
    def save(self, data):
        print("Збережено у консоль:")
        print(data)

class FileSaver(DataSaver):
    def __init__(self, file_name):
        self.file_name = file_name

    def save(self, data):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            file.write(data)
        print(f"Дані збережено у файл {self.file_name}")

# Dependency Inversion Principle (DIP) - залежність від абстракцій
class TextManager:
    def __init__(self, handler, processor, saver):
        self.handler = handler
        self.processor = processor
        self.saver = saver

    def manage(self):
        text = self.handler.read_file()
        results = self.processor.process_text(text)
        formatted_results = "\n".join(f"{key}: {value}" for key, value in results.items())
        self.saver.save(formatted_results)


# Демонстрація 
if __name__ == "__main__":
    handler = FileHandler("lab_example.txt")
    transformers = [ToUpperCase(), RemoveExtraSpaces(), AddPrefix("Префікс:")]
    processor = TextProcessor(transformers)
    saver = ConsoleSaver()  

    print(handler.write_file("  Це тестовий   текст.   Зайві пробіли. "))

    manager = TextManager(handler, processor, saver)
    manager.manage()
