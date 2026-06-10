import pandas as pd 

def extract_orders(conn=None):
    return pd.DataFrame(columns=['order_id', 'order_date', 'shipping_cost', 'order_total'])


