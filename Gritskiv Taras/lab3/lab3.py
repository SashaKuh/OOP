data=[-1,40,45,-854,-85,456,-5]
positive_numbers=[]
negative_numbers=[]
for i in data:
    if i >=0:
        positive_numbers.append(i)
    else:
        negative_numbers.append(i)
else:
    print('Додатні чила: {0}\nВідємні числа: {1}'.format(positive_numbers,negative_numbers))