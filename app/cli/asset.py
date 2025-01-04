import typer

from app.controllers import AssetController
from app.database import get_db_session

app = typer.Typer()


@app.command()
def add(symbol: str, name: str, type: str) -> None:
    with get_db_session() as db:
        controller = AssetController(db)
        controller.add_asset(symbol, name, type)


@app.command()
def remove(symbol: str) -> None:
    print(f"deleted {symbol}")


if __name__ == "__main__":
    app()
