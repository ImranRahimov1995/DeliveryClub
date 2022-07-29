from decimal import Decimal
from datetime import datetime

from pydantic import BaseModel, Field


class AfterGoogleSheetsApiValidation(BaseModel):
    """
        Validator который будет валидировать данные пришедшие с Google sheets
    """
    id: int = Field(gt=0)
    order_id: int
    price: Decimal = Field(gt=0)
    delivery_date: datetime
