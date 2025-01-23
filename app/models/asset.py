from typing import TYPE_CHECKING, Optional

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

if TYPE_CHECKING:
    pass


class Asset(Base):
    __tablename__ = "assets"

    asset_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    symbol: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String)
    decimal_places: Mapped[int] = mapped_column(Integer, nullable=False)
    current_unit_price: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # # Relationships
    # purchase_lots: Mapped[list["PurchaseLot"]] = relationship(back_populates="asset")
    # income_events: Mapped[list["IncomeEvent"]] = relationship(back_populates="asset")
    # sales: Mapped[list["SalesPl"]] = relationship(back_populates="asset")
    # transfers: Mapped[list["WalletTransfer"]] = relationship(back_populates="asset")
    # transfer_fees: Mapped[list["TransferFeePl"]] = relationship(back_populates="asset")
