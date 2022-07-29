import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from config.celery import app
from apps.delivery_club.models import DeliveryRecord
from apps.core.celery_tasks import send_notification_in_telegram


@receiver(post_save, sender=DeliveryRecord)
def create_task_which_send_notification(sender, instance, created, **kwargs):
    """
        Это функция, которая запускается
        после метода save DeliveryRecord.
        Создает для каждой записи ETA задачу которая выполняется
        во время которое указали в delivery_date.

    """

    send_notification_in_telegram.apply_async(
        args=[instance.pk, ],
        eta=datetime.datetime.combine(
            instance.delivery_date,
            datetime.time(0, 0, 0)
        ),
        task_id="ETA-" + str(instance.pk)
    )
