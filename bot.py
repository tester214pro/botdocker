import telebot
from telebot import types
import murad
import mprace

bot = telebot.TeleBot(murad.TOKEN, parse_mode=None)


# Приветствие при нажатии команды старт.
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    IPHONE14 = types.KeyboardButton(murad.IPHONE14)
    IPHONE13 = types.KeyboardButton(murad.IPHONE13)
    markup.add(IPHONE14,IPHONE13)
    bot.send_message(message.chat.id, murad.PRIVET, reply_markup=markup)


@bot.message_handler(commands=['help'])  # Нажатие команды помощь.
def send_help(message):
    bot.send_message(message.chat.id, murad.HELP)


@bot.message_handler(content_types=['text'])  # Будет обработчик кнопок
def send_button(message):
    if (message.text == murad.IPHONE13):
        bot.send_message(message.chat.id, mprace.PRAICE13)
    elif (message.text == murad.IPHONE14):
        bot.send_message(message.chat.id, mprace.PRAISE14)      
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю.")


# bot.infinity_polling()
bot.polling()
# bot.infinity_polling(interval=2, timeout=5)
