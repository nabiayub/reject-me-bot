import asyncio
import logging
import sys
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from config import config
from handlers import router


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(f"{config.webhook_url}{config.webhook_path}")


def main() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    
    bot = Bot(token=config.bot_token)
    dp = Dispatcher()
    dp.include_router(router)
    dp.startup.register(on_startup)

    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    webhook_requests_handler.register(app, path=config.webhook_path)
    setup_application(app, dp, bot=bot)

    print(f"Bot starting on {config.app_host}:{config.app_port}...")
    web.run_app(app, host=config.app_host, port=config.app_port)


if __name__ == "__main__":
    main()
