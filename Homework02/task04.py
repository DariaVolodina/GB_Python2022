# Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа
# при просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9),
# 1427 - нет

# def subsequence(x):
#     count = 1
#     temp = x
#     while temp > 9:
#         temp /= 10
#         count += 1
#     # print(count) #check
#
#     x1 = x // (10 ** (count - 1))
#     # print(x1) #check
#     x -= x1 * (10 ** (count - 1))
#     count -= 1
#
#     while count != 0:
#         x2 = x // (10 ** (count - 1))
#         # print(x2) #check
#         if x2 < x1:
#             print('последовательность цифр HE упорядочена по возрастанию')
#             break
#         else:
#             x -= x2 * (10 ** (count - 1))
#             count -= 1
#             x1 = x2
#
#     if count == 0:
#         print('да, последовательность цифр упорядочена по возрастанию')
#
#
# num = int(input('Input multi-digit number: '))
# subsequence(num)

#Var2
# numbers = int(input('Enter number: '))
# while numbers > 10:
#     if numbers // 10 % 10 > numbers % 10:
#         print('no')
#         break
#     numbers = numbers // 10
# else:
#     print('yes')


#Var3
n, flag = int(input('Enter number: ')), 'YES'
while n // 10:
    if (n % 10) < ((n % 100) // 10):
        flag = 'NO'
        n = 0
    n //= 10

print(flag)