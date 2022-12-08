# 1) Сделать игру морской бой
# ОДНО ПОЛЕ, 1 КОРАБЛЬ

import random

def show_list(my_list):
    for i in my_list:
        for j in i:
            print(j, end=' ')
        print()

# show field with moves
def user_move(list1, r, c):
    del list1[r][c]
    list1[r].insert(c, '+')
    show_list(list1)

# show field with hidden boat
def show_results():
    del field[r1][r2]
    field[r1].insert(r2,'$') # boat hidden
    show_list(field)


size = 4    # SIZE of field possible to change size of the field afterwards
field = [[0 for j in range(size)] for i in range(size)]

r1 = random.randint(0, 3)   # BOAT hidden
r2 = random.randint(0, 3)

attempts = 0    # LEVEL, possible to change quantity of attempts
n = int(input('Choose level (1 = easy, 2 = medium, 3 = I am an extrasence!\nLevel: '))
if n == 1:
    attempts = 9
elif n == 2:
    attempts = 6
elif n == 3:
    attempts = 3
else:
    print('This level does not exist yet')

move_count = 1
while move_count <= attempts:
    row_move = int(input(f'Your move, Sir. Field {size} * {size}.\nRow: ')) - 1
    col_move = int(input('Column: ')) - 1
    move_count += 1
    user_move(field, row_move, col_move)
    if row_move == r1 and col_move == r2:
        print('You WIN')
        show_results()
        break

if move_count > attempts:
    print('no moves left. You LOSE')
    show_results()