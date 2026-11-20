from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from typing import List

from app.schemas.manga import Manga, MangaCreate, MangaUpdate
from app.database import get_session
from app.services.manga import get_all_mangas_service, get_mangas_by_genre_service, search_mangas_service, get_manga_by_id_service, get_manga_chapters_service, get_manga_chapter_service, add_manga_service, update_manga_service, delete_manga_service

router = APIRouter(prefix="/mangas", tags=["Mangas"])

@router.get("/", response_model=List[Manga])
async def get_mangas(session: Session = Depends(get_session)):
    """Retrieve all mangas."""
    return get_all_mangas_service(session)

@router.get("/genre", response_model=List[Manga])
async def get_mangas_by_genre(genre: str, session: Session = Depends(get_session)):
    """Retrieve mangas by genre."""
    return get_mangas_by_genre_service(genre, session)

@router.get("/search", response_model=List[Manga])
async def search_mangas(query: str, session: Session = Depends(get_session)):
    """Search mangas by title."""
    return search_mangas_service(query, session)

@router.get("/{manga_id}", response_model=Manga)
async def get_manga(manga_id: int, session: Session = Depends(get_session)):    
    """Retrieve a specific manga by its ID."""
    return get_manga_by_id_service(manga_id, session)

@router.get("/{manga_id}/chapters")
async def get_manga_chapters(manga_id: int, session: Session = Depends(get_session)):
    """Retrieve chapters of a specific manga by its ID."""
    return get_manga_chapters_service(manga_id, session)

@router.get("/{manga_id}/chapters/{chapter_id}")
async def get_manga_chapter(manga_id: int, chapter_id: int, session: Session = Depends(get_session)):
    """Retrieve a specific chapter of a manga by manga ID and chapter ID."""
    return get_manga_chapter_service(manga_id, chapter_id, session)

@router.post("/add", response_model=Manga, status_code=status.HTTP_201_CREATED)
async def add_manga(manga: MangaCreate, session: Session = Depends(get_session)):
    """Add a new manga to the database."""
    return add_manga_service(manga, session)

@router.put("/update/{manga_id}", response_model=Manga)
async def update_manga(manga_id: int, manga: MangaUpdate, session: Session = Depends(get_session)):
    """Update an existing manga in the database."""
    return update_manga_service(manga_id, manga, session)

@router.delete("/delete/{manga_id}")
async def delete_manga(manga_id: int, session: Session = Depends(get_session)):
    """Delete a manga from the database."""
    return delete_manga_service(manga_id, session)