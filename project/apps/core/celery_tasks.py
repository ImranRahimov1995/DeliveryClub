from datetime import datetime
from decimal import Decimal

from config.celery import app
from celery.signals import worker_ready

from apps.core.models import CurrencyStorage
from apps.delivery_club.models import DeliveryRecord
from apps.core.pydantic_validator import AfterGoogleSheetsApiValidation
from apps.core.external_services.telegram import TelegramBot
from apps.core.external_services.currency import get_todays_currency
from apps.core.external_services.sync_with_google_sheets import (
    get_all_data,
    get_all_orders_id,
)


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


@app.task
def sync_with_remote_table():
    """
        Background задача, которая использует внешний сервис,
        получает данные, валидирует
        и синхронизирует их с базой данных.

        Задача будет отрабатывать каждые 10 секунд.

    """
    dataset = get_all_data()

    for row in dataset:
        try:
            validated_data = AfterGoogleSheetsApiValidation(
                id=row['№'],
                order_id=row['заказ №'],
                price=row['стоимость,$'],
                delivery_date=datetime.strptime(
                    row['срок поставки'],
                    "%d.%m.%Y"
                )
            )

        except:
            continue

        if validated_data:
            try:

                instance = DeliveryRecord.objects.get(
                    order_id=validated_data.order_id
                )

                # здесь проверяем если все поля равны ничего не изменяем
                if instance.row_id == validated_data.id and \
                        instance.price == validated_data.price and \
                        instance.delivery_date == validated_data.delivery_date.date():
                    continue

                instance.row_id = validated_data.id
                instance.price = validated_data.price
                instance.delivery_date = validated_data.delivery_date

                instance.save()

            except DeliveryRecord.DoesNotExist:

                instance = DeliveryRecord.objects.create(
                    row_id=validated_data.id,
                    order_id=validated_data.order_id,
                    price=validated_data.price,
                    delivery_date=validated_data.delivery_date
                )
            except Exception as e:
                pass


@app.task
def delete_unnecessary_records():
    """
        Здесь мы получаем все номера заказов c GoogleSheetsDocument
        Затем получаем все значение столбцов order_id из базы данных.
        Сверяем их, удоляем те которые не существует в GoogleSheetsDocument

        Задача будет отрабатывать каждые 25 секунд.

    """
    remote_order_ids = get_all_orders_id()

    db_order_ids = DeliveryRecord.objects.values_list('id', 'order_id')

    waiting_for_delete_ids = []

    for record in db_order_ids:
        if str(record[1]) not in remote_order_ids:
            waiting_for_delete_ids.append(record[0])

    if waiting_for_delete_ids:
        DeliveryRecord.objects.filter(id__in=waiting_for_delete_ids).delete()

    return True


@app.task
def send_notification_in_telegram(record_id):
    """
        Background задача для отправки уведомление в телеграм.

        Срабатывает при истечении срока поставки.

    """
    TelegramBot.send_notification(
        DeliveryRecord.objects.get(id=record_id)
    )
