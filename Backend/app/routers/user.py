from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas, models, crud
from app.crud import user as crud_user
from app.database import AsyncSessionLocal
from app.utils.jwt_handler import create_access_token, decode_token
from app.dependencies import get_db, get_current_user, get_current_user_opt

router = APIRouter(tags=["auth"])


""" Register """
@router.post("/register", response_model=schemas.user.UserRead, status_code=status.HTTP_201_CREATED)
async def register(user_in: schemas.user.UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await  crud_user.get_user_by_email(db, str(user_in.email))
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return await crud_user.create_user(db, user_in)

""" Login """
@router.post("/login", response_model=schemas.user.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user = await crud_user.auth_user(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(subject=user.email)
    return {"access_token": access_token, "token_type": "bearer"}



"""User data"""
@router.get('/me', response_model=schemas.user.UserRead)
async def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user


""" Update user """
@router.put("/me", response_model=schemas.user.UserRead)
async def update_user_me(user_update: schemas.user.UserUpdate, db: AsyncSession = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    try:
        updated_user = await crud.user.update_user(db, current_user.id, user_update)
        return updated_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))