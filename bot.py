import asyncio
import logging
import os


from utils import read_config
from handlers.Balance import balance_router
from handlers.start import start_router
from handlers.solveshortlink import shortlink_router
from handlers.help import help_router
from handlers import balanceadder

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode



TOKEN = os.getenv("BOT_TOKEN")
#print(TOKEN)


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # Register all the routers from handlers package
    dp.include_routers(
        start_router,
        balance_router,
        shortlink_router,
        help_router
    )

    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))

    # And the run events dispatching
    await dp.start_polling(bot)
    
async def start_script():
    await asyncio.gather(main(), balanceadder.runapp())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start_script())
