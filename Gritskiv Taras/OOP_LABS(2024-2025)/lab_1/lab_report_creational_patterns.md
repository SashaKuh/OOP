
# Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій

### Звіт про виконання лабораторної роботи №1
### Тема: "Твірні шаблони проектування"

| Виконав: студент групи КН-31 Грицків Тарас |  
| ------------------------------------------ |  
| Перевірив: Татомир Андрій                  |  

---

### Мета
Познайомитися з групою твірних шаблонів проектування та дослідити їхнє застосування на практиці.

---

### Хід роботи

1. Теоретичний опис твірної групи шаблонів.
2. Теоретичний опис вибраного шаблону.
3. Приклад коду, що реалізовує вибраний шаблон.
4. UML-діаграма для пояснення архітектури.

---

### Теоретичний опис твірних шаблонів проектування

Твірні шаблони проектування (або породжувальні патерни) — це повторювані рішення для типових проблем, які виникають під час розробки програмного забезпечення. Вони допомагають робити код більш гнучким, зрозумілим і легким для підтримки, забезпечуючи ефективне управління процесом створення об'єктів.

Основні твірні патерни:

- Фабричний метод: Визначає інтерфейс для створення об'єктів, але дозволяє підкласам вирішувати, який клас інстанціювати. Це зручно, коли потрібно створювати об'єкти на основі певних умов.
- Абстрактна фабрика: Надає інтерфейс для створення сімейств пов'язаних або залежних об'єктів без вказування їх конкретних класів.
- Будівельник: Розділяє процес створення складного об'єкта на кілька кроків, дозволяючи створювати різні представлення цього об'єкта.
- Прототип: Створює нові об'єкти шляхом копіювання існуючого об'єкта (прототипу).
- Одинак: Гарантує, що існує лише один екземпляр класу, забезпечуючи глобальний доступ до нього.

---

### Фабричний метод

Фабричний метод — це один із основних твірних патернів проектування. Він надає інтерфейс для створення об'єктів у суперкласі, але дозволяє підкласам змінювати тип створюваних об'єктів. Таким чином, фабричний метод забезпечує гнучкість у виборі типу об'єкта, що створюється, без прив'язки до конкретних класів під час написання коду.

#### Переваги фабричного методу:
- Розширюваність: Легко додати нові класи без зміни існуючого коду.
- Гнучкість: Дає можливість вибирати тип створюваних об'єктів динамічно, під час виконання програми.
- Інкапсуляція: Всі деталі створення об'єктів приховані у фабричних методах.

#### Коли використовувати фабричний метод:
- Коли створення об'єктів залежить від умов або конфігурацій, що можуть змінюватись під час виконання програми.
- Коли потрібно створювати різні класи об'єктів, що мають спільний базовий клас або інтерфейс.

```mermaid
classDiagram
    Vehicle <|-- Car
    Vehicle <|-- Plane
    Vehicle <|-- Ship
    VehicleFactory --> Vehicle

    class Vehicle {
        +move()
    }

    class Car {
        +move()
    }

    class Plane {
        +move()
    }

    class Ship {
        +move()
    }

    class VehicleFactory {
        +create_vehicle(vehicle_type: str): Vehicle
    }
```

---

### Висновок

На цій лабораторній роботі я ознайомився з твірними шаблонами проектування, зокрема з **Фабричним методом**. Я навчився, як за допомогою цього патерну можна створювати об'єкти різних типів, не вказуючи їх безпосередньо в коді, що сприяє гнучкості та масштабованості програмних систем.

---


