from decimal import Decimal

from pydantic import BaseModel

from src.enums.enum_gender import EnumGender


class BMetabolicRate(BaseModel):
    weight: Decimal
    height: int
    age: int
    gender: EnumGender
