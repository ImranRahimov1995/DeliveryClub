import redis
import telebot

TOKEN = "5438953231:AAFJs5SIkjOrA_5N2183FIA74TNBy7dNxPI"

r = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password='')

if __name__ == '__main__':
    bot = telebot.TeleBot(TOKEN)


    @bot.message_handler(commands=['start'])
    def start_message(message):
        r.sadd('users',message.chat.id)
        bot.send_message(message.chat.id, "Привет ✌️ ")
        print(r.smembers('users'))


    bot.infinity_polling()
