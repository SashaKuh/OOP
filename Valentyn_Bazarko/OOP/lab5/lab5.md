## Львівський Національний Університет Природокористування
## Кафедра Інформаційних систем та Технологій



### Звіт про виконання лабораторної роботи №5
# "Рефакторинг"



| Виконав: студент групи КН-31 Базарко Валентин |
|----------------------------------------------|
| Перевірив:Татомир Андрій            |




Мета
Познайомитися з основними принципами та найбільш поширеними техніками рефакторингу програмного забезпечення.


Хід роботи
1. Дати загальний опис принципів рефакторингу.
2. Ознайомитися із основними техніками рефакторингу.
3. Познайомитися із поняттям “запахів коду”.
_____________________________
### Чистий код

Чистий код" або "clean code" - це термін, який використовується для опису коду, який легко читати, зрозуміти та підтримувати. Такий код має такі основні характеристики:

Основні характеристики чистого коду:
Описові імена змінних, функцій і класів:

Імена змінних, функцій і класів повинні бути чіткими і зрозумілими, щоб будь-хто міг легко зрозуміти їх призначення.

Чітка структура і форматування:

Код повинен бути добре відформатований з дотриманням відступів, що покращує його читабельність.

Коментарі та документація:

Важливі частини коду повинні бути пояснені коментарями. Докстрінги використовуються для пояснення функцій, класів і методів.

Однофункціональність методів і функцій:

Функції та методи повинні виконувати лише одну задачу. Це полегшує їх тестування та повторне використання.

Обробка помилок:

Код повинен включати механізми обробки помилок для забезпечення стабільності та надійності.

Тестування:

Чистий код має бути легко тестованим. Хороша практика - це написання тестів для важливих функцій.
_____________

### Переваги чистого коду:
Простота підтримки та оновлення: Завдяки зрозумілим іменам і чіткій структурі, код легко підтримувати і розширювати.

Зручність у тестуванні: Чистий код легше тестувати, що підвищує надійність програмного забезпечення.

Легкість у читанні: Чіткі імена і коментарі допомагають зрозуміти логіку коду навіть через тривалий час.

### Брудний код
"Брудний код" або "dirty code" - це код, який важко читати, розуміти та підтримувати. Він часто створює проблеми для розробників і може спричинити помилки, збільшуючи час і зусилля на підтримку програмного забезпечення. 

Основні характеристики брудного коду:
Невиразні імена змінних, функцій та класів:

Використання коротких або незрозумілих імен, які не відображають призначення змінних, функцій або класів.

Відсутність коментарів:

Код не містить коментарів, що пояснюють логіку або важливі частини коду.

Жорстко закодовані значення:

Використання жорстко закодованих значень (наприклад, магічних чисел) без пояснень або зовнішніх конфігурацій.

Відсутність структурованості та форматування:

Код не дотримується стандартів форматування, містить нерегулярні відступи та структуру, що ускладнює його читання.

Відсутність обробки помилок:

Код не враховує можливі помилки та не містить механізмів їх обробки, що може призвести до збоїв у програмі.

Надмірна складність:

Код містить надмірно складну логіку або занадто багато функціональності в одному методі або класі.

Недоліки брудного коду:
Незрозумілі імена: Назви функції func і змінних a, b, r не є описовими.

Відсутність коментарів: Немає пояснень, що саме робить функція.

Жорстко закодовані значення: Значення 5 в параметрі функції передано без пояснень.

Відсутність обробки помилок: Немає перевірки на випадок помилок.

Наслідки:
Важкість у підтримці: Підтримка і модифікація коду займають більше часу та зусиль.

Висока ймовірність помилок: Складніше виявляти та виправляти помилки.

Зниження продуктивності команди: Інші розробники витрачають більше часу на розуміння і роботу з кодом.
[Код1](code_before.py) [Код2](code_after.py)
## Висновки. 

Чистий код сприяє більш ефективній співпраці між розробниками, знижує ймовірність помилок та підвищує надійність програмного забезпечення.Брудний код створює значні труднощі в процесі розробки, тестування та підтримки програмного забезпечення, що може призвести до збільшення витрат часу та ресурсів.Перехід до написання чистого коду потребує свідомих зусиль та дотримання принципів і кращих практик програмування. Це вклад у довгострокову успішність програмного проєкту, який окупається через зниження технічного боргу, покращення якості продукту та підвищення задоволеності команди.
