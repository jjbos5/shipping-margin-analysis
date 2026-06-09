"""Test for the ShipWorks SQL extractor."""
from src.extract_shipworks import extract_orders

def test_extract_orders_is_callable():
    """The extract_orders function exists and can be called."""
    assert callable(extract_orders)