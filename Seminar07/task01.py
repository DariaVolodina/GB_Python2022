weekdays = {1: 'MO.txt', 2: 'TU.txt', 3: 'WE.txt', 4: 'TH.txt', 5: 'FR.txt', 6: "SA.txt", 7: 'SU.txt'}

schedule_change = int(input('Enter 1 to read, 2 - to add, 3 - to change: '))
while schedule_change < 1 or schedule_change > 3:
    schedule_change = int(input('Error. Try again (1, 2 or 3) : '))

if schedule_change == 1:
    day = int(input('Enter day of week (from 1 to 7): '))
    with open(weekdays[day], 'r', encoding='utf-8') as my_f:
        print(my_f.readlines())

elif schedule_change == 2:
    day = int(input('Enter day of week (from 1 to 7): '))
    event = input('What event would U like to add? ')
    with open(weekdays[day], 'a', encoding='utf-8') as my_f:
        my_f.write('\n')
        my_f.write(event)

elif schedule_change == 3:
    day = int(input('Enter day of week (from 1 to 7): '))
    event = input('What event would U like to add? ')
    with open(weekdays[day], 'w', encoding='utf-8') as my_f:
        my_f.write(event)