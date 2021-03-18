from pydantic import BaseModel


class Server(BaseModel):
    port: int = 8000
    host: str = 'localhost'
    reload: bool = True