from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)


class UserCreate(UserBase):
    """
    Schema for user registration.
    """
    password: str = Field(..., min_length=8, max_length=100)


class UserLogin(BaseModel):
    """
    Schema for login requests.
    """
    username: str
    password: str


class UserResponse(UserBase):
    """
    Schema returned to the client.
    """
    id: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    """
    Schema for updating user information.
    """
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None