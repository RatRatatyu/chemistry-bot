from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Start menu button that opens the options menu

start_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Поехали!", callback_data="optionStart")]
    ]
)