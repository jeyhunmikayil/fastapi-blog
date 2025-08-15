from email_utils import send_otp_email

otp = "123456"
email = "j.mikayil@gmail.com"

if send_otp_email(email, otp):
    print("OTP sent!")
else:
    print("Failed to send OTP.")


