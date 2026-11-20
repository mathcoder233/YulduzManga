from sqlmodel import SQLModel, Field

class MangaModel(SQLModel, table=True):
    __tablename__ = "mangas"

    id: int | None = Field(default=None, primary_key=True)

    title: str
    author: str
    description: str
    chapters: int