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

def translite(mes):
        translite_name = []
        not_mapping = []
        slovar = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo',
            'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
            'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh',
            'ц':'c','ч':'ch','ш':'sh','щ':'sch','ъ':'','ы':'y','ь':'','э':'e',
            'ю':'u','я':'ya','А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'YO',
            'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
            'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'KH',
            'Ц':'C','Ч':'CH','Ш':'SH','Щ':'SCH','Ъ':'','Ы':'y','Ь':'','Э':'E',
            'Ю':'U','Я':'YA', ' ': ' '}
        for char in mes:
            if char in slovar.keys():
                translite_name.append(slovar[char])
            else:
                not_mapping.append(char)
        if len(not_mapping) > 0:
            print('Not mapping char: %s' % (not_mapping))
        return 'Your name in transliteration: ' + ''.join(translite_name)

@dp.message()
async def send_echo(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text =  translite(message.text)
    logging.info(f'{user_name} {user_id}: {text}')
    await message.answer(text=text)

# 5. pulling
if __name__ == '__main__':
    dp.run_polling(bot)