from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas
from app.crud import user as crud_user
from app.database import AsyncSessionLocal
from app.utils.jwt_handler import create_access_token, decode_token

router = APIRouter(prefix="/auth", tags=["auth"])


""" Register """
@router.post("/register", response_model=schemas.user.UserRead, status_code=status.HTTP_201_CREATED)
async def register(user_in: schemas.user.UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await  crud_user.get_user_by_email(db, str(user_in.email))
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return await crud_user.create_user(db, user_in)

""" Login """
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user = await crud_user.auth_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credential",
            headers={"WWW-Auth": "Bearer"},
        )

    access_token = create_access_token(subject=user.email)
    return {"access_token": access_token, "token_type": "bearer"}



"""User data"""
@router.get('/me', response_model=schemas.user.UserRead)
async def read_users_me(current_user: schemas.user.UserRead = Depends(get_current_user)):
    return current_user