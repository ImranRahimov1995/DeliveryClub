from typing import Literal, NamedTuple
from decimal import Decimal

from apps.core.models import CurrencyStorage


class Currency(NamedTuple):
    char_code: Literal['USD', "GBP", "AZN"]
    value: str


def convert_to_rub(currency: Currency) -> Decimal:
    """
    Простейший конвентер валют в рубли
    который берет два числа умножает друг на друга и возразращает значение
    """
    instance = CurrencyStorage.objects.get(char_code=currency[0])

    result = instance.value * currency[1]

    return result
