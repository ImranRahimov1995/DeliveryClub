from django.db import models

from utils.models.timestamp import TimeStamp


class Subscriber(TimeStamp):
    """
        Модель в которой будут сохраняться все chat_id людей, которые
        подпишутся в телеграмме.

        Для дальнейшей рассылки

    """
    chat_id = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Telegram subscriber"
        verbose_name_plural = "Telegram subscribers"

