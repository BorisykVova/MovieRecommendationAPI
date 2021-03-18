from tortoise import Tortoise

# from .config import TORTOISE_ORM
from configs import get_config


async def setup():
    config = get_config()
    await Tortoise.init(config=config.DATABASE.dict())
    await Tortoise.generate_schemas()


async def shutdown():
    await Tortoise.close_connections()
