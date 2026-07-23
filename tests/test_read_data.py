import pandas as pd
import src.read_data as rd


def test_read_data():
    result = rd.read_orders("data/sample_orders.csv")
    assert len(result) == 5