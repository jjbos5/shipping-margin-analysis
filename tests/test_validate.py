import pandas as pd
import src.validate as val

def test_counts_missing_cost():
    missing = pd.DataFrame({ "shipping_charged": [45.00, 0.00, 12.00, 0.00], 
        "shipping_cost": [45.00, 0.00, 12.00, 0.00]})
    result = val.count_missing_costs(missing)
    assert result == 2

def test_negative_shipping_cost():
    negative = pd.DataFrame({ "shipping_charged": [12.00, 0.00, 15.00, 8.00],
        "shipping_cost": [12.00, -5.00, 15.00, 8.00]})
    result = val.negative_shipping_costs(negative)
    assert result == 1 
