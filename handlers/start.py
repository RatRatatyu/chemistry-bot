from aiogram import Router
from aiogram.filters import CommandStart
from aiogram import html
from aiogram.types import Message

from keyboards import start_inline_kb

router = Router()

#router for start command
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    
    await message.answer(f"""Привет, {html.bold(message.from_user.full_name)}! Я твой помощник по химии, а именно по изучению Таблицы Менделеева!  
                         \nТы можешь поиграть в мини-игру и проверить свои знания или повторить элементы в Таблице Менделеева. Ну что, начнём?""", reply_markup= start_inline_kb)
    