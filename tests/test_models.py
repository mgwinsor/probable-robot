# from datetime import date
# from decimal import Decimal
#
# import pytest
#
# from app.models import Transaction, TransactionType
#
#
# @pytest.fixture
# def sample_date():
#     return date(2025, 1, 10)
#
#
# @pytest.fixture
# def sample_transaction_data(sample_date):
#     return {
#         "asset_id": 0,
#         "lot_id": 0,
#         "transaction_type": TransactionType.BUY,
#         "quantity": Decimal("2.5"),
#         "price_per_unit": Decimal("400.00"),
#         "fee": Decimal("0.50"),
#         "transaction_date": sample_date,
#     }
#
#
# def test_buy_transaction_init(sample_transaction_data):
#     """
#     Test that a buy transaction correctly initializes with properly calculated
#     cost basis and net proceeds
#     """
#     transaction = Transaction(**sample_transaction_data)
#     expected_cost_basis = (
#         sample_transaction_data["quantity"] * sample_transaction_data["price_per_unit"]
#         + sample_transaction_data["fee"]
#     )
#
#     assert transaction.cost_basis == expected_cost_basis
#     assert transaction.net_proceeds == Decimal(0)
#     assert transaction.remaining_quantity == sample_transaction_data["quantity"]
#
#
# def test_sell_transaction_init(sample_transaction_data):
#     """
#     Test that a sell transaction correctly initializes with properly calculated
#     cost basis and net proceeds
#     """
#
#     sample_transaction_data["transaction_type"] = TransactionType.SELL
#
#     transaction = Transaction(**sample_transaction_data)
#     expected_net_proceeds = (
#         sample_transaction_data["quantity"] * sample_transaction_data["price_per_unit"]
#         - sample_transaction_data["fee"]
#     )
#
#     assert transaction.cost_basis == Decimal(0)
#     assert transaction.net_proceeds == expected_net_proceeds
#     assert transaction.remaining_quantity == sample_transaction_data["quantity"]
