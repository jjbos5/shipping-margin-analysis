import src.load_warehouse as lwh 
import pandas as pd 
import sqlite3
def test_load_warehouse_is_callable():
    assert callable(lwh.load_orders)

def test_load_orders_writes_in_database():
    df = pd.DataFrame({"order_id": [1, 2]})
    conn = sqlite3.connect(":memory:") 
    lwh.load_orders(df, conn )
    result = pd.read_sql("SELECT * FROM orders", conn)
    assert len(result) == 2

    