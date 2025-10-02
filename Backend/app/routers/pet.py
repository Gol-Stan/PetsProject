from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from app import schemas, crud, models
from app.database import get_db
from app.dependencies import get_current_user, get_currnet_user_opt

router = APIRouter()


@router.post("/pets", response_model=schemas.pet.PetPrivate)
async def create_pet(pet_in: schemas.pet.PetBase, db: AsyncSession = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    new_pet = await crud.pet.create_pet(db, pet_in, owner_id=current_user.id)
    return  schemas.pet.PetPrivate.from_orm(new_pet)


@router.get("/pets/qr/{qr_code}", response_model=schemas.pet.PetPublic)
async def get_pet_by_qr(qr_code: str, db: AsyncSession = Depends(get_db), current_user: Optional[models.User] = Depends(get_currnet_user_opt)):
    pet = await crud.pet.get_pet_by_qr(db, qr_code)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    if current_user and pet.owner_id == current_user.id:
        return schemas.pet.PetPrivate.from_orm(pet)

    return schemas.pet.PetPublic.from_orm(pet)

@router.get("/pets/my", response_model=list[schemas.pet.PetPrivate])
async def get_my_pets(db: AsyncSession = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    pets = await crud.pet.get_my_pets(db, owner_id=current_user.id)
    return [schemas.pet.PetPrivate.from_orm(p) for p in pets]