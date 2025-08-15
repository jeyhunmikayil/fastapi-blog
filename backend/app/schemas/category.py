# app/schemas/category.py
from pydantic import BaseModel, Field
from typing import Optional


class CategoryBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=120)
    description: Optional[str] = Field(None, max_length=500)
    
class CategoryCreate(CategoryBase):
    pass # slug will be auto-generated from name  

class CategoryUpdate(CategoryBase):
    name: Optional[str] = Field(None, min_length=2, max_length=120)
    description: Optional[str] = Field(None, max_length=500)

class CategoryOut(CategoryBase):
    id: int
    slug: str
    class Config:
        from_attributes = True
        
        
        

