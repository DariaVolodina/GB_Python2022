# 1) Есть список: ['a','b','c','d','e']
# Необходимо написать программу, которая сдвинет список spisok следующим образом:

# list1 = ['a','b','c','d','e']
# print(list1[2:] + list1[:2])
# # print(list2)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# a = int(input('Enter number: '))
#
# list1 = []
# if a == 0:
#     list1.append(1)
# for i in range(a):
#
#     list1.append((i + 1) * list1[i - 1])
# print(list1)


# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     *Пример:*
#     - [2, 3, 4, 5, 6] => [12, 15, 4];
#     - [2, 3, 5, 6] => [12, 15]

# list2 = [2, 3, 4, 5, 6]
# new_list = []
#
# for i in range(len(list2)//2):
#     new_list.append(list2[i] * list2[len(list2) - 1 - i])
#
# if len(list2) % 2:
#     new_list.append(list2[len(list2) // 2])
#
# print(new_list)


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#     *Пример:*
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#
a = int(input('Enter number: '))
list1 = [0, 1]

for i in range(2, a + 1):
    list1.append(list1[i - 1] + list1[i - 2])

list1.insert(0, 1)
for i in range(1, a):
    list1.insert(0, list1[1] - list[0])

print(list1)