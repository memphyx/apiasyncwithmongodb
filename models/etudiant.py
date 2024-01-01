from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, field_validator
from enum import Enum
from beanie import Document, PydanticObjectId
from typing import Optional, Any
from bson import ObjectId


class ProfessionEnum(str, Enum):
    ETUDIANT = 'ETUDIANT'
    FONCTIONNAIRE = 'FONCTIONNAIRE'
    ELEVE = "ELEVE"
    STAGIAIRE = 'STAGIAIRE'
    AUTRE = 'AUTRE'


class Edutiant(Document):
    nom: str
    prenom: str
    age: int = Field(default=0, ge=0)
    lieu_de_naissance: str
    email: EmailStr = Field(unique=True)
    region: str = Field(default="Agneby")
    profession: Optional[ProfessionEnum] = Field(default=ProfessionEnum.AUTRE)
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
                'profession': 'STAGIAIRE',
                "date_created": datetime.now()
            }
        }

    class Settings:
        name = "Edutiant"


class EdutiantBasemodel(BaseModel):
    nom: Optional[str]
    prenom: Optional[str]
    age: Optional[int]
    lieu_de_naissance: Optional[str]
    email: Optional[EmailStr]
    region: Optional[str] = Field(default="Agneby")
    profession: Optional[ProfessionEnum] = Field(default=ProfessionEnum.AUTRE)


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        json_schema_extra = {

            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation réussie",
                "data": "Sample data",
            }
        }


class Response_all(BaseModel):
    status_code: int
    response_type: str
    description: str
    size: int
    data: Optional[Any]

    class Config:
        json_schema_extra = {

            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation réussie",
                "size": "value",
                "data": "Sample data"
            }
        }
