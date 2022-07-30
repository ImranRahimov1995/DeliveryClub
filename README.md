# DeliveryClub
### Тестовое задание Python

Время выполнение : 24 часа.

Ссылка на GoogleSheetsDocument:

https://docs.google.com/spreadsheets/d/10UY-C44xn24_SnQx7tQ7iCcePPipPaSaTTT_x6-RIHU/edit?usp=sharing

Стек : Django Postgres Redis Nginx Celery
___________
### Инструкция для запуска и проверки


1. Создайте папку запустите терминал в ней.

2. `git clone https://github.com/ImranRahimov1995/DeliveryClub.git`

3. `docker-compose build --no-cache`   (Долгая сборка возможно)

4. `docker-compose up`

5.  open in browser http://0.0.0.0

_______________________________________________

## Для проверки телеграм :

1. Нужно подписаться на https://t.me/DeliveryTimeExpiredBot

2. Нужно отправить `/start`

3. Создать запись в документе с просроченной датой доставки. (22.05.2022)

4. Через 10-15 секунд бот отправит сообщение.

___________________________________________________
## О приложении :

Приложение имеет графический интерфейс.

Обнавляет данные каждые 10 секунд,фиксирует удоление каждый 25 секунд.

Курс Цб РФ.

Приложение фиксирует добавление, удоление,обновление записей.

Валидирует данные(неправильные данные не добавляются), уникален для номера заказа. 

Отправляет уведомление в телеграм по истечении срока.

Про безопастность я в курсе. просто ради удобства использование для вас , я оставил в проекте открытым некоторые файлы.

Комментарии по разработки находятся в коде.

Коммиты информативны.