from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from typing import List

from app.schemas.manga import MangaRead
from app.schemas.manga import MangaRead
from app.schemas.user import UserRead, UserCreate, UserUpdate
from app.database import get_session
from app.services.user import get_all_users_service, get_user_by_id_service, add_user_service, update_user_service, delete_user_service


router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[UserRead])
async def get_users(session: Session = Depends(get_session)):
    """Retrieve all users."""
    return get_all_users_service(session)