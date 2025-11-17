from aiogram import Router
from aiogram.types import CallbackQuery
from keyboards import options_inline_kb
router = Router()

# Callback handler for "optionStart": sends welcome message and displays inline options

@router.callback_query(lambda c: c.data == "optionStart")
async def start_option_handler(callback: CallbackQuery):
    await callback.message.answer("""Отлично! Мой юный химик, давай начнём! Сначала повторим элементы таблицы Менделеева или сразу сыграем в мини-игру?
                                  \nВыбор за тобой.""",reply_markup= options_inline_kb)
    await callback.answer()