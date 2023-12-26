from typing import List, Union
from schema import *


# methode de verification de la presence d'un email
async def fc_verif_email(etudiant: Edutiant):
    check_email = await Edutiant.find_one(Edutiant.email == etudiant.email)

    if check_email:
        return check_email


# methode d'ajout d'un objet
async def fc_add_etudiant(new_etudiant_add: Edutiant) -> Edutiant:
    etudiant = await new_etudiant_add.create()
    return etudiant


# methode d'obtention des etudiant
async def fc_all_etudiants() -> List[Edutiant]:
    etudiants = await Edutiant.all().to_list()
    return etudiants


# methode d'obtention d'un etudiant par iD
async def fc_etudiant_by_id(id: PydanticObjectId) -> Edutiant:
    etudiant = await Edutiant.get(id)

    if etudiant:
        return etudiant


# methode de mise à jour d'un objet par ID
async def fc_maj(id: PydanticObjectId, data: dict) -> Union[bool, Edutiant]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in des_body.items()
    }}
    student = await Edutiant.get(id)
    if student:
        await student.update(update_query)
        return student
    return False


# Methode de la suppression d'un objet par id

async def fc_del_etu(id: PydanticObjectId) -> Edutiant:
    del_etu = await Edutiant.get(id)
    if del_etu:
        await del_etu.delete()
        return del_etu
