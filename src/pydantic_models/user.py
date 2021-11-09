from pydantic import BaseModel, EmailStr, SecretStr, validator
from src.utils import validate_new_password
from datetime import date


class UserAuthModel(BaseModel):
    email: EmailStr
    password: SecretStr


class UserCreateModel(UserAuthModel):
    email: EmailStr
    password: SecretStr
    name: str
    birth_date: date

    @validator('password')
    def password_acceptable(cls, v):
        success, msg = validate_new_password(v)
        if not success:
            raise ValueError(msg)
        return v

