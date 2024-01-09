from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, field_validator
from enum import Enum
from beanie import Document, PydanticObjectId, Indexed
from typing import Optional, Any
from bson import ObjectId


class ProfessionEnum(str, Enum):
    ETUDIANT = 'ETUDIANT'
    FONCTIONNAIRE = 'FONCTIONNAIRE'
    ELEVE = "ELEVE"
    STAGIAIRE = 'STAGIAIRE'
    AUTRE = 'AUTRE'


class TypePersonneEnum(str, Enum):
    ENFANT = "ENFANT"
    JEUNE = "JEUNE"
    ADULTE = "ADULTE"
    INCONNU = "INCONNU"


class Edutiant(Document):
    nom: str
    prenom: str
    age: int = Field(default=0, ge=0)
    contact: str = Field(default=" ", max_length=10)
    lieu_de_naissance: str
    email: EmailStr = Field(unique=True)
    region: str = Field(default="Agneby")
    profession: Optional[ProfessionEnum] = Field(default=ProfessionEnum.AUTRE)
    is_active: bool = Field(default=True)
    date_created: datetime = datetime.now()
    type_personne: Optional[TypePersonneEnum] = Field(default=TypePersonneEnum.INCONNU)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Définir le champ type_personne en fonction de l'âge lors de la création
        self.type_personne = self.calculate_type_personne()

    def calculate_type_personne(self):
        if self.age is not None:
            if self.age < 18:
                return TypePersonneEnum.ENFANT
            elif 18 <= self.age < 25:
                return TypePersonneEnum.JEUNE
            else:
                return TypePersonneEnum.ADULTE
        return TypePersonneEnum.INCONNU

    class Config:
        allow_population_by_field_name = True
        json_schema_extra = {
            "example": {
                "nom": "Agnéro",
                "prenom": "Moîse",
                "contact": "0757311618",
                "age": "34",
                "lieu_de_naissance": "Dabou",
                "email": "qdvqdc@gmail.com",
                "region": "lagunes",
                'profession': 'STAGIAIRE',
                'is_active': "True",
                "date_created": datetime.now()
            }
        }

    class Settings:
        name = "Edutiant"


class EdutiantBasemodel(BaseModel):
    nom: Optional[str]
    prenom: Optional[str]
    age: Optional[int]
    contact: str = Field(Indexed(str, unique=True))
    lieu_de_naissance: Optional[str]
    email: Optional[EmailStr]
    region: Optional[str] = Field(default="Agneby")
    profession: Optional[ProfessionEnum] = Field(default=ProfessionEnum.AUTRE)
    is_active: bool = Field(default=True)


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
