# Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій

### Звіт про виконання лабораторної роботи №4
### Тема: "Принципи проєктування програмного забезпечення"

| Виконав: студент групи КН-31 Грицків Тарас |  
| ------------------------------------------ |  
| Перевірив: Татомир Андрій Володимирович                  |  

---

### Мета
Познайомитися з найбільш поширеними сучасними принципами проєктування програмного забезпечення.

---

### Хід роботи

1. Теоретичний опис принципів проєктування.
2. Теоретичний опис вибраного принципу проєктування.
3. Приклад коду, що реалізовує вибраний принцип .
4. UML-діаграма для пояснення архітектури.

---

# Принципи SOLID

SOLID — це набір принципів об'єктно-орієнтованого проєктування, які допомагають створювати більш масштабовані та зрозумілі програми. 

## 1. Single Responsibility Principle (SRP) — Принцип єдиної відповідальності

**Клас повинен мати одну й тільки одну причину для змін.**

Це означає, що клас повинен виконувати тільки одну функцію або представляти одну концепцію.


## 2. Open/Closed Principle (OCP) — Принцип відкритості/закритості

**Програмні сутності мають бути відкритими для розширення, але закритими для модифікації.**

Це означає, що ми можемо додавати нову функціональність без зміни існуючого коду, використовуючи абстракції та наслідування.

## 3. Liskov Substitution Principle (LSP) — Принцип підстановки Барбари Лісков

**Об'єкти базового класу повинні бути замінені об'єктами його підкласів без порушення логіки програми.**

## 4. Interface Segregation Principle (ISP) — Принцип розділення інтерфейсу

**Клієнти не повинні залежати від інтерфейсів, які вони не використовують.**

Це означає, що варто створювати вузькоспеціалізовані інтерфейси для окремих завдань.

## 5. Dependency Inversion Principle (DIP) — Принцип інверсії залежностей

**Модулі вищого рівня не повинні залежати від модулів нижчого рівня. Обидва повинні залежати від абстракцій.**

# Interface Segregation Principle (Принцип розділення інтерфейсу)

**Принцип розділення інтерфейсу (Interface Segregation Principle, ISP)** — це один із SOLID-принципів, який рекомендує створювати вузькоспеціалізовані інтерфейси, призначені для конкретних завдань. Згідно з ISP, клієнти не повинні залежати від інтерфейсів, які вони не використовують. Якщо клас реалізує інтерфейс, але не використовує всі його методи, це може свідчити про порушення цього принципу.

## Основна ідея принципу ISP

Основна ідея ISP полягає в тому, щоб уникати "великих" інтерфейсів із великою кількістю методів. Замість цього, слід створювати кілька інтерфейсів, кожен з яких буде мати вузькоспеціалізовані функції. Це робить систему більш гнучкою і зручною для розширення.

### Плюси та мінуси принципу розділення інтерфейсу (Interface Segregation Principle, ISP)

Принцип розділення інтерфейсу (ISP) спрямований на те, щоб кожен інтерфейс був спеціалізованим та не містив зайвих методів, які не використовуються певними класами. Це забезпечує гнучкість у проєктуванні та підвищує зручність підтримки коду, проте може мати і свої недоліки.

---

### Плюси

1. **Зменшення залежностей**: Клієнти залежать тільки від тих методів, які їм дійсно потрібні. Це робить код більш незалежним і мінімізує зв'язки між різними частинами системи.
  
2. **Покращення читабельності**: Чіткі та вузькоспеціалізовані інтерфейси роблять код зрозумілішим. Програмістам легше зрозуміти, яку функціональність реалізує кожен інтерфейс.

3. **Простіше тестування**: Завдяки розділенню інтерфейсів можна окремо тестувати конкретну функціональність, зосереджуючись тільки на потрібних методах. Це зменшує кількість зайвого коду при написанні тестів.

4. **Підтримка принципу інкапсуляції**: ISP допомагає дотримуватися інкапсуляції, оскільки класу надаються тільки необхідні методи. Класам не потрібно реалізовувати методи, які вони не використовують.

