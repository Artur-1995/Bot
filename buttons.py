import aiogram
import telebot
kb_search_aiogram = aiogram.types.InlineKeyboardMarkup(row_width=1)
btn1 = aiogram.types.InlineKeyboardButton(text='Ввести название города', callback_data='input_city_name')
btn2 = aiogram.types.InlineKeyboardButton(text='Определить город', callback_data='get_geo')
kb_search_aiogram.add(btn1, btn2)

kb_search_telebot = telebot.types.InlineKeyboardMarkup(row_width=1)
btn1 = telebot.types.InlineKeyboardButton(text='Ввести название города', callback_data='input_city_name')
btn2 = telebot.types.InlineKeyboardButton(text='Определить город', callback_data='get_geo')
kb_search_telebot.add(btn1, btn2)

keyboard_continuation = telebot.types.InlineKeyboardMarkup(row_width=1)
btn1 = telebot.types.InlineKeyboardButton(text='Да', callback_data='input_city_name')
keyboard_continuation.add(btn1)

keyboard_back = telebot.types.InlineKeyboardMarkup(row_width=1)
btn1 = telebot.types.InlineKeyboardButton(text='Ввести в ручную?', callback_data='input_city_name')
keyboard_back.add(btn1)

kb_search_telebot_short = telebot.types.InlineKeyboardMarkup(row_width=1)
btn1 = telebot.types.InlineKeyboardButton(text='Ввести название города', callback_data='input_city_name')
kb_search_telebot_short.add(btn1)

