import typer
from controllers import AssetController

app = typer.Typer()
conroller = AssetController()


@app.command()
def add(name: str) -> None:
    """Add a new asset"""
    conroller.add_asset(name)


@app.command()
def list() -> None:
    print("listing assets...")


if __name__ == "__main__":
    app()
