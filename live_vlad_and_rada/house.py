from termcolor import cprint


class House:

    def __init__(self):
        self.name = 'дом'
        self.food_man = 100
        self.food_dog = 100
        self.mud = 0

    def __str__(self):
        return 'В доме еды - {}, у собаки - {}, грязи - {}'.format(self.food_man, self.food_dog, self.mud)


if __name__ == "__main__":
    pass