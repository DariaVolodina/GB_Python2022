# Создайте класс Soup (для определения типа супа),
# принимающий 1 аргумент при инициализации (отвечающий за основной продукт к выбираемому супу).
# В этом классе реализуйте метод show_my_soup(),
# выводящий на печать «Суп - {Основной продукт}» в случае наличия добавки,
# а иначе отобразится следующая фраза: «Обычный кипяток»

class Soup():
    def __init__(self, main_product):
        self.main_product = main_product

    def show_my_soup(self):
        if self.main_product.isalpha():
           print(f'Суп - {self.main_product}')
        else:
            print('Обычный кипяток')


soup_1 = Soup('свекла')
soup_2 = Soup('рыба')
soup_3 = Soup('капуста')
soup_4 = Soup('курица')
soup_5 = Soup('')
my_soup = Soup(' ')

soup_1.show_my_soup()
soup_2.show_my_soup()
soup_3.show_my_soup()
soup_4.show_my_soup()
soup_5.show_my_soup()
my_soup.show_my_soup()

