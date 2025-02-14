from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from services.services import process_choice, choice_winner
from lexicon.lexicon import LEXICON
from keyboards.keyboard import kb_builder_desire, kb_builder_player_buttons

router = Router()

# Старт с предложением сыграть или перейти в праивла
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'],
                         reply_markup=kb_builder_desire.as_markup(resize_keyboard=True, one_time_keyboard=True))

# Правила игры
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['/help'])

# Игра с клавиатурой предметов на выбор
@router.message(F.text == LEXICON['desire'][0])
async def process_choice_item(message: Message):
    await message.answer(text=LEXICON['want'],
                         reply_markup=kb_builder_player_buttons.as_markup(resize_keyboard=True))

# Пользоваель не хочет играть
@router.message(F.text == LEXICON['desire'][-1])
async def process_choice_item(message: Message):
    await message.answer(text=LEXICON['dont_want'])

# Определение пебедителя и предложение сыграть еще раз
@router.message(F.text.in_(LEXICON['items']))
async def process_winner(message: Message):
    await message.answer(text=choice_winner(message.text, process_choice()),
                         reply_markup=kb_builder_desire.as_markup(resize_keyboard=True, one_time_keyboard=True))

# Ответ на остальные сообщения
@router.message()
async def process_other_message(message: Message):
    await message.answer(text=LEXICON['other'])

