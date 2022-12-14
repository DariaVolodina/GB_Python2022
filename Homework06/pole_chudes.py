# 1) Сделать Предыдущее ДЗ с использование функций
# Необязательное
# 2*) Сделать поле чудес . Компьютер загадывает слово.
# А мы его угадываем. Делаем с помощью функций.
# Кто хочет посложней - добавляем очки и баран.

import time
import random

def baraban():
    global user_points
    play = 1  # continue game. 0 - exit game, exit programme immediately
    points_var = [x for x in range(0, 301, 50)] + [400, 500, 'ПРИЗ', '*2', 'ПОЛНЫЙ ноль']
    res = random.choice(points_var)
    time.sleep(0.5)
    print(f'На барабане {res}')

    time.sleep(1)
    if res == 'ПРИЗ':
        play = int(input('Вы можете забрать приз, а можете продолжить игру. \nВведите 0 - чтобы забрать приз, 1 - чтобы продолжить: '))
        if play == 0:
            print('You exited the GAME. But you have a prize - open this black box at home!')
            quit()
    elif res == '*2':
        user_points *= 2
        print(f'Все ваши очки удвоились. Теперь в вашей копилке {user_points} баллов!!!')
    elif res == 'ПОЛНЫЙ ноль':
        user_points = 0
        print('Увы! Все заработанные баллы и призы сгорели.')
    else:
        user_points += res
        print(f'Теперь в вашей копилке {user_points} баллов')


def guess_word(word):
    num_of_letters = len(word)
    word1 = '*' * num_of_letters  # вместо букв - звездочки
    win = 0  # 1 - слово угадано.. переход к следующему
    moves = []

    while win == 0:
        print(f'Крутите барабан!')
        print(word1)
        letter = input('Мы открываем букву: ')  # буква алфавита
        letter = letter.upper()
        while letter in moves:  # случай, если пользователь повторился с буквой
            letter = input('Повторяетесь, сударь! Давайте-ка еще раз. Буква: ')
            letter = letter.upper()
        moves.append(letter)

        w1 = list(word1)
        if letter not in word:
            print('Такой буквы нет.')

        else:
            if letter in word:
                count_letter = word.count(letter)
                print(f'И это правильный ответ! Открываем букву {letter}')
                time.sleep(1)
                w1[word.index(letter)] = letter
                f = word.find(letter) + 1

                while count_letter > 1:
                    word2 = word[f:]
                    letter2 = word2.index(letter)
                    f += letter2 + 1  # надо сделать цикл - если 3 буквы, 4 и тд
                    w1[f - 1] = letter
                    count_letter -= 1

                word1 = ''.join(w1)
                baraban()


        if '*' not in word1:  # ПОБЕДА, если все буквы открыты
            win = 1
            print('Слово УГАДАНО! Браво!\n')


user_points = 0
word_dict = {'ХОНСЮ': 'Самый крупный остров Японского архипелага', \
             'АВОСЬКА': 'В 1931 году Аркадий Райкин \nсам придумал и произнес со сцены некое слово. \nОно стремительно вошло в обиход — так \nстали называть несуразную легкую сумку.', \
             'ПОСЛУШАНИЕ': 'Пельмени издавна заготавливают в форме ушек. \nЧто символизируют такие пельмени?', \
             'БУРЕВЕСТНИК': 'В словаре Владимира Ивановича Даля встречается старинное название барометра. Какое?', \
             'ОДИНОЧЕСТВО': 'Ювелиры часто говорят, что бриллиантам необходимо это.', \
             'УВЕРЕННОСТЬ': 'Английский писатель Киплинг говорил: «Женская интуиция намного точнее, чем мужская...»', \
             'ЧЕМОДАН': 'Соседи по улице знали Дмитрия Ивановича Менделеева \nкак замечательного мастера по изготовлению чего?', \
             'ВОЙНА': 'Какого слова нет в языке народов Арктики?', \
             'СКОВОРОДА': 'Что использовали в Китае для глажки белья вместо утюга?', \
             'ЖУПА': 'Как у западных и южных славян назывались селение, деревня, курень?', \
             'СКРЕПКА': 'Во время второй мировой войны \nэтот предмет являлся символом единства у Норвежцев. \nВ честь него даже построили памятник', \
             'ВРАТАРЬ': 'Так в старину называли сторожа городских ворот', \
             'ВОРОТНИК': 'Что мексиканцы изготовляли из волокнистой древесины кактусов', \
             'ЧЕРЕПАХА': 'Какое животное дало название распространенному в Древнем Риме \nспособу боевого построения?'}
word_list = list(word_dict.keys())
player = input('Добро пожаловать на шоу "Поле чудес"! Представьтесь: ')

rounds = 1
while rounds < 4:   # всего 3 раунда = 3 слова
    print('РАУНД', rounds, '!')
    word_to_guess = random.choice(word_list)  # загаданное слово
    print('СТЕРЕТЬ ПОСЛЕ ПРОВЕРКИ! загадано..... ', word_to_guess)  # check the PROGRAMME (the right word)
    print('Внимание! Вопрос: ', word_dict[word_to_guess])  # загадка
    guess_word(word_to_guess)
    word_list.remove(word_to_guess)
    word_dict.pop(word_to_guess)

    rounds += 1

print(f'GAME is over. На вашем счету {user_points} баллов! Вы богач!')
