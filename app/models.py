from datetime import date, datetime
from decimal import Decimal
from enum import Enum

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
        ForeignKey("assets.asset_id", ondelete="RESTRICT"),
        index=True,
    )
    lot_id: Mapped[int] = mapped_column(Integer)
    transaction_type: Mapped[TransactionType] = mapped_column(
        SqlEnum(TransactionType),
        nullable=False,
    )
    quantity: Mapped[Decimal] = mapped_column(Numeric(precision=18, scale=8))
    remaining_quantity: Mapped[Decimal] = mapped_column(Numeric(precision=18, scale=8))
    price: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    fee: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
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


class Portfolio:
    def __init__(self, db: Session) -> None:
        self.db = db

    def add(self, symbol: str, name: str, type: str) -> Asset:
        db_asset = Asset(symbol=symbol, name=name, type=type)
        self.db.add(db_asset)
        return db_asset

    def remove(self, symbol: str) -> Asset | None:
        asset = self.db.query(Asset).filter(Asset.symbol == symbol).first()
        if asset:
            self.db.delete(asset)
            self.db.commit()
        return asset
