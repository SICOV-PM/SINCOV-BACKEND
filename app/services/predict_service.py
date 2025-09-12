import random

def mock_predict(features: list[float]) -> float:
    return round(random.uniform(0.2, 0.9), 2)
