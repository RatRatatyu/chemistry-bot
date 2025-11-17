from aiogram import Router
from aiogram.types import CallbackQuery, Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import asyncio

from keyboards import options_inline_kb
from process.game_proces import game_question
from process.answer_processor import answer_checker

router = Router()
#class for FSM state
class GameState(StatesGroup):
    waiting_for_answer = State()

#router to start game
@router.callback_query(lambda c: c.data == "gameStart")
async def start_game_handler(callback: CallbackQuery, state: FSMContext):
    
    await callback.message.answer("""Давай поиграем!\nЯ задам тебе 5 вопросов по таблице Менделеива. Я уверен что у тебя все получиться!
                                  \nЕсли что то пойдет не так напиши (сдаться)""")
    
#Initialize game state (score and question index), switch to answer-waiting state,
#generate a new question, save its ID, and send the question to the user

    await state.update_data(score=0, question_index=0)
    await state.set_state(GameState.waiting_for_answer)
    question_text, question_num = game_question()
    await state.update_data(current_question=question_num)
    await callback.message.answer(question_text)

    await callback.answer()

#router which will work only when FSM state is active
@router.message(GameState.waiting_for_answer)
async def handle_answer(message: Message, state: FSMContext):
    stop_word = "сдаться"
    user_answer = message.text.strip().lower()

    #Checkin stop word
    if user_answer == stop_word:
        await state.clear()
        await message.answer("Не переживай, в следующий раз получится!")
        await asyncio.sleep(1)
        await message.answer("Возвращаю тебя в главное меню 🔙")
        await asyncio.sleep(1.5)
        await message.answer(
             """\nОтлично! Мой юный химик, давай начнём! Сначала повторим элементы таблицы Менделеева или сразу сыграем в мини-игру?
                \nВыбор за тобой.""",
            reply_markup=options_inline_kb
        )
        return

    #Getting state data
    data = await state.get_data()
    question_num = data.get("current_question")
    score = data.get("score", 0)
    question_index = data.get("question_index", 0)

    #Cheking user input
    result = answer_checker(user_answer, question_num)
    if result == "Правильно":
        score += 1

    await message.answer(result)

    #Updating index and score
    question_index += 1
    await state.update_data(score=score, question_index=question_index)

    #Checking if question is finished
    if question_index >= 5:
        await message.answer(f"Ты ответил на все вопросы! 🎉\nТвой результат: {score}/5")
        await asyncio.sleep(1)
        await message.answer("Возвращаю тебя в главное меню 🔙")
        await asyncio.sleep(1.5)
        await message.answer(
            "Отлично! Мой юный химик, давай начнём!\n"
            "Сначала повторим элементы таблицы Менделеева или сразу сыграем в мини-игру?",
            reply_markup=options_inline_kb
        )
        await state.clear()
    else:
        #Send next question
        question_text, question_num = game_question()
        await state.update_data(current_question=question_num)
        await message.answer(question_text)