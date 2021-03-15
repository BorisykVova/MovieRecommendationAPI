from tortoise import Tortoise

from .config import TORTOISE_ORM


async def setup():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()


async def shutdown():
    await Tortoise.close_connections()
