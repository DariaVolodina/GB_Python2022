# Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр,
# которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст
# 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых


def check_div(x):
    num1 = num3 = num10 = num25 = 0
    num25 = x // 25
    x = x % 25
    num10 = x // 10
    x = x % 10
    num3 = x // 3
    num1 = x % 3
    print(f'К выдаче: \n25-рублёвых купюр = {num25}\n10-рублёвых купюр = {num10}\n3-рублёвых купюр = {num3}\n1 рублёвых = {num1}')


num = int(input('Input salary: '))

if num <= 0:
    print('no salary')
else:
    check_div(num)


