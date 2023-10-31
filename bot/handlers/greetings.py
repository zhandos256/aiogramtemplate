from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from misc import message_text


router = Router()


@router.message(Command('start'))
async def start(message: Message):
    await message.answer(message_text.hello)


@router.message(Command('help'))
async def help(message: Message):
    await message.answer(message_text.help)
