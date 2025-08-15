# api/posts.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.post import PostCreate, PostOut, SlugUpdate
from app.crud import post as crud
from app.core.database import SessionLocal
from app.core.deps import get_db
from app.core.auth import get_current_user, require_admin

router = APIRouter()

@router.get("/", response_model=list[PostOut])
def list_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db)

@router.post("/", response_model=PostOut, dependencies=[Depends(require_admin)])
def add_post(post: PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(post, db)

@router.put("/{post_id}", response_model=PostOut, dependencies=[Depends(require_admin)])
def edit_post(post_id: int, post_data: PostCreate, db: Session = Depends(get_db)):
    return crud.update_post(post_id, post_data, db)

@router.delete("/{post_id}", dependencies=[Depends(require_admin)])
def remove_post(post_id:int, db: Session = Depends(get_db)):
    return crud.delete_post(post_id, db)

# api/posts.py
@router.put('/edit-slug/{post_id}', response_model=PostOut, dependencies=[Depends(require_admin)])
def edit_slug(post_id: int, payload: SlugUpdate, db: Session = Depends(get_db)):
    return crud.update_slug(post_id, payload.new_slug, db)