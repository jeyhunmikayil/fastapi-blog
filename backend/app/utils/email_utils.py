import httpx
import os
from dotenv import load_dotenv

load_dotenv()

BREVO_API_KEY = os.getenv("BREVO_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")

def send_otp_email(to_email: str, otp_code: str) -> bool:
    url = "https://api.brevo.com/v3/smtp/email"

    payload = {
        "sender": {"name": "Blog Admin", "email": SENDER_EMAIL},
        "to": [{"email": to_email}],
        "subject": "Your OTP Code",
        "htmlContent": f"<p>Your OTP is: <strong>{otp_code}</strong>.<br>It expires in 1 hour.</p>"
    }

    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }

    try:
        response = httpx.post(url, json=payload, headers=headers)
        return response.status_code == 201
    except Exception as e:
        print("Brevo error:", e)
        return False
