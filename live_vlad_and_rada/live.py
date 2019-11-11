from termcolor import cprint

from man import Man
from house import House

vlad = Man(name='Vlad')
house = House()
vlad.go_to_house(name_house=house)
