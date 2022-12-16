# Сгенерируйте список на 30 элементов.
# Отсортируйте список по возрастанию, методом сортировки выбором

from random import randint
def sort_list(my_list):
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print(my_list)


a = 30
list1 = []

for _ in range(a):
    list1.append(randint(0, 100))
print(list1)
print('Список, отсортированный по возрастанию:')
sort_list(list1)
