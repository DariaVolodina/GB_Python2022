# 1) Камень - ножницы - бумага

from random import randint
list1 = {1: 'камень', 2: "ножницы", 3: "бумага"}

while True:
    player = int(input('Choose from 1 = камень, 2 = ножницы, 3 = бумага or print 0 to exit: \n'))
    if player == 0:
        break
    else:
        comp_choice = randint(1, 3)
        print(comp_choice)
        if player == comp_choice:
            print('DRAW')
        elif player == 1 and comp_choice == 2 or player == 3 and comp_choice == 1 or player == 2 and comp_choice == 3:
            print('You win')
        else:
            print('You lose')



