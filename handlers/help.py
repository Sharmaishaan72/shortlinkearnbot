import os

from utils.dbfunc import users

from aiogram import Router
from aiogram.types import Message



help_router = Router()
db = users()

@help_router.message(lambda message: message.text=="Help")
async def help_handler(message: Message) -> None:
    """
    help handler
    """
    try:
        
        await message.answer(text=f'Hello {message.from_user.first_name}! I am a bot that can help you to earn {os.getenv("currency")} by solving shortlinks.')
    except Exception as e:
        await message.answer("Some error, try again!")
