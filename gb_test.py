# -*- coding: utf-8 -*-
import config
import telebot
import time

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def gb_strong(message):
    if message.text == 'Хэй бот скинь свой любимый трек':
        f = open('photo2.jpg', 'rb')
        v = open('music/GB_squad.ogg', 'rb')
        bot.send_photo(message.chat.id, f)
        bot.send_voice(message.chat.id, v)
    if message.text == 'Ты ебанутый?':
        time.sleep(0.2)
        bot.send_message(message.chat.id, 'Закройся лох это шедевр')
    if message.text == 'Я создал монстра':
        time.sleep(0.3)
        bot.send_message(message.chat.id, 'Я тебя щас забаню кожаный ублюдок')

if __name__ == '__main__':
    bot.polling(none_stop=True)