
# Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій

### Звіт про виконання лабораторної роботи №1
### Тема: "Твірні шаблони проектування"

| Виконав: студент групи КН-31 Сітка Владислав |  
| ------------------------------------------ |  
| Перевірив: Татомир Андрій                  |  

---

### Мета
Познайомитися з групою твірних шаблонів проектування та дослідити їхнє застосування на практиці.

---

### Завдання

1. Дати теоретичний опис твірної групи шаблонів.
2. Відповідно до индивідуального завдання:
    - дати теоретичний опис даного шаблону;
    - навести приклад коду який реалізовує даний шаблон;
    - скласти його UML-діяграму.

---

### Твірні шаблони

Це один з типів шаблонів проектування в програмуванні, який фокусується на процесі створення об'єктів. Основна мета твірних шаблонів — надання гнучкості у виборі стратегії створення об'єктів, а також уникнення прямого використання оператора new для створення об'єктів. Це дозволяє зменшити залежність класів від конкретних реалізацій і полегшує розширення коду.

### Шаблон 'Прототип'

Прототип — дозволяє копіювати вже існуючі об'єкти замість створення нових шляхом виклику їх конструктора.Це патерн проектування, що дозволяє копіювати об'єкти, не вдаючись у подробиці їх реалізації. Це корисно , коли створення об’єкта є ресурсомістким або складним, оскільки клонування значно спрощує цей процес.

### Посилання на код

[Код](Prototype.py)


```mermaid
classDiagram
    class Prototype {
        +clone(): Prototype
    }

    class ConcretePrototype1 {
        +clone(): Prototype
    }
    
    class ConcretePrototype2 {
        +clone(): Prototype
    }

    class Client {
        +prototype: Prototype
        +operation(): void
    }

    Prototype <|-- ConcretePrototype1
    Prototype <|-- ConcretePrototype2
    Client --> Prototype

```
---

### Висновок

У ході виконання лабораторної роботи №1 на тему "Твірні шаблони проектування" я ознайомився з основами твірних шаблонів, їх призначенням та застосуванням у програмуванні. Особливу увагу було приділено шаблону **Прототип**, який дозволяє створювати копії об'єктів без їх прямої інстанціації, що полегшує роботу з об'єктами, що мають складну структуру.

Я вивчив основні компоненти шаблону "Прототип", такі як базовий прототип і конкретні прототипи, а також метод клонування. Це допомогло зрозуміти, як можна використовувати цей шаблон для створення нових об'єктів на основі існуючих.

Крім того, я реалізував приклад коду, що демонструє роботу шаблону, та створив UML-діаграму, яка ілюструє зв'язки між компонентами.

---


