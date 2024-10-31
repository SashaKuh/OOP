class Node:
    """Клас вузла, який зберігає значення і посилання на наступний елемент."""
    def __init__(self, value):
        self.value = value
        self.next = None  

class LinkedListIterator:
    """Клас ітератора для пов'язаного списку."""
    def __init__(self, head):
        self.current = head  

    def __iter__(self):
        return self  

    def __next__(self):
        if self.current is None:
            raise StopIteration  
        else:
            value = self.current.value  
            self.current = self.current.next  
            return value

class LinkedList:
    def __init__(self):
        self.head = None  
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, value):
        current = self.head
        if current and current.value == value:
            self.head = current.next
            return
        previous = None
        while current and current.value != value:
            previous = current
            current = current.next
        if current:
            previous.next = current.next  # Пропускаємо видалений вузол
    
    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None
    
    def __iter__(self):
        return LinkedListIterator(self.head)  # Повертає новий ітератор для голови списку
    
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return f"{values}"

# Приклад використання
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(0)

print("Пов'язаний список:", linked_list)  

for value in linked_list:
    print("Елемент:", value)
