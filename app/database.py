from sqlmodel import create_engine, Session, SQLModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from pydantic import Field

class Settings(BaseSettings):
    database_url: str = Field(alias="DATABASE_URL")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()

engine = create_engine(settings.database_url, echo=True)

def create_db_and_tables():
    """Creates database tables based on your SQLModel definitions."""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Dependency that provides a database session for your API routes."""
    with Session(engine) as session:
        yield session