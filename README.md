# SINCOV – Backend

API backend para consultar **estaciones**, **reportes** y **predicciones** de calidad del aire (p. ej., PM2.5).  
Está construido con **Python** y **FastAPI** (arquitectura por capas: `api` → `services` → `schemas`), con pruebas en `pytest` y soporte listo para **Docker**.

---

## 🚧 Estado
Estable para desarrollo local. Revisa la licencia en `LICENSE`.

---

## 🗂️ Estructura del proyecto

SINCOV-BACKEND/
├─ app/
│ ├─ api/
│ │ ├─ routes_predict.py
│ │ ├─ routes_reports.py
│ │ └─ routes_stations.py
│ ├─ schemas/
│ │ └─ predict_schema.py
│ ├─ services/
│ │ ├─ predict_service.py
│ │ ├─ reports_service.py
│ │ └─ stations_service.py
│ └─ main.py
├─ tests/
│ └─ test_api.py
├─ .gitignore
├─ Dockerfile
├─ LICENSE
├─ README.md
├─ requirements.txt
└─ requirements-freeze.txt

yaml
Copy code

- **`app/main.py`**: punto de entrada; define la app FastAPI y monta las rutas.
- **`app/api/*`**: controladores (endpoints HTTP).
- **`app/services/*`**: lógica de negocio / acceso a datos.
- **`app/schemas/*`**: modelos Pydantic para validación/serialización.
- **`tests/`**: pruebas `pytest`.

---

## ⚙️ Requisitos

- Python **3.10+**
- `pip` y `venv` (o conda/poetry si prefieres)
- (Opcional) Docker 24+

---

## 🚀 Configuración y ejecución local

```bash
# 1) Clonar
git clone <URL_DEL_REPO>.git
cd SINCOV-BACKEND

# 2) Crear y activar entorno
python -m venv .venv
# Windows:
. .venv/Scripts/activate
# Linux/macOS:
source .venv/bin/activate

# 3) Instalar dependencias
pip install -r requirements.txt
# (Opcional) uso reproducible:
# pip install -r requirements-freeze.txt

# 4) Ejecutar en desarrollo
uvicorn app.main:app --reload --port 8000
Documentación interactiva: http://localhost:8000/docs

Esquema OpenAPI: http://localhost:8000/openapi.json

Si necesitas variables de entorno (.env), añádelas y cárgalas en main.py/servicios según corresponda.

🐳 Ejecutar con Docker
bash
Copy code
# Construir
docker build -t sincov-backend .

# Correr (puerto 8000)
docker run --rm -p 8000:8000 sincov-backend
Asegúrate de que el CMD del Dockerfile ejecute uvicorn app.main:app --host 0.0.0.0 --port 8000.

🔌 Endpoints (referencia rápida)
Las rutas exactas pueden variar según cómo estén montadas en main.py. Por convención se usa el prefijo /api.

Estaciones
GET /api/stations → Lista de estaciones.

GET /api/stations/{station_id} → Detalle de estación.

Reportes
GET /api/reports → Reportes disponibles (filtros opcionales por fecha/estación).

GET /api/reports/{report_id} → Detalle de reporte.

Predicción
POST /api/predict → Recibe un payload (ver predict_schema.py) y retorna predicción.

Ejemplos curl:

bash
Copy code
# Estaciones
curl -s http://localhost:8000/api/stations

# Reportes (ejemplo con query params)
curl -s "http://localhost:8000/api/reports?station=KENNEDY&date=2025-04-01"

# Predicción (ajusta el JSON a tu schema real)
curl -s -X POST http://localhost:8000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"station":"KENNEDY","datetime":"2025-04-01T08:00:00","features":{"temp":18.2,"wind":2.1,"humidity":62}}'
✅ Tests
bash
Copy code
# Ejecutar todas las pruebas
pytest -q

# Ver cobertura (si está configurada)
pytest --maxfail=1 --disable-warnings -q --cov=app
🧱 Decisiones de diseño
FastAPI + Pydantic para tipado y validación.

Capa de servicios para aislar la lógica de negocio del layer HTTP.

Schemas para contratos claros de entrada/salida.

Tests que validan el contrato de la API y casos principales.

📦 Despliegue (sugerido)
Producción con uvicorn/gunicorn detrás de un reverse proxy (Nginx).

Variables de entorno para credenciales, orígenes CORS y config del modelo/datos.

Healthcheck en /health (agregar si no existe).
