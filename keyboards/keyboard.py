# Создание кнопок
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON

# Кнопки Камень, Ножницы, Бумага
player_buttons: list = [KeyboardButton(text=i) for i in LEXICON['items']]
kb_builder_player_buttons = ReplyKeyboardBuilder()
kb_builder_player_buttons.row(*player_buttons, width=3)


# Кнопка выбора играть или нет
desire: list = [KeyboardButton(text=i.capitalize()) for i in LEXICON['desire']]
kb_builder_desire = ReplyKeyboardBuilder()
kb_builder_desire.row(*desire, width=1)
