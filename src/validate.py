def count_missing_costs(df):
    missing = df[df["shipping_cost"] == 0]
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

def zero_cost_impact(df):
    zero = df[df["shipping_cost"] == 0]
    zero_cost = (zero["shipping_charged"] - zero["shipping_cost"]).sum()
    return zero_cost

def data_quality_report(df):
    quality_report = {"zero_cost": count_missing_costs(df),
                      "negative_cost": negative_shipping_costs(df),
                      "missing_cost": count_missing_shipping_cost(df),
                      "zero_cost_impact": zero_cost_impact(df)}
    return quality_report
