#data collections   Коллекции данных
# list compressions

# nums = []
# n = 10
# for i in range(n):
#     if i % 2 == 0:
#         nums.append(i ** 3)
#
# print(nums)

# # same thing
# n = 10
# nums = [x**3 for x in range(n) if x % 2 == 0] # генератор списка
# print(nums)

# СЛОВАРИ,ключи DICTIONARY
dict1 = {'Name': 'Bob', 'Age': 30, 123: True}
print(dict1)
# print(dict1['Name'])

# dict2 = dict(name='TTT', age='HOHO')
# print(dict2)
#
# for x in dict1:
#     print(x, dict1[x])
# print(dict1)

# print(dict1.get('Name', 'NO'))
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
#
# dict1['Name'] = 'Mark'
#
# dict1['Name2'] = 'Mark222'
# print(dict1)


c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in c:
    print(i)

print(c[1][1])
c[1][2] = 10
print(c)