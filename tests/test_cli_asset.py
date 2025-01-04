from typer.testing import CliRunner

from app.cli.asset import app

runner = CliRunner()


def test_asset_add():
    result = runner.invoke(app, ["add", "BTC", "Bitcoin", "crytpo"])
    assert result.exit_code == 0
    assert "Added Bitcoin to your asset list!" in result.stdout
