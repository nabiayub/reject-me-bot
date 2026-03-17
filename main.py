import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import config
from handlers import router


async def main():
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token=config.bot_token)
    dp = Dispatcher()
    
    dp.include_router(router)
    
    print("Bot is starting...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped.")
