from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from passlib.context import CryptContext

from models.admin import *

security = HTTPBasic()
hash_helper = CryptContext(schemes=["bcrypt"])


async def validate_login(credentials: HTTPBasicCredentials = Depends(security)):
    admin = Admin.find_one({"email": credentials.username})
    if admin:
        password = hash_helper.verify(credentials.password, admin['password'])
        if not password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password"
            )
        return True
    return False
