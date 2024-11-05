from decimal import Decimal

from pydantic import BaseModel

from src.enums.enum_intensity import EnumIntensity


class BRMIntensity(BaseModel):
    tmb_brm: Decimal
    intensity: EnumIntensity
