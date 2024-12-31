from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from utils import dbfunc

start_router = Router()
db = dbfunc.users()

@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    check = db.checkuserexists(message.from_user.id)
    if check:
        await message.answer(f"Hello, {message.from_user.full_name}! Welcome back!",
                             reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                 keyboard=[
                                     [KeyboardButton(text="Balance"), KeyboardButton(text='Solve Shortlink')],
                                     [KeyboardButton(text="Help")]
                                 ]),
                             resize_keyboard=True
                             )
    else:
        await message.answer(f"Hello, {message.from_user.full_name}!",
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                             keyboard=[
                                 [KeyboardButton(text="Balance"),KeyboardButton(text='Solve Shortlink')],
                                 [KeyboardButton(text="Help")]
                                 ]),
                                 )
        db.adduser(message.from_user.id)