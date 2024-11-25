# Клас, що представляє комп'ютер
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return (f"Computer with {self.cpu} CPU, {self.ram} RAM, "
                f"{self.storage} storage, and {self.gpu} GPU.")


# Клас будівельник для створення об'єкта(компютера)
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        return self.computer


builder = ComputerBuilder()
my_computer = (
    builder.set_cpu("Intel Core i9")
    .set_ram("32GB")
    .set_storage("1TB SSD")
    .set_gpu("NVIDIA RTX 4090")
    .build()
)

print(my_computer)
