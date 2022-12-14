print('lesson 07')
# работа с файлами: текстовые, бинарные
# режимы на чтение, на редактирование и т д
# можно брать ссылку с удаленного файла

# f = open(file_name, file_mode)
# r   # чтение файла
# w   # запись файла
# a  # ДОзапись файла

f = open('test.txt', 'r', encoding='utf-8')
print(f)
f.close()   # не забыть закрыть файл

#Более современным считается использование конструкции WITH - автоматически закроет файл
with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read(10))    # в скобках - размер (количество символов)
    print(f.read(5))
    print(f.read(10))

print('******')
with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.readline())
    print(f.readline())

with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.readlines())

# запись информации в файл
with open('test.txt', 'a', encoding='utf-8') as f:
    f.write('\n/Python')



