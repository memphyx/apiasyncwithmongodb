from datetime import datetime

from pydantic import BaseModel, EmailStr, Field
from beanie import Document, PydanticObjectId
from typing import Optional, Any
from bson import ObjectId


class Edutiant(Document):
    nom: str
    prenom: str
    age: int
    lieu_de_naissance: str
    email: EmailStr
    region: str = Field(default="Agneby")
    date_created: datetime = datetime.now()


class Config:
    json_schema_extra = {
        "example": {
            "nom": "Agnéro",
            "prenom": "Moîse",
            "age": "34",
            "lieu_de_naissance": "Dabou",
            "email": "qdvqdc@gmail.com",
            "region": "lagunes",
            "date_created": datetime.now()
        }
    }


class Settings:
    name = "edutiant"


class EdutiantBasemodel(BaseModel):
    nom: Optional[str]
    prenom: Optional[str]
    age: Optional[int]
    lieu_de_naissance: Optional[str]
    email: Optional[EmailStr]
    region: Optional[str] = Field(default="Agneby")


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    size: Optional[Any]
    data: Optional[Any]


    class Config:
        json_schema_extra = {

            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation réussie",
                "data": "Sample data",
                "size": ""
            }
        }
