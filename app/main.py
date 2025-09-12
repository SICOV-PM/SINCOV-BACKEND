from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes_predict, routes_reports, routes_stations

app = FastAPI(title="SINCOV-PM API", version="0.1")

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permitir todas las orígenes
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rutas
app.include_router(routes_predict.router)
app.include_router(routes_reports.router)
app.include_router(routes_stations.router)
