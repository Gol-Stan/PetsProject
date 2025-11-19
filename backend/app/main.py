from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app import database
from app.routers import user, pet, breed, email
from app.database import engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost"
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://frontend:3000",
        "http://localhost:80",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/auth")
app.include_router(pet.router, prefix="/pets")
app.include_router(breed.router, prefix="/breeds")
app.include_router(email.router, prefix="/email")


app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
async def root():
    return {"message": "FastAPI работает! Перейдите на /docs для документации"}


@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(database.Base.metadata.create_all)


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "PetWorld API"}