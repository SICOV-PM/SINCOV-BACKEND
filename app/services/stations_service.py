import random

def get_mock_stations():
    return [
        {"id": 1, "lat": 4.65, "lng": -74.1, "value": round(random.uniform(0.3, 0.9), 2)},
        {"id": 2, "lat": 4.61, "lng": -74.08, "value": round(random.uniform(0.2, 0.8), 2)},
        {"id": 3, "lat": 4.63, "lng": -74.07, "value": round(random.uniform(0.4, 0.95), 2)},
        {"id": 4, "lat": 4.60, "lng": -74.05, "value": round(random.uniform(0.1, 0.7), 2)},
    ]
