# Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій

### Звіт про виконання лабораторної роботи №2
### Тема: "Поведінкові патерни проектування"

| Виконав: студент групи КН-31 Грицків Тарас |  
| ------------------------------------------ |  
| Перевірив: Татомир Андрій                  |  

---

### Мета
Познайомитися з групою поведінкових патернів та дослідити їхнє застосування на практиці.

---

### Хід роботи

1. Теоретичний опис поведінкових патернів.
2. Теоретичний опис вибраного патерну.
3. Приклад коду, що реалізовує вибраний патерн.
4. UML-діаграма для пояснення архітектури.

---

### Опис поведінкових патернів

Поведінкові патерни проектування – це шаблони, які визначають способи взаємодії між об’єктами та розподіляють відповідальність за виконання завдань. Вони дозволяють змінювати поведінку об'єктів під час виконання програми без необхідності змінювати їхню структуру.

**Основні цілі поведінкових патернів:**

- **Гнучкість**: дають можливість змінювати поведінку системи без змін її основної структури.
- **Повторюваність**: використовують готові рішення для типових завдань.
- **Зручність у використанні**: спрощують розуміння коду завдяки стандартизованим підходам до розв'язання задач.

---

### Приклади поведінкових патернів

- **Стратегія**: визначає набір алгоритмів, інкапсулює кожен з них і робить їх взаємозамінними.
- **Спостерігач**: дозволяє об'єктам підписуватись на події в інших об'єктах.
- **Ітератор**: забезпечує послідовний доступ до елементів агрегованого об'єкта без розкриття його внутрішньої структури.
- **Команда**: інкапсулює запит як об'єкт, що дозволяє виконувати його пізніше, або відміняти.

---

### Ітератор: 

**Ітератор** – це поведінковий патерн, який надає механізм для послідовного доступу до елементів складної структури даних (наприклад, списків, дерев) без розкриття її внутрішньої організації.

#### Переваги ітератора:

- **Абстрагування**: клієнтський код не залежить від внутрішньої структури колекції.
- **Гнучкість**: ітератори дозволяють різні методи обходу даних, включно з обходом у прямому чи зворотному напрямку.
- **Спрощення**: деталі обходу даних приховані всередині ітератора, що спрощує роботу з великими структурами даних.

#### Реалізація патерну ітератор

# Пояснення коду ітератора

Цей код реалізує ітератор на Python, який проходить по списку і повертає два значення: індекс елемента та його значення, помножене на цей індекс.

# Реалізація Пов'язаного Списку з Ітератором

Цей проєкт реалізує однозв'язний список (`LinkedList`) на Python, у якому кожен вузол містить значення та посилання на наступний елемент. Також реалізовано окремий клас ітератора для зручного проходження по елементах списку. Ітерація відбувається завдяки класу `LinkedListIterator`, який визначає, як послідовно отримувати елементи зі списку.

Код можна знайти у файлі [`lab_3_update.py`](./lab_3_update.py).

## Структура проєкту

- `Node`: Клас вузла, який зберігає значення та посилання на наступний вузол у списку.
- `LinkedList`: Основний клас пов'язаного списку з методами для додавання, видалення, пошуку елементів та підтримкою ітерації.
- `LinkedListIterator`: Окремий клас ітератора, який забезпечує послідовний доступ до елементів списку.

## Класи та їх методи

### Клас `Node`

Клас вузла `Node` представляє елемент у пов'язаному списку.

- **Атрибути**:
  - `value`: Значення вузла.
  - `next`: Посилання на наступний вузол у списку.

### Клас `LinkedList`

Клас `LinkedList` реалізує пов'язаний список з основними методами для маніпуляції елементами та підтримкою ітерації.

- **Методи**:
  - `__init__()`: Ініціалізує порожній список із початковим вузлом `head = None`.
  - `append(value)`: Додає новий елемент в кінець списку.
  - `prepend(value)`: Додає новий елемент на початок списку.
  - `delete(value)`: Видаляє перше входження елемента зі значенням `value`.
  - `find(value)`: Шукає елемент зі значенням `value` і повертає його, якщо знайдено.
  - `__iter__()`: Повертає екземпляр `LinkedListIterator` для ітерації по елементах списку.
  - `__str__()`: Повертає рядок, що представляє список

#### UML-diagram

```mermaid
classDiagram
    class Node {
        - value: Any
        - next: Node
        + __init__(value: Any)
    }
    
    class LinkedList {
        - head: Node
        + __init__()
        + append(value: Any)
        + prepend(value: Any)
        + delete(value: Any)
        + find(value: Any) Node
        + __iter__() LinkedListIterator
        + __str__() str
    }
    
    class LinkedListIterator {
        - current: Node
        + __init__(head: Node)
        + __iter__() LinkedListIterator
        + __next__() Any
    }
    
    Node --> LinkedList : "включає"
    LinkedListIterator --> Node : "ітерація за"
    LinkedList --> LinkedListIterator : "створює ітератор"
