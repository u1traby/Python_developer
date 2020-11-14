# # -*- coding: utf-8 -*-
#
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# # Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

# point = sd.get_point(500, 250)

COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_PURPLE = (255, 0, 255)


# sd.circle(center_position=point, radius=100, color=COLOR_RED, width=2)
# radius = 90
# for _ in range(3):
#     radius -= 20
#     sd.circle(center_position=point, color=COLOR_PURPLE, radius=radius, width=2)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
#
# def bubble(point, step):
#     radius = 50
#     for _ in range(3):
#         radius -= step
#         sd.circle(center_position=point, color=COLOR_PURPLE, radius=radius, width=2)
#
#
# point = sd.get_point(500, 250)
# bubble(point=point, step=10)


#
# # Нарисовать 10 пузырьков в ряд
# def bubble(point, step):
#     radius = 50
#     sd.circle(center_position=point, color=COLOR_PURPLE, radius=radius, width=2)
#
#
# for x in range(100, 1100, 100):
#     point = sd.get_point(x, 100)
#     bubble(point=point, step=5)

# Нарисовать три ряда по 10 пузырьков

# def bubble(point, step):
#     radius = 50
#     sd.circle(center_position=point, color=sd.random_color(), radius=radius, width=2)
#
# for y in range(100, 301, 100):
#     for x in range(100, 1100, 100):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# for _ in range(100):
#     point = sd.random_point()
#     step = random.randint(1, 50)
#     bubble(point=point, step=step)
#
sd.pause()
