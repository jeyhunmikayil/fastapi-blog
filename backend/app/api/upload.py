from fastapi import APIRouter, File, UploadFile, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from uuid import uuid4
import os
from app.core.config import settings
from app.core.auth import require_admin # protect uploads if you want

router = APIRouter()

ALLOWED_IMAGE_TYPES = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
    "image/gif": ".gif"
}

@router.post("/upload-image", dependencies=[Depends(require_admin)])
async def upload_image(file: UploadFile = File(...)):
    # 1) Valdiate content type
    ext = ALLOWED_IMAGE_TYPES.get(file.content_type)
    if not ext:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only image uploads are allowed (jpeg, png, webp, gif)."
            )
    # 2) Ensure upload dir exists (via our config helper)
    abs_upload_dir = settings.upload_path
    
    # 3) Generate unique filename
    filename = f"{uuid4().hex}{ext}"
    abs_path = os.path.join(abs_upload_dir, filename)

    # 4) Persist file
    try:
        # Avoid reading entire file into memory; stream it to disk
        with open(abs_path, "wb") as out:
            while True:
                chunk = await file.read(1024 * 1024) # 1MB chunks
                if not chunk:
                    break
                out.write(chunk)
    finally:
        file.close()

    # 5) Build public URL (BASE_URL + /UPLOAD_DIR/filename)
    public_url = f"{settings.BASE_URL.rstrip('/')}/{settings.UPLOAD_DIR.strip('/')}/{filename}"
    
    return JSONResponse({"image_url": public_url})
