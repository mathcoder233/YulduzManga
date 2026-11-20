from sqlmodel import SQLModel, Field
from app.helper import create_id

class MangaModel(SQLModel, table=True):
    __tablename__ = "mangas"

    id: int = Field(default_factory=create_id, primary_key=True)
    title: str
    author: str
    description: str
    chapters: int