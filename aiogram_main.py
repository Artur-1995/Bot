from Tokens import API_TOKEN, OWM_TOKEN
from buttons import kb_search_aiogram as kb_search
from pyowm import OWM
from aiogram import Bot, types, Dispatcher, executor
import random

excepshon_answer = ('Давай еще разок по внимательнее', "Все обыскал, ненашел такого города!\nПопробуй еще раз...")

owm = OWM(OWM_TOKEN)
bot = Bot(API_TOKEN)

dp = Dispatcher(bot)
mgr = owm.weather_manager()
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user)+
                     '\nЯ могу сказать какая погода в твоем городе', reply_markup=kb_search)

# @dp.callback_query_handler(text="input_city_name")
# async def send_random_value(callback: types.CallbackQuery):
#     await callback.message.answer('В каком городе хотите узнать погоду?')
# @dp.message_handler(types.Message)
# async def echo_message(message: types.Message):
#     # await message.delete()
#     try:
#         clouds = {'scattered clouds': 'Ясно',
#                   'overcast clouds': 'Облачно',
#                   'few clouds': 'Небольшая облачность',
#                   'broken clouds': 'Облачно с прояснениями',
#                   'clear sky': 'Чистое небо',
#                   'moderate rain': 'Умеренный дождь'}
#         try:
#             observation = mgr.weather_at_place(message.text)
#             w = observation.weather
#             msg = str(message.text).upper()[0] + str(message.text).lower()[1:]
#
#         except:
#             await bot.send_message(message.chat.id, random.choice(excepshon_answer).upper())
#
#
#
#         await message.answer((f'Погода в городе {msg}' +
#                                '\n' + "Температура " + str(int(w.temperature('celsius')['temp'])) +
#                                '\n' + f"Скорость ветра {int(w.wind()['speed'])} м/с" +
#                                '\n' + (clouds[w.detailed_status] if w.detailed_status in clouds.keys() else '') +
#                                '\n' + 'Посмотреть погоду в другом городе?'))
#
#
#     except:
#         await bot.send_message(message.chat.id, random.choice(excepshon_answer))
#

if __name__ == '__main__':
    executor.start_polling(dp)