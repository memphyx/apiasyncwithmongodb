from contextlib import asynccontextmanager

from fastapi import FastAPI, Body, APIRouter, HTTPException
from schema import *
from fonction import *
from database import *
from beanie import PydanticObjectId
from bson import ObjectId

router = APIRouter()


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
    print(new_etudiant)
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
async def etudiant_by_id(id):
    etudiant = await fc_etudiant_by_id(id)

    if not etudiant:
        raise HTTPException(
            status_code=404,
            detail="le ID ne correspond pas a celui d'un etudiant",

        )

    else:

        return {

            "status_code": 200,
            "response_type": "success",
            "description": "Operation reussie",
            "data": etudiant
        }


# modifions un etudiant par l'ID

@app.put('/v1/etudiant/{id}', response_description="mise à jour d'un etudiant", response_model=Response)
async def update_student(id: PydanticObjectId, req: EdutiantBasemodel = Body(...)):
    updated_student = await fc_maj(id, req.dict())
    if updated_student:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Student with ID: {} updated".format(id),
            "data": updated_student
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Student with ID: {} not found".format(id),
        "data": False
    }

# Suppresseions d'un etudiant par l'ID