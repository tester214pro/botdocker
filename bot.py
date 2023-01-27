
import telebot
from telebot import types
import murad



bot = telebot.TeleBot(murad.TOKEN , parse_mode=None)

xxx = (start_message)


@bot.message_handler(commands=['start'])
def xxx (message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('❤Наш Инстаграм')
    keyboard.row('Заказать Нож')
    bot.send_message(message.chat.id, 'Привет Выберите кнопку!', reply_markup=keyboard)

   
    
    
@bot.message_handler(commands=['help'])
def send_help(message):
	bot.send_message(message.chat.id, "Нужна помощь кликни /start ?")




@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == '❤наш инстаграм':
        bot.send_message(message.chat.id, 'Отправляю сылку на Инстаграм  https://www.instagram.com/kizlyarskie_noji_ot_murada/ ')
    elif message.text.lower() == 'заказать нож':
        bot.send_message(message.chat.id, 'ok!')







bot.polling()
