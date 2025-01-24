from typer.testing import CliRunner

from app.main import app

runner = CliRunner()


def test_asset_add():
    result = runner.invoke(
        app, ["asset", "add", "BTC", "Bitcoin", "18", "--price", "3000"]
    )
    assert result.exit_code == 0
    assert "Added Bitcoin to your asset list!" in result.stdout


def test_asset_add_no_current_price():
    result = runner.invoke(app, ["asset", "add", "BTC", "Bitcoin", "18"])
    assert result.exit_code == 0
    assert "Added Bitcoin to your asset list!" in result.stdout


def test_asset_unique_add():
    _ = runner.invoke(app, ["asset", "add", "BTC", "Bitcoin", "18", "--price", "3000"])
    result = runner.invoke(
        app, ["asset", "add", "BTC", "Bitcoin", "18", "--price", "3000"]
    )
    assert result.exit_code == 0
    assert "BTC already added!" in result.stdout


def test_asset_add_decimal():
    result = runner.invoke(
        app, ["asset", "add", "BTC", "Bitcoin", "18", "--price", "30.125"]
    )
    assert result.exit_code == 0
    assert "Added Bitcoin to your asset list!" in result.stdout
    # TODO: query database to check rounded values


# def test_asset_remove():
#     _ = runner.invoke(app, ["asset", "add", "BTC", "Bitcoin", "crypto"])
#     result = runner.invoke(app, ["asset", "remove", "BTC"])
#     assert result.exit_code == 0
#     assert "Removed Bitcoin from your asset list!" in result.stdout
#
#
# def test_missing_asset_remove():
#     result = runner.invoke(app, ["asset", "remove", "BTC"])
#     assert result.exit_code == 0
#     assert "No asset found with symbol BTC" in result.stdout
