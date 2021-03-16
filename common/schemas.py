from enum import Enum

from pydantic import BaseModel

class Status(str, Enum):
    OK = 'ok'
    FAILED = 'failed'


class StatusResponse(BaseModel):
    detail: Status
