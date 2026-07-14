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
