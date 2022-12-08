# *) Не обязательное задание - Крестики-нолики
import random
import time
import math


def show_field(my_list, my_size):
    size1 = int(math.sqrt(my_size))
    for s in range(size1):
        print(my_list[s * size1:size1 + size1 * s])


def move(list1, symbol1, x):
    list1.pop(x)
    list1.insert(x, symbol1)
    show_field(list1, size)
    print()


size = 9  # size of field
field = [(1 + i) for i in range(size)]

# User can choose whether to play with Comp or with person
players = int(input("Let's play tic-and-toe. Game for one person (enter 1) or two (enter 2)? "))
if players == 1:
    player1 = 'You'
    player2 = 'Computer'
elif players == 2:
    player1 = input('Player 1, enter your name: ')
    player2 = input('Player 2, enter your name: ')
else:
    print('oops... something went wrong.')  # mistake

show_field(field, size)
print("Let the lot decide who goes first...")
first_move = random.choice([0, 1])
flag = 0  # who moves? 0 -> moves user
time.sleep(2)  # pause
if first_move == 1:
    flag = 1  # 1 -> moves computer or player2
    symbol_1 = 'X'
    symbol_0 = 0
    print(f'{player2} goes first!')
else:
    print(f'{player1} will go first!')
    symbol_1 = 0
    symbol_0 = 'X'

win = 0
r1 = r2 = 0
possible_moves = [(0 + i) for i in range(size)]

while win == 0:
    if flag == 1:
        if players == 1:
            r1 = random.choice(possible_moves)
        if players == 2:
            r1 = int(input(f'{player2}, go! Choose where to put an {symbol_0}: ')) - 1
        while r1 not in possible_moves:
            r1 = int(input(f'No way! Try again: ')) - 1  # occupied
        possible_moves.remove(r1)
        print(f'{player2} moved: ')
        time.sleep(1)
        move(field, symbol_1, r1)
        flag = 0
    if flag == 0:
        r2 = int(input(f'{player1}, your turn! Choose where to put an {symbol_0}: ')) - 1
        while r2 not in possible_moves:
            r2 = int(input(f'No way! Try again: ')) - 1  # occupied
        possible_moves.remove(r2)
        time.sleep(1)
        move(field, symbol_0, r2)
        flag = 1
    if field[0] == field[1] == field[2] or \
            field[3] == field[4] == field[5] or \
            field[6] == field[7] == field[8] or \
            field[0] == field[3] == field[6] or \
            field[1] == field[4] == field[7] or \
            field[2] == field[5] == field[8] or \
            field[0] == field[4] == field[8] or \
            field[6] == field[4] == field[2]:
        win = 1
        if flag == 0:
            print(f'{player2} WON! {player1} LOST')
        else:
            print(f'{player1} WON! Congratulations!')
