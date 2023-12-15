from typing import List, Union
from beanie import PydanticObjectId
from schema import *
from bson.objectid import ObjectId


async def fc_add_etudiant(new_etudiant_add: Edutiant) -> Edutiant:
    etudiant = await new_etudiant_add.create()
    return etudiant


async def fc_all_etudiants() -> List[Edutiant]:
    etudiants = await Edutiant.all().to_list()
    return etudiants


async def fc_etudiant_by_id(id: PydanticObjectId) -> Edutiant:
    etudiant = await Edutiant.get(id)

    if etudiant:
        return etudiant
