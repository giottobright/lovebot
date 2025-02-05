import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")  # Укажем токен в .env
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Логирование
logging.basicConfig(level=logging.INFO)

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(
        "Открыть приложение", web_app=WebAppInfo(url="https://lovedaily.netlify.app/")
    )
    keyboard.add(button)

    await message.answer("Перейти в приложение:", reply_markup=keyboard)

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
