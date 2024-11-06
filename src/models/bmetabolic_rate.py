from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from src.enums.enum_gender import EnumGender


class BMetabolicRate(BaseModel):
    weight: Decimal
    height: int
    age: int
    gender: EnumGender

    user_id: Optional[int] = None
