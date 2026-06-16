"""Test for the ShipWorks SQL extractor."""
import pandas as pd
from src.extract_shipworks import extract_orders
from unittest.mock import MagicMock
 
def test_extract_orders_is_callable():
    """The extract_orders function exists and can be called."""
    assert callable(extract_orders)

def test_extract_orders_returns_dataframe():
    """extract_orders should return a pandas DataFrame"""
    result = extract_orders()
    assert isinstance(result, pd.DataFrame)

def test_extract_orders_returns_expected_columns():
    """extract_orders should return a DataFrame with the bake-off columns."""
    result = extract_orders()
    expected_columns = ['order_id', 'order_date', 'shipping_cost', 'order_total']
    assert list(result.columns) == expected_columns 

def test_extract_orders_accepts_connection_argument():
    """extract_orders should accept a database connection"""
    result = extract_orders(None)
    assert isinstance(result, pd.DataFrame)

def test_extract_orders_accepts_date_range():
    """extract_orders should accept date range"""
    result = extract_orders(conn=None, start_date='2024-01-01', end_date='2024-12-31')
    assert isinstance(result, pd.DataFrame)

def test_extract_orders_queries_the_connection():
    """should give us fake data"""
    fake_data = [(23, '2024-01-04', 86.00, 100.94)]
    conn = MagicMock()
    conn.cursor.return_value.fetchall.return_value = fake_data
    result = extract_orders(conn)
    assert len(result) == 1