# app/api/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.deps import get_db
from app.schemas.auth import OTPRequest, TokenResponse
from app.models.otp import OTP
from app.models.user import User
from datetime import datetime
from jose import jwt
from app.core.config import settings
from datetime import datetime, timedelta
from app.schemas.auth import OTPRequestInput
import random
from app.utils.email_utils import send_otp_email

router = APIRouter()



@router.post("/request-otp")
def request_otp(data: OTPRequestInput, db: Session = Depends(get_db)):
    
   # Check if user exists
   user = db.query(User).filter(User.email == data.email).first()
   if not user:
       raise HTTPException(status_code=404, detail="User not found")
   
   # Generate 6 digit OTP
   code = str(random.randint(100000,999999))
   
   # Store code in DB (delete previous OTP for this email if exists)
   db.query(OTP).filter(OTP.email == data.email).delete()
   otp = OTP(email=data.email, code=code, expires_at=datetime.utcnow() + timedelta(minutes=10))
   db.add(otp)
   db.commit()
   
   # Send OTP to email
   if send_otp_email(data.email, code):
       return {"message":"OTP sent"}
   else:
       raise HTTPException(status_code=500, detail="Failed to send OTP")    
    



@router.post("/login", response_model=TokenResponse)
def login_with_otp(payload: OTPRequest, db: Session = Depends(get_db)):
    # 1. Validate OTP
    otp = db.query(OTP).filter(OTP.email == payload.email, OTP.code == payload.otp).first()
    if not otp or otp.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Invalid or expired OTP")

    # 2. Check user exists
    user = db.query(User).filter(User.email == payload.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # 3. Create JWT with expiration
    expire = datetime.utcnow() + timedelta(hours=1)  # 1 hour valid
    payload = {
        "sub": user.email,
        "exp": expire
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

    return {"access_token": token}



