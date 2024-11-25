from abc import ABC, abstractmethod

# Продукт
class Computer:
    def __init__(self):
        self.parts = {}
    
    def add_part(self, key, value):
        self.parts[key] = value
    
    def show_specs(self):
        print("Специфікація комп'ютера:")
        for key, value in self.parts.items():
            print(f"{key}: {value}")

# Абстрактний будівельник
class ComputerBuilder(ABC):
    def __init__(self):
        self.computer = Computer()
    
    def get_computer(self):
        return self.computer
    
    @abstractmethod
    def build_processor(self):
        pass
    
    @abstractmethod
    def build_memory(self):
        pass
    
    @abstractmethod
    def build_storage(self):
        pass

# Конкретний будівельник для ігрового комп'ютера
class GamingComputerBuilder(ComputerBuilder):
    def build_processor(self):
        self.computer.add_part("Процесор", "Intel Core i9-12900K")
        
    def build_memory(self):
        self.computer.add_part("Оперативна пам'ять", "32GB DDR5")
        
    def build_storage(self):
        self.computer.add_part("Накопичувач", "2TB NVMe SSD")

# Конкретний будівельник для офісного комп'ютера
class OfficeComputerBuilder(ComputerBuilder):
    def build_processor(self):
        self.computer.add_part("Процесор", "Intel Core i3-12100")
        
    def build_memory(self):
        self.computer.add_part("Оперативна пам'ять", "8GB DDR4")
        
    def build_storage(self):
        self.computer.add_part("Накопичувач", "256GB SSD")

# Директор
class ComputerAssembler:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder
    
    def construct_computer(self):
        self.builder.build_processor()
        self.builder.build_memory()
        self.builder.build_storage()

# Приклад використання
def main():
    # Створення ігрового комп'ютера
    gaming_builder = GamingComputerBuilder()
    assembler = ComputerAssembler(gaming_builder)
    assembler.construct_computer()
    gaming_computer = gaming_builder.get_computer()
    print("Ігровий комп'ютер:")
    gaming_computer.show_specs()
    
    print("\n" + "="*50 + "\n")
    
    # Створення офісного комп'ютера
    office_builder = OfficeComputerBuilder()
    assembler = ComputerAssembler(office_builder)
    assembler.construct_computer()
    office_computer = office_builder.get_computer()
    print("Офісний комп'ютер:")
    office_computer.show_specs()

if __name__ == "__main__":
    main()
