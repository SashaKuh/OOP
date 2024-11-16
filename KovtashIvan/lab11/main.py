class Computer:
    def __init__(self):
        self.parts = {}
    
    def add_part(self, key, value):
        self.parts[key] = value
    
    def show_specs(self):
        print("Специфікація комп'ютера:")
        for key, value in self.parts.items():
            print(f"{key}: {value}")

# Базовий будівельник
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()
    
    def get_computer(self):
        return self.computer
    
    def build_processor(self):
        pass
    
    def build_memory(self):
        pass
    
    def build_storage(self):
        pass

# Конкретний будівельник для ігрового ПК
class GamingComputerBuilder(ComputerBuilder):
    def build_processor(self):
        self.computer.add_part("Процесор", "Intel Core i9-12900K")
    
    def build_memory(self):
        self.computer.add_part("Оперативна пам'ять", "32GB DDR5 5200MHz")
    
    def build_storage(self):
        self.computer.add_part("Накопичувач", "2TB NVMe SSD")

# Конкретний будівельник для офісного ПК
class OfficeComputerBuilder(ComputerBuilder):
    def build_processor(self):
        self.computer.add_part("Процесор", "Intel Core i5-12400")
    
    def build_memory(self):
        self.computer.add_part("Оперативна пам'ять", "16GB DDR4 3200MHz")
    
    def build_storage(self):
        self.computer.add_part("Накопичувач", "512GB SATA SSD")

# Директор
class ComputerAssembler:
    def __init__(self, builder):
        self.builder = builder
    
    def construct_computer(self):
        self.builder.build_processor()
        self.builder.build_memory()
        self.builder.build_storage()

# Демонстрація роботи
if __name__ == "__main__":
    # Створення ігрового ПК
    gaming_builder = GamingComputerBuilder()
    assembler = ComputerAssembler(gaming_builder)
    assembler.construct_computer()
    gaming_pc = gaming_builder.get_computer()
    print("Ігровий ПК:")
    gaming_pc.show_specs()
    
    print("\n" + "="*50 + "\n")
    
    # Створення офісного ПК
    office_builder = OfficeComputerBuilder()
    assembler = ComputerAssembler(office_builder)
    assembler.construct_computer()
    office_pc = office_builder.get_computer()
    print("Офісний ПК:")
    office_pc.show_specs()