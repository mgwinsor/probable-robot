from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base

if TYPE_CHECKING:
    from app.models import Asset, PurchaseLot, Wallet


class WalletTransfer(Base):
    __tablename__ = "wallet_transfers"

    transfer_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    asset_id: Mapped[int] = mapped_column(ForeignKey("assets.asset_id"), nullable=False)
    from_wallet_id: Mapped[int] = mapped_column(
        ForeignKey("wallets.wallet_id"),
        nullable=False,
    )
    to_wallet_id: Mapped[int] = mapped_column(
        ForeignKey("wallets.wallet_id"),
        nullable=False,
    )
    transfer_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)  # In base units
    transfer_fee: Mapped[int] = mapped_column(Integer, nullable=False)  # In cents
    lot_id: Mapped[int] = mapped_column(
        ForeignKey("purchase_lots.lot_id"),
        nullable=False,
    )

    # Relationships
    asset: Mapped["Asset"] = relationship(back_populates="transfers")
    from_wallet: Mapped["Wallet"] = relationship(
        back_populates="outgoing_transfers",
        foreign_keys=[from_wallet_id],
    )
    to_wallet: Mapped["Wallet"] = relationship(
        back_populates="incoming_transfers",
        foreign_keys=[to_wallet_id],
    )
    lot: Mapped["PurchaseLot"] = relationship(back_populates="transfers")
