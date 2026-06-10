"""Test for the ShipWorks SQL extractor."""
import pandas as pd
from src.extract_shipworks import extract_orders

def test_extract_orders_is_callable():
    """The extract_orders function exists and can be called."""
    assert callable(extract_orders)

def test_extract_orders_returns_dataframe():
    """extract_orders should return a pandas DataFrame"""
    result = extract_orders()
    assert isinstance(result, pd.DataFrame)