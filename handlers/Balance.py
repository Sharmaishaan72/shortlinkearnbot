import os

from utils.dbfunc import users

from aiogram import Router
from aiogram.types import Message


# For each module with handlers we can create a separate router.
balance_router = Router()
db = users()

@balance_router.message(lambda message: message.text=="Balance")
async def echo_handler(message: Message) -> None:
    """
    Handler will send balance of the user
    """
    try:
        
        await message.answer(text=f'Your balance is {db.getbalance(message.from_user.id)} {os.getenv("currency")}\nEarn more by solving shortlinks')
    except Exception as e:
        await message.answer("Some error, try again!")
