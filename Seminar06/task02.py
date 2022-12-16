# 2) Требуется по запросу выдавать N различных паролей
# длиной M символов,состоящихизстрочных и
# прописных латинских букв и цифр, кроме тех,
# которые легко перепутать между собой:
# «l» (L маленькое), «I» (i большое), «1» (цифра),
# «o» и «O» (большая и маленькая буквы) и «0» (цифра).
#
# Решение должно содержать две функции: вспомогательную generate_password(m),
# возвращающую случайный пароль длиной m символов, и основную main(n, m),
# возвращающую список из n различных паролей, каждый длиной m символов.

import random


def generate_password(m):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',\
                '1','2', '3', '4', '5', '6', '7', '8', '9', '0']
    exception = "lLIi1oO0"
    for i in alphabet:
        if i in exception: alphabet.remove(i)
    password = []
    for i in range(m):
        password.append(random.choice(alphabet))
    return ''.join(password)


def main(n, m):
    list_of_pass = []
    for i in range(n):
        list_of_pass.append(generate_password(m))
    return list_of_pass


print(main(5, 5))
