def eqalization(a, b, c):
    if a<b<c:
        return "Значення вірні"
    else:
        return "Значення не вірні"

a = 67
b = 54
c = 89

resultat = eqalization(a, b, c)
print("Результат:",resultat)

#функція як параметир у іншій функції
def greeting(a):
    print("Привіт",a)

def name(greet):
    greet("Валентин")

name(greeting)