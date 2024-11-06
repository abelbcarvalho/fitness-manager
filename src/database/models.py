from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    DECIMAL,
    ForeignKey,
    Enum,
    Integer,
    String,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)

from src.enums.enum_gender import EnumGender
from src.enums.enum_intensity import EnumIntensity


class Base(DeclarativeBase):
    pass


class UserDB(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    date_born: Mapped[date] = mapped_column(Date, nullable=False)
    gender: Mapped[EnumGender] = mapped_column(Enum(EnumIntensity), nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[Decimal] = mapped_column(DECIMAL(6, 3), nullable=False)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    update_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), onupdate=datetime.now())


class BMetabolicRateDB(Base):
    __tablename__ = "metabolic_rate"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    weight: Mapped[Decimal] = mapped_column(DECIMAL(6,3), nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    gender: Mapped[EnumGender] = mapped_column(Enum(EnumGender), nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"), nullable=False)
    user: Mapped[UserDB] = mapped_column(back_populates="metabolic_rates")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), onupdate=datetime.now())


class BRMIntensityDB(Base):
    __tablename__ = "brm_intensity"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    tmb_brm: Mapped[Decimal] = mapped_column(DECIMAL, nullable=False)
    intensity: Mapped[EnumIntensity] = mapped_column(Enum(EnumIntensity), nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"), nullable=False)
    user: Mapped[UserDB] = mapped_column(back_populates="brm_intensities")

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(), onupdate=datetime.now())
