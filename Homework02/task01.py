# Вводим с клавиатуры целое число X и У.
# Выводим на экран количество чисел между Х и У,
# которые делятся на 2 и 3


num1 = int(input('Input first integer number: '))
num2 = int(input('Input second integer number: '))

sum1, sum2 = 0, 0

if num1 == num2:
    print('Incorrect input. Numbers are equal')

else:
    if num1 > num2:
        temp = 0
        temp = num2
        num2 = num1
        num1 = temp

    # print(num1, num2) # проверка

    num = num1
    while num != (num2 + 1):
        if num % 2 == 0:
            sum1 += 1
        if num % 3 == 0:
            sum2 += 1
        num += 1

    print(f"From {num1} to {num2} there're {sum1} number(s) divisible by 2")
    print(f'and {sum2} number(s) divisible by 3')
