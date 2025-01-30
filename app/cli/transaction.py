from datetime import datetime
from decimal import Decimal

import typer

from app.controllers import AssetController
from app.database import get_db_session

app = typer.Typer()


@app.command()
def add(
    symbol: str,
    acquisition_date: str,
    quantity: float,
    cost_per_unit: float,
    transaction_fee: float,
) -> None:
    quantity_f = Decimal(str(quantity))
    price_per_unit_f = Decimal(str(cost_per_unit))
    fee_f = Decimal(str(transaction_fee))
    date_d = datetime.strptime(acquisition_date, "%Y-%m-%d").date()

    with get_db_session() as db:
        controller = AssetController(db)
        controller.add_transaction(
            symbol,
            acquisition_date,
            quantity_f,
            price_per_unit_f,
            fee_f,
        )
