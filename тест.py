import telebot
from telebot import types
import random

API_TOKEN = '5352403062:AAEkTwEEcCnNSJSqYzi9xyZzenwosHxSMcQ'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Рандом')
    item2 = types.KeyboardButton('Курс')
    item3 = types.KeyboardButton('Инфо')
    item4 = types.KeyboardButton('Другое')

    markup.add(item1,item2, item3, item4)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_type=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Рандом':
            bot.send_message(message.chat.id, 'Ваше число: '+ str(random.randint(0, 1000)))
        elif message.text == 'Курс':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('us')
            item2 = types.KeyboardButton('eu')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Курс', reply_markup=markup)
        elif message.text == 'Инфо':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('О боте')
            item2 = types.KeyboardButton('Что в коробке?')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Инфо', reply_markup=markup)
        elif message.text == 'Другое':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Настройки')
            item2 = types.KeyboardButton('Подписка')
            item3 = types.KeyboardButton('Стикер')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, back)
            bot.send_message(message.chat.id, 'Другое', reply_markup=markup)
        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Рандом')
            item2 = types.KeyboardButton('Курс')
            item3 = types.KeyboardButton('Инфо')
            item4 = types.KeyboardButton('Другое')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Назад', reply_markup=markup)
        elif message.text == 'Стикер':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'На на', reply_markup=markup)



bot.polling(none_stop=True)


