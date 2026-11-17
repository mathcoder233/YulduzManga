from pydantic import BaseModel, ConfigDict

class Manga(BaseModel):
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
    title: str
    author: str
    description: str
    chapters: int

class MangaDelete(BaseModel):
    id: int