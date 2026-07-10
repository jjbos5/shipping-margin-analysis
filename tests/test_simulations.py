import src.simulations as sim
import pandas as pd

def test_simulation_is_callable():
    assert callable(sim.simulations)

def test_where_we_stand_with_shipping():
    test1 = pd.DataFrame({"shipping_charged": [12.0, 16.50, 6.00],
        "shipping_cost":[15.00, 22.00, 5.00] })
    result = sim.net_bleed(test1)
    assert result == result
