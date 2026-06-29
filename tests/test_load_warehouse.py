import src.load_warehouse as lwh 
import pandas as pd 
import sqlite3
def test_load_warehouse_is_callable():
    assert callable(lwh.load_orders)

def test_load_orders_accepts_a_dataframe():
    df = pd.DataFrame()
    lwh.load_orders(df)

def test_load_orders_accepts_a_database():
    df = pd.DataFrame()
    conn = sqlite3.connect(":memory:")
    lwh.load_orders(df, conn )

    