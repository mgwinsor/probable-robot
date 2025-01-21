from typing import TYPE_CHECKING, Optional

from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base

if TYPE_CHECKING:
    from app.models import IncomeEvent, PurchaseLot


class AcquisitionType(Base):
    __tablename__ = "acquisition_types"

    type_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)

    # Relationships
    purchase_lots: Mapped[list["PurchaseLot"]] = relationship(
        back_populates="acquisition_type"
    )
    income_events: Mapped[list["IncomeEvent"]] = relationship(
        back_populates="acquisition_type"
    )
