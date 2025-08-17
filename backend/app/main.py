# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.core.config import settings
from app.api import posts, auth, upload, categories 
from fastapi.security import HTTPBearer
from fastapi.openapi.models import APIKey, APIKeyIn, SecuritySchemeType
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
import app.models  # noqa: F401  <-- ensures Post, Category, etc. are imported


# Create db tables if they not exists
Base.metadata.create_all(bind=engine)


app = FastAPI(title="Blog API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS.split(","),
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve uploaded files from /<UPLOAD_DIR>
# e.g. http://localhost:8000/uploads/<file>
app.mount(
    f"/{settings.UPLOAD_DIR.strip('/')}",
    StaticFiles(directory=settings.upload_path),
    name="uploads",
)

app.include_router(posts.router, prefix="/posts", tags=["Posts"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(upload.router, prefix="/upload", tags=["Uploads"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])

@app.get("/")
def read_home():
    return {
        "message":"Homepage Works"
    }

from app.core.openapi import custom_openapi
app.openapi = lambda: custom_openapi(app)