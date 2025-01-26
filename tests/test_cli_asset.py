from typer.testing import CliRunner

from app.database import get_db_session
from app.main import app
from app.models import Asset

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

    with get_db_session() as db:
        asset = db.query(Asset).filter(Asset.symbol == "BTC").first()
        assert asset is not None
        assert asset.current_unit_price == 3013


def test_asset_list_one():
    _ = runner.invoke(app, ["asset", "add", "BTC", "Bitcoin", "18", "--price", "3000"])
    result = runner.invoke(app, ["asset", "list", "BTC"])
    assert result.exit_code == 0
    assert "BTC" in result.stdout


def test_asset_list_all():
    _ = runner.invoke(app, ["asset", "add", "BTC", "Bitcoin", "18", "--price", "3000"])
    _ = runner.invoke(app, ["asset", "add", "ETH", "Ethereum", "18", "--price", "1300"])
    result = runner.invoke(app, ["asset", "list"])
    assert result.exit_code == 0
    assert "BTC" in result.stdout
    assert "ETH" in result.stdout


def test_asset_remove():
    _ = runner.invoke(app, ["asset", "add", "BTC", "Bitcoin", "18", "--price", "3000"])
    result = runner.invoke(app, ["asset", "remove", "BTC"])
    assert result.exit_code == 0
    assert "Removed Bitcoin from your asset list!" in result.stdout


def test_missing_asset_remove():
    result = runner.invoke(app, ["asset", "remove", "BTC"])
    assert result.exit_code == 0
    assert "No asset found with symbol BTC" in result.stdout


def test_asset_update():
    _ = runner.invoke(app, ["asset", "add", "BTC", "Bitcoin", "18", "--price", "3000"])
    result = runner.invoke(app, ["asset", "update", "BTC", "--price", "4000"])
    assert result.exit_code == 0
    assert "4000" in result.stdout


def test_asset_update_missing_symbol():
    result = runner.invoke(app, ["asset", "update", "BTC", "--price", "4000"])
    assert result.exit_code == 0
    assert "No asset found with symbol BTC." in result.stdout
