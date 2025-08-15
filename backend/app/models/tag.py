from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base
from sqlalchemy.orm import relationship

class Tag(Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False, index=True)
    slug = Column(String(160), unique=True, nullable=False, index=True)
    posts = relationship("Post", back_populates="tags")



from sqlalchemy import Column, Integer, String, Table, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.core.database import Base

# Association table
post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
    UniqueConstraint("post_id", "tag_id", name="uq_post_tag"),
)

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False, index=True)
    slug = Column(String(160), unique=True, nullable=False, index=True)

    # backref from Post defined there
