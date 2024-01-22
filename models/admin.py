from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class Admin(Document):
    fullname: str
    email: EmailStr
    password: str
    is_active: bool = Field(default=True)
    create_at: datetime = datetime.now()

    class collection:
        name = "admin"

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "mempyx",
                "email": "fksfsl@gmail.com",
                "password": "SA88sds",
                "is_active": "true",
                "create_at": datetime.now()
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
                "fullname": "memphyx",
                "email": "fksfsl@gmail.com",
            }
        }
