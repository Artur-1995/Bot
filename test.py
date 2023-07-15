from aiogram import Bot, Dispatcher, executor, types
from buttons import API_TOKEN

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)

@dp.message_handler(commands=['start'])
async def help_command(message:types.Message):
    await message.answer(text='Добро пожаловать в наш Телеграмм Бот!')
    await  message.delete()

if __name__=='__main__':
    executor.start_polling(dp)
