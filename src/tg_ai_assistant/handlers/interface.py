from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from tg_ai_assistant.resources.texts import Interface_MainMenu
from tg_ai_assistant.utils.config import admin_check

router = Router()

@router.message(Command("start"))
async def start_command(message: Message):
    user = message.from_user
    if admin_check(user.id):
        await message.answer(text = Interface_MainMenu)
