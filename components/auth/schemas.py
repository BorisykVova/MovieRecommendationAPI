from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    email: str
    username: str

    class Config:
        orm_mode = True


class UserCreate(User):
    password: str


class UserUpdate(UserCreate):
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
