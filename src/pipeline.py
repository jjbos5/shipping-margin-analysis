from src.read_data import read_orders, standardize_columns
from src.simulations import net_bleed

def run_analysis(path):
    orders = read_orders(path)
    standardize_orders = standardize_columns(orders)
    return net_bleed(standardize_orders)