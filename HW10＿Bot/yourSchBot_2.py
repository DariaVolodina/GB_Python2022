from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, Poll
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler, \
    PollAnswerHandler, PollHandler
from credits2 import bot_token
import requests
from bs4 import BeautifulSoup as bs
from random import randint


bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

weekdays = {1: 'MO.txt', 2: 'TU.txt', 3: 'WE.txt', 4: 'TH.txt', 5: 'FR.txt', 6: "SA.txt", 7: 'SU.txt'}
day_num = 0


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет! Я - твой ежедневник📔. Давай общаться!👋\n\n'
                                                       '/show - показать расписание📓\n/change - изменить\n/add - добавить событие🖊(сначала "/show")\n'
                                                       '/del - удалить событие✖ (сначала "/show")\n/lol - я устал! Расскажи анекдот\n')


def parse_joke(update, context):
    url = 'https://www.mk.ru/editions/daily/2022/12/21/goryachaya-pyaterka-anekdotov-mk.html'
    response = requests.get(url).text
    soup = bs(response, 'html.parser')
    joke1 = soup.find('div', class_='article__body').text
    joke1 = joke1.replace('\n', '').split('\xa0')
    num_of_joke = randint(0, len(joke1) - 1)
    context.bot.send_message(update.effective_chat.id, ''.join(joke1[num_of_joke]))


def show_schedule(update, context):
    keyboard = [
        [InlineKeyboardButton('ПН', callback_data='1'), InlineKeyboardButton('ВT', callback_data='2'),
         InlineKeyboardButton('СР', callback_data='3')],
        [InlineKeyboardButton('ЧТ', callback_data='4'), InlineKeyboardButton('ПТ', callback_data='5'),
        InlineKeyboardButton('СБ', callback_data='6'), InlineKeyboardButton('ВС', callback_data='7')]
    ]
    update.message.reply_text('Ну-с, дружище, выбирай...', reply_markup=InlineKeyboardMarkup(keyboard))


def action_button(update, context):
    keyboard = [
        [InlineKeyboardButton('Добавить событие', callback_data='+'), InlineKeyboardButton('Удалить событие', callback_data='-')],
        [InlineKeyboardButton('И так сойдёт...', callback_data='0')]
    ]
    update.message.reply_text('Ваши действия: ', reply_markup=InlineKeyboardMarkup(keyboard))


def read_file(week_dict, day_num):
    with open(week_dict[day_num], 'r', encoding='utf-8') as my_f:
        return my_f.readlines()


def change_file(week_dict, row_to_clean):
    row = row_to_clean - 10
    with open(week_dict[day_num], 'r', encoding='utf-8') as my_file:
        current_txt = my_file.readlines()
    with open(week_dict[day_num], 'w', encoding='utf-8') as my_file:
        current_txt.pop(row)
        new_txt = ''.join(current_txt)  # преобразование списка в строку для дальнейшей записи в файл
        my_file.write(new_txt)
    with open(week_dict[day_num], 'r', encoding='utf-8') as my_file:
        return my_file.readlines()


def delete_event(update, context):
    txt = read_file(weekdays, day_num)
    keyboard = []
    for i in range(1, len(txt)):
        sbj = [InlineKeyboardButton(txt[i], callback_data=str(i+10))]
        keyboard.append(sbj)
    update.message.reply_text('Что удаляем?', reply_markup=InlineKeyboardMarkup(keyboard))


def get_new_data(update, context):
    new_data = update.message.text
    with open(weekdays[day_num], 'a', encoding='utf-8') as my_file:
        my_file.writelines('\n' + new_data)
    with open(weekdays[day_num], 'r', encoding='utf-8') as my_file:
        new_sch = my_file.readlines()
    context.bot.send_message(update.effective_chat.id, ''.join(new_sch))


def add_in_schedule(update, context):
    context.bot.send_message(update.effective_chat.id, 'Что добавить?📝')


def button_push(update, context):
    global day_num
    query = update.callback_query
    query.answer()
    if query.data == '0':
        context.bot.send_message(update.effective_chat.id, 'Хозяин - барин')
    elif query.data == '-':
        context.bot.send_message(update.effective_chat.id, 'Команда "/del"')
    elif query.data == '+':
        context.bot.send_message(update.effective_chat.id, 'Команда "/add"')
    elif int(query.data) > 10:
        context.bot.send_message(update.effective_chat.id, ''.join(change_file(weekdays, int(query.data))))
    else:
        context.bot.send_message(update.effective_chat.id, ''.join(read_file(weekdays, int(query.data))))
        day_num = int(query.data)


def unknown_command(update, context):
    context.bot.send_message(update.effective_chat.id, 'Кажется, мы друг друга не поняли. Давай ещё разок!')


def repeat_message(update, context):
    msg = update.message.text.upper()
    if '?' in msg:
        context.bot.send_message(update.effective_chat.id, '...надо подумать.')
    elif msg.isalpha:
        context.bot.send_message(update.effective_chat.id, msg)


start_handler = CommandHandler('start', start)  # регистрируем обработчик команды "старт" в диспетчере.
show_handler = CommandHandler('show', show_schedule)
joke_handler = CommandHandler('lol', parse_joke)
button_handler = CallbackQueryHandler(button_push)
action_handler = CommandHandler('change', action_button)
delete_handler = CommandHandler('del', delete_event)
add_handler = CommandHandler('add', add_in_schedule)
new_event_handler = MessageHandler(Filters.text, get_new_data)

message_handler = MessageHandler(Filters.text, repeat_message)  # требует доработки
unknown_handler = MessageHandler(Filters.command, unknown_command)  # требует доработки


dispatcher.add_handler(start_handler)
dispatcher.add_handler(show_handler)
dispatcher.add_handler(joke_handler)
dispatcher.add_handler(button_handler)
dispatcher.add_handler(action_handler)
dispatcher.add_handler(delete_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(new_event_handler)

dispatcher.add_handler(message_handler)
dispatcher.add_handler(unknown_handler)


updater.start_polling()
updater.idle()