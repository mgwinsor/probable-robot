from decimal import Decimal, InvalidOperation

import typer
from typing_extensions import Annotated

from app.controllers import AssetController
from app.database import get_db_session

app = typer.Typer()


@app.command()
def add(
    symbol: str,
    name: str,
    decimals: int,
    price: Annotated[
        str | None, typer.Option(help="Current asset price in USD")
    ] = None,
) -> None:
    price_decimal: Decimal | None = None
    if price is not None:
        try:
            price_str = price.strip().replace("$", "").replace(",", "")
            price_decimal = Decimal(price_str)
        except (ValueError, InvalidOperation):
            typer.echo(f"Invalid price format: {price}.")
            raise typer.Exit(1)

    with get_db_session() as db:
        controller = AssetController(db)
        if price_decimal is not None:
            controller.add_asset(symbol, name, decimals, price_decimal)
        else:
            controller.add_asset(symbol, name, decimals, None)


@app.command()
def remove(symbol: str) -> None:
    with get_db_session() as db:
        controller = AssetController(db)
        controller.remove_asset(symbol)


@app.command()
def list(symbol: Annotated[str, typer.Argument(help="Asset symbol")] = "all") -> None:
    with get_db_session() as db:
        controller = AssetController(db)
        if symbol == "all":
            controller.list_all_assets()
        else:
            controller.list_asset(symbol)


if __name__ == "__main__":
    app()
