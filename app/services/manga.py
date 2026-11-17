from sqlmodel import Session, select
from fastapi import HTTPException 
from app.schemas.manga import MangaCreate, MangaUpdate
from app.models.manga import MangaModel

def get_all_mangas_service(session: Session):
    return session.exec(select(MangaModel)).all()

def get_mangas_by_genre_service(genre: str, session: Session):
    statement = select(MangaModel).where(MangaModel.genre == genre)
    return session.exec(statement).all()

def search_mangas_service(query: str, session: Session):
    statement = select(MangaModel).where(MangaModel.title.contains(query))
    return session.exec(statement).all()

def get_manga_by_id_service(manga_id: int, session: Session):
    statement = select(MangaModel).where(MangaModel.id == manga_id)
    result = session.exec(statement).first()
    if not result:
        raise HTTPException(status_code=404, detail="Manga not found")
    return result

def get_manga_chapters_service(manga_id: int, session: Session):
    manga = get_manga_by_id_service(manga_id, session)
    return manga.chapters

def get_manga_chapter_service(manga_id: int, chapter_id: int, session: Session):
    manga = get_manga_by_id_service(manga_id, session)
    chapter = next((ch for ch in manga.chapters if ch.id == chapter_id), None)
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return chapter

def add_manga_service(manga_data: MangaCreate, session: Session):
    # Convert Pydantic create schema to database model instance
    db_manga = MangaModel(**manga_data.model_dump())
    session.add(db_manga)
    session.commit()
    session.refresh(db_manga)
    return db_manga

def update_manga_service(manga_id: int, manga_data: MangaUpdate, session: Session):
    existing_manga = get_manga_by_id_service(manga_id, session)
    
    # Update fields from the update schema
    update_data = manga_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(existing_manga, key, value)
    
    session.add(existing_manga)
    session.commit()
    session.refresh(existing_manga)
    return existing_manga

def delete_manga_service(manga_id: int, session: Session):
    manga = get_manga_by_id_service(manga_id, session)
    session.delete(manga)
    session.commit()
    return {"message": "Manga deleted successfully"}