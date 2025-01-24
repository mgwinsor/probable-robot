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

    # def remove_asset(self, symbol: str) -> None:
    #     asset = self.portfolio.remove(symbol)
    #     self.view.show_asset_removed(asset, symbol)
    #
    # def list_asset(self, symbol: str) -> None:
    #     asset = self.portfolio.list_asset(symbol)
    #     self.view.show_asset_listed(asset, symbol)
    #
    # def list_all_assets(self) -> None:
    #     assets = self.portfolio.list_all_assets()
    #     self.view.show_all_assets(assets)

    # def add_transaction(
    #     self,
    #     symbol: str,
    #     lot_id: int,
    #     transaction_type: TransactionType,
    #     quantity: Decimal,
    #     price_per_unit: Decimal,
    #     fee: Decimal,
    #     transaction_date: date,
    # ) -> None:
    #     transaction = self.portfolio.transaction_add(
    #         symbol,
    #         lot_id,
    #         transaction_type,
    #         quantity,
    #         price_per_unit,
    #         fee,
    #         transaction_date,
    #     )
    #     self.view.show_transaction_added(transaction)
