from datetime import date
from decimal import Decimal

from sqlalchemy.orm import Session

from app.models import Portfolio, TransactionType
from app.views import PortfolioView


class AssetController:
    def __init__(self, db: Session) -> None:
        self.portfolio = Portfolio(db)
        self.view = PortfolioView()

    def add_asset(self, symbol: str, name: str, asset_type: str) -> None:
        asset = self.portfolio.add(symbol, name, asset_type)
        self.view.show_asset_added(asset)

    def remove_asset(self, symbol: str) -> None:
        asset = self.portfolio.remove(symbol)
        self.view.show_asset_removed(asset, symbol)

    def list_asset(self, symbol: str) -> None:
        asset = self.portfolio.list_asset(symbol)
        self.view.show_asset_listed(asset, symbol)

    def list_all_assets(self) -> None:
        assets = self.portfolio.list_all_assets()
        self.view.show_all_assets(assets)

    def add_transaction(
        self,
        symbol: str,
        lot_id: int,
        transaction_type: TransactionType,
        quantity: Decimal,
        price_per_unit: Decimal,
        fee: Decimal,
        transaction_date: date,
    ) -> None:
        asset = self.portfolio.list_asset(symbol)
