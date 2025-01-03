from models import Asset
from rich.console import Console


class PortfolioView:
    def __init__(self) -> None:
        self.console = Console()

    def show_asset_added(self, asset: Asset) -> None:
        self.console.print(f"Added {asset.name} to your asset list!")
