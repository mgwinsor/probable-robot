from datetime import datetime
from typing import TYPE_CHECKING, Any, Optional

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base

if TYPE_CHECKING:
    from app.models import Asset, IncomeEvent, SaleLotPl, Wallet


class PurchaseLot(Base):
    __tablename__ = "purchase_lots"

    lot_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    asset_id: Mapped[int] = mapped_column(ForeignKey("assets.asset_id"), nullable=False)
    current_wallet_id: Mapped[int] = mapped_column(
        ForeignKey("wallets.wallet_id"),
        nullable=False,
    )
    original_wallet_id: Mapped[int] = mapped_column(
        ForeignKey("wallets.wallet_id"),
        nullable=False,
    )
    acquisition_type_id: Mapped[int] = mapped_column(
        ForeignKey("aquisition_types.type_id"),
        nullable=False,
    )
    acquisition_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)  # In base units
    cost_per_unit: Mapped[int] = mapped_column(Integer, nullable=False)  # In cents
    transaction_fees: Mapped[int] = mapped_column(Integer, nullable=False)  # In cents
    remaining_quantity: Mapped[int] = mapped_column(  # In base units
        Integer,
        nullable=False,
        default=None,
    )
    income_event_id: Mapped[int] = mapped_column(ForeignKey("income_events.event_id"))

    # Relationships
    asset: Mapped["Asset"] = relationship(back_populates="purchase_lots")
    income_events: Mapped[Optional["IncomeEvent"]] = relationship(
        back_populates="purchase_lots"
    )
    sale_allocations: Mapped[list["SaleLotPl"]] = relationship(
        back_populates="purchase_lots"
    )
    transfers: Mapped[list["Wallet"]] = relationship(back_populates="lot")

    def __init__(self, **kw: Any):
        super().__init__(**kw)
        if self.remaining_quantity is None:
            self.remaining_quantity = self.quantity
