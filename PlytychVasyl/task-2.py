from random import randint as rdt 
#2.змінні
number=27
word='Hellow LNUP'
print(number,"-",word)
#3. поняття динамічної типізації
print(type(number))
number=str(number)
print(type(number))
#4.базові операції та приведення типів
a=27
b=2
print(f'a={a}\nb={b}\n{a+b}-додавання\n{a-b}-віднімання\n{a*b}-множення\n{a/b}-ділення\n{a//b}-ціле число при діленні\n{a%b}-остача від ділення\n{b**3}-піднесення до степення')
#тип “List”
list=[3,'hello',34,12,53,'word','3',3]
print(list)
print('довжина списку-',len(list))
print('зріз списку', list[3:])
list.pop()#видаляє останій елемент за замовчуваням, можна вказувати індекс
list.append(21)#додає елемент в кінець
list.insert(2,1)#вставляє 2 на 1 місце
list.count(3)#кількість входжень елемента
list.remove(3)#вилучає перше входження елемента
list.reverse()#зворотній порядок списку
list.index(34)#індекс елемента
#стрічки
sentens="вивчення ООП"
print(sentens[2:7])
print(sentens+"з куратором")
print(sentens*5)
#Робота із словниками
dict_OOP={
    'Taras':5,
    'Sasha':4,
    'Valentyn':3,
    'vlad':5
    }
print(dict_OOP)
print(dict_OOP.get('Valentyn'))
dict_OOP.pop('Taras')
print(dict_OOP)

