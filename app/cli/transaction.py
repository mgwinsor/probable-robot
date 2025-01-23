# from datetime import datetime
# from decimal import Decimal

import typer

# from app.controllers import AssetController
# from app.database import get_db_session

app = typer.Typer()


# @app.command()
# def add(
#     symbol: str,
#     lot_id: int,
#     transaction_type: TransactionType,
#     quantity: float,
#     price_per_unit: float,
#     fee: float,
#     transaction_date: str,
# ) -> None:
#     quantity_f = Decimal(str(quantity))
#     price_per_unit_f = Decimal(str(price_per_unit))
#     fee_f = Decimal(str(fee))
#     date_d = datetime.strptime(transaction_date, "%Y-%m-%d").date()
#
#     with get_db_session() as db:
#         controller = AssetController(db)
#         controller.add_transaction(
#             symbol,
#             lot_id,
#             transaction_type,
#             quantity_f,
#             price_per_unit_f,
#             fee_f,
#             date_d,
#         )
