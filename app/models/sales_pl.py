from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base

if TYPE_CHECKING:
    from app.models import Asset, SaleLotPl, Wallet


class SalesPl(Base):
    __tablename__ = "sales_pl"

    sale_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    asset_id: Mapped[int] = mapped_column(ForeignKey("assets.asset_id"), nullable=False)
    wallet_id: Mapped[int] = mapped_column(
        ForeignKey("wallets.wallet_id"),
        nullable=False,
    )
    sale_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    price_per_unit: Mapped[int] = mapped_column(Integer, nullable=False)  # In cents
    total_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    transaction_fee: Mapped[int] = mapped_column(Integer, nullable=False)  # In cents
    total_realized_pl: Mapped[int] = mapped_column(Integer, nullable=False)  # In cents

    # Relationships
    asset: Mapped["Asset"] = relationship(back_populates="sales")
    wallet: Mapped["Wallet"] = relationship(back_populates="sales")
    lot_allocations: Mapped[list["SaleLotPl"]] = relationship(back_populates="sales")
