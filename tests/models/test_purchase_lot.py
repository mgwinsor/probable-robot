# from datetime import datetime
# from unittest.mock import Mock
#
# from app.models import PurchaseLot
#
#
# def test_purchase_lot_init():
#     """
#     Test that a buy transaction correctly initializes with a properly
#     calculated cost basis and remaining_quantity
#     """
#     mock_asset = Mock()
#     mock_asset.decimal_places = 8
#     mock_asset.id = 0
#
#     test_data = {
#         "asset": mock_asset,
#         "current_wallet_id": 1,
#         "original_wallet_id": 1,
#         "acquisition_type_id": 0,
#         "acquisition_date": datetime(2025, 1, 21),
#         "quantity_base_units": 100000000,  # 1.00000000 in standard units
#         "cost_per_unit": 20_00,  # USD 20.00 in pennies
#         "transaction_fee": 1_50,  # USD 1.50 in pennies
#     }
#     purchase_lot = PurchaseLot(**test_data)
#
#     assert purchase_lot.remaining_quantity == test_data["quantity_base_units"]
#
#     # 1.00000000 * $20.00 + $1.50 = $21.50 = 2150 cents
#     assert purchase_lot.cost_basis == 2150
