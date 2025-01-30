from decimal import Decimal

from sqlalchemy.orm import Session

from app.models import PortfolioManager
from app.views import PortfolioView


class AssetController:
    def __init__(self, db: Session) -> None:
        self.portfolio = PortfolioManager(db)
        self.view = PortfolioView()

    def add_asset(
        self,
        symbol: str,
        name: str,
        decimal_places: int,
        current_price: Decimal | None,
    ) -> None:
        asset = self.portfolio.add(symbol, name, decimal_places, current_price)
        self.view.show_asset_added(symbol, asset)

    def remove_asset(self, symbol: str) -> None:
        asset = self.portfolio.remove(symbol)
        self.view.show_asset_removed(asset, symbol)

    def list_asset(self, symbol: str) -> None:
        asset = self.portfolio.list_asset(symbol)
        self.view.show_asset_listed(asset, symbol)

    def list_all_assets(self) -> None:
        assets = self.portfolio.list_all_assets()
        self.view.show_all_assets(assets)

    def update_asset(self, symbol: str, new_price: Decimal):
        asset = self.portfolio.update_asset(symbol, new_price)
        self.view.show_updated_asset(asset, symbol)

    def add_transaction(
        self,
        symbol: str,
        acquisition_date: str,
        quantity: float,
        cost_per_unit: float,
        transaction_fee: float,
    ) -> None:
        transaction = self.portfolio.purchase_lot_add(
            symbol,
            acquisition_date,
            quantity,
            cost_per_unit,
            transaction_fee,
        )
        self.view.show_transaction_added(transaction)
