from telebot import types

API_TOKEN = '5352403062:AAEkTwEEcCnNSJSqYzi9xyZzenwosHxSMcQ'

kb = types.InlineKeyboardMarkup(row_width=1)
btn1 = types.InlineKeyboardButton(text='Ввести название города', callback_data='btn1')
btn2 = types.InlineKeyboardButton(text='Определить город', callback_data='btn2')
# item2 = types.KeyboardButton('Скинуть точку', request_location=True)
kb.add(btn1, btn2)