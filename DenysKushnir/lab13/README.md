## Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій

### Звіт про виконання лабораторної роботи №13
# "Поведінкові шаблони проектування"

| Виконав: студент групи КН-31 Кушнір Денис |
|------------------------------------------|
| Перевірив: Татомир Андрій                |

**Мета:** Ознайомитися з групою поведінкових шаблонів проектування.

### Хід роботи

1. Надати теоретичний опис групи поведінкових шаблонів.
2. Описати вибраний шаблон.
3. Привести приклад коду, що реалізує даний шаблон.
4. Скласти UML-діаграму.

**Поведінкові патерни проектування** — це шаблони, які фокусуються на алгоритмах і розподілі відповідальності між об'єктами. Вони допомагають визначити, як об'єкти взаємодіють один з одним, і спрощують управління складними логічними зв'язками.

### Основні типи поведінкових патернів:

- **Команда** — патерн, який інкапсулює запити як об'єкти, що дозволяє їх передавати, зберігати, скасовувати або логувати.

- **Спостерігач** — патерн, що визначає відношення «один до багатьох» між об'єктами, так що при зміні стану одного об'єкта всі його спостерігачі отримують повідомлення про цю зміну.

- **Стратегія** — патерн, який дозволяє визначити сімейство алгоритмів, інкапсулювати їх і робити їх взаємозамінними.

- **Стан** — патерн, який дозволяє об'єкту змінювати свою поведінку в залежності від свого стану.

- **Ітератор** — патерн, який забезпечує спосіб послідовного доступу до елементів складу без розкриття його внутрішньої структури.


**Для чого використовують шаблони проєктування:**

На відміну від готових функцій чи бібліотек, патерн не можна просто взяти й скопіювати в програму. Патерн являє собою не якийсь конкретний код, а загальний принцип вирішення певної проблеми, який майже завжди треба підлаштовувати для потреб тієї чи іншої програми.

Патерни часто плутають з алгоритмами, адже обидва поняття описують типові рішення відомих проблем. Але якщо алгоритм — це чіткий набір дій, то патерн — це високорівневий опис рішення, реалізація якого може відрізнятися у двох різних програмах.

Якщо провести аналогії, то алгоритм — це кулінарний рецепт з чіткими кроками, а патерн — інженерне креслення, на якому намальовано рішення без конкретних кроків його отримання.


**Опис коду у файлі main.py:**
[Посилання на реалізацію](main.py)


**Переваги цього підходу:**

Спрощення складності: Патерн дозволяє відокремити обробку запитів від логіки програми, що спрощує управління складними системами.
Легкість в розширенні: Додавання нових команд не вимагає змін у коді, який їх використовує, оскільки нові команди можуть просто реалізувати інтерфейс команди.


**Недоліки цього підходу:**

Складність управління: З управлінням великою кількістю команд може бути важко, особливо якщо вони мають складну логіку.
Залежність від контексту: Команди можуть мати залежності від контексту, в якому вони використовуються, що може ускладнити їх повторне використання.


```mermaid
classDiagram
    class Command {
        <<interface>>
        + execute()
    }

    class Light {
        + on()
        + off()
    }

    class LightOnCommand {
        - light: Light
        + execute()
    }

    class LightOffCommand {
        - light: Light
        + execute()
    }

    class RemoteControl {
        - command: Command
        + set_command(command: Command)
        + press_button()
    }

    Command <|.. LightOnCommand
    Command <|.. LightOffCommand
    RemoteControl --> Command : set_command()
    RemoteControl --> Light : interacts with

```

**Висновок:**
На цій лабораторній роботі я ознайомився з принципами роботи поведінкових патернів проектування, зокрема, з патерном Команда. Реалізація цього патерну продемонструвала, як інкапсулювати запити та взаємодіяти з об'єктами, не змішуючи логіку управління з бізнес-логікою.

