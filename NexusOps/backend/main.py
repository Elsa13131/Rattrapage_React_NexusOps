
from fastapi import FastAPI

app = FastAPI(
    title="NexusOps API",
    description="API de supervision des équipements et incidents",
    version="1.0.0"
)

@app.get("/")
def accueil():
    return {"message": "Bienvenue sur l'API NexusOps"}
