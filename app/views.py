from rich.console import Console
from rich.table import Table
from sqlalchemy import inspect

from app.models import Asset


class PortfolioView:
    def __init__(self) -> None:
        self.console = Console()

    def show_asset_added(self, symbol: str, asset: Asset | None) -> None:
        if asset:
            self.console.print(f"Added {asset.name} to your asset list!")
        else:
            self.console.print(f"{symbol} already added!")

    # def show_asset_removed(self, asset: Asset | None, symbol: str) -> None:
    #     if asset:
    #         self.console.print(f"Removed {asset.name} from your asset list!")
    #     else:
    #         self.console.print(f"No asset found with symbol {symbol}.")

    def show_asset_listed(self, asset: Asset | None, symbol: str) -> None:
        if asset:
            table = Table(title=f"Asset Details for {asset.symbol}")

            inspector = inspect(Asset)
            columns = inspector.columns.keys()

            for col in columns:
                table.add_column(col.replace("_", " ").title())

            table.add_row(
                *(
                    str(getattr(asset, col)) if getattr(asset, col) is not None else "-"
                    for col in columns
                )
            )

            self.console.print(table)
        else:
            self.console.print(f"No asset found with symbol {symbol}.")

    def show_all_assets(self, assets: list[Asset]) -> None:
        table = Table(title="Details for All Assets")

        inspector = inspect(Asset)
        columns = inspector.columns.keys()

        for col in columns:
            table.add_column(col.replace("_", " ").title())

        for asset in assets:
            table.add_row(
                *(
                    str(getattr(asset, col)) if getattr(asset, col) is not None else "-"
                    for col in columns
                )
            )
        self.console.print(table)

    #
    # def show_transaction_added(self, transaction: Transaction) -> None:
    #     self.console.print(f"Added {transaction.lot_id} to your transactions list!")
