from django.db import models

from utils.models.timestamp import TimeStamp


class CurrencyStorage(TimeStamp):
    """
        Хранилище для хранения курса валют.
        char_code = "USD"
        value = 62.054

        В будущем можно добавить и другие валюты для конвертации

    """
    char_code = models.CharField(max_length=100, unique=True, db_index=True)
    value = models.DecimalField(max_digits=7, decimal_places=4)

    class Meta:
        verbose_name = "Today's currency"
        verbose_name_plural = "Today's currency"

