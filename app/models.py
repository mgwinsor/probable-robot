from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Any

from sqlalchemy import Date, DateTime
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import ForeignKey, Integer, Numeric, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class TransactionType(str, Enum):
    BUY = "buy"
    SELL = "sell"


class Asset(Base):
    __tablename__ = "assets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    symbol: Mapped[str] = mapped_column(String, unique=True)
    name: Mapped[str] = mapped_column(String)
    asset_type: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        onupdate=func.now(),
        nullable=True,
    )


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    asset_id: Mapped[int] = mapped_column(
        ForeignKey("assets.id", ondelete="RESTRICT"),
        index=True,
    )
    lot_id: Mapped[int] = mapped_column(Integer)
    transaction_type: Mapped[TransactionType] = mapped_column(
        SqlEnum(TransactionType),
        nullable=False,
    )
    quantity: Mapped[Decimal] = mapped_column(Numeric(precision=18, scale=8))
    remaining_quantity: Mapped[Decimal] = mapped_column(Numeric(precision=18, scale=8))
    price_per_unit: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    fee: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    cost_basis: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    net_proceeds: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    transaction_date: Mapped[date] = mapped_column(Date, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        onupdate=func.now(),
        nullable=True,
    )

    def __init__(self, **kw: Any):
        super().__init__(**kw)
        self.remaining_quantity = self.quantity
        if self.transaction_type == TransactionType.BUY:
            self.cost_basis = (self.quantity * self.price_per_unit) + self.fee
            self.net_proceeds = Decimal(0)
        else:
            self.cost_basis = Decimal(0)
            self.net_proceeds = (self.quantity * self.price_per_unit) - self.fee


class Portfolio:
    def __init__(self, db: Session) -> None:
        self.db = db

    def add(self, symbol: str, name: str, asset_type: str) -> Asset:
        db_asset = Asset(symbol=symbol, name=name, asset_type=asset_type)
        self.db.add(db_asset)
        return db_asset

    def remove(self, symbol: str) -> Asset | None:
        asset = self.db.query(Asset).filter(Asset.symbol == symbol).first()
        if asset:
            self.db.delete(asset)
            self.db.commit()
        return asset

    def list_asset(self, symbol: str) -> Asset | None:
        asset = self.db.query(Asset).filter(Asset.symbol == symbol).first()
        return asset

    def list_all_assets(self):
        assets = self.db.query(Asset).all()
        return assets

    def transaction_add(self) -> Transaction:
        db_transaction = Transaction()
        return db_transaction
