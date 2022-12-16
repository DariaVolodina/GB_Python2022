print('GB lesson 3')
#
# s = 'Java C# Python'

# if 'C#' in s:
#     print('ok')
# else:
#     print('no')
#
# print(s[2])
# print(s[-1])

# for i in range(len(s)):
    # print(s[i])
#
# for i in s:
#     print(i)

#срезы
s = 'Java C# Python'
# print(s[2:7])
print(s[2:10:2])
print(s[:10])
print(s[:])
print(s[::-1])

# print(len(s))
#
# for i in range(len(s) - 1, 0, -1):
#     print(s[i])

print(s.capitalize())
print(s.title())
print(s.lower())
print(s.upper())

print(s.count('a')) #подсчет количества вхождений
print(s.startswith('Java'))
print(s.find('va'))
print(s.replace('va', 'BO'))

print(s.isdigit())
print(s.isalpha())

