from rich.console import Console

from app.models import Asset


class PortfolioView:
    def __init__(self) -> None:
        self.console = Console()

    def show_asset_added(self, asset: Asset) -> None:
        self.console.print(f"Added {asset.name} to your asset list!")

    def show_asset_removed(self, asset: Asset | None, symbol: str) -> None:
        if asset:
            self.console.print(f"Removed {asset.name} from your asset list!")
        else:
            self.console.print(f"No asset found with symbol {symbol}.")
