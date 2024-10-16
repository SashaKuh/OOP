class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self._first_name = first
        self._last_name = last

    @full_name.deleter
    def full_name(self):
        del self._first_name
        del self._last_name
person = Person("John", "Doe")
print("Full name:", person.full_name) 
person.full_name = "Alice Smith" 
print("Updated full name:", person.full_name)
del person.full_name 
print("After deletion:", person.full_name)  
