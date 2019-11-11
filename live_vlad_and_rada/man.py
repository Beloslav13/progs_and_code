from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullnes = 50
        self.money = 200
        self.energy = 100
        self.house = None

    def __str__(self):
        return 'Я - {}, моя сытость - {}, денег - {} и энергии - {}'.format(
            self.name, self.fullnes, self.money, self.energy
        )

    def go_to_house(self, name_house):
        self.house = name_house
        cprint('{} переехал в {}'.format(self.name, name_house.name), color='cyan')

    def eat(self):
        self.fullnes += 20
        # добавить остатки еды
        cprint('{} покушал.'.format(self.name), color='yellow')


if __name__ == '__main__':
    vlad = Man(name='Vlad')

