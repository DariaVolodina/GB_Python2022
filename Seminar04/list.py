print('lesson 4')

name1 = 'Bob'
name2 = 'Bobik'
name3 = 'Bobert'
name4 = 'Bob Bobych'

list1 = ['Bob', 'Bobik', 'Bobert', 'Bob Bobych']
# print(list1[2])

list1[3] = 'Dima'
print(list1)
# print(len(list1))
# print(list1[-1])

for s in list1: # так чаще делают
    print(s, end=' ')
print()

# for i in range(len(list1)):
#     print(list1[i])

# if 'Bobert' in list1:
#     print('yes')
# else:
#     print('no')

# print(list1[1:3]) #срезы
#
# list1.append('Ann') # добавление элемента в конец списка
# print(list1)

list1.insert(2, 'Boris') # вставка - нужно указать индекс, остальные элементы списка сдвинутся вправо
print(list1)

#УДАЛЕНИЕ
list1.remove('Bobik') # удаляет только первое совпавшее значение
print(list1)

list1.pop() # удаляет последний элемент
print(list1)

a = list1.pop(0) # удаляет указанный элемент + МОЖЕТ возвращать значение
print(list1)
print(a)

c = list1.copy() # копия списка
print(c)

b = []
b.append(1)
print(b)

b.sort()
b.reverse()

d = [2, 5, 8, 1, 4, 77]
print(d.sort())


e = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # двумерный массив
