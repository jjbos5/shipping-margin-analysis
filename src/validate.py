def count_missing_costs(df):
    missing = df[df["shipping_cost"] ==0]
    missing_counts = len(missing)
    return missing_counts