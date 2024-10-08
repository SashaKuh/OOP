class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            value = self._collection[self._index]
            self._index += 1
            return value
        except IndexError:
            raise StopIteration

class Collection:
    def __init__(self):
        self._items = []

    def __iter__(self):
        return Iterator(self._items)

    def add(self, item):
        self._items.append(item)

# Використання
collection = Collection()
collection.add("A")
collection.add("B")
collection.add("C")

for item in collection:
    print(item)