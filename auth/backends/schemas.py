from enum import Enum
from typing import Optional

from pydantic import BaseModel


class TokenType(str, Enum):
    BEARER = 'bearer'


class Token(BaseModel):
    access_token: str
    token_type: TokenType

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    username: Optional[str] = None
