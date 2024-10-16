Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... x = 10
... if x > 0:
...     print("Positive")
... elif x < 0:
...     print("Negative")
... else:
...     print("Zero")
... 
... x = True
... y = False
... 
... print(x and y) 
... print(x or y)   
... print(not x)    
... 
... a = 10
... b = 5
... c = 7
... 
... if a > b and a > c:
...     print("a is the largest")
... elif b > a and b > c:
...     print("b is the largest")
... else:
...     print("c is the largest")
... 
... my_list = [1, 2, 3, 4, 5]
... for num in my_list:
...     print(num)
... 
... x = 0
... while x < 5:
...     print(x)
...     x += 1
... 
... a = 10
b = 5
c = 7

if a > b and a > c:
    print("a is the largest")
elif b > a and b > c:
    print("b is the largest")
else:
    print("c is the largest")

start = 1
end = 10

for num in range(start, end+1):
    if num % 2 == 0:
        print(num)

n = 5
factorial = 1

for i in range(1, n+1):
    factorial *= i

print("Factorial of", n, "is", factorial)
