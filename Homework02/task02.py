# Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное
# и второе максимальное число из введенных чисел.


x = int(input('Input amount of numbers: '))

if x < 0:
    x = abs(x)

while x < 2:
    x = int(input('Can not be less than 2 numbers. \nInput amount: '))

num = int(input(f'number 1 = '))
x_max = x_max2 = num

for i in range(1, x):
    num1 = int(input(f'number {i + 1} = '))
    if num1 > x_max:
        x_max2 = x_max
        x_max = num1
        # print(x_max, x_max2) # check
    elif x_max > num1 > x_max2:
        x_max2 = num1
        # print(x_max, x_max2) # check


print(f'Maximum number is {x_max}')
print(f'Second maximum number is {x_max2}')
