from random import randint
#створюю дві змінні
a=10
b='Hello World'
print(a,b)
#Використання динамічної типізації
a=str(a)
print(type(a))
#Базові операції
c=100
d=10
print(f'Додавання: {c+d}\nВіднімання: {c-d}\nМноження: {c*d}\nДілення:{c/d} \nДілення на ціло: {c//3} \nОстача від ділення: {d%3}')



#Створюю список у якому є різні типи данних
my_list=[1,2,3,4,True,'4','5',True,'6',7.2,8.984,9,True,False,'Like','Day']
print(f"Цілий список: {my_list}\nВиведення рандомного елементу списку: {my_list[randint(0,15)]}")
#Базові дії над списками
my_list.append(10)
print(my_list)
copy_list=my_list.copy()
print(copy_list)
print(copy_list.count(True))
print(copy_list.pop())
copy_list.clear()
print(copy_list)
#Дії над стрічками
my_str='Сьогодні дуже гарний день.'
print(my_str*3)
print(my_str+' '+'Cонечко світить.')
print(my_str[0])
print(my_str[0:9])
count=0
for i in my_str:
    if i == 'о':
        count+=1
print(f'У нашій стрічці є {count} букв о')
#Робота із словниками
my_dict={
    'Taras':5,
    'Sasha':4,
    'Valentyn':3
}
print(my_dict)
print(my_dict['Sasha'])
my_dict.pop('Sasha')
print(my_dict)
print(my_dict.get('Valentyn'))