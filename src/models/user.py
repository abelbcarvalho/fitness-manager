from decimal import Decimal

from datetime import date

from pydantic import BaseModel

from src.enums.enum_gender import EnumGender


class User(BaseModel):
    full_name: str
    date_born: date
    gender: EnumGender
    height: int
    weight: Decimal
