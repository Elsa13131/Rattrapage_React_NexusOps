
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.equipment_routes import router as equipment_router
from routes.incident_routes import router as incident_router
from routes.user_routes import router as user_router
from database import Base, engine 
import database_models
app = FastAPI(
    title="NexusOps API",
    description="API de supervision des équipements et incidents",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)
app.include_router(equipment_router)
app.include_router(incident_router)
app.include_router(user_router)

@app.get("/")
def accueil():
    return {"message": "Bienvenue sur l'API NexusOps"}
