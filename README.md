# Manga Yulduz Backend

Backend API for **Manga Yulduz**, an online manga reading platform built with **FastAPI** and **PostgreSQL**.

## Features

- FastAPI REST API
- SQLModel ORM
- PostgreSQL database
- CRUD operations for manga
- Automatic database table creation
- Interactive API documentation (Swagger UI)

## Tech Stack

- Python 3.13
- FastAPI
- SQLModel
- PostgreSQL
- Pydantic Settings
- Uvicorn

## Project Structure

```text
app/
├── models/
├── routers/
├── schemas/
├── services/
├── database.py
└── main.py
```

## Installation

```bash
git clone <repository-url>
cd <repository-name>

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=your_database_connection_string
```

## Run

```bash
python -m uvicorn app.main:app --reload
```

Open:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Current Progress

- Database configuration
- SQLModel integration
- Manga model
- Manga router
- Database session dependency

## Future Plans

- User authentication (JWT)
- User management
- Chapters API
- Comments
- Favorites
- Reading history
- Search
- Admin panel

---

This project is under active development.