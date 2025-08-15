# crud/posts.py
from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate
from slugify import slugify
from fastapi import HTTPException, status
import logging

logger = logging.getLogger(__name__)

def get_posts(db: Session):
    return db.query(Post).all()

def create_post(post: PostCreate, db: Session):
    db_post = Post(
        title=post.title,
        content=post.content,
        slug=slugify(post.title)
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def update_post(post_id: int, post_data: PostCreate, db: Session):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    post.title = post_data.title
    post.content = post_data.content
    post.slug = slugify(post_data.title)
    
    db.commit()
    db.refresh(post)
    return post


def delete_post(post_id: int, db: Session):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    db.delete(post)
    db.commit()
    return {"message":"Post deleted"}


def update_slug(post_id: int, new_slug: str, db: Session):
    """
    Update the slug of a blog post after validating input and checking for conflicts.

    This function performs the following checks:
    - Ensures the new slug is not empty or too short.
    - Prevents the use of reserved keywords as slugs.
    - Verifies that the post exists.
    - Ensures the new slug is not already used by another post.

    If all checks pass, the slug is updated and the post is returned.

    Args:
        post_id (int): The ID of the post to update.
        new_slug (str): The new slug to assign to the post.
        db (Session): SQLAlchemy database session.

    Returns:
        Post: The updated post object with the new slug.

    Raises:
        HTTPException: 
            - 400 if the slug is reserved or already taken.
            - 404 if the post is not found.
            - 422 if the slug is empty or too short.
    """ 
    
    slugified = slugify(new_slug)
    
    # Check if slug is reserved
    reserved_slugs = {"about", "contact", "login", "admin"}
    if slugified in reserved_slugs:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail=f"This slug is reserved and cannot be used"
        )
    
    # Check if slug is empty or to short
    if not slugified or len(slugified.strip()) < 3:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Slug is empty or too short"
            )
        
    # Check if post with this id exists or not
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {post_id} not found"
        )
    
    # Check if slug already exists for any other post
    existing = db.query(Post).filter(Post.slug == slugified, Post.id != post_id).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Slug is already in use: \"{slugified}\""
            )
    
    post.slug = slugify(new_slug)
    db.commit()
    db.refresh(post)
    # logger.info(f"Post {post_id} slug updated to: {post.slug}")
    return post