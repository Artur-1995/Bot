from Tokens import API_TOKEN, OWM_TOKEN
from aiogram import Bot, types, Dispatcher, executor
from pyowm import OWM
import random
import os

excepshon_answer = ('Мда, давай еще разок по внимательнее', "Все обыскал, нет блин такого города!\nПопробуй еще раз...")

owm = OWM(OWM_TOKEN)
bot = Bot(API_TOKEN)

# owm = OWM('4c714a80d1c7bbf3329a0f310a5ab450')
# bot = Bot('5352403062:AAEkTwEEcCnNSJSqYzi9xyZzenwosHxSMcQ')
dp = Dispatcher(bot)
mgr = owm.weather_manager()
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    # await message.answer('Привет, {0.first_name}!'.format(message.from_user)+
    #                  '\nЯ могу сказать какая погода в твоем городе')
    await message.answer('Привет, {0.first_name}!'.format(message.from_user)+
                     '\nЯ могу сказать какая погода в твоем городе')
@dp.message_handler(types.Message)
async def echo_message(message: types.Message):
    # await message.delete()
    try:
        clouds = {'scattered clouds': 'Ясно',
                  'overcast clouds': 'Облачно',
                  'few clouds': 'Небольшая облачность',
                  'broken clouds': 'Облачно с прояснениями',
                  'clear sky': 'Чистое небо',
                  'moderate rain': 'Умеренный дождь'}
        try:
            observation = mgr.weather_at_place(message.text)
            w = observation.weather
            msg = str(message.text).upper()[0] + str(message.text).lower()[1:]

        except:
            await bot.send_message(message.chat.id, random.choice(excepshon_answer).upper())



        await message.answer((f'Погода в городе {msg}' +
                               '\n' + "Температура " + str(int(w.temperature('celsius')['temp'])) +
                               '\n' + f"Скорость ветра {int(w.wind()['speed'])} м/с" +
                               '\n' + (clouds[w.detailed_status] if w.detailed_status in clouds.keys() else '') +
                               '\n' + 'Посмотреть погоду в другом городе?'))


    except:
        await bot.send_message(message.chat.id, random.choice(excepshon_answer))


# input()




if __name__ == '__main__':
    executor.start_polling(dp)