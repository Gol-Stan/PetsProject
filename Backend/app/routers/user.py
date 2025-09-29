from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError

from app.database import AsyncSessionLocal
from app.utils.jwt_handler import create_access_token, decode_token
from app import schemas
from app.crud import user as crud_user

router = APIRouter(prefix="/auth", tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_db():
    async with AsyncSession() as db:
        yield db

""" Register """
@router.post("/register", response_model=schemas.user.UserRead, status_code=status.HTTP_201_CREATED)
async def register(user_in: schemas.user.UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await  crud_user.get_user_by_email(db, user_in.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return await crud_user.create_user(db, user_in)

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user = await crud_user.auth_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credantial",
            headers={"WWW-Auth": "Bearer"},
        )

    access_token = create_access_token(subject=user.email)
    return {"access_token": {access_token}, "token_type": "bearer"}


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

@router.get('/me', response_model=schemas.user.UserRead)
async def read_users_me(current_user=Depends(get_current_user)):
    return current_user