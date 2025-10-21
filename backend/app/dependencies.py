from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from watchfiles import awatch

from app import schemas
from app.crud import user as crud_user
from app.database import AsyncSessionLocal, get_db
from app.utils.jwt_handler import create_access_token, decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")



""" Token check"""
async def get_current_user(token: str = Depends(oauth2_scheme), db:AsyncSession = Depends(get_db)):
    try:
        payload = decode_token(token)
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )

    user = await crud_user.get_user_by_email(db, email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,detail="User not found"
        )

    return user


async def get_current_user_opt( token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    try:
        payload = decode_token(token)
        email: str = payload.get("sub")
        if not email:
            return None
    except JWTError:
        return None

    return await crud_user.get_user_by_email(db, email)