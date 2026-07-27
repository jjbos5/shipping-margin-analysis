import pandas as pd
import src.read_data as rd


def test_read_data():
    result = rd.read_orders("data/sample_orders.csv")
    assert len(result) == 5

def test_column_names():
    test1 = pd.DataFrame({"ShipCharged": [7.00, 15.00, 0.00, 5.00],
        "ShipCost": [7.00, 15.00, 10.00, 5.00]})
    result = rd.standardize_columns(test1)
    assert "shipping_charged" in result.columns