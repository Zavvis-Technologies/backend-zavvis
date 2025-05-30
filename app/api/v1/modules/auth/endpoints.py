from app.db.models.user import User
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.v1.modules.auth import schemas
from app.api.v1.modules.auth.services import create_user, authenticate_user, generate_tokens
from app.core.security import decode_token
from app.core.config import settings

router = APIRouter()

@router.post("/signup", response_model=schemas.TokenResponse)
def register_user(payload: schemas.SignupRequest, db: Session = Depends(get_db)):
    user = create_user(payload.full_name, payload.email, payload.password, db)
    return generate_tokens(user)

@router.post("/login", response_model=schemas.TokenResponse)
def login_user(payload: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(payload.email, payload.password, db)
    return generate_tokens(user)

@router.post("/refresh", response_model=schemas.TokenResponse)
def refresh_token(payload: schemas.RefreshTokenRequest):
    data = decode_token(payload.refresh_token, settings.REFRESH_SECRET_KEY)
    return generate_tokens(user=type("User", (object,), {"email": data["sub"]})())

@router.get("/me", response_model=schemas.UserProfile)
def get_profile(current_user_email: str = Depends(lambda token: decode_token(token, settings.SECRET_KEY)["sub"]), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == current_user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Optional: Password update/reset
@router.put("/change-password")
def change_password(payload: schemas.ChangePasswordRequest, current_user_email: str = Depends(lambda token: decode_token(token, settings.SECRET_KEY)["sub"]), db: Session = Depends(get_db)):
    user = authenticate_user(current_user_email, payload.current_password, db)
    user.hashed_password = hash_password(payload.new_password)
    db.commit()
    return {"message": "Password updated"}

# You can add forgot/reset password logic if needed
@router.post("/forgot-password")
def forgot_password(payload: schemas.ForgotPasswordRequest):
    # TODO: Generate password reset token
    # TODO: Email the token with a reset link
    return {"message": "Password reset link sent if email exists."}


@router.post("/reset-password")
def reset_password(payload: schemas.ResetPasswordRequest):
    # TODO: Validate token from email
    # TODO: Update user password with new hashed one
    return {"message": "Password has been reset successfully."}
