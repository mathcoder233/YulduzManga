from pydantic import BaseModel, ConfigDict

class MangaRead(BaseModel):
    id: int
    title: str
    author: str
    description: str
    chapters: int

    model_config = ConfigDict(from_attributes=True)

class MangaCreate(BaseModel):
    title: str
    author: str
    description: str
    chapters: int

class MangaUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    description: str | None = None
    chapters: int | None = None
