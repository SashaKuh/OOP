#if else
x = 1
if x > 0:
    print("x is positive")
elif x == 0:
    print("x equals 0")
else:
    print("x is negative")

#boolean operators
x = 1
if x > 0 and x < 1:
    print("x is between 0 and 10 exclusive")

#cycles for & while
for i in range(2):
    print(i)

count = 0
while count < 2:
    print(count)
    count += 1
