import asyncio
from tortoise import Tortoise
from app.db.config import TORTOISE_ORM


async def init_db():
    await Tortoise.init(TORTOISE_ORM)
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()


async def main():
    try:
        await init_db()
        print("Database initialized")
    finally:
        await close_db()
        print("Database closed")

if __name__ == "__main__":
    asyncio.run(main())
