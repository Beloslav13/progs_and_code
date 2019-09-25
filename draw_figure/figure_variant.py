# -*- coding: utf-8 -*-
import simple_draw as sd


def draw_figure(point, angle, length, angle_degree_change):
        start_point = point
        side = 360 / angle_degree_change

        for _ in range(int(side)):
            v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=1)
            l1 = sd.line(start_point=start_point, end_point=v1.end_point, color=user_color[que][1])
            start_point = v1.end_point
            angle += angle_degree_change
        sd.line(start_point=v1.end_point, end_point=point, color=user_color[que][1])


# Треугольник
def draw_triangle(point, angle=0, length=200):
    draw_figure(point=point, angle=20, length=100, angle_degree_change=120)


# квадрат
def draw_square(point, angle=0, length=200):
    draw_figure(point=point, angle=20, length=100, angle_degree_change=90)


# пятиугольник
def draw_pentagon(point, angle=0, length=200):
    draw_figure(point=point, angle=20, length=100, angle_degree_change=72)


# шестиугольник
def draw_hexagon(point, angle=0, length=200):
    draw_figure(point=point, angle=20, length=100, angle_degree_change=60)


colors = sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE

# Словарь цветов фигур
user_color = {
    '0':
        ('red', sd.COLOR_RED),
    '1':
        ('orange', sd.COLOR_ORANGE),
    '2':
        ('yellow', sd.COLOR_YELLOW),
    '3':
        ('green', sd.COLOR_GREEN),
    '4':
        ('cyan', sd.COLOR_CYAN),
    '5':
        ('blue', sd.COLOR_BLUE),
    '6':
        ('purple', sd.COLOR_PURPLE),
}

# Выбор цвета
print('Возможные цвета:')
for numb_color in user_color.keys():
    print(numb_color, ':', user_color[numb_color][0])
que = input('Введите желаемый цвет: ')

# Словарь названия фигур и названия функций
user_figure = {
    '0':
        {'name_figure': 'треугольник', 'name_func': draw_triangle},
    '1':
        {'name_figure': 'квадрат', 'name_func': draw_square},
    '2':
        {'name_figure': 'пятиугольник', 'name_func': draw_pentagon},
    '3':
        {'name_figure': 'шестиугольник', 'name_func': draw_hexagon},
}

# Выбор фигуры
print('Возможные фигуры:')
for key in user_figure.keys():
    print(key, ':', user_figure[key]['name_figure'])
que2 = input('Введите желаемую фигуру: ')

# Проверка, есть ли ответ пользователя в определенном словаре.
if que in user_color and que2 in user_figure:
    point = sd.get_point(300, 200)
    func = user_figure[que2]['name_func']
    func(point=point, angle=20, length=100)

else:
    print('Введено некорректное значение!')


sd.pause()
