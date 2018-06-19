# -*- coding: utf8 -*-import telebot
import telebot
import constants
bot = telebot.TeleBot(constants.token)
# bot.send_message(193500889,"test")
# upd = bot.get_updates()
# print(upd)
#
# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)
print(bot.get_me())

def log(message, answer):
    print("\n ------")
    from datetime import datetime
    print(datetime.now())
    print("сообщение от (0) (1). (id = (2)) \n Текст - (3)".format(message.from_user.first_name,
                                                                    message.from_user.last_name,
                                                                    str(message.from_user.id),
                                                                    message.text))
    print(answer)

@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, "мои пожелания весьма специфичны")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "ты не умеешь играть в эту игру"
    if message.text == "привет":
        answer = "B"
        log(message, answer)
        bot.send_message(message.chat.id, "хелоу")
    elif message.text == "пока":
        answer = "давай"
        bot.send_message(message.chat.id, "давай")
        log(message, answer)
    elif message.text == "1" and str(message.from_user.id) == "583080158":
        bot.send_message(message.chat.id, "ты избранный Нео")
    else:
        bot.send_message(message.chat.id, answer)
        log(message, answer)
bot.polling(none_stop=True, interval=0)