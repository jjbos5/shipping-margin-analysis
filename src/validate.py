def count_missing_costs(df):
    missing = df[df["shipping_cost"] ==0]
    missing_counts = len(missing)
    return missing_counts 

def negative_shipping_costs(df):
    negative = df[df["shipping_cost"] <0]
    negative_shipping = len(negative)
    return negative_shipping

def count_missing_shipping_cost(df):
    missing = df[df["shipping_cost"].isnull()]
    missing_cost = len(missing)
    return missing_cost
