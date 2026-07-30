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

def test_filtered_by_year_data():
    dates = pd.DataFrame({"OrderDate": ["2023-05-01", "2024-06-15", 
        "2025-03-20", "2026-02-10"]})
    result = rd.filter_year(dates, 2024, 2025)
    assert len(result) == 2 