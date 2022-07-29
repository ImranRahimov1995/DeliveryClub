from django.db import models

from utils.models.timestamp import TimeStamp


class DeliveryRecord(TimeStamp):
    """
        Таблица записей которая будет синхорнизироваться
        с GoogleSheetsDocumment

        где:

        row_id = №
        order_id = заказ №
        price = стоимость,$
        price_in_rub = стоимость,₽
        delivery_date = срок поставки

        Дополнительно присутвует :
        created = Дата создания записи в таблице
        updated = Дата обновления записи в таблице

    """

    row_id = models.BigIntegerField()
    order_id = models.BigIntegerField(unique=True, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_in_rub = models.DecimalField(max_digits=10,
                                       decimal_places=2,
                                       blank=True)
    delivery_date = models.DateField()

    class Meta:
        verbose_name = "Delivery record"
        verbose_name_plural = "Delivery records"

    def __str__(self):
        return str(self.order_id)
