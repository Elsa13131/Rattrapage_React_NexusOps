
from fastapi import FastAPI
from routes.equipment_routes import router as equipment_router
from routes.incident_routes import router as incident_router
from routes.user_routes import router as user_router
app = FastAPI(
    title="NexusOps API",
    description="API de supervision des équipements et incidents",
    version="1.0.0"
)
app.include_router(equipment_router)
app.include_router(incident_router)
app.include_router(user_router)

@app.get("/")
def accueil():
    return {"message": "Bienvenue sur l'API NexusOps"}

