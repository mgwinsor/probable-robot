import cli.asset
import typer

app = typer.Typer()
app.add_typer(cli.asset.app, name="asset")


@app.command()
def list() -> None:
    print("listing assets...")


if __name__ == "__main__":
    app()
