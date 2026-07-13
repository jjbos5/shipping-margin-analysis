import src.simulations as sim
import pandas as pd

def test_simulation_is_callable():
    assert callable(sim.simulations)

def test_where_we_stand_with_shipping():
    test1 = pd.DataFrame({"shipping_charged": [12.0, 16.50, 6.00],
        "shipping_cost":[15.00, 22.00, 5.00] })
    result = sim.net_bleed(test1)
    assert result == -7.5

def test_when_shipping_was_free():
    test2 = pd.DataFrame({"shipping_charged": [12.00, 0, 0, 0],
        "shipping_cost": [15.00, 24.00, 10.00, 36.00]  })
    result = sim.free_shipping(test2)
    assert result == -70