# 1) Сделать игру морской бой
# 2 ПОЛя, по 1 КОРАБЛю

import random

def show_list(my_list):
    for i in my_list:
        for j in i:
            print(j, end=' ')
        print()

# show field with moves
def show_comp_field(list1, r1, c1):
    del list1[r1][c1]
    list1[r1].insert(c1, '+')
    print("Computer's field HERE")
    show_list(list1)
    print('=======')


def show_user_field(list2, r2, c2):
    del list2[r2][c2]
    list2[r2].insert(c2, '+')
    print('Computer moved. Your field HERE')
    show_list(list2)
    print('=======')


# show field with hidden boat
def show_results():
    del field_comp[comp_r][comp_c]
    field_comp[comp_r].insert(comp_c,'W')   # boat hidden
    show_list(field_comp)


size = 4    # SIZE of field possible to change size of the field afterwards
field_comp = [[0 for j in range(size)] for i in range(size)]
field_user = [[0 for j in range(size)] for i in range(size)]

comp_r = random.randint(0, 3)   # BOAT hidden
comp_c = random.randint(0, 3)
# print(comp_r + 1, comp_c + 1)     # CHECK where comp placed his boat

boat_r = int(input(f'So, where have you placed the boat? Field {size} * {size}\nRow: ')) - 1
boat_c = int(input('Column: ')) - 1
print('your field, Commandor')
del field_user[boat_r][boat_c]
field_user[boat_r].insert(boat_c, 'V')
show_list(field_user)

flag = 0    # 0=user 1=computer
win = 0

r = [0, 1, 2, 3]
c = [0, 1, 2, 3]

while win == 0:
    if flag == 0:
        row_move = int(input(f'Your move, Sir.\nRow: ')) - 1
        col_move = int(input('Column: ')) - 1
        show_comp_field(field_comp, row_move, col_move)
        flag = 1

        if row_move == comp_r and col_move == comp_c:
            print('You WIN')
            show_results()
            win = 1
            break

    if flag == 1:
        rr = random.choice(r)
        cc = random.choice(c)
        r.remove(rr)
        c.remove(cc)
        show_user_field(field_user, rr, cc)
        flag = 0

        if rr == boat_r and cc == boat_c:
            print('Computer WIN. You LOSE')
            show_results()
            win = 1
