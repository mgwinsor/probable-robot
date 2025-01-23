# from datetime import datetime
# from decimal import Decimal
# from typing import TYPE_CHECKING, Any, Optional
#
# from sqlalchemy import DateTime, ForeignKey, Integer
# from sqlalchemy.orm import Mapped, mapped_column, relationship
#
# from app.models.base import Base
#
# if TYPE_CHECKING:
#     from app.models import AcquisitionType, Asset, IncomeEvent, SaleLotPl
#
#
# class PurchaseLot(Base):
#     __tablename__ = "purchase_lots"
#
#     lot_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     asset_id: Mapped[int] = mapped_column(ForeignKey("assets.asset_id"), nullable=False)
#     current_wallet_id: Mapped[int] = mapped_column(
#         ForeignKey("wallets.wallet_id"),
#         nullable=False,
#     )
#     original_wallet_id: Mapped[int] = mapped_column(
#         ForeignKey("wallets.wallet_id"),
#         nullable=False,
#     )
#     acquisition_type_id: Mapped[int] = mapped_column(
#         ForeignKey("acquisition_types.type_id"),
#         nullable=False,
#     )
#     acquisition_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
#     quantity_base_units: Mapped[int] = mapped_column(Integer, nullable=False)
#     cost_per_unit: Mapped[int] = mapped_column(Integer, nullable=False)  # In cents
#     transaction_fee: Mapped[int] = mapped_column(Integer, nullable=False)  # In cents
#     cost_basis: Mapped[int] = mapped_column(Integer, nullable=False)
#     remaining_quantity: Mapped[int] = mapped_column(  # In base units
#         Integer,
#         nullable=False,
#         default=None,
#     )
#     income_event_id: Mapped[int] = mapped_column(ForeignKey("income_events.event_id"))
#
#     # Relationships
#     asset: Mapped["Asset"] = relationship(back_populates="purchase_lots")
#     income_events: Mapped[Optional["IncomeEvent"]] = relationship(
#         back_populates="purchase_lots"
#     )
#     acquisition_type: Mapped["AcquisitionType"] = relationship(
#         back_populates="purchase_lots"
#     )
#     sale_allocations: Mapped[list["SaleLotPl"]] = relationship(
#         back_populates="purchase_lots",
#     )
#     # transfers: Mapped[list["Wallet"]] = relationship(
#     #     back_populates="lot",
#     #     foreign_keys=[],
#     # )
#
#     def __init__(self, **kw: Any):
#         super().__init__(**kw)
#         if self.remaining_quantity is None:
#             self.remaining_quantity = self.quantity_base_units
#         self._get_cost_basis()
#
#     def _get_cost_basis(self):
#         standard_quantity = Decimal(self.quantity_base_units) / Decimal(
#             10**self.asset.decimal_places
#         )
#         cost_per_unit_dollars = Decimal(self.cost_per_unit) / Decimal(100)
#         fee_dollars = Decimal(self.transaction_fee) / Decimal(100)
#         total_cost_dollars = (standard_quantity * cost_per_unit_dollars) + fee_dollars
#         self.cost_basis = int(total_cost_dollars * 100)
