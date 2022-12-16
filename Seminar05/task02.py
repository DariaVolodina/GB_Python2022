# 2) Морской бой. 1 поле 1 корабль сначала. список списков

list1 = []

for i in range(4):
    list2 = []
    for j in range(4):
        list2.append(0)
        print(0, end=' ')
    list1.append(list2)
    print()
print(list1)

