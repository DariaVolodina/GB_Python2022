# Напишите программу, которая принимает на вход координаты точки
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def quarter(x, y):
    if x > 0 and y > 0:
        return '1'
    elif x < 0 and y > 0:
        return '2'
    elif x < 0 and y < 0:
        return '3'
    else:
        return '4'


num1 = int(input('Input coordinate X: '))
num2 = int(input('Input coordinate Y: '))

if num1 == 0 or num2 == 0:
    print('Точка находится на оси координат')
else:
    print(f'Точка с координатами ({num1}, {num2}) находится в четверти {quarter(num1, num2)}')