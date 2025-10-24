from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, crud
from app.database import get_db
from app.dependencies import get_current_admin

router = APIRouter(tags=["breed"])


@router.post("/", response_model=schemas.breed.BreedList, status_code=status.HTTP_201_CREATED)
async def create_breed(breed_in: schemas.breed.BreedCreate, db: AsyncSession = Depends(get_db), admin_user = Depends(get_current_admin)):
    try:
        breed = await  crud.breed.create_breed(db, breed_in)
        return breed
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))


@router.get("/", response_model=list[schemas.breed.BreedList])
async def list_breeds(db: AsyncSession = Depends(get_db)):
    breeds = await crud.breed.get_all_breeds(db)
    return breeds


@router.put("/{breed_id}", response_model=schemas.breed.BreedList)
async def update_breed(breed_id: int, breed_in: schemas.breed.BreedUpdate, db: AsyncSession = Depends(get_db), admin_user = Depends(get_current_admin)):
    try:
        breed = await crud.breed.update_breed(db, breed_id, breed_in)
        if not breed:
            raise HTTPException(status_code=404, detail="Breed not found")
        return breed
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))



@router.delete("/{breed_id}")
async def delete_breed(breed_id: int, db: AsyncSession = Depends(get_db), admin_user = Depends(get_current_admin)):
    try:
        breed = await crud.breed.delete_breed(db, breed_id)
        if not breed:
            raise HTTPException(status_code=404, detail="Breed not found")
        return {"message": f"Breed with id {breed_id} deleted"}
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))