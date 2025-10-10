from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, Union
from app import schemas, crud, models
from app.database import get_db
from app.dependencies import get_current_user, get_current_user_opt

router = APIRouter(tags=["Pets"])


@router.post("/", response_model=schemas.pet.PetPrivate)
async def create_pet(pet_in: schemas.pet.PetPrivate, db: AsyncSession = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    new_pet = await crud.pet.create_pet(db, pet_in, owner_id=current_user.id)
    return  schemas.pet.PetPrivate.from_orm(new_pet)


@router.get("/qr/{qr_code}", response_model=Union[schemas.pet.PetPublic, schemas.pet.PetPrivate])
async def get_pet_by_qr(qr_code: str, db: AsyncSession = Depends(get_db), current_user: Optional[models.User] = Depends(get_current_user_opt)):
    pet = await crud.pet.get_pet_by_qr(db, qr_code)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    if current_user and pet.owner_id == current_user.id:
        return schemas.pet.PetPrivate.from_orm(pet)

    return schemas.pet.PetPublic.from_orm(pet)

@router.get("/my", response_model=list[schemas.pet.PetPrivate])
async def get_my_pets(db: AsyncSession = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    pets = await crud.pet.get_my_pets(db, owner_id=current_user.id)
    return [schemas.pet.PetPrivate.from_orm(p) for p in pets]


@router.delete("/pets/{pet_id}")
async def delete_pet(pet_id: int, db: AsyncSession = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    pet = await crud.pet.delete_pet(db, pet_id, owner_id=current_user.id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found or not yours")
    return {"message": f"Pet with id {pet_id} has been deleted"}