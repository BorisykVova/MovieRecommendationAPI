from pydantic import BaseModel


class Auth(BaseModel):
    algorithm: str = 'HS256'
    secret_key: str = 'very_secret_key'
