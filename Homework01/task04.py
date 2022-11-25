# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек
# в этой четверти (x и y).

def diapason(quarter_num):
    if quarter_num == 1:
        return ('x > 0, y > 0')
    elif quarter_num == 2:
        return ('x < 0, y > 0')
    elif quarter_num == 3:
        return ('x < 0, y < 0')
    elif quarter_num == 4:
        return ('x > 0, y < 0')
    else:
        return ('Incorrect number of quarter')

num = int(input('Задайте номер четверти: '))
print(f'Диапазон возможных координат точек в {num} четверти: {diapason(num)}')