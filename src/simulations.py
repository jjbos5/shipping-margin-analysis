import pandas as pd

def simulations():
    print ("this is a test")

def net_bleed(df):
    shipping_calc = (df["shipping_charged"] - df["shipping_cost"]).sum() 
    return shipping_calc

def free_shipping(df):
    free = df[df["shipping_charged"] ==0]
    shipping_calc = (free["shipping_charged"] - free["shipping_cost"]).sum()
    return shipping_calc

def paid_shipping(df):
    paid = df[df["shipping_charged"] >0]
    shipping_calc = (paid["shipping_charged"] - paid["shipping_cost"]).sum()
    return shipping_calc

def bleed_by_year(df):
    df['OrderDate'] = pd.to_datetime(df['OrderDate'], format ='ISO8601').dt.year
    df["bleed_calc"] = (df["shipping_charged"] - df["shipping_cost"])
    bleed_calc_years = df["bleed_calc"].groupby(df['OrderDate']).sum()
    return bleed_calc_years