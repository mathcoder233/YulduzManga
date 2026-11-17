# main.py
from fastapi import FastAPI
from routers import manga  # Assumes your router file is named mangas.py inside the routers folder

app = FastAPI(title="Manga Reader API", version="1.0")

# Plug your manga router into the main app
app.include_router(manga.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Manga API! Go to /docs to test your endpoints."}