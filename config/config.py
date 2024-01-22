from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings

from models.admin import Admin
from models.etudiant import Etudiant


class Settings(BaseSettings):
    # databse configurations
    DATABASE_URL: Optional[str] = None

    "jwt"
    secret_key: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    algorithm: str = "HS256"

    class Config:
        env_file = ".env.dev"
        from_attributes = True


"""async def initiate_database():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(database=client.get_default_database(),
                      document_models=[Admin, Etudiant])"""
