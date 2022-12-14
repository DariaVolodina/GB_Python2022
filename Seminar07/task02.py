# Schedule + BOT консольный

def read_schedule(week_dict, day_num):
    with open(week_dict[day_num], 'r', encoding='utf-8') as my_f:
        print(''.join(my_f.readlines()))


def add_event(week_dict, day_num, start_time, finish_time, txt):
    with open(week_dict[day_num], 'r', encoding='utf-8') as my_file:
        current_txt = my_file.readlines()
    with open(week_dict[day_num], 'w', encoding='utf-8') as my_file:
        for j in range(start_time, finish_time):  # замена каждой строки, на которой мероприятие
            t = str(j) + ':00'
            current_txt.pop(j)  # удаление исходника
            current_txt.insert(j, t + ' ' + txt + '\n')  # вписываем исходное время + мероприятие для каждого d
        new_txt = ''.join(current_txt)  # преобразование списка в строку для дальнейшей записи в файл
        my_file.write(new_txt)


weekdays = {1: 'MO.txt', 2: 'TU.txt', 3: 'WE.txt', 4: 'TH.txt', 5: 'FR.txt', 6: "SA.txt", 7: 'SU.txt'}
weekday_names = {1: 'понедельник', 2: 'вторник', 3: 'среду', 4: 'четверг', 5: 'пятницу', 6: "субботу", 7: 'воскресенье'}

# for i in range(1, 8):   # добавляем в каждый файл время ТОЛЬКО ОДИН РАЗ, чтобы не удалялись события
#     with open(weekdays[i], 'w', encoding='utf-8') as my_f:
#         for j in range(24):
#             t = str(j)
#             my_f.write(t + ':00\n')

schedule_change = int(input('Enter 1 to read, 2 - to add, 3 - to change: '))
while schedule_change < 1 or schedule_change > 3:
    schedule_change = int(input('Error. Try again (1, 2 or 3) : '))

if schedule_change == 1:
    day = int(input('Enter day of week (from 1 to 7): '))
    read_schedule(weekdays, day)

elif schedule_change == 2:
    day = int(input('Enter day of week (from 1 to 7): '))
    time_of_event = int(input('Enter start time (from 0 to 23): '))
    end_of_event = int(input('What time will it finish? Enter from 1 to 23: '))
    event = input('What event would U like to add? ')
    add_event(weekdays, day, time_of_event, end_of_event, event)

elif schedule_change == 3:
    day = int(input('В какой день Вы хотели бы внести изменения (enter from 1 to 7): '))
    print('Вот ваше расписание на ', weekday_names[day])
    read_schedule(weekdays, day)
    action = int(input('Enter 1 to delete an event, 2 - to add an event: '))
    while action != 0:
         if action == 1:
            t1 = int(input('CLEAN from what time? Enter from 0 to 23: '))
            t2 = int(input('Till what time to clean? Enter finish time from 0 to 23: '))
            while t1 > t2:
                t2 = int(input('Finish time can not be earlier than start time. Enter finish time: '))
            if t1 == t2:
                t2 = t1 + 1
            add_event(weekdays, day, t1, t2, '')
            action = int(input('Enter 1 to delete an event, 2 - to add an event, 0 - to quit: '))

         elif action == 2:
            time_of_event = int(input('Enter start time (from 0 to 23): '))
            end_of_event = int(input('What time will it finish? Enter from 1 to 23: '))
            event = input('What event would U like to add? ')
            add_event(weekdays, day, time_of_event, end_of_event, event)
            action = int(input('Enter 1 to delete an event, 2 - to change time, 3 - to add an event, 0 - to quit: '))





