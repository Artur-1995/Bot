import os

from pyowm import OWM
import telebot
from dotenv import load_dotenv, find_dotenv

import buttons
from constants import wether_date, callback_data

load_dotenv(find_dotenv())
API_TOKEN = os.getenv("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    user_name = message.from_user.first_name

    bot.send_message(message.chat.id, text=f'Привет, {user_name}!' +
                '\nЯ могу сказать какая погода в твоем городе!', reply_markup=buttons.kb_search_telebot)
    print(f'Пользователя \'{user_name}\' запустил бота!')

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    callback_data(callback)
@bot.message_handler(func=lambda message: True)
def search_wether(message):
    wether_date(message)

if __name__ == "__main__":
    bot.polling()