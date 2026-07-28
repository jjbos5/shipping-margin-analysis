from src.pipeline import run_analysis

def test_pipeline():
    result = run_analysis("data/sample_orders.csv")
    assert result == -118
