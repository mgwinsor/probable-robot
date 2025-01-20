from typing import TYPE_CHECKING, Optional

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base

if TYPE_CHECKING:
    from app.models import IncomeEvent, PurchaseLot, SalesPl, WalletTransfer


class Wallet(Base):
    __tablename__ = "wallets"

    wallet_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    address: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String)

    purchase_lots_current: Mapped[list["PurchaseLot"]] = relationship(
        back_populates="current_wallet",
        foreign_keys="[PurchaseLot.current_wallet_id]",
    )
    purchase_lots_original: Mapped[list["PurchaseLot"]] = relationship(
        back_populates="original_wallet",
        foreign_keys="[PurchaseLot.original_wallet_id]",
    )
    income_events: Mapped[list["IncomeEvent"]] = relationship(back_populates="wallet")
    sales: Mapped[list["SalesPl"]] = relationship(back_populates="wallet")
    outgoint_transfers: Mapped["WalletTransfer"] = relationship(
        back_populates="from_wallet",
        foreign_keys="[WalletTransfer.from_wallet_id]",
    )
    incoming_transfer: Mapped["WalletTransfer"] = relationship(
        back_populates="to_wallet",
        foreign_keys="[WalletTransfer.to_wallet_id]",
    )
