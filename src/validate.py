def count_missing_costs(df):
    missing = df[df["shipping_cost"] ==0]
    missing_counts = len(missing)
    return missing_counts 

def negative_shipping_costs(df):
    negative = df[df["shipping_cost"] <0]
    negative_shipping = len(negative)
    return negative_shipping
