# 3.1 Вводим с клавиатуры десятичное число.
# Необходимо перевести его  в двоичную систему счисления.
#
# def to_binary(num):
#     ans = ''
#     while num > 0:
#         help = num % 2
#         ans = str(help) + ans
#         num //= 2
#     return ans
#
# print(to_binary(num))


# 3.2 Вводим любую строку текста (на русском).
# Необходимо посчитать количество гласных и согласных букв.

# def count_letters(txt: str):
#     txt = txt.strip()
#     count_vowels = 0
#     count_consonants = 0
#
#     for i in 'a', 'o', 'i', 'u', 'e':
#         count_vowels += txt.count(i)
#
#     count_consonants = len(txt) - count_vowels
#
#     print('vowels = ', count_vowels)
#     print('consonants = ', count_consonants)
#
# s = input('Enter text: ')

# count_letters(s)

# 3.3 Вводим любое слово\словочетание - определить, является ли оно палиндромом

# string = input('Введите слово: ')
# string = string.lower()
# newString = ''
#
# for i in range(len(string)-1, -1, -1):
#     newString += string[i]
#
# if string == newString:
#     print('Это палиндром!')
# else:
#     print('Это не палиндром!')



# 3.4 Напишем программу, которая из введённой строки пользователя,
# поделит её пополам и поменяет половинки местами
#
# txt = input("Введите текст: ")
# a = txt[0:(len(txt)//2)]
# b = txt[(len(txt)//2):len(txt)]
# print(b+a)


