from aiogram.filters import BaseFilter
from aiogram.types import Message

admins = []
users = []


class AdminFilter(BaseFilter):
    async def __call__(self, message: Message):
        return True if message.from_user.id in admins else False


class UserFilter(BaseFilter):
    async def __call__(self, message: Message):
        return True if message.from_user.id in users else False
