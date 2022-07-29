import requests

from typing import Tuple
from decimal import Decimal
from datetime import datetime

from bs4 import BeautifulSoup

from django.conf import settings


def get_todays_currency() -> Tuple[Decimal, str]:
    """
        Обращается к апи центра банка
        парсит xml, возвращает курс рубля к доллару

        для парсинга xml используется BeautifulSoup
    """
    year, month, day = str(datetime.now().date()).split('-')

    response = requests.get(
        settings.CBR_API_URL,
        params={"date_req": f"{day}/{month}/{year}"},
    )

    soup = BeautifulSoup(response.content, 'lxml')

    currency = soup.find(attrs={'id': 'R01235'}).find('value').text
    currency = currency.replace(',', '.')
    char_code = soup.find(attrs={'id': 'R01235'}).find('charcode').text

    return Decimal(currency), char_code



