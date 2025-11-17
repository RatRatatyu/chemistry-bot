from aiogram import Router
from aiogram.types import CallbackQuery, Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import asyncio

from process.elements_processor import processorElement
from keyboards import options_inline_kb  

router = Router()
#class for FSM state
class ElementsState(StatesGroup):
    waiting_for_elements = State()

#router showing table
@router.callback_query(lambda c: c.data == "elementsTable")
async def start_elements_handler(callback: CallbackQuery, state: FSMContext):
    photo = FSInputFile(r"Images\table.jpg")
    await callback.message.answer_photo(
        
        photo= photo,
        caption="""Отлично! Вот таблица Менделеева! Напиши любой элемент, и я дам тебе небольшую характеристику.
                \nЕсли захочешь выйти в главное меню напиши одно из следущих слов (выход,стоп,назад,меню)"""
    )
    #setting state to wait for user input
    await state.set_state(ElementsState.waiting_for_elements)
    await callback.answer()

#router which will work only when FSM state is active
@router.message(ElementsState.waiting_for_elements)
async def elements_info_handler(message: Message, state: FSMContext):
    element = message.text.strip().lower()
    stop_words = ["выход", "стоп", "назад", "меню"]
    
    #Checkin stop word
    if element in stop_words:
        await state.clear()  
        await message.answer("Возвращаю тебя в главное меню 🔙")
        await asyncio.sleep(1.5)
        await message.answer(
            """\nОтлично! Мой юный химик, давай начнём! Сначала повторим элементы таблицы Менделеева или сразу сыграем в мини-игру?
                \nВыбор за тобой.""",
            reply_markup=options_inline_kb
        )
        return
    # Process element name and return description
    process = processorElement(element)
    await message.answer(process)

    
    