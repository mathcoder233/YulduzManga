from fastapi import FastAPI
from app.routers.manga import router as manga_router
from app.database import create_db_and_tables
from fastapi.middleware.cors import CORSMiddleware
create_db_and_tables()
app = FastAPI(title="Manga API", description="API for managing mangas and their chapters.", version="1.0.0")
app.include_router(manga_router)
@app.get("/")
async def root():
    return {"message": "Welcome to the Manga API!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://yulduzmanga-frontend-nu.vercel.app"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)