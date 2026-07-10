def simulations():
    print ("this is a test")

def net_bleed(df):
    shipping_calc = (df["shipping_charged"] - df["shipping_cost"]).sum() 
    return 
