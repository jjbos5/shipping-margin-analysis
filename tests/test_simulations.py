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

def test_when_shipping_was_paid():
    test3 = pd.DataFrame({"shipping_charged": [24.00, 0.00, 36.00, 123.00], 
        "shipping_cost": [24.00, 45.00, 36.00, 123.00]})
    result = sim.paid_shipping(test3)
    assert result == 0

def test_bleed_by_year():
    test4 = pd.DataFrame({"OrderDate": ["2023-05-01", "2024-06-15", 
        "2025-03-20", "2026-02-10 12:00:00.777000", "2024-07-27"],
        "shipping_charged": [24.00, 0.00, 36.00, 123.00, 23.00], 
        "shipping_cost": [24.00, 45.00, 36.00, 123.00, 60.00]})
    result = sim.bleed_by_year(test4)
    assert result[2024] == -82