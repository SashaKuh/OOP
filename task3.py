
# 2. Використання умовного оператора
y=11
if y > 5:
    print("x більше 5")
else:
    print("x менше або дорівнює 5")
# 3. Використання булевої логіки
a = True
if a!=False:
    print("a - правда")

# 4. Складні умови
num = 7
if num > 0 and (num % 2 == 0 or num % 3 == 0):
    print("Число більше 0 і кратне 2 або 3")

# 5. Цикли
# Визначення суми перших 5 натуральних чисел
total = 0
for i in range(1, 6):
    total += i
print("Сума перших 5 натуральних чисел:", total)

# Факторіал числа 5 
number = 5
result = 1
while number > 0:
    result *= number
    number -= 1

print("Факторіал числа 5 дорівнює", result)
