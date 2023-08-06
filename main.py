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

# @bot.message_handler(func=lambda message: True)
@bot.message_handler(commands=['start'])
def start_command(message):
    user_name = message.from_user.first_name

    if message.text == '/start':
        bot.send_message(message.chat.id, text=f'Привет, {user_name}!' +
                    '\nЯ могу сказать какая погода в твоем городе!', reply_markup=buttons.kb_search_telebot)
        print(f'Пользователя \'{user_name}\' запустил бота!')
    if message.text != '/start':
        bot.send_message(message.chat.id, 'Сначала нужно выбрать вариант из меню',
                         reply_markup=buttons.kb_search_telebot)
        print(
            f'Пользователь \'{message.from_user.first_name}\' ввел \"{message.text}\" и обошел шаблон взаимодействия')

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):

    user_name = callback.from_user.first_name

    if callback.data == 'get_geo':
        bot.send_message(callback.message.chat.id, f'{user_name} эта функция пока что для тебя недоступна!',
                         reply_markup=buttons.keyboard_back)
        print(f'Поиск города по геолокации для пользователя \'{user_name}\' недоступно!')
    if callback.data == 'input_city_name':
        bot.send_message(callback.message.chat.id, f'{user_name} напиши название города')
        print(f'Ожидание ввода от пользователя \'{user_name}\'')

        @bot.message_handler(func=lambda message: True)

        def search_wether(message):
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
                bot.reply_to(message, (f'Погода в городе {msg} '
                                       f'\nТемпература ' + str(int(w.temperature('celsius')['temp'])) +
                                       f"\nСкорость ветра {int(w.wind()['speed'])} м/с"
                                       f"\n{(clouds[w.detailed_status] if w.detailed_status in clouds.keys() else '')}"
                                        ))

                bot.send_message(message.chat.id, text='Посмотреть погоду в другом городе?', reply_markup=buttons.keyboard_continuation)
                print(f'Пользователь \'{user_name}\' искал погоду в городе \'{message.text}\'')

            except:
                bot.send_message(message.chat.id, 'Ошибка! Город не найден.', reply_markup=buttons.kb_search_telebot_short)
                print(f'Пользователь \'{user_name}\' ввел нераспознанное названия города \"{message.text}\"')


if __name__ == "__main__":
    bot.polling()