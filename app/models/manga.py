from sqlmodel import SQLModel, Field
from typing import Optional

class MangaModel(SQLModel, table=True):
    __tablename__ = "mangas"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    description: str
    chapters: int