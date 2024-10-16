from random import randint

#створюю дві змінні

a=100
b='100'
print(a,b)

#Використання динамічної типізації
b=str(b)
print(type(b))

#Базові операції
c=100
d=100
print(f'+: {c+d}\n-: {c-d}\n*: {c*d}\n/:{c/d} \n//: {c//3} \n%: {d%3}')

#Створюю список у якому є різні типи данних

my_list=[100,True,False,'4',7.2,'Hi']
print(f"all_list: {my_list}\nrand_elem: {my_list[randint(0,5)]}")

#Базові дії над списками

my_list.append(0)
print(my_list)
copy_list=my_list.copy()
print(copy_list)
print(copy_list.count(True))
print(copy_list.pop())
copy_list.clear()
print(copy_list)

#Дії над стрічками

my_str='oop'
print(my_str*3)
print(my_str+' '+'ppo')
print(my_str[0])
print(my_str[0:3])
count=0
for i in my_str:
    if i == 'p':
        count+=1
print(f'sum_p: {count}')
#Робота із словниками
my_dict={
    'bed':2,
    'table':3,
    'window':1
}
print(my_dict)
print(my_dict['table'])
my_dict.pop('table')
print(my_dict)
print(my_dict.get('window'))