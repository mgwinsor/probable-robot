from datetime import date, datetime
from decimal import Decimal

import pytest

from app.models import Transaction, TransactionType


@pytest.fixture
def sample_timestamp():
    return datetime(2025, 1, 10, 12, 0, 0)


def test_buy_transaction_initialization():
    """
    Test that a buy transaction correctly initializes with properly calculated
    cost basis and net proceeds
    """
    transaction_data = {
        "asset_id": 0,
        "lot_id": 0,
        "transaction_type": TransactionType.BUY,
        "quantity": Decimal("2.5"),
        "price_per_unit": Decimal("400.00"),
        "fee": Decimal("0.50"),
        "transaction_date": date(2025, 1, 10),
    }

    transaction = Transaction(**transaction_data)
    expected_cost_basis = (
        transaction_data["quantity"] * transaction_data["price_per_unit"]
        + transaction_data["fee"]
    )

    assert transaction.cost_basis == expected_cost_basis
    assert transaction.net_proceeds == Decimal(0)
    assert transaction.remaining_quantity == transaction_data["quantity"]
