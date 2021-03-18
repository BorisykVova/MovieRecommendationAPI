from typing import List, Dict

from pydantic import BaseModel

Name = str


class Credentials(BaseModel):
    port: int
    database: str
    user: str = 'root'
    password: str = 'root'
    host: str = 'localhost'


class Connection(BaseModel):
    engine: str
    credentials: Credentials


class App(BaseModel):
    models: List[str]
    default_connection: str


class Database(BaseModel):
    connections: Dict[Name, Connection]
    apps: Dict[Name, App]
