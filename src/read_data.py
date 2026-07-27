import pandas as pd

def read_orders(path):
    return pd.read_csv(path)

def standardize_columns(df):
    return df.rename(columns={"ShipCharged": "shipping_charged", "ShipCost": "shipping_cost"})
    