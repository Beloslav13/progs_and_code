from termcolor import cprint


# 9-1,9-4
class Restaurant:

    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        cprint('Ресторан - {}, тип - {}'.format(self.restaurant_name, self.cuisine_type), color='magenta')

    def open_restaurant(self):
        cprint('Ресторан {} открыт'.format(self.restaurant_name), color='green')

    # 9-4
    def set_number_served(self, number):
        self.number_served = number
        return self.number_served

    def increment_number_served(self, number):
        self.number_served += number
        return self.number_served


restaurant = Restaurant(name='ZVA', type='burgers')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_KFC = Restaurant(name='KFC', type='burgers')
restaurant_mcdonalds = Restaurant(name='Mcdonalds', type='burgers')
restaurant_laterassa = Restaurant(name='Laterasa', type='pizza')

restaurant_KFC.describe_restaurant()
restaurant_mcdonalds.describe_restaurant()
restaurant_laterassa.describe_restaurant()

# 9-4
restaurant_94 = Restaurant(name='new', type='bgrs')
print(restaurant_94.number_served)
restaurant_94.number_served = 10
print(restaurant_94.number_served)
print(restaurant_94.set_number_served(number=23))
print(restaurant_94.number_served)
print(restaurant_94.increment_number_served(number=100))


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
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempt(self):
        self.login_attempts = 0
        return self.login_attempts


vlad = User(name='Vlad', last_name='ZVA', old=23, city='Belgorod')
nadya = User(name='Nadya', last_name='Belya', old=22, city='Belgorod')

# 9-5
new_user = User(name='User', last_name='Test', old=20, city='BGD')
new_user.increment_login_attempts()
new_user.increment_login_attempts()
print(new_user.login_attempts)
new_user.reset_login_attempt()
print(new_user.login_attempts)

vlad.greet_user()
vlad.describe_user()
nadya.greet_user()
nadya.describe_user()
