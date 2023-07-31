import aiogram
from telebot import types
kb_search_aiogram = aiogram.types.InlineKeyboardMarkup(row_width=1)
btn_input_city_name = types.InlineKeyboardButton(text='Ввести название города', callback_data='input_city_name')
btn_get_geo = types.InlineKeyboardButton(text='Определить город', callback_data='get_geo')
kb_search_aiogram.add(btn_input_city_name, btn_get_geo)

btn_input_city_name = types.InlineKeyboardButton(text='Ввести название города', callback_data='input_city_name')
btn_get_geo = types.InlineKeyboardButton(text='Определить город', callback_data='get_geo')
btn_yes = types.InlineKeyboardButton(text='Да', callback_data='input_city_name')
btn_ask_input_city_name = types.InlineKeyboardButton(text='Ввести в ручную?', callback_data='input_city_name')


kb_search_telebot = types.InlineKeyboardMarkup(row_width=1)
btn_input_city_name
btn_get_geo
kb_search_telebot.add(btn_input_city_name, btn_get_geo)

keyboard_continuation = types.InlineKeyboardMarkup(row_width=1)
btn_yes
keyboard_continuation.add(btn_yes)

keyboard_back = types.InlineKeyboardMarkup(row_width=1)
btn_ask_input_city_name
keyboard_back.add(btn_ask_input_city_name)

kb_search_telebot_short = types.InlineKeyboardMarkup(row_width=1)
btn_input_city_name
kb_search_telebot_short.add(btn_input_city_name)


