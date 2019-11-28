name_guest = input('Как Вас зовут? ')
filename = 'guest.txt'
with open(filename, 'w', encoding='utf8') as file:
    file.write(name_guest)

name_break = True
filename = 'guest_book.txt'
while name_break:
    name = input('Как Вас зовут? ')
    with open(filename, 'a', encoding='utf8') as file:
        hello = f'Привет {name}!'
        file.write(hello + '\n')
        print(hello)
        if name == 'zva':
            name_break = False
