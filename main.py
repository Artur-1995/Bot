import telebot
from pyowm import OWM
from telebot import types
import buttons

owm = OWM('4c714a80d1c7bbf3329a0f310a5ab450')
mgr = owm.weather_manager()
API_TOKEN = '5352403062:AAEkTwEEcCnNSJSqYzi9xyZzenwosHxSMcQ'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user)+
                     '\nЯ могу сказать какая погода в твоем городе', reply_markup=buttons.kb)

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn1_2':
        buttons.kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Ввести название города', callback_data='btn1')
        btn2 = types.InlineKeyboardButton(text='Определить город', callback_data='btn2')
        buttons.kb.add(btn1, btn2)
        bot.send_message(callback.message.chat.id, 'Как искать?', reply_markup=buttons.kb)
    if callback.data == 'btn1':
        bot.send_message(callback.message.chat.id, 'Напишите название города')

        @bot.message_handler(func=lambda message: True)
        def echo_message(message):
            try:
                buttons.kb = types.InlineKeyboardMarkup(row_width=1)
                btn1_2 = types.InlineKeyboardButton(text='Да', callback_data='btn1_2')
                buttons.kb.add(btn1_2)

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
                               '\n' + (clouds[w.detailed_status] if w.detailed_status in clouds.keys() else '')+
                               '\n' + 'Посмотреть погоду в другом городе?'), reply_markup=buttons.kb)

            except:
                bot.send_message(message.chat.id, 'Ошибка! Город не найден.')
        input()


    if callback.data == 'btn2':
        buttons.kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton(text='Отправить точку', request_location=True)
        buttons.kb.add(btn1)
        bot.send_message(callback.message.chat.id, 'Для этого нужно поделиться местоположением', reply_markup=buttons.kb)


bot.polling(none_stop=True)