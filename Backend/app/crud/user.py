from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app import models, schemas
from passlib.context import CryptContext

pwd_content = CryptContext(schemes=["bcrypt"], deprecated ="auto")

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(models.User).filter(models.User.email == email))
    return result.scalars().first()

async def create_user(db: AsyncSession, user_in: schemas.user.UserCreate):
    hashed_pw = pwd_content.hash(user_in.password)
    db_user = models.User(
        name=user_in.name,
        email=user_in.email,
        phone=user_in.phone,
        hashed_password = hashed_pw
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_content.verify(plain_password, hashed_password)

async def auth_user(db: AsyncSession, email: str, password: str):
    user = await get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