5. **Гнучкість розширення**: У разі потреби додати новий функціонал можна створити новий інтерфейс або модифікувати один із існуючих без зміни інших частин системи.

---

### Мінуси

1. **Збільшення кількості інтерфейсів**: ISP може призвести до створення великої кількості інтерфейсів, особливо в складних системах. Це може ускладнити навігацію по коду та знизити загальну оглядовість проєкту.

2. **Ускладнення структури системи**: Коли інтерфейси розділені на дуже дрібні частини, це може створювати враження надмірної деталізації, що ускладнює розуміння загальної архітектури, особливо для нових розробників у проєкті.

3. **Необхідність додаткового планування**: Визначення вузьких інтерфейсів потребує ретельного аналізу вимог до кожного компонента системи. Це додає часу на етапі проєктування, що може бути недоліком для малих проєктів або швидких MVP-рішень.

4. **Ризик надмірної спеціалізації**: Якщо інтерфейси поділені занадто сильно, це може призвести до ситуації, коли класи потребують одночасної реалізації кількох інтерфейсів, щоб охопити необхідну функціональність, що може ускладнити підтримку та розвиток системи.

---

## Приклад на Python

Уявімо систему мультимедійних пристроїв, таких як радіо і телевізор, де деякі пристрої можуть тільки відтворювати аудіо, а інші — і аудіо, і відео. Щоб дотримуватися принципу ISP, ми створимо два інтерфейси: один для відтворення аудіо, інший — для відтворення відео.

Код можна знайти у файлі [`lab_4.py`](./lab_4.py).

### Пояснення коду

1. **Інтерфейс `AudioDevice`**: це абстрактний базовий клас із методом `play_audio()`. Клас `AudioDevice` представляє пристрої, здатні відтворювати аудіо, тому він містить лише один метод `play_audio()`. У Python ми реалізуємо абстрактні класи за допомогою модуля `abc`, і кожен абстрактний метод позначаємо декоратором `@abstractmethod`.

2. **Інтерфейс `VideoDevice`**: аналогічно `AudioDevice`, `VideoDevice` — це абстрактний клас із методом `play_video()`. Він представляє пристрої, що здатні відтворювати відео. Це дозволяє уникати зайвих методів у тих класах, де вони не потрібні.

3. **Клас `Radio`**: цей клас реалізує лише інтерфейс `AudioDevice`, оскільки радіо може відтворювати лише аудіо. Метод `play_audio()` виводить повідомлення про відтворення аудіо на радіо. Оскільки `Radio` не потребує відтворення відео, йому не потрібно реалізовувати методи з `VideoDevice`, що і є реалізацією принципу ISP.

4. **Клас `Television`**: телевізор може відтворювати як аудіо, так і відео, тому цей клас реалізує обидва інтерфейси — `AudioDevice` і `VideoDevice`. У класі `Television` реалізовані методи `play_audio()` і `play_video()`, що виводять повідомлення про відтворення аудіо і відео відповідно.

5. **Функція `start_audio()`**: ця функція приймає пристрій, що реалізує інтерфейс `AudioDevice`, і викликає метод `play_audio()`. Таким чином, ми можемо передати як об'єкт `Radio`, так і `Television` у цю функцію, оскільки обидва класи реалізують `AudioDevice`.

### Висновок

Цей приклад демонструє, як принцип ISP дозволяє створювати вузькоспеціалізовані інтерфейси. Завдяки цьому принципу ми уникаємо ситуацій, коли клас повинен реалізовувати методи, які він не використовує. У випадку з `Radio` та `Television`, кожен клас реалізує лише ті інтерфейси, які йому дійсно потрібні.



```mermaid
classDiagram
    class AudioDevice {
        +play_audio()
    }
    
    class VideoDevice {
        +play_video()
    }
    
    class Radio {
        +play_audio()
    }
    
    class Television {
        +play_audio()
        +play_video()
    }
    
    AudioDevice <|.. Radio
    AudioDevice <|.. Television
    VideoDevice <|.. Television


