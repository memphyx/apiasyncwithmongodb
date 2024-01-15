from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr


class Admin(Document):
    fullname: str
    email: EmailStr
    password: str

    class collection:
        name = "admin"

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "mempyx",
                "email": "fksfsl@gmail.com",
                "password": "SA88sds"
            }
        }


class AdminSignin(HTTPBasicCredentials):
    class Config:
        json_schema_extra = {
            "example": {

                "username": "fksfsl@gmail.com",
                "password": "SA88sds"

            }
        }


class AdminData(BaseModel):
    fullname: str
    email: EmailStr

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "mempyx",
                "email": "fksfsl@gmail.com",
            }
        }
