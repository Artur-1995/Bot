import buttons
from Token import API_TOKEN
from aiogram import Bot, types, Dispatcher, executor


bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Привет!\nНапиши мне что-нибудь!")

if __name__ == '__main__':
    executor.start_polling(dp)