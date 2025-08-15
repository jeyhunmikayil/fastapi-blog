# schemas/auth.py
from pydantic import BaseModel, EmailStr

class OTPRequestInput(BaseModel):
    # used when requesting new otp
    # email: str
    email: str = "j.mikayil@gmail.com" # temporary

class OTPRequest(BaseModel):
    # used when when entering sent otp
    email: EmailStr = "j.mikayil@gmail.com" # temporary for dev
    otp: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    
    