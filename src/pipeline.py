from src.read_data import read_orders, standardize_columns, filter_year
from src.simulations import net_bleed

def run_analysis(path, start_year=None, end_year=None):
    orders = read_orders(path)
    standardize_orders = standardize_columns(orders)
    if start_year and end_year:
        standardize_orders = filter_year(standardize_orders, start_year, end_year)
    return net_bleed(standardize_orders)