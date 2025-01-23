# from datetime import datetime
# from typing import TYPE_CHECKING
#
# from sqlalchemy import DateTime, ForeignKey, Integer
# from sqlalchemy.orm import Mapped, mapped_column, relationship
#
# from app.models.base import Base
#
# if TYPE_CHECKING:
#     from app.models import AcquisitionType, Asset, PurchaseLot, Wallet
#
#
# class IncomeEvent(Base):
#     __tablename__ = "income_events"
#
#     event_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
#     asset_id: Mapped[int] = mapped_column(ForeignKey("assets.asset_id"), nullable=False)
#     wallet_id: Mapped[int] = mapped_column(
#         ForeignKey("wallets.wallet_id"),
#         nullable=False,
#     )
#     acquisition_type_id: Mapped[int] = mapped_column(
#         ForeignKey("acquisition_types.type_id"),
#         nullable=False,
#     )
#     date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
#     quantity: Mapped[int] = mapped_column(Integer, nullable=False)  # In base units
#     fmv_per_unit: Mapped[int] = mapped_column(Integer, nullable=False)  # In cents
#
#     # Relationships
#     asset: Mapped["Asset"] = relationship(back_populates="income_events")
#     wallet: Mapped["Wallet"] = relationship(back_populates="income_events")
#     acquisition_type: Mapped["AcquisitionType"] = relationship(
#         back_populates="income_events"
#     )
#     purchase_lots: Mapped["PurchaseLot"] = relationship(back_populates="income_events")
