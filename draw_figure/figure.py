import simple_draw as sd

# Общая функция фигур
def figure(point, angle, length, angle_degree_change):
    start_point = point
    # Передаем side кол-во сторон, которое будет отрисовываться 
    side = 360 / angle_degree_change
    # Запускаем цикл для отрисовки фигуры
    for _ in range(int(side)):
        v1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=1)
        v1.draw()
        start_point = v1.end_point
        angle += angle_degree_change
    sd.line(start_point=v1.end_point, end_point=point)


# Треугольник
def triangle(point, angle=0, length=200):
    figure(point=point, angle=20, length=100, angle_degree_change=120)


point = sd.get_point(100, 100)
triangle(point=point, angle=20, length=100)


# квадрат
def square(point, angle=0, length=200):
    figure(point=point, angle=20, length=100, angle_degree_change=90)


point = sd.get_point(450, 100)
square(point=point, angle=20, length=100)


# пятиугольник
def pentagon(point, angle=0, length=200):
    figure(point=point, angle=20, length=100, angle_degree_change=72)


point = sd.get_point(100, 350)
pentagon(point=point, angle=20, length=100)


# шестиугольник
def hexagon(point, angle=0, length=200):
    figure(point=point, angle=20, length=100, angle_degree_change=60)


point = sd.get_point(400, 350)
hexagon(point=point, angle=20, length=100)

sd.pause()
