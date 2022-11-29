# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

def isfloat(s: str):
    if ',' in s:    #замена символа на случай, если пользователь введёт дробь с помощью / или ,
        s = s.replace(',', '.')
    if '/' in s:
        s = s.replace('/', '.')

    s1 = s
    marks = '''!@#$^&*(){}[]:;"',./<>?~'''
    for i in s1:
        if i in marks:
            s1 = s1.replace(i, '')
    # if s1.isalpha():
    if not s1.isdigit(): # корректно для русской раскладки
        print('Cтрока HE является числом')

    else:
        if float(s) % 1 != 0:
            print('Cтрока является дробным числом')
        else:
            print('Cтрока HE является дробным числом')


x = input('Enter something: ')
isfloat(x)