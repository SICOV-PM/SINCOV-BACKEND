from fastapi import APIRouter
from app.services.reports_service import get_mock_reports

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/")
def reports(days: int = 7):
    return {"reports": get_mock_reports(days)}
