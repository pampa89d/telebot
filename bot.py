# 1. import libs
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

# 2. Initialeze
TOKEN = os.getenv('TOKEN')
bot = Bot(token='7801747532:AAExe2yV88JocFiz8cTMzYRbBeen4KFJ65I')
dp = Dispatcher()
logging.basicConfig(
    level = logging.INFO,
    filename = os.path.dirname(__file__) + '/logfile.log',
    format = '%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s',
    datefmt = '%H:%M:%S'
    )

# 3. processing start
@dp.message(Command(commands=['start'])) # [*args]
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Hello, {user_name}!'
    logging.info(f'{user_name} {user_id} launch bot')
    await bot.send_message(chat_id=user_id, text=text)

# 4.proccessing all messages
@dp.message()
async def send_echo(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_name} {user_id}: {text}')
    await message.answer(text=text)

# 5. pulling
if __name__ == '__main__':
    dp.run_polling(bot)