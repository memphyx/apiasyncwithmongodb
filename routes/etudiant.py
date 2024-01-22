from fastapi import Body, APIRouter, HTTPException
from fonction import *
from database import *
from beanie import PydanticObjectId

router = APIRouter()


# Ajoutons un Etudiant dans BD
@router.post("/v1/etudiant", response_description="Votre etudiant a bien été ajouté dans la base de donnée",
             response_model=Response)
async def ajout_etudiant(etudiant: Etudiant = Body(...)):
    # verification de la taille du nom
    # print(len(etudiant.nom.split()))
    print("post")
    nbre_de_nom = len(etudiant.nom.split())

    if nbre_de_nom > 1:
        raise HTTPException(
            status_code=409, detail="le nom doit contenir un mot"
        )
    # verification de l'existence d'un email
    elif await fc_verif_email(etudiant):
        raise HTTPException(
            status_code=409,
            detail="l'email existe deja , "
        )
    elif await fc_verif_contact(etudiant):
        raise HTTPException(
            status_code=409,
            detail="le contact existe deja"
        )

    else:
        # enregistrement d'un etudiant
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Operation reussie",
            "data": await fc_add_etudiant(etudiant),
        }


# recuperation de tous les etudiants
@router.get("/v1/etudiants", response_description="Tout les etudiants", response_model=Response_all)
async def tout_les_etudiants():
    all_etudiants = await fc_all_etudiants()
    size_data = len(all_etudiants)
    # print(size_data)
    if size_data == 0:
        raise HTTPException(
            status_code=404,
            detail="Vous n'avez aucune donnée actuellement"
        )

    else:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Operation reussie",
            "size": size_data,
            "data": all_etudiants,

        }


# recuperons un etudiant
@router.get("/v1/etudiant/{id}", response_description="recuperation d'un etudiant par id", response_model=Response)
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

@router.put('/v1/etudiant/{id}', response_description="mise à jour d'un etudiant", response_model=Response)
async def update_student(id: PydanticObjectId, req: EdutiantBasemodel = Body(...)):
    updated_student = await fc_maj(id, req.dict())
    if updated_student:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Student with ID: {} updated".format(id),
            "data": updated_student
        }
    else:
        return {
            "status_code": 404,
            "response_type": "error",
            "description": "An error occurred. Student with ID: {} not found".format(id),
            "data": False
        }


# Suppresseions d'un etudiant par l'ID
@router.delete('/v1/etudiant/{id}', response_description="suppression dun etudiant", response_model=Response)
async def del_etudiant(id: PydanticObjectId):
    etudiant_del_by_id = await fc_del_etu(id)
    if not etudiant_del_by_id:
        raise HTTPException(
            status_code=404, detail="id introuvable"
        )
    else:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "l'etudiant avec le ID: {} supprimer".format(id),
            "data": etudiant_del_by_id
        }
