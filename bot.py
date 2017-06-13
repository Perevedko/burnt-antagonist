# coding: utf-8
import telebot

token = 'insert your token here'
bot = telebot.TeleBot(token)
burnt_id = 191080189

@bot.message_handler(commands=['start'])
def start_handler(message):
    text = 'Дратути'
    # print(message)
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    # print(message)
    # print('got message')
    if message.chat.id == burnt_id:
        answers_dict = {
            'сложно': 'ты тупой',
            'работ': 'РЯЯЯЯЯБОТА ПРИШЛО ВРЕМЯ ПОТНО ПОРАБОТАТЬ РАБОТА САМА СЕБЯ НЕ ПОРАБОТАЕТ',
            'калий': 'Бёрни, привет тебе от Сосны.'
        }
        text = message.text.lower()
        for word, answer in answers_dict.items():
            if word in text:
                bot.reply_to(message, answer)
                return

if __name__ == '__main__':
    print('Anti Burnt!')
    bot.polling(none_stop=True)
