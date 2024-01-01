from  fastapi import HTTPException , Depends, status
from fastapi.security import HTTPBasicCredentials,HTTPBasic
from passlib.context import CryptContext

from database.database import admin_collection
