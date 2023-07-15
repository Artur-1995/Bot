import telebot
from telebot import types

API_TOKEN = '5352403062:AAEkTwEEcCnNSJSqYzi9xyZzenwosHxSMcQ'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn = types.InlineKeyboardButton(text='Кнопка 1', callback_data='btn1')
    btn1 = types.InlineKeyboardButton(text='Кнопка   2', callback_data='btn2')
    kb.add(btn,btn1)
    bot.send_message(message.chat.id, '1', reply_markup=kb)

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn1':
        bot.send_message(callback.message.chat.id, 'Вы нажали кнопку 1!')
    if callback.data == 'btn2':
        bot.send_message(callback.message.chat.id, 'Вы нажали кнопку 2!')

bot.polling()