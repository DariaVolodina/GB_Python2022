print('lesson 8')

# Класс, объект, атрибут (свойство), метод..... ООП
# в пайтоне всё объект (список, переменная, цифры...)

# print(type(1))   # 1 - это экземпляр класса ИНТ
# print(type('abc'))
# print(type([10, 20, 30]))

class Fruit:    # имена классов - с Большой Буквы
    pass        # пустая инструкция, которая ничего не выполняет

# a = Fruit()
# b = Fruit()
#
# a.name = 'apple'
# a.weight = 120
#
# b.name = 'orange'
# b.weight = 150
#
# b.weight -= 50
#
# print(a.name, a.weight)
# print(b.name, b.weight)


# МЕТОДЫ - чем отличаются от функций?
# class Hello:
#     def hello_world(self):  # FUNCTION inside CLASS # SELF - ссылаемся сами на себя. очень важный параметр
#         print('Hello, world')
#
#     def greeting(self, name):
#         print(f'Hi, {name}')
#
# # Hello.hello_world(greet)
# greet = Hello()     # экземпляр класса хэллоу
# greet.hello_world()
# greet.greeting('Bob')

class Car:
    def __init__(self, color):     # при создании каждого нового экземпляра класса будет вызываться этот метод
        self.e_on = False
        self.color = color

    def start(self):        # SELF - контекстный объект
        self.e_on = True

    def drive_to(self, city):
        if self.e_on:
            print(f'Going to {city} on a {self.color} car')
        else:
            print('Will not go anywhere... Battery low')

c = Car('red')
c.start()
c.drive_to('Sochi')


# ПОЛИМОРФИЗМ - свойство кода работать с разными типами данных
print(1 + 2)
print(1.3 + 2.3)
print('1.2' + '2.5')
print('f(1,2)')

class Book:
    def __init__(self, name, auth):
        self.name = name
        self.auth = auth

    def get_name(self):
        return self.name

    def get_auth(self):
        return self.auth


book = Book('War & Warld', 'Tolstoi')
print(f'The book {book.get_name()}, author - {book.get_auth()}')
print(book.name)


from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


def print_shape_info(shape):
    print(f'Area = {shape.area()}, perimeter = {shape.perimeter()}')


square = Square(10)
print(square.area())
print(square.perimeter())
print_shape_info(square)

circle = Circle(10)
print_shape_info(circle)


class Time:
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds

    # def __sub__(self, other):   # метод САБ срабатывает на МИНУС
    # есть методы и с другими математическими операциями, со сравнениями ...
    def __add__(self, other):
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        m += s // 60
        s = s % 60
        return Time(m, s)


    def info(self):
        return f'{self.minutes} : {self.seconds}'

    def __str__(self):
        return f'!!! {self.minutes} : {self.seconds}'


t1 = Time(5, 30)
print(t1.info())

t2 = Time(3, 50)
print(t2.info())

t3 = t1 + t2
print(t3.info())

print(t1)   # отработал метод STR

