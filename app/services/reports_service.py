from datetime import datetime, timedelta
import random

def get_mock_reports(days: int):
    today = datetime.today()
    reports = []
    for i in range(days):
        date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
        avg = round(random.uniform(0.2, 0.9), 2)
        status = (
            "Muy Alto" if avg >= 0.8 else
            "Alto" if avg >= 0.6 else
            "Moderado" if avg >= 0.4 else
            "Bueno"
        )
        reports.append({"date": date, "avg": avg, "status": status})
    return reports[::-1]
