from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends

from database import init_db

# from auth.jwt_bearer import JWTBearer
# from config.config import initiate_database
# from routes.admin import router as AdminRouter
from routes.etudiant import router as EtudiantRouter

app = FastAPI()


# token_listener = JWTBearer()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan, title="Student", version="0.0.1")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


# app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(EtudiantRouter, tags=["Etudiants"], prefix="/etudiant", )

"""dependencies=[Depends(token_listener)]"""
