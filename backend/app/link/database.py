from tortoise import Tortoise

from . import models
from .config import DB_URL


async def startup():
    await Tortoise.init(db_url=DB_URL, modules={'modules': [models]})
    await Tortoise.generate_schemas(safe=True)


async def shutdown():
    await Tortoise.close_connections()