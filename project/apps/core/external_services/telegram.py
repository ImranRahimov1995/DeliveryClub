from redis import Redis
from telebot import TeleBot
from django.conf import settings

from apps.core.models import Subscriber
from apps.delivery_club.models import DeliveryRecord


class TelegramBot:
    bot = TeleBot(settings.TELEGRAM_TOKEN)

    @classmethod
    def send_notification(cls, instance: DeliveryRecord) -> None:
        """
            Этот метод отправляет всем пользователем
            в базе данных уведомление.

        """
        message = f"Время доставки заказа номер {instance.order_id} иссякло."

        cls.sync_new_subscribers()

        subscribers = Subscriber.objects.all()

        for subscriber in subscribers:
            cls.bot.send_message(
                subscriber.chat_id,
                message
            )

    @classmethod
    def sync_new_subscribers(cls) -> None:
        """
             Этот метод подключается к Redis
             и берет из множества новые chat_id.
             Затем создает записи Subscriber если их нет в базе

         """
        r = Redis(
            host='redis',
            port=6379,
            password=''
        )

        from_redis_chat_ids = r.smembers('users')

        for _ in from_redis_chat_ids:
            _, _ = Subscriber.objects.get_or_create(
                chat_id=_.decode('-utf-8')
            )
