#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

point = sd.get_point(600, 30)


def draw_branches(point, angle, length):
    '''
        Recursive tree branch rendering function
    '''
    if length < 1:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()

    # first side of the branch
    next_point = v1.end_point
    next_angle = angle - 30
    next_length = length * 0.75
    angle_deg = sd.random_number(a = 3, b = 30)
    draw_branches(point=next_point, angle=next_angle, length=next_length)
    # second side branches
    next_angle2 = angle + 30
    draw_branches(point=next_point, angle=next_angle2 + angle_deg, length=next_length)


draw_branches(point=point, angle=90, length=100)

sd.pause()
