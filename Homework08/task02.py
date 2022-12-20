# Делаем программу , где используем классы.
# Где класс будет содержать имя студента name,
# номер группы group и список полученных оценок progress.

# В самой программе вводим список студентов.
# После выводим список , отсортированный по имени,
# потом выводятся студенты, имеющие неудовлетворительные оценки.

from random import choice
from random import randint

class Student():
    def __init__(self, name, group_num, progress):
        self.name = name
        self.group_num = group_num
        self.progress = progress
        # print('done')

    def show_name(self):
        return self.name


students_list = ['Ivanov', 'Stepanov', 'Sergeev', 'Matveev', 'Petrov', 'Semyonov', 'Ryabikov', 'Nesterov', 'Adams']
students_list.sort()
gr = ['group A', 'group B', 'group C']
scores = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5] # иначе, по теории вероятности, двоичников будет слишком много
neud_list = []

for i in range(len(students_list)):
    x = 'st' + str(i + 1)
    score1 = []
    num_of_scores = randint(5, 10)
    for j in range(num_of_scores):
        score1.append(choice(scores))
    if 2 in score1:
        neud_list.append(students_list[i])
    # print(students_list[i])
    # print(x)
    # print(score1)
    x = Student(students_list[i], choice(gr), score1)

print(students_list)
print('Неудотворительные оценки имеют следующие студенты: \n', '\n '.join(neud_list))
