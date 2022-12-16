# 3.5 Вводим любую строку и нужно посчитать кол-во символов в верхнем регистре

my_str = input('Enter string: ')

i, count = 0, 0
for i in my_str:
    if i.isupper():
        count += 1

print('символов в верхнем регистре = ', count)

# 3.6 Безопасный пароль. Пользователь вбивает пароль.
# Нужно сказать - безопасный он или нет.
# Безопасным считается, если он от 8 символов, есть верхний и нижний регистр.
# А так же цифры. Можеет, при желании, добавить и спец. символы

# def check_safety(s):
#     if len(s) < 8:
#         print('NOT safe. Password should contain 8 symbols or more')
#     # if s.isalpha(): # если есть специальные символы (без цифр), пропускает пароль
#     #     print('NOT safe. Add digits')
#     if s.isdigit():
#         print('NOT safe. Add letters')
#
#     count, count_low, count_upper = 0, 0, 0
#     for i in s:
#         if i.isdigit():
#             count += 1
#         if i.islower():
#             count_low += 1
#         if i.isupper():
#             count_upper += 1
#     if count == 0:
#         print('NOT safe. Add digits')
#     elif count_low == 0:
#         print('NOT safe. Add lower case symbols')
#     elif count_upper == 0:
#         print('NOT safe. Add upper case symbols')
#     else:
#         print('GOOD password!')
#
#
# password = input('Enter password: ')
# check_safety(password)


# 3.7 Вводим строку с клавиатуры. Необходимо сказать, какой символ встречается чаще всего
#
# my_str = str(input('Введите строку: '))
# max_symbol = ''
# ind, max_ind = 0, 0
#
# for i in range(len(my_str)):
#     ind = my_str.count(my_str[i])
#     if ind > max_ind:
#         max_ind = ind
#         max_symbol = my_str[i]
# print(f'Элемент {max_symbol} встречается наибольшее количестов раз, а именно: {max_ind}')


# 3.8 Написать программу, которая скажет в веденной строке индекс второго символа "в"

# def second_v(s: str):
#     s = s.lower()
#     if s.count('в') < 2:
#         print('Error! No second symbol of "в"')
#     else:
#         i = s.find('в')
#         res = s.find('в', i + 1, len(s)) # string.find(substring,start,end)
#         print(res)
#
#
# txt = '01в345в'
# # txt = input('Enter string: ')
# second_v(txt)