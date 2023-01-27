
import telebot
# from telebot import types
from telebot import types
import mtoken

tokenid = "5955466488:AAHgKxmA1OzaDO7N63qAgbRW7TQ4r9Iht9o"


bot = telebot.TeleBot(tokenid, parse_mode=None)


def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Актуальный Прайс')
    keyboard.row('Заказать')
    keyboard.row('Наш Телеграм канал')
    keyboard.row('Заказать')
    keyboard.row('Наш Телеграм канал')
    keyboard.row('Заказать')
    bot.send_message(message.chat.id, 'Привет Выберите кнопку!',
                     reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Нужна помощь кликни /start ?")


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'Актуальный Прайс':
        bot.send_document(message.chat.id, '/mtoken')
    elif message.text.lower() == 'заказать':
        bot.send_message(message.chat.id, 'ok!')


bot.polling()
