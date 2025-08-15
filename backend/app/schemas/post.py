# backend/app/schemas/category.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.schemas.category import CategoryOut

class PostCreate(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
    category_id: Optional[int] = None # category reference
    # author: str
    
    class Config:
        from_attributes = True # old orm_mode = True  in  Pydantic v2

class PostOut(PostCreate):
    id: int
    slug: str
    # author: str
    created_at: datetime
    category: Optional[CategoryOut] = None # nested category details
    
    class Config:
        from_attributes = True # old orm_mode = True  in  Pydantic v2

class SlugUpdate(BaseModel):
    # Create and add a validator to the SlugUpdate schema:
    new_slug: str = Field(..., min_length=3, max_length=100)