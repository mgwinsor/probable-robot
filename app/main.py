import typer

import app.cli.asset as cli_asset
import app.cli.transaction as cli_transaction

app = typer.Typer()
app.add_typer(cli_asset.app, name="asset")
app.add_typer(cli_transaction.app, name="transaction")

if __name__ == "__main__":
    app()
