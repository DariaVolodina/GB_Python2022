# Решить следующую задачу:  генерируем среднее арифметическое
# последовательности дробных чисел, вводимых с клавиатуры.
# После того, как введем последнее число  - программа
# выводит среднее арифметическое, максимальное и минимальное значение.
# (не пользуемся списками и встроенными функциями)
# Количество чисел задаётся в начале работы программы


num = int(input('Введите количество чисел: '))

n = float(input('Input number: '))
n_max = n
n_min = n
sum = n

for i in range(1, num):
    n2 = float(input('Input number: '))
    sum += n2
    if n2 > n_max:
        n_max = n2
    elif n2 < n_min:
        n_min = n2

print(sum)
num1 = sum / num
print(f'Среднее арифметическое = {round(num1, 2)}')
print(f'min value = {n_min}')
print(f'max value = {n_max}')


