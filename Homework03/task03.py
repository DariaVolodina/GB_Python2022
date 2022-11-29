# 3.12 Вводим с клаиватуры строку. Необходимо вывести строку,
# где развернём подстроку между первой и
# последней буквой "о" из исходной строки.
# Если она только одна или её нет - то сообщить,
# что буква "о" - одна или не встречается.

def reverse(s: str):
    s = s.lower()
    if s.count('o') == 0:
        print('No "O" in here')
    elif s.count('o') == 1:
        print('There is only one "O"')
    else:
        s1 = s.find('o')
        s_reverse = ''
        s_reverse = s[::-1]
        s2 = len(s) - s_reverse.find('o') - 1
        # print('s1 = ', s1) # check
        # print('s2 = ', s2) # check
        res = ''
        res = s[:s1] + s[s2:s1:-1] + s[s2:len(s)]
        print(res)


txt = input('Enter string: ')
reverse(txt)