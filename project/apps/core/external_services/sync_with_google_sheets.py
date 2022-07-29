from typing import Dict, List
import gspread

from django.conf import settings

gc = gspread.service_account(
    filename=settings.GOOGLE_SHEETS_CREDENTIALS_JSON_PATH
)


def get_all_data() -> Dict:
    """
        Обращается к Gogle Sheets Api получает все записи в таблице
    """
    gsheet = gc.open("TestWork")
    dataset = gsheet.sheet1.get_all_records()

    return dataset


def get_all_orders_id() -> List:
    """
        Обращается к Gogle Sheets Api получает все значение
        в столбце "заказ №"
    """
    gsheet = gc.open("TestWork")
    dataset = gsheet.sheet1.col_values(2)

    return dataset[1:]
