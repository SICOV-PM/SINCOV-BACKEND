from fastapi import APIRouter
from app.services.stations_service import get_mock_stations

router = APIRouter(prefix="/stations", tags=["Stations"])

@router.get("/")
def stations():
    return {"stations": get_mock_stations()}
