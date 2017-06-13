# coding: utf-8
import telebot
from config import token
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_handler(message):
    text = 'Дратути'
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    answers_dict = {
        'калий': 'литий',
        'литий': 'гелий',
        'гелий': 'калий',
        'лёха': 'говна лепёха'
    }
    text = message.text.lower()
    for word, answer in answers_dict.items():
        if word in text:
            bot.reply_to(message, answer)
            return

if __name__ == '__main__':
    print('k a l i u m!')
    bot.polling(none_stop=True)
