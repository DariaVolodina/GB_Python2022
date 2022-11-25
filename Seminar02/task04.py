# Решить следующую задачу,, выводящиена экран "электронный таймер".
# Ставим таймер - часы, минуты, секунды.
# После отсчета срабатывает будильник


import time
hours = int(input('введите кол-во часов: '))
mins = int(input('введите кол-во минут: '))
secs = int(input('введите кол-во секунд: '))
num_of_secs = secs+mins*60+hours*3600
while num_of_secs:
    m, s = divmod(num_of_secs, 60)
    min_sec_format = '{:02d}:{:02d}'.format(m, s)
    print(min_sec_format)
    time.sleep(1)
    num_of_secs -= 1
print('finish')
