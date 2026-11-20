from pydantic import BaseModel

class UserRead(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserUpdate(BaseModel):
    username: str
    email: str
    is_active: bool
