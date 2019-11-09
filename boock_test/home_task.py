# Задания из книги "Изучаем Python" Эрик Мэтиз.

from termcolor import cprint


# 9-1,9-4
class Restaurant:

    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        """ Выводит название и тип ресторана. """
        cprint('Ресторан - {}, тип - {}'.format(self.restaurant_name, self.cuisine_type), color='magenta')

    def open_restaurant(self):
        cprint('Ресторан {} открыт'.format(self.restaurant_name), color='green')

    # 9-4
    def set_number_served(self, number):
        """ Устанавливает кол-во обслуживания людей. """
        self.number_served = number
        return self.number_served

    def increment_number_served(self, number):
        """ Инкрементирует кол-во обслуживания людей. """
        self.number_served += number
        return self.number_served


# 9-3, 9-5
class User:

    def __init__(self, name, last_name, old, city):
        self.first_name = name
        self.last_name = last_name
        self.old = old
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        cprint('Имя - {}, второе имя - {}, возраст - {}, город - {}'.format(
            self.first_name, self.last_name, self.old, self.city
        ), color='cyan')

    def greet_user(self):
        cprint('Привет, {}!'.format(self.first_name), color='grey')

    # 9-5
    def increment_login_attempts(self):
        """ Увеличивает кол-во попыток входа. """
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempt(self):
        """ Сбрасывает кол-во попыток входа. """
        self.login_attempts = 0
        return self.login_attempts


class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = None

    def print_flavors(self):
        cprint(self.flavors, color='cyan')


restaurant = Restaurant(name='ZVA', type='burgers')
restaurant_KFC = Restaurant(name='KFC', type='burgers')
restaurant_mcdonalds = Restaurant(name='Mcdonalds', type='burgers')
restaurant_laterassa = Restaurant(name='Laterasa', type='pizza')
restaurant_94 = Restaurant(name='new', type='bgrs')

vlad = User(name='Vlad', last_name='ZVA', old=23, city='Belgorod')
nadya = User(name='Nadya', last_name='Belya', old=22, city='Belgorod')
# 9-5
new_user = User(name='User', last_name='Test', old=20, city='BGD')

# Var class IceCream
my_test_list = ['Vlad', 2, 'Zva', ]
ice_cream = IceCreamStand(name='IceCream', type='Cafe')
ice_cream.describe_restaurant()
template = ' '
result_test_list = []

for elem in my_test_list:
    result_elem = str(elem)
    result_test_list.append(result_elem)
    append_elem = template.join(result_test_list)
    ice_cream.flavors = append_elem
ice_cream.print_flavors()
