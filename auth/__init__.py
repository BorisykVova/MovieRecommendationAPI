from .endpoints import auth
from . import models, schemas
from .backends import schemas as backend_schemas

ROUTER = auth
