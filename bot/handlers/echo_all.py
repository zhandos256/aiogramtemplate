from aiogram import Router
from aiogram.types import Message

from misc import message_text

router = Router()


@router.message()
async def echo_all(message: Message):
    await message.answer(message_text.echo_all)
