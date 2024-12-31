import os
import time

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message,InlineKeyboardMarkup,InlineKeyboardButton

from utils.shortlinkcreator import ShortLinkCreator
from utils.api import createmainlink



shortlink_router = Router()
shortlink = ShortLinkCreator()

@shortlink_router.message(lambda message: message.text=="Solve Shortlink")
async def echo_handler(message: Message) -> None:
    """
    Sends shortlink
    """
    try:
      last24h = shortlink.returncountlast24h(message.from_user.id,time.time())+1
      if  last24h<= int(os.getenv("max_links_24h")):
        newlink = createmainlink(shortlink.createshortlink(message.from_user.id,float(os.getenv("reward"))))
        await message.answer(
            text=f'Here is shortlink\n\nYou have generated {last24h}/{os.getenv("max_links_24h")} - resets 24h after you solve the {os.getenv("max_links_24h")}th shortlink',
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text='Shortlink', url=f"{newlink}")]
                    ]
                    ))
      else:
        await message.answer(f'You have reached the maximum limit of shortlinks in 24 hours. Try again later')
    except Exception as e:
        await message.answer(f"some error , try again!")
