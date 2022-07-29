from decimal import Decimal

from config.celery import app
from celery.signals import worker_ready

from apps.core.models import CurrencyStorage
from apps.delivery_club.models import DeliveryRecord
from apps.core.external_services.currency import get_todays_currency


@app.task
def currency_control():
    """
        Эта задача будет отрабатывать каждый час.
        Она проверяет курс центра банка и записывает значение
        в базу данных.

    """

    _currency, _char_code = get_todays_currency()

    try:
        db_record, _ = CurrencyStorage.objects.get_or_create(
            char_code=_char_code,
        )
        _old_value = db_record.value
        db_record.value = _currency
        db_record.save()

        # Проверяем если курс изменился обнавляем все записи
        if _old_value != Decimal(_currency):
            for instance in DeliveryRecord.objects.all():
                instance.save()

    except Exception as e:
        return False

    return True


@worker_ready.connect
def at_ready(sender, **kwargs):
    """
        Это функуия отрабатывает когда worker celery бывает готов,
        т.е после запуска
    """
    return currency_control.apply_async()
