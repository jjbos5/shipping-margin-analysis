import pandas as pd

def read_orders(path):
    return pd.read_csv(path)

def standardize_columns(df):
    return df.rename(columns={"ShipCharged": "shipping_charged", "ShipCost": "shipping_cost"})

def filter_year(df, start_year, end_year):
    df["OrderDate"] = pd.to_datetime(df["OrderDate"], format='ISO8601')
    filter = df[(df["OrderDate"].dt.year >= start_year) & (df["OrderDate"].dt.year <= end_year)]
    return filter