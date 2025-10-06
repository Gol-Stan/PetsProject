from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, crud
from app.database import get_db

router = APIRouter(prefix="/breeds", tags=["breeds"])


@router.post("/", response_model=schemas.breed.BreedList, status_code=status.HTTP_201_CREATED)
async def create_breed(breed_in: schemas.breed.BreedCreate, db: AsyncSession = Depends(get_db)):
    return await crud.breed.create_breed(db, breed_in)


@router.get("/", response_model=list[schemas.breed.BreedList])
async def list_breeds(db: AsyncSession = Depends(get_db)):
    breeds = await crud.breed.get_all_breeds(db)
    return [schemas.breed.BreedList.from_orm(b) for b in breeds]


@router.put("/{breed_id}", response_model=schemas.breed.BreedList)
async def update_breed(breed_id: int, breed_in: schemas.breed.Breed, db: AsyncSession = Depends(get_db)):
    breed = await crud.breed.update_breed(db, breed_id, breed_in)
    if not breed:
        raise HTTPException(status_code=404, detail="Breed not found")
    return breed


@router.delete("/{breed_id}")
async def delete_breed(breed_id: int, db: AsyncSession = Depends(get_db)):
    breed = await crud.breed.delete_breed(db, breed_id)
    if not breed:
        raise HTTPException(status_code=404, detail="Breed not found")
    return {"message": f"Breed with id {breed_id} deleted"}
