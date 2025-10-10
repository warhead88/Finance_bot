import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import Config
from db.db import init_db
from handlers import start, earn, spend

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

async def main():
    bot = Bot(token=Config.BOT_TOKEN)
    dp = Dispatcher()
    
    dp.include_router(start.router)
    dp.include_router(earn.router)
    dp.include_router(spend.router)

    await init_db()
    
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(e)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
