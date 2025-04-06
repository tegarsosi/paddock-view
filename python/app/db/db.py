from tortoise import Tortoise
from python.app.settings import settings


async def init_db():
    await Tortoise.init(
        db_url=settings.db_url,
        modules={"models": ["app.db.models"]},
    )
    await Tortoise.generate_schemas()
