#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import telebot
from pyowm import OWM
from telebot import types
import buttons
from telebot.async_telebot import AsyncTeleBot
bot = AsyncTeleBot(buttons.API_TOKEN)



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, 'Привет, {0.first_name}!'.format(message.from_user)+
                     '\nЯ могу сказать какая погода в твоем городе',
                       reply_markup=buttons.kb)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn1_2':
        buttons.kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Ввести название города', callback_data='btn1')
        # btn2 = types.InlineKeyboardButton(text='Определить город', callback_data='btn2')
        buttons.kb.add(btn1)
        # await bot.send_message(callback.message, 'Как искать?', reply_markup=buttons.kb)

@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


import asyncio
asyncio.run(bot.polling())