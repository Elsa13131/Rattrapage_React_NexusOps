
from fastapi import FastAPI
from routes.equipment_routes import router as equipment_router
app = FastAPI(
    title="NexusOps API",
    description="API de supervision des équipements et incidents",
    version="1.0.0"
)
app.include_router(equipment_router)

@app.get("/")
def accueil():
    return {"message": "Bienvenue sur l'API NexusOps"}
