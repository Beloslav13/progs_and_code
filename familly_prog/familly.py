# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


class House:
    total_money = 0
    total_food = 0

    def __init__(self):
        self.name = 'дом'
        self.money = 100
        self.food = 50
        self.mud = 0
        self.cat_food = 30

    def __str__(self):
        return '{}: денег - {}, еды - {}, грязи - {}'.format(self.name.title(), self.money,
                                                             self.food,
                                                             self.mud)

    def add_mud(self):
        self.mud += 5


class Man:
    total_buy_coat = 0

    def __init__(self, name, house):
        self.house = house
        self.name = name
        self.fullnes = 30
        self.happy = 100

    def __str__(self):
        return '{} сытость - {}, счастья - {}'.format(self.name, self.fullnes, self.happy)

    def eat(self):
        if self.house.food >= 30:
            House.total_food += 30
            self.fullnes += 30
            self.house.food -= 30
            cprint('Человек по имени {} принял пищу'.format(self.name), color='green')
        else:
            cprint('еда у {} закончилась...'.format(self.name))

    def work(self):
        House.total_money += 150
        self.fullnes -= 10
        self.house.money += 150
        cprint('{} сходил на работу и положил деньги в тумбочку'.format(self.name), color='green')

    def pet_cat(self):
        self.happy += 5
        cprint('Человек {} целый день тюскал кота...'.format(self.name))


class Husband(Man):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 10)
        if self.house.mud > 90:
            self.happy -= 10
        if self.fullnes <= 0 or self.happy <= 10:
            cprint('{} умер...'.format(self.name))
        elif self.fullnes <= 20:
            self.eat()
        elif self.house.money <= 100:
            self.work()
        elif self.happy <= 50:
            self.gaming()
        elif dice == 1:
            self.gaming()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.pet_cat()
        else:
            cprint('{} ничего не делал act'.format(self.name))

    def eat(self):
        super().eat()

    def work(self):
        super().work()

    def gaming(self):
        if self.happy <= 50:
            self.fullnes -= 10
            self.happy += 20
            cprint('{} целый день играл в World of Tanks'.format(self.name), color='green')
        else:
            self.eat()


class Wife(Man):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 10)
        if self.house.mud > 90:
            self.happy -= 10
        if self.fullnes <= 0 or self.happy <= 10:
            cprint('{} умерла...'.format(self.name))
        elif self.house.mud >= 100:
            self.clean_house()
        elif self.fullnes <= 20:
            self.eat()
        elif self.house.food <= 100:
            self.shopping()
        elif self.happy <= 50:
            self.buy_fur_coat()
        elif dice == 1:
            self.shopping()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.pet_cat()
        elif dice == 4:
            self.buy_fur_coat()
        else:
            cprint('{} ничего не делала'.format(self.name))

    def eat(self):
        super().eat()

    def shopping(self):
        if self.house.money >= 110:
            self.fullnes -= 10
            self.house.food += 100
            self.house.cat_food += 10
            self.house.money -= 110
            cprint('{} сходила в магазин за едой'.format(self.name), color='yellow')
        else:
            cprint('деньги на еду закончились...', color='red')

    def buy_fur_coat(self):
        Man.total_buy_coat += 1
        if self.house.money > 350:
            self.fullnes -= 10
            self.happy += 60
            self.house.money -= 350
            cprint('{} купила себе шубу'.format(self.name), color='green')
        else:
            cprint('денег на шубу не хватает....', color='red')

    def clean_house(self):
        if self.house.mud >= 100:
            self.fullnes -= 10
            self.house.mud -= 100
            cprint('{} убиралась в доме'.format(self.name), color='yellow')
        else:
            cprint('грязи еще маловато...', color='red')

    def work(self):
        """Переопределение метода в случае вызова его у жены."""
        cprint('{} не ходит на работу!'.format(self.name), color='red')


class Cat:

    def __init__(self, name, house):
        self.house = house
        self.name = name
        self.fullnes = 30

    def __str__(self):
        return '{} сытость - {}'.format(self.name, self.fullnes)

    def act(self):
        dice = randint(1, 5)
        if self.fullnes < 0:
            cprint('{} умер от голода...', color='red')
        elif self.fullnes <= 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.soil()
        else:
            self.sleep()

    def eat(self):
        if self.house.cat_food >= 10:
            self.fullnes += 20
            self.house.cat_food -= 10
            cprint('{} поел'.format(self.name), color='magenta')
        else:
            cprint('еда у кота закончилась', color='red')

    def sleep(self):
        self.fullnes -= 10
        cprint('{} спал целый день'.format(self.name), color='magenta')

    def soil(self):
        self.fullnes -= 10
        self.house.mud += 5
        cprint('{} драл обои'.format(self.name), color='magenta')


class Child(Man):

    def __init__(self, name):
        super().__init__(name=name, house=home)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullnes < 0:
            cprint('{} умер...........'.format(self.name), color='red')
        elif self.fullnes <= 10:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food >= 10:
            self.fullnes += 10
            self.house.food -= 10
            cprint('{} покушал'.format(self.name), color='grey')
        else:
            cprint('еда у ребенка закончилась...', color='red')

    def sleep(self):
        self.fullnes -= 10
        cprint('{} спал'.format(self.name), color='grey')


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='cyan')

cprint('{} съедено еды'.format(House.total_food))
cprint('{} заработано денег'.format(House.total_money))
cprint('{} куплено шуб'.format(Man.total_buy_coat))
