`## Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій



### Звіт про виконання лабораторної роботи №2
# "Твірні шаблони проектування"



| Виконав: студент групи КН-31 Грицків Тарас |
|----------------------------------------------|
| Перевірив: Татомир Андрій                    |




**Мета: Познайомитися з групою поведінкових патернів**


Хід роботи

1. Дати теоретичний опис поведінкових патернів.
2. Дати теоретичний опис вибраного патерну.
3. Навести приклад коду який реалізовує даний патерн.
4. Скласти його UML-діаграму.

Патерни поведінки – це шаблони проектування, які визначають алгоритми обчислення, розподіляють відповідальність між об'єктами та дозволяють змінювати поведінку об'єкта під час виконання. Вони фокусуються на тому, як об'єкти взаємодіють один з одним і як вони виконують завдання.

**Основні цілі патернів поведінки:**

    •   Збільшення гнучкості: Дозволяють змінювати поведінку програми без зміни її основної структури.

    •   Покращення повторюваності: Використовують готові рішення для типових задач.

    •   Спрощення розуміння коду: Забезпечують стандартизований підхід до розв'язання проблем.
**Приклади патернів поведінки:**

    •   Стратегія: Визначає сімейство алгоритмів, інкапсулює кожен з них і робить їх взаємозамінними.

    •   Спостерігач: Дозволяє об'єктам підписатися на події, що відбуваються в інших об'єктах.

    •   Ітератор: Надає послідовний доступ до елементів агрегованого об'єкта без розкриття його внутрішньої реалізації.

    •   Команда: Інкапсулює запит як об'єкт, що дозволяє відкладати або виконувати його в різний час, а також відміняти.

Ітератор - це поведінковий патерн, який забезпечує послідовний доступ до елементів агрегованого об'єкта, не розкриваючи його внутрішньої структури. Це дозволяє обходити різні колекції (списки, дерева, і т.д.) за єдиним інтерфейсом.

**Переваги ітератора:**

    •   Абстрагування від внутрішньої структури колекції: Клієнтський код не залежить від конкретної реалізації колекції.
    •   Підтримка різних способів обходу: Можливість обходу в прямому та зворотному напрямку, пропуск елементів тощо.
    •   Спрощення обходу складних структур даних: Ітератор бере на себе деталі обходу, дозволяючи клієнту зосередитися на логіці обробки елементів.
**Опис коду у файлі Lab_2:**

1. Клас Iterator:

    •   Зберігає посилання на колекцію та індекс поточного елемента.

    •   Метод __next__ повертає наступний елемент колекції або піднімає виключення StopIteration, коли елементи закінчилися.

2. Клас Collection:

    •   Зберігає список елементів.
    •   Метод __iter__ повертає екземпляр ітератора для цієї колекції.

3. Використання:

    •   Створюється екземпляр колекції.
    •   Елементи додаються до колекції.
    •   Цикл for автоматично використовує метод __iter__ для отримання ітератора і метод __next__ для обходу елементів.

**Висновок**

Патерн ітератор є потужним інструментом для роботи з різними колекціями даних. Він дозволяє абстрагуватися від внутрішньої структури колекції, забезпечує гнучкий механізм обходу елементів і спрощує написання клієнтського коду. В Python ітератори інтегровані в мову, що робить їх використання простим і природним.