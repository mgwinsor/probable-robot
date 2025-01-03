from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Asset(Base):
    __tablename__ = "assets"

    asset_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    symbol: Mapped[str] = mapped_column(String, unique=True)
    name: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)


class Portfolio:
    def __init__(self, db: Session) -> None:
        self.db = db

    def add(self, symbol: str, name: str, type: str) -> Asset:
        db_asset = Asset(symbol=symbol, name=name, type=type)
        self.db.add(db_asset)
        return db_asset
