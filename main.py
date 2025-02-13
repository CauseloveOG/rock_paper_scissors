import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config_data.config import Config, load_config
from handlers import user_handlers

# Инициализация логгеров
logger = logging.getLogger(__name__)

# Функция конфигурирования и запуска бота
async def main() -> None:
    # Конфигурация логирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    # Загрузка конфиг в переменную
    config: Config = load_config()

    # Инициализация бота и диспетчера
    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    # Подключение роутеров
    dp.include_router(user_handlers.router)

    # Получение апдейтов от ТГ
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())