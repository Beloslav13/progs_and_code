import simple_draw as sd

# Общая функция фигур
def draw_figure(point, angle, length, angle_degree_change):
    start_point = point
    # Передаем side кол-во сторон, которое будет отрисовываться 
    side = 360 / angle_degree_change
    # Запускаем цикл для отрисовки фигуры
    for _ in range(int(side)):
        v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=1)
        v1.draw()
        start_point = v1.end_point
        angle += angle_degree_change
    sd.line(start_point=start_point, end_point=point)


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


point = sd.get_point(100, 100)
draw_triangle(point=point, angle=20, length=100)

point = sd.get_point(450, 100)
draw_square(point=point, angle=20, length=100)

point = sd.get_point(100, 350)
draw_pentagon(point=point, angle=20, length=100)

point = sd.get_point(400, 350)
draw_hexagon(point=point, angle=20, length=100)

sd.pause()
