from src.pipeline import run_analysis

def test_pipeline():
    result = run_analysis("data/sample_orders.csv")
    assert result == -118

def test_run_analysis():
    result = run_analysis("data/sample_orders.csv", 2024, 2025)
    assert result == -98