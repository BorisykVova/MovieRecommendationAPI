from fastapi import APIRouter

from typing import NamedTuple

from . import auth


class Component(NamedTuple):
    prefix: str
    router: APIRouter


COMPONENTS = (
    Component(router=auth.ROUTER, prefix='/auth'),
)
