from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from credits2 import bot_token
import requests
from bs4 import BeautifulSoup as bs
from random import randint


bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)  # связываемся с сервером, получаем обновление
dispatcher = updater.dispatcher     # распределяет сообщения от пользователя по хэндлерам

weekdays = {1: 'MO.txt', 2: 'TU.txt', 3: 'WE.txt', 4: 'TH.txt', 5: 'FR.txt', 6: "SA.txt", 7: 'SU.txt'}


def start(update, context):     # первый ХЭНДЛЕР для обработки сообщений пользователя
    context.bot.send_message(update.effective_chat.id, 'Привет! Я - твой ежедневник📔. Давай общаться!👋\n\n'
                                                       '/show - показать расписание📓\n/add - добавить событие🖊\n'
                                                       '/del - удалить событие✖\n/change - изменить время события\n'
                                                       '/lol - я устал! Расскажи анекдот\n'
                                                       '/day - дни недели')


def delete_event(update, context):
    context.bot.send_message(update.effective_chat.id, 'Ща удалим. Что лишнее?')


def add_event(update, context):
    context.bot.send_message(update.effective_chat.id, 'На какой день добавим?')


def change_event(update, context):
    context.bot.send_message(update.effective_chat.id, 'Не вопрос! Что исправляем?')


def parse_joke(update, context):
    url = 'https://www.mk.ru/editions/daily/2022/12/21/goryachaya-pyaterka-anekdotov-mk.html'
    response = requests.get(url).text
    soup = bs(response, 'html.parser')
    joke1 = soup.find('div', class_='article__body').text
    joke1 = joke1.replace('\n', '').split('\xa0')
    num_of_joke = randint(0, len(joke1) - 1)
    context.bot.send_message(update.effective_chat.id, ''.join(joke1[num_of_joke]))
    # context.bot.send_message(update.effective_chat.id, 'хо-хо-хо')


# def get_day(update, context):
#     keyboard = [
#         [InlineKeyboardButton('Понедельник', callback_data='1'), InlineKeyboardButton('Вторник', callback_data='2'),
#         InlineKeyboardButton('Среда', callback_data='3')], [InlineKeyboardButton('Четверг', callback_data='4'),
#         InlineKeyboardButton('Пятница', callback_data='5'),
#         InlineKeyboardButton('Суббота', callback_data='6'), InlineKeyboardButton('Воскресенье', callback_data='7')]
#     ]
#     update.message.reply_text('Ну-с выбирай...', reply_markup=InlineKeyboardMarkup(keyboard))
#
def show_schedule(update, context):
    keyboard = [
        [InlineKeyboardButton('Понедельник', callback_data='1'), InlineKeyboardButton('Вторник', callback_data='2'),
         InlineKeyboardButton('Среда', callback_data='3')], [InlineKeyboardButton('Четверг', callback_data='4'),
                                                             InlineKeyboardButton('Пятница', callback_data='5'),
                                                             InlineKeyboardButton('СБ', callback_data='6'),
                                                             InlineKeyboardButton('ВС', callback_data='7')]
    ]
    update.message.reply_text('Ну-с выбирай...', reply_markup=InlineKeyboardMarkup(keyboard))

    # context.bot.send_message(update.effective_chat.id, 'Ну ты, дружище, занятой...')


def button_push(update, context):
    query = update.callback_query
    query.answer()
    if query.data == '1':
        context.bot.send_message(update.effective_chat.id, "Рабочая неделя стартует!")
    elif query.data == '2':
        context.bot.send_message(update.effective_chat.id, "День в офисе второй")
    elif query.data == '3':
        context.bot.send_message(update.effective_chat.id, "Среда")
    elif query.data == '4':
        context.bot.send_message(update.effective_chat.id, "ЧТ")
    elif query.data == '5':
        context.bot.send_message(update.effective_chat.id, "Meet your FRIends on FRIday")
    elif query.data == '6':
        context.bot.send_message(update.effective_chat.id, "Суббота у БОТА")
    elif query.data == '7':
        context.bot.send_message(update.effective_chat.id, "Воскресеньем отдохнём?")



def unknown_command(update, context):
    context.bot.send_message(update.effective_chat.id, 'Кажется, мы друг друга не поняли. Давай ещё разок!')


def repeat_message(update, context):
    msg = update.message.text.upper()
    # start_list = ['КТО', 'ЧТО ДЕЛАТЬ', 'ПРЕДСТАВЬ', 'КОМАНД', 'ПОДСКА']
    # count_i = 0
    # i = 0
    # while i < len(start_list):
    #     if start_list[i] in msg: count_i += 1
    #     break
    # if count_i > 0:
    #     context.bot.send_message(update.effective_chat.id, start(update, context))
    # elif '?' in msg:
    if '?' in msg:
        context.bot.send_message(update.effective_chat.id, '...надо подумать.')
    else:
        context.bot.send_message(update.effective_chat.id, msg)


start_handler = CommandHandler('start', start)  # регистрируем обработчик команды "старт" в диспетчере.
show_handler = CommandHandler('show', show_schedule)
delete_handler = CommandHandler('del', delete_event)
add_handler = CommandHandler('add', add_event)
change_handler = CommandHandler('change', change_event)
joke_handler = CommandHandler('lol', parse_joke)

unknown_handler = MessageHandler(Filters.command, unknown_command)
button_handler = CallbackQueryHandler(button_push)
message_handler = MessageHandler(Filters.text, repeat_message)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(show_handler)
dispatcher.add_handler(delete_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(change_handler)
dispatcher.add_handler(joke_handler)

dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(button_handler)
dispatcher.add_handler(message_handler)



updater.start_polling() # Запускаем цикл приёма и обработки сообщений
updater.idle()  # Ждём завершения приложения при нажатии CTRL + C