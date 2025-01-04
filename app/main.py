import typer

import app.cli.asset as cli_asset

app = typer.Typer()
app.add_typer(cli_asset.app, name="asset")


@app.command()
def list() -> None:
    print("listing assets...")


if __name__ == "__main__":
    app()
