from models import Portfolio
from sqlalchemy.orm import Session
from views import PortfolioView


class AssetController:
    def __init__(self, db: Session) -> None:
        self.portfolio = Portfolio(db)
        self.view = PortfolioView()

    def add_asset(self, symbol: str, name: str, type: str) -> None:
        asset = self.portfolio.add(symbol, name, type)
        self.view.show_asset_added(asset)
