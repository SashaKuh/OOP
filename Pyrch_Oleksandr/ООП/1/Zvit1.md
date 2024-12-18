
# Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій

### Звіт про виконання лабораторної роботи №1
### Тема: "Твірні шаблони проектування"

| Виконав: студент групи КН-31 Пирч Олександр |  
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

Твірні шаблони (англ. Creational patterns) — це шаблони проєктування, що абстрагують процес побудови об'єктів. Вони допоможуть зробити систему незалежною від способу створення, композиції та представлення її об'єктів.

Шаблон, який породжує класи, використовує успадкування, щоб варіювати створюваний клас, а шаблон, що створює об'єкти, делегує інстанціювання іншому об'єктові.

Ці шаблони важливі, коли система більше залежить від композиції об'єктів, ніж від успадкування класів.

Таким чином, замість прямого кодування фіксованого набору поведінок, визначається невеликий набір фундаментальних поведінок, за допомогою композиції яких можна отримувати складніші.

Таким чином, для створення об'єктів з конкретною поведінкою потрібно щось більше, ніж просте інстанціювання екземпляру класу.

Шаблони, що породжують, інкапсулюють знання про конкретні класи, які застосовуються у системі та приховують деталі того, як ці класи створюються і стикуються між собою.

Єдина інформація про об'єкти, що відома системі — їхні інтерфейси.

### Абстрактний метод

Шаблон Абстрактна фабрика використовується для створення сімейств пов'язаних об'єктів без необхідності вказувати їхні конкретні класи. Це дозволяє створювати групи об'єктів, які працюють разом, і забезпечує, що клієнт працює з об'єктами через загальний інтерфейс..

####  Основні характеристики:
- Створює сімейства пов'язаних об'єктів: Абстрактна фабрика надає інтерфейс для створення кількох різних об'єктів, що можуть працювати разом.
- Змінює тип створюваних об'єктів: Клієнтський код не залежить від конкретних класів створюваних об'єктів.
- Спрощує заміну цілих груп об'єктів: Заміна одного набору об'єктів на інший стає простою задачею завдяки інтерфейсу фабрики.

#### Як реалізувати шаблон Сінглтон:
1) Визначається абстрактна фабрика для створення кожного типу об'єкта (кнопки, чекбокси тощо).
2) Кожна конкретна фабрика реалізує інтерфейс абстрактної фабрики для створення продуктів у своєму стилі (наприклад, Windows або MacOS).
3) Клієнтський код використовує інтерфейс абстрактної фабрики для створення об'єктів, не знаючи їх конкретних класів.

#### Приклад використання:
Припустимо, ми хочемо створити інтерфейс для різних видів GUI (графічного інтерфейсу користувача) елементів, таких як кнопки та чекбокси. У нас є два стилі — Windows та MacOS. Шаблон Abstract Factory дозволить створювати відповідні елементи GUI в залежності від вибраної платформи.

```mermaid
classDiagram
    class GUIFactory {
        <<interface>>
        +create_button(): Button
        +create_checkbox(): Checkbox
    }

    class WindowsFactory {
        +create_button(): WindowsButton
        +create_checkbox(): WindowsCheckbox
    }

    class MacOSFactory {
        +create_button(): MacOSButton
        +create_checkbox(): MacOSCheckbox
    }

    class Button {
        <<interface>>
        +render(): str
    }

    class Checkbox {
        <<interface>>
        +render(): str
    }

    class WindowsButton {
        +render(): str
    }

    class MacOSButton {
        +render(): str
    }

    class WindowsCheckbox {
        +render(): str
    }

    class MacOSCheckbox {
        +render(): str
    }

    GUIFactory <|.. WindowsFactory
    GUIFactory <|.. MacOSFactory
    Button <|.. WindowsButton
    Button <|.. MacOSButton
    Checkbox <|.. WindowsCheckbox
    Checkbox <|.. MacOSCheckbox

```

---

### Висновок

Шаблон Абстрактна фабрика дозволяє легко розширювати програму, створюючи нові сімейства продуктів. Він корисний тоді, коли програма має працювати з кількома платформами або системами, і важливо, щоб ці елементи інтегрувалися між собою. Використання цього шаблону дозволяє зберігати чистоту архітектури, відокремлюючи створення об'єктів від їх використання. Однак, це може призвести до ускладнення коду при великій кількості продуктів або платформ.

