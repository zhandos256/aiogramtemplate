from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from misc import message_text

router = Router()


@router.message(Command('cancel'))
async def cancel(message: Message, state: FSMContext):
    st = await state.get_state()
    if st is not None:
        await message.answer(message_text.operation_canceled)
        await state.clear()
    else:
        await message.answer(message_text.echo_all)
