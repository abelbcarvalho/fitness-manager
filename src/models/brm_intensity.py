from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from src.enums.enum_intensity import EnumIntensity


class BRMIntensity(BaseModel):
    tmb_brm: Decimal
    intensity: EnumIntensity

    user_id: Optional[int] = None
