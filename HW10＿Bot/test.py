from operator import itemgetter
from telebot import types
import telebot

name = ''
bot = telebot.TeleBot('5929215785:AAGPmEby5tQxCl8HwFraCVEd6SxbIfafQag')
weekdays = {1: 'MN.txt', 2: 'TUE.txt', 3: 'WDN.txt', 4: 'THU.txt', 5: 'FR.txt', 6: "STD.txt", 7: 'SUN.txt'}


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Выбери действие: 1) Чтение 2)Добавление 3)Замена")
    bot.register_next_step_handler(message, start)
    else:
    bot.send_message(message.from_user.id, "Неизвестная команда. Напиши /start.")


def start(message):
    global surname
    surname = message.text
    if surname == '1':
        bot.send_message(message.from_user.id, "Выберите день недели(1-7)")
    bot.register_next_step_handler(message, op_text)
    else:
    bot.send_message(message.from_user.id, 'Неизвестная команда, напишите /start')
    if surname == '2':
        bot.send_message(message.from_user.id, "Выберите день недели(1-7)")
    bot.register_next_step_handler(message, add_text)


def op_text(message):
    temp = int(message.text)
    with open(weekdays[temp], 'r', encoding='utf-8') as my_f:
        for lin in my_f:
            bot.send_message(message.from_user.id, lin)