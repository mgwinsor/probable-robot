from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base
from app.models.purchase_lot import PurchaseLot

if TYPE_CHECKING:
    from app.models import SalesPl


class SaleLotPl(Base):
    __tablename__ = "sale_lot_pl"

    allocation_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    sale_id: Mapped[int] = mapped_column(ForeignKey("sales_pl.sale_id"), nullable=False)
    lot_id: Mapped[int] = mapped_column(
        ForeignKey("purchase_lots.lot_id"),
        nullable=False,
    )
    quantity_sold: Mapped[int] = mapped_column(Integer, nullable=False)  # In base units
    allocated_purchase_fee: Mapped[int] = mapped_column(Integer, nullable=False)
    allocated_sale_fee: Mapped[int] = mapped_column(Integer, nullable=False)  # In cents
    realized_pl: Mapped[int] = mapped_column(Integer, nullable=False)  # In cents

    # Relationships
    sale: Mapped["SalesPl"] = relationship(back_populates="lot_allocations")
    purchase_lot: Mapped["PurchaseLot"] = relationship(
        back_populates="sale_allocations"
    )

    # Check constraint to ensure lots and sales are from the same current wallet
    __table_args__ = (
        CheckConstraint(
            """
            (SELECT wallet_id FROM sales_pl WHERE sale_id = sale_lot_pl.sale_id) =
            (SELECT current_wallet_id FROM purchase_lots WHERE lot_id = sale_lot_pl.lot_id)
            """,
            name="same_wallet",
        ),
    )
