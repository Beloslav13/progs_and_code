def filter_list(my_list):
    """Фильтрует список."""
    _list = []
    for elem in my_list:
        if not isinstance(elem, str):
            _list.append(elem)
    return _list


# print(filter_list([1, 2, 'a', 'b']))
# print(filter_list([1, 'a', 'b', 0, 15]))
# print(filter_list([1, 2, 'aasf', '1', '123', 123]))


def find_it(number):
    """Найти нечетный int в списке."""
    for index, numb in enumerate(number):
        if number.count(numb) % 2 != 0:
            return numb


# print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))


def getCount(input_str):
    """Возвращает кол-во гласных(пример)"""
    num_vowels = 0
    chars = 'aeiou'
    for index, char_input in enumerate(input_str):
        for char in chars:
            if char == char_input:
                num_vowels += 1
    return num_vowels


# print(getCount("abracadabra"))

def my_numbers(chars):
    """Возвращает номера строк"""
    template = []
    for index, char in enumerate(chars):
        index = index + 1
        template.append(str(index) + ': ' + char)
    return template


# print(my_numbers(["a", "b", "c"]))

def find_short(s):
    """Возвращает длину самого короткого слова в строке."""
    template = []
    words = s.split()
    for word in words:
        word_len = len(word)
        template.append(word_len)
    return min(template)


# print(find_short("bitcoin take over the world maybe who knows perhaps"))

def accum(string):

    count = 1
    for char in string:
        template = ' '
        new_char = char * count
        count += 1
        # template.append(a)
        a = template.join(new_char)
        template.join(a)
        print(template)
        print(a)


print(accum("ZpglnRxqenU"))

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.name = 'дом'
        self.money = 100
        self.food = 50
        self.mud = 0

    def __str__(self):
        return '{}: денег - {}, еды - {}, грязи - {}'.format(self.name.title(), self.money,
                                                             self.food,
                                                             self.mud)


class Husband:

    def __init__(self, name):
        self.name = name
        self.fullnes = 30
        self.happy = 1006

    def __str__(self):
        res = super().__str__()
        return '{} сытость - {}, счастья - {}'.format(self.name, self.fullnes, self.happy)

    def act(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def gaming(self):
        pass


class Wife:

    def __init__(self, name):
        self.name = name
        self.fullnes = 30
        self.happy = 100

    def __str__(self):
        res = super().__str__()
        return '{} сытость - {}, счастья - {}'.format(self.name, self.fullnes, self.happy)

    def act(self):
        pass

    def eat(self):
        pass

    def shopping(self):
        pass

    def buy_fur_coat(self):
        pass

    def clean_house(self):
        pass


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')
