from decimal import ROUND_HALF_UP, Decimal

from sqlalchemy.orm import Session

from app.models import Asset


class PortfolioManager:
    def __init__(self, db: Session) -> None:
        self.db = db

    def add(
        self,
        symbol: str,
        name: str,
        decimal_places: int,
        current_price: Decimal | None,
    ) -> Asset | None:
        # Convert current_price from USD to pennies
        current_price_int: int | None = None
        if current_price is not None:
            current_price_int = self._convert_price_decimal_to_int(current_price)

        db_asset = Asset(
            symbol=symbol,
            name=name,
            decimal_places=decimal_places,
            current_unit_price=current_price_int,
        )
        check_exists = self.db.query(Asset).filter(Asset.symbol == symbol).first()
        if check_exists is None:
            self.db.add(db_asset)
            return db_asset
        return None

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

    def update_asset(self, symbol: str, price: Decimal) -> Asset | None:
        new_price = self._convert_price_decimal_to_int(price)

        asset = self.db.query(Asset).filter(Asset.symbol == symbol).first()
        print(f"Here :{asset}")
        if asset:
            asset.current_unit_price = new_price
            self.db.commit()
            return asset
        return None

    def _convert_price_decimal_to_int(self, price: Decimal) -> int:
        return int(price.quantize(Decimal("0.01"), ROUND_HALF_UP) * 100)

    # def transaction_add(
    #     self,
    #     symbol,
    #     lot_id,
    #     transaction_type,
    #     quantity,
    #     price_per_unit,
    #     fee,
    #     transaction_date,
    # ) -> Transaction:
    #     asset = self.list_asset(symbol)
    #     if asset is None:
    #         raise ValueError(f"{symbol} not found in asset list.")
    #
    #     db_transaction = Transaction(
    #         asset_id=asset.id,
    #         lot_id=lot_id,
    #         transaction_type=transaction_type,
    #         quantity=quantity,
    #         price_per_unit=price_per_unit,
    #         fee=fee,
    #         transaction_date=transaction_date,
    #     )
    #     self.db.add(db_transaction)
    #     return db_transaction
