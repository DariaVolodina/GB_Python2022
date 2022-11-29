# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его
# в шестнадцатиричную систему счисления.

def convert_to16(num: int):
    res = ''
    while num > 0:
        res1 = str(num % 16)
        if res1 == '10':
            res1 = 'A'
        elif res1 == '11':
            res1 = 'B'
        elif res1 == '12':
            res1 = 'C'
        elif res1 == '13':
            res1 = 'D'
        elif res1 == '14':
            res1 = 'E'
        elif res1 == '15':
            res1 = 'F'

        res = res1 + res
        num //= 16
    return res


n = int(input('Enter decimal number: '))

print('в 16-ричной системе = ', convert_to16(n))