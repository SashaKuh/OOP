#Умовні оператори
x = 5
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

#Оператори булевої логіки
print(True and False)  
print(True or False)   
print(not True)        

#Складні умови 
x = 13
y = 15
if x > 0 and y > 0:
    print("Both x and y are positive")
elif x > 0 or y > 0:
    print("At least one of x or y is positive")
else:
    print("Both x and y are non-positive")

#Цикли
x = 0
while x < 5:
    print(x)
    x += 1
for i in range(5):
    print(i)

#