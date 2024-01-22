from typing import List, Union
from models.etudiant import *
from models.admin import *


# methode d'ajout dun admin

async def add_admin(new_admin: Admin) -> Admin:
    admin = await new_admin.create()
    return admin


# methode de verification de la presence d'un email
async def fc_verif_email(etudiant: Etudiant):
    check_email = await Etudiant.find_one(Etudiant.email == etudiant.email)

    if check_email:
        return check_email


# methode de verification de la presence d'un contact       
async def fc_verif_contact(etudiant: Etudiant):
    check_contact = await Etudiant.find_one(Etudiant.contact == etudiant.contact)

    if check_contact:
        return check_contact


# methode de verification de la taille du nom

"""async def fc_len_name(etudiant: Edutiant):
    taille_nom = await Edutiant.find(len(etudiant.nom))"""


# methode d'ajout d'un objet
async def fc_add_etudiant(new_etudiant_add: Etudiant) -> Etudiant:
    etudiant = await new_etudiant_add.create()
    return etudiant


# methode d'obtention des etudiant
async def fc_all_etudiants() -> List[Etudiant]:
    etudiants = await Etudiant.all().to_list()
    return etudiants


# methode d'obtention d'un etudiant par iD
async def fc_etudiant_by_id(id: PydanticObjectId) -> Etudiant:
    etudiant = await Etudiant.get(id)

    if etudiant:
        return etudiant


# methode de mise à jour d'un objet par ID
async def fc_maj(id: PydanticObjectId, data: dict) -> Union[bool, Etudiant]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in des_body.items()
    }}
    student = await Etudiant.get(id)
    if student:
        await student.update(update_query)
        return student
    return False


# Methode de la suppression d'un objet par id

async def fc_del_etu(id: PydanticObjectId) -> Etudiant:
    del_etu = await Etudiant.get(id)
    if del_etu:
        await del_etu.delete()
        return del_etu
