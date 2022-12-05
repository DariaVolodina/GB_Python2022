# Написать программу, которая генерирует
# двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки
# (не пользуемся встроенными методами подсчета суммы)

def create_list(x: int):
    from random import randint
    list1 = []
    for _ in range(x):
        c = randint(0, 10)
        list1.append(c)
    return list1


def average(list2):
    new_list = []
    for i in range(len(list2)):
        res = 0
        for j in range(len(list2[i])):
            res += list2[i][j]
        res = round((res / len(list2[i])), 2)
        new_list.append(res)
    return new_list


a = int(input('Enter number: '))
b = int(input('Enter number of rows: '))

full_list = []
for _ in range(b):
    full_list.append(create_list(a))

print(full_list)
print(average(full_list))
