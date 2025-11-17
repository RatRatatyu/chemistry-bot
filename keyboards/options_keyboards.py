from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Buttons for the options menu: selecting further actions

options_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="Повторить элементы", callback_data = "elementsTable"),
        InlineKeyboardButton(text="Начать игру", callback_data= "gameStart")
        ]
        
        ]

)