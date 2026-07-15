import pandas as pd
import src.validate as val

def test_counts_missing_cost():
    missing = pd.DataFrame({ "shipping_charged": [45.00, 0.00, 12.00, 0.00], 
        "shipping_cost": [45.00, 0.00, 12.00, 0.00]})
    result = val.count_missing_costs(missing)
    assert result == 2
