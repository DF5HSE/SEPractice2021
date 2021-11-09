"""pydantic models"""
from datetime import date
from pydantic import BaseModel, EmailStr, SecretStr, validator
from src.utils import validate_new_password  # type: ignore


class UserAuthModel(BaseModel):
    """auth model"""
    email: EmailStr
    password: SecretStr


class UserCreateModel(UserAuthModel):
    """create class"""
    email: EmailStr
    password: SecretStr
    name: str
    birth_date: date

    @validator('password')
    def password_acceptable(cls, value):  # pylint: disable=all
        """
        :param value:
        :return:
        """
        success, msg = validate_new_password(value)
        if not success:
            raise ValueError(msg)
        return value
