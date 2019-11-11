from random import randint


class Die:

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        number = randint(1, self.sides)
        print(number)

    def upgrade_side(self, sides):
        self.sides = sides


die = Die()
print(f'{die.sides} сторон')
for _ in range(11):
    die.roll_die()
print('--------------')

die.upgrade_side(10)
print(f'{die.sides} сторон')
for _ in range(11):
    pass
    die.roll_die()

print('--------------')
die.upgrade_side(20)
print(f'{die.sides} сторон')
for _ in range(11):
    die.roll_die()