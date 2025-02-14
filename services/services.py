import random

from lexicon.lexicon import LEXICON

# Определения случайного предмета бота
def process_choice() -> str:
    return random.choice(LEXICON['items'])

# Выбор победителя
def choice_winner(user_item: str, bot_item: str) -> str:
    if user_item == bot_item:
        return (f'🤝 Оба выбрали {user_item}! Ничья!\n'
                'Скучно не будет? Давай еще раз!')
    elif bot_item == LEXICON['loses'][user_item]:
        return (f'🔥 Твой {user_item} разгромил мой {bot_item}! Ты выиграл! Поздравляю! 🎉\n'
                'Сыграем еще?')
    else:
        return (f'😈 Мой {bot_item} победил твой {user_item}! Не везет... Но ты можешь взять реванш! 💪\n'
                'Хочешь реванш?')
