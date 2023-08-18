import os

from pyowm import OWM
import telebot
from dotenv import load_dotenv, find_dotenv

import buttons

load_dotenv(find_dotenv())
OWM_TOKEN = os.getenv("OWM_TOKEN")
API_TOKEN = os.getenv("API_TOKEN")

owm = OWM(OWM_TOKEN)
bot = telebot.TeleBot(API_TOKEN)
mgr = owm.weather_manager()


def callback_data(callback):
    user_name = callback.from_user.first_name

    if callback.data == 'get_geo':
        bot.send_message(callback.message.chat.id, f'{user_name} эта функция пока что для тебя недоступна!',
                         reply_markup=buttons.keyboard_back)
        print(f'Поиск города по геолокации для пользователя \'{user_name}\' недоступно!')

    if callback.data == 'input_city_name':
        bot.send_message(callback.message.chat.id, f'{user_name} напиши название города')
        print(f'Ожидание ввода от пользователя \'{user_name}\'')


def wether_date(message):

    user_name = message.from_user.first_name
    try:
        clouds = {'scattered clouds': 'Ясно',
                  'overcast clouds': 'Облачно',
                  'few clouds': 'Небольшая облачность',
                  'broken clouds': 'Облачно с прояснениями',
                  'clear sky': 'Чистое небо',
                  'moderate rain': 'Умеренный дождь'}
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        msg = str(message.text).upper()[0] + str(message.text).lower()[1:]

        bot.reply_to(message, (f'Погода в городе {msg}' +
                               '\n' + "Температура " + str(int(w.temperature('celsius')['temp'])) +
                               '\n' + f"Скорость ветра {int(w.wind()['speed'])} м/с" +
                               '\n' + (
                                   clouds[w.detailed_status] if w.detailed_status in clouds.keys() else '')))

        answer_user = ['Посмотреть погоду в другом городе?', buttons.keyboard_continuation]
        answer_admin = f'Пользователь \'{str(user_name)}\' искал погоду в городе \'{message.text}\''

    except Exception:
        answer_user = ['Ошибка! Город не найден.', buttons.kb_search_telebot_short]
        answer_admin = f'Пользователь \'{str(user_name)}\' ввел нераспознанное названия города \"{message.text}\"'

    bot.send_message(message.chat.id, text=answer_user[0], reply_markup=answer_user[1])
    print(answer_admin)