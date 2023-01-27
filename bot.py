
import telebot
from telebot import types
import murad



bot = telebot.TeleBot(murad.TOKEN , parse_mode=None)


@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Магазин", url='https://ya.ru')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)


    

bot.polling()