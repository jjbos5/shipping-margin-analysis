def load_orders(df, conn):
    df.to_sql("orders", conn, index=False)