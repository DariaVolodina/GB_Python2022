# Функции
print('lesson 6')

def numbers():
    pass    # пустая строка (чтобы не было ошибок)

def numbers1(x, y):
    if x > y:
        return x
    else:
        return y

x1 = numbers1(11, 777)
x2 = numbers1(113, 77)
x3 = numbers1(543, 212)
print(x1, x2, x3)

# АНОНИМНЫЕ функции - LAMBDA функции
# часто использует для заполнения списков, разовых операций.
r = lambda a, b: a + b if a > b else a - b
print(r(3, 5))

hi = lambda : "Hello, everybody"    # так не делают.
print(hi())                # Вообще слишком часто использовать не надо

# рекурсии