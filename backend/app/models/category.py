from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    slug = Column(String(150), unique=True, nullable=False, index=True)
    description = Column(String(255), nullable=True, index=True)
    posts = relationship("Post", back_populates="category")