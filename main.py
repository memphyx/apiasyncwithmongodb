from contextlib import asynccontextmanager

from fastapi import FastAPI, Body, APIRouter, HTTPException
from schema import *
from fonction import *
from database import *
from beanie import PydanticObjectId
from bson import ObjectId


router = APIRouter(tags=['Etudiant'], prefix='/etudiant')


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan, title="Student", version="0.0.1")


# Ajoutons un Etudiant dans BD

@app.post("/v1/etudiant", response_description="Votre etudiant a bien été ajouté dans la base de donnée",
          response_model=Response)
async def ajout_etudiant(etudiant: Edutiant = Body(...)):
    new_etudiant = await fc_add_etudiant(etudiant)

    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Operation reussie",
        "data": new_etudiant,
    }


# recuperation de tous les etudiants
@app.get("/v1/etudiants", response_description="Tout les etudiants", response_model=Response)
async def tout_les_etudiants():
    all_etudiants = await fc_all_etudiants()

    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Operation reussie",
        "data": all_etudiants
    }


# recuperons un etudiant

@app.get("/v1/etudiant/{id}", response_description="recuperation d'un etudiant par id", response_model=Response)
async def etudiant_by_id(id: PydanticObjectId):
    etudiant = fc_etudiant_by_id(id)

    if etudiant:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Operation reussie",
            "data": etudiant
        }
    return {
        "status_code": 404,
        "response_type": "success",
        "description": "id ne correspond pas a celui d'un etudiant",

    }
