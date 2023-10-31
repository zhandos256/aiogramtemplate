import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from handlers import (
    greetings,
    echo_all,
    cancel,
    other
)
from misc import env


async def on_startup(dp: Dispatcher):
    dp.include_routers(
        greetings.router,
        cancel.router,
        other.router,
        echo_all.router
    )

    # register startups
    # dp.startup.register()


async def configure_bot():
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout
    )

    bot = Bot(token=env.TOKEN)
    dp = Dispatcher()

    await on_startup(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


def start_bot():
    asyncio.run(configure_bot())
