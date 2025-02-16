LEXICON: dict[str, str | list | dict] = {
    '/start': '🎮 Добро пожаловать в "Камень, Ножницы, Бумага — Битва с Ботом!" 🎮\n'
              'Я — твой цифровой соперник, готовый сразиться с тобой в легендарной игре!\n\n'
              '👉 Хочешь начать игру? Жми <b>Давай!</b>\n'
              '👉 Хочешь узнать правила? Жми /help',

    '/help': '📖 Правила просты:\n'
             '— Камень 🗿 бьет ножницы ✂️\n'
             '— Ножницы ✂️ режут бумагу 📜\n'
             '— Бумага 📜 накрывает камень 🗿\n'
             'Хочешь начать игру?',

    'desire': ['Давай!', 'Не хочу.'],

    'want': '🎲 Отлично! Сделай свой выбор!',

    'dont_want': 'Хорошо. Если, вдруг, захочешь сыграть - открой клавиатуру и нажми "Давай!',

    'items': ['🗿Камень', '✂️Ножницы', '📜Бумага'],

    'loses': {'🗿Камень': '✂️Ножницы',
            '📜Бумага': '🗿Камень',
            '✂️Ножницы': '📜Бумага'},

    'other': '❌ Упс!\nКажется, ты выбрал что-то не то... Попробуй еще раз.\nИли нажми /help для подсказки.'
}
