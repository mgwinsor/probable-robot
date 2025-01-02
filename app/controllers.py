from models import Portfolio
from views import PortfolioView


class AssetController:
    def __init__(self) -> None:
        self.portfolio = Portfolio()
        self.view = PortfolioView()

    def add_asset(self, name: str) -> None:
        asset = self.portfolio.add(name)
        self.view.show_asset_added(asset)
