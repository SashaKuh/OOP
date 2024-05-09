"""
1. Class - це як темплейт для створення обєктів.
"""


class MyCV:
    def __init__(self, name, age):
        self.name = name
        self.age = age


"""
2. Обєкт - це екземпляр класу. Він має поведінку вказану у класі/класах з яких його створили
"""

Marko = MyCV("Marko", 25)


"""
3. Клас визначає структуру та поведінку, а об'єкт - це конкретний екземпляр цього класу,
 який має конкретні властивості і може виконувати певні дії, які описані у класі.
"""

"""
4. Змінна класу - це змінна, яка визначена в класі і доступна для всіх екземплярів (об'єктів) цього класу.
 Це означає, що значення такої змінної буде спільним для всіх екземплярів класу,
"""


class MyCVDesc:
    description = "This class describes person"

    def __init__(self, name, age, years_of_experience):
        self.name = name
        self.age = age
        self.years_of_experience = years_of_experience

    def age_on_first_job(self):
        print(self.age - self.years_of_experience)


# 5.
Taras = MyCVDesc("Taras", 33, 7)

Taras.age_on_first_job()


"""
6. from some_file import MyCVDesc
"""


"""
7. Тварина - це клас. Тварини можуть жити у воді, в повітрі, на суші. Видавати різні звуки, мати різні подоби і тд.
Собака - це екземпляр класу Тварини, Він конкретно живе на суші, каже Гав і має характерний вигляд (4 лапи, хвіст).
"""
