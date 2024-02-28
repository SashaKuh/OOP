# Базові операції
x = 5
y = 2
print(x + y)  
print(x - y)  
print(x * y)  
print(x / y)  
print(x // y) 
print(x % y)  
print(x ** y) 

# Приведення типів
num_str = "10"
num_int = int(num_str)  
num_float = float(num_str) 

my_list = [1, 2, 3, "four", 5.0]

# Зчитування значень елементів
print(my_list[0])   
print(my_list[3])   

# Задання значень елементів
my_list[1] = "two"
print(my_list)      

# Арифметичні оператори
print(2 + 3)   
print(5 - 2)
print(2 * 4)   

# Логічні оператори
print(True and False)  
print(True or False)  
print(not True)        

# Оператори порівняння
print(5 > 3)   
print(5 == 5)  
print(10 != 5) 

#Форматування стрічок
name = "Alice"
age = 30
print("Мене звати {0} і мені {1} років.".format(name, age))

#Робота зі стрічками
my_string = "Hello"
print(my_string[0])     # Виведе: H
print(my_string[1:3])   # Виведе: el
print(len(my_string))   # Виведе: 5

#Робота із словником
my_dict = {"name": "Nazar", "age": 18, "city": "Lviv"}
print(my_dict["name"])  
print(my_dict["age"])  
my_dict["age"] = 18
print(my_dict["age"]) 

# Додавання нового елементу
my_dict["gender"] = "Male"
print(my_dict)       
