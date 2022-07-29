import os

import redis
import telebot

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN",None)

r = redis.Redis(
    host='redis',
    port=6379,
    password='')

if __name__ == '__main__':
    bot = telebot.TeleBot(TELEGRAM_TOKEN)


    @bot.message_handler(commands=['start'])
    def start_message(message):
        """
            Простой метод который сохраняет подписчиков в редис

        """
        r.sadd('users', message.chat.id)
        _message = "Привет ✌️, Вы успешно подписались "
        bot.send_message(message.chat.id, _message)


    bot.infinity_polling()
