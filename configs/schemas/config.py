from typing import Optional

from pydantic import BaseModel

from .auth import Auth
from .server import Server
from .database import Database


class Config(BaseModel):
    AUTH: Optional[Auth] = None
    SERVER: Optional[Server] = None
    DATABASE: Optional[Database] = None
