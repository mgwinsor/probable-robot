import typer

import app.cli.asset as cli_asset

app = typer.Typer()
app.add_typer(cli_asset.app, name="asset")

if __name__ == "__main__":
    app()
