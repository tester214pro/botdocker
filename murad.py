TOKEN = "5955466488:AAHgKxmA1OzaDO7N63qAgbRW7TQ4r9Iht9o" 

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('❤Наш Инстаграм')
    keyboard.row('Заказать Нож')
    bot.send_message(message.chat.id, 'Привет Выберите кнопку!', reply_markup=keyboard)
