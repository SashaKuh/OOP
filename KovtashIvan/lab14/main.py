from abc import ABC, abstractmethod
from typing import List

# Interface Segregation Principle - розділяємо інтерфейси
class FileReader(ABC):
    @abstractmethod
    def read(self) -> str:
        pass

class FileWriter(ABC):
    @abstractmethod
    def write(self, text: str) -> str:
        pass

# Single Responsibility Principle - кожен клас має одну відповідальність
class TextFileHandler(FileReader, FileWriter):
    def __init__(self, filename: str):
        self.filename = filename
    
    def read(self) -> str:
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return f"Помилка: Файл {self.filename} не знайдено"
    
    def write(self, text: str) -> str:
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                file.write(text)
            return "Файл успішно записано"
        except Exception as e:
            return f"Помилка при записі файлу: {str(e)}"

# Open/Closed Principle - можна розширювати, не змінюючи
class TextOperation(ABC):
    @abstractmethod
    def execute(self, text: str) -> str:
        pass

class UpperCaseOperation(TextOperation):
    def execute(self, text: str) -> str:
        return text.upper()

class LowerCaseOperation(TextOperation):
    def execute(self, text: str) -> str:
        return text.lower()

class SpaceRemovalOperation(TextOperation):
    def execute(self, text: str) -> str:
        return " ".join(text.split())

# Liskov Substitution Principle - підкласи можуть замінити базові класи
class TextAnalyzer:
    @staticmethod
    def analyze(text: str, operations: List[TextOperation]) -> dict:
        results = {}
        for operation in operations:
            results[operation.__class__.__name__] = operation.execute(text)
        return results

# Dependency Inversion Principle - залежність від абстракцій
class TextProcessor:
    def __init__(self, file_handler: FileReader):
        self.file_handler = file_handler
        self.operations: List[TextOperation] = []
    
    def add_operation(self, operation: TextOperation):
        self.operations.append(operation)
    
    def process(self) -> dict:
        text = self.file_handler.read()
        return TextAnalyzer.analyze(text, self.operations)

# Демонстрація роботи
if __name__ == "__main__":
    # Створюємо обробник файлів
    file_handler = TextFileHandler("example.txt")
    
    # Записуємо тестовий текст
    sample_text = "Це приклад тексту. Він містить декілька речень.   З   декількома   пробілами."
    print(file_handler.write(sample_text))
    
    # Створюємо процесор тексту
    processor = TextProcessor(file_handler)
    
    # Додаємо операції
    processor.add_operation(UpperCaseOperation())
    processor.add_operation(LowerCaseOperation())
    processor.add_operation(SpaceRemovalOperation())
    
    # Обробляємо текст
    results = processor.process()
    
    # Виводимо результати
    print("\nРезультати обробки:")
    for operation, result in results.items():
        print(f"\n{operation}:")
        print(result)