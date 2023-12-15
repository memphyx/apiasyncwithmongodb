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
