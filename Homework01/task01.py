# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли
# этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def check_weekday(a):
    if a > 5:
        print("It's weekend")
    else:
        print('Not weekend')

num = int(input('Input number from 1 to 7: '))
while num < 1 or num > 7:
    num = int(input('Incorrect number. Try again: '))

check_weekday(num)