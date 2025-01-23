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
    price: Annotated[int | None, typer.Option(help="Current asset price")] = None,
) -> None:
    with get_db_session() as db:
        controller = AssetController(db)
        controller.add_asset(symbol, name, decimals, price)


# @app.command()
# def remove(symbol: str) -> None:
#     with get_db_session() as db:
#         controller = AssetController(db)
#         controller.remove_asset(symbol)
#
#
# @app.command()
# def list(symbol: Annotated[str, typer.Argument(help="Asset symbol")] = "all") -> None:
#     with get_db_session() as db:
#         controller = AssetController(db)
#         if symbol == "all":
#             controller.list_all_assets()
#         else:
#             controller.list_asset(symbol)


if __name__ == "__main__":
    app()
