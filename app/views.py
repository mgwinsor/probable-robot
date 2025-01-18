from rich.console import Console

from app.models import Asset, Transaction


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

    def show_asset_listed(self, asset: Asset | None, symbol: str) -> None:
        if asset:
            output = f"{asset.symbol}\t{asset.name}\t{asset.asset_type}"
            self.console.print(output)
        else:
            self.console.print(f"No asset found with symbol {symbol}.")

    def show_all_assets(self, assets: list[Asset]) -> None:
        for asset in assets:
            output = f"{asset.symbol}\t{asset.name}\t{asset.asset_type}"
            self.console.print(output)

    def show_transaction_added(self, transaction: Transaction) -> None:
        self.console.print(f"Added {transaction.lot_id} to your transactions list!")
