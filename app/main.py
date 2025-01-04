import typer

import app.cli.asset as cli_asset


def main():
    app = typer.Typer()
    app.add_typer(cli_asset.app, name="asset")
    app()


if __name__ == "__main__":
    main()
