# import colorgram
import random
from turtle import Turtle, Screen

# colors = []
# extracted_colors = colorgram.extract('damien-hirst-1994-controlled-substance-key-painting.jpg', 38)
#
# for color in extracted_colors:
#     colors.append((color.rgb[0], color.rgb[1], color.rgb[2]))


hirst_color_palette = [(248, 244, 245), (231, 227, 219), (19, 17, 19), (210, 147, 95), (219, 231, 236), (139, 167, 17),
                       (159, 56, 9), (112, 147, 184), (42, 112, 163), (224, 212, 124), (119, 183, 148), (220, 236, 228),
                       (199, 130, 138), (6, 46, 81), (82, 45, 18), (138, 6, 1), (78, 155, 81), (230, 105, 37),
                       (246, 197, 0),
                       (96, 94, 96), (5, 68, 125), (77, 141, 80), (106, 30, 32), (228, 172, 164), (207, 183, 186),
                       (159, 116, 122),
                       (86, 134, 172), (100, 58, 24), (164, 208, 179), (176, 189, 210), (12, 14, 13), (88, 136, 165),
                       (170, 200, 211)]

lucky = Turtle()
screen = Screen()
screen.colormode(255)
lucky.speed(0)
lucky.up()
lucky.hideturtle()


def up_move_down(x, y):
    lucky.setpos(x, y)
    lucky.dot(20, random.choice(hirst_color_palette))


def fill_row(x, y):
    for i in range(10):
        up_move_down(x, y)
        x += 50


def paint(x, y):
    for _ in range(10):
        fill_row(x, y)
        y += 50  # change column


paint(-250, -250)

screen.exitonclick()
