class Iterator:
    def __init__(self, my_list):
        self.my_list = my_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.my_list):
            value = self.my_list[self.index] * self.index
            result = (self.index, value)
            self.index += 1
            return result
        else:
            raise StopIteration

my_list = [10, 20, 30, 40]
iterator = Iterator(my_list)
for index, value in iterator:
    print(f"Index: {index}, Value: {value}")
