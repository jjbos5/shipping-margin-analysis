import pandas as pd 

def extract_orders(conn=None, start_date=None, end_date=None):
    if conn is None:
        return pd.DataFrame(columns=['order_id', 'order_date', 'shipping_cost', 'order_total'])
    else:
        cursor = conn.cursor()
        cursor.execute("SELECT order_id, order_date, shipping_cost, order_total FROM orders")
        rows = cursor.fetchall() 
        return pd.DataFrame(rows, columns=['order_id', 'order_date', 'shipping_cost', 'order_total'])


